#!/usr/bin/env python3
"""Prepare, enrich, cache, and render a human-readable corpus report."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts.api.call_responses import (  # noqa: E402
    calculate_cost, output_text, parse_json_output, resolve_model,
    structured_output_format,
)

PROMPT_VERSION = "0.1"
REPORT_SCHEMA_VERSION = "0.1"
DEFAULT_PROMPT = Path("prompts/corpus_report/enrich_occurrence_v0_1.md")
DEFAULT_SCHEMA = Path("prompts/corpus_report/enrichment_schema_v0_1.json")
DEFAULT_CATALOG = Path("config/api_models.json")
DEFAULT_OUTPUT_ROOT = Path("results/corpus_reports")
DISPLAY_CONTEXT_MAX = 1600


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return value


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_hash(value: object) -> str:
    return sha256_bytes(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                   separators=(",", ":")).encode("utf-8"))


def repository_path(path: Path, repo_root: Path) -> Path:
    return path if path.is_absolute() else repo_root / path


def portable_path(value: str) -> Path:
    return Path(value.replace("\\", "/"))


def valid_annotation_attempt(occurrence_root: Path) -> Path:
    valid = [status.parent for status in occurrence_root.glob("attempt-*/status.json")
             if read_json(status).get("state") == "valid"]
    if len(valid) != 1:
        raise ValueError(
            f"expected exactly one valid annotation for {occurrence_root.name}; found {len(valid)}"
        )
    return valid[0]


def core_annotation(output: dict) -> dict:
    core = output.get("core_love_content", output.get("core_classification"))
    if not isinstance(core, dict):
        raise ValueError("annotation lacks core classification")
    support = core["label_support"]
    return {
        "scores": {
            "P": support["performative"],
            "T": support["truth_conditional"],
            "E": support["exclamatory_reflexive"],
            "O": support["other"],
        },
        "confidence": core["confidence"],
        "ontology_fit": output["ontology_assessment"]["fit"],
        "utterance_status": output["utterance_status"],
        "analysis": core["analysis"],
        "ambiguity_note": core.get("ambiguity"),
        "contextual_interpretation": output.get("contextual_interpretation"),
        "evidence": output.get("evidence", []),
        "background_knowledge": output.get("background_knowledge"),
    }


def bounded_context(occurrence: dict, maximum: int = DISPLAY_CONTEXT_MAX) -> str:
    """Clip context deterministically around the target without clipping the target."""
    context = occurrence["context"]
    if len(context) <= maximum:
        return context
    relative_start = occurrence["start"] - occurrence["context_start"]
    relative_end = relative_start + len(occurrence["match"])
    if relative_start < 0 or relative_end > len(context):
        raise ValueError(f"target offsets fall outside context for {occurrence['occurrence_id']}")
    budget = maximum - len(occurrence["match"])
    before = min(relative_start, budget // 2)
    after = min(len(context) - relative_end, budget - before)
    before = min(relative_start, budget - after)
    start, end = relative_start - before, relative_end + after
    clipped = context[start:end]
    return ("…" if start else "") + clipped + ("…" if end < len(context) else "")


def collect_occurrences(batch_runs: list[Path], repo_root: Path) -> tuple[list[dict], list[dict]]:
    records, batches, identities = [], [], set()
    for batch_index, batch_run in enumerate(batch_runs):
        summary_path = batch_run / "summary.json"
        if not summary_path.is_file():
            raise ValueError(f"missing batch summary: {summary_path}")
        summary = read_json(summary_path)
        if summary.get("status") != "complete" or summary.get("dry_run"):
            raise ValueError(f"batch is not a completed real run: {batch_run}")
        if summary.get("texts_completed") != summary.get("texts_requested") \
                or summary.get("failures") or summary.get("valid_annotations") != summary.get("occurrences"):
            raise ValueError(f"batch is partial or internally incomplete: {batch_run}")
        batch_count = 0
        for work_index, text in enumerate(summary["texts"]):
            if text.get("status") != "complete" \
                    or text.get("valid_occurrences") != text.get("extracted_occurrences"):
                raise ValueError(f"incomplete text {text.get('source_id')} in {batch_run}")
            text_run = batch_run / "texts" / text["source_id"]
            manifest = read_json(text_run / "manifest.json")
            source_reference = read_json(text_run / "source_reference.json")
            provenance_path = repository_path(portable_path(source_reference["provenance_path"]), repo_root)
            if not provenance_path.is_file():
                raise ValueError(f"unresolved provenance pointer: {provenance_path}")
            provenance = read_json(provenance_path)
            input_by_id = {p.stem: read_json(p) for p in (text_run / "inputs").glob("*.json")}
            passage_records = [json.loads(line) for line in
                               (text_run / "extraction" / "passages.jsonl").read_text(
                                   encoding="utf-8").splitlines() if line.strip()]
            passage_by_id = {item["occurrence_id"]: item for item in passage_records}
            if len(passage_by_id) != len(passage_records):
                raise ValueError(f"duplicate occurrence ID within extraction: {text_run}")
            annotation_roots = list((text_run / "annotations").iterdir())
            if set(input_by_id) != set(passage_by_id) or {p.name for p in annotation_roots} != set(passage_by_id):
                raise ValueError(f"input/extraction/annotation occurrence sets differ: {text_run}")
            ordered = sorted(passage_records, key=lambda item: (item["start"], item["occurrence_id"]))
            for occurrence_index, occurrence in enumerate(ordered, 1):
                occurrence_id = occurrence["occurrence_id"]
                identity = (str(batch_run.resolve()), text["source_id"], occurrence_id)
                if identity in identities:
                    raise ValueError(f"duplicate report occurrence identity: {identity}")
                identities.add(identity)
                annotation_attempt = valid_annotation_attempt(text_run / "annotations" / occurrence_id)
                annotation_output = read_json(annotation_attempt / "output.json")
                prepared_input = input_by_id[occurrence_id]
                if annotation_output.get("occurrence_id") != occurrence_id:
                    raise ValueError(f"annotation occurrence mismatch: {annotation_attempt}")
                metadata = prepared_input["metadata"]
                annotation = core_annotation(annotation_output)
                record = {
                    "report_occurrence_key": sha256_bytes("\0".join(identity).encode("utf-8"))[:20],
                    "occurrence_id": occurrence_id,
                    "batch_id": summary["batch_id"],
                    "batch_run": str(batch_run.relative_to(repo_root)),
                    "batch_index": batch_index,
                    "work_index": work_index,
                    "occurrence_index": occurrence_index,
                    "work_id": occurrence["work_id"],
                    "source_id": occurrence["source_id"],
                    "title": metadata["title"],
                    "author": metadata["author"],
                    "language": occurrence["language"],
                    "source_location": metadata["location"],
                    "target": {"text": occurrence["match"], "start": occurrence["start"],
                               "end": occurrence["end"]},
                    "original_passage": bounded_context(occurrence),
                    "annotation": annotation,
                    "annotation_provenance": {
                        "path": str((annotation_attempt / "output.json").relative_to(repo_root)),
                        "annotation_version": manifest["annotation_version"],
                        "model": manifest["api_model"],
                        "prompt_path": manifest["prompt_path"],
                        "prompt_sha256": manifest["prompt_sha256"],
                        "schema_path": manifest["schema_path"],
                        "schema_sha256": manifest["schema_sha256"],
                    },
                    "source_provenance": str(provenance_path.relative_to(repo_root)),
                }
                records.append(record)
                batch_count += 1
        if batch_count != summary["occurrences"]:
            raise ValueError(
                f"batch occurrence mismatch for {summary['batch_id']}: "
                f"summary={summary['occurrences']}, collected={batch_count}"
            )
        batches.append({"batch_id": summary["batch_id"], "path": str(batch_run.relative_to(repo_root)),
                        "works": summary["texts_requested"], "occurrences": summary["occurrences"]})
    if len(identities) != len(records):
        raise ValueError("combined report contains duplicate occurrence records")
    return records, batches


def enrichment_input(record: dict) -> dict:
    annotation = record["annotation"]
    return {
        "occurrence_id": record["occurrence_id"], "title": record["title"],
        "author": record["author"], "language": record["language"],
        "source_passage": record["original_passage"], "target_span": record["target"],
        "source_location": record["source_location"],
        "utterance_status": annotation["utterance_status"],
        "scores": annotation["scores"], "confidence": annotation["confidence"],
        "ontology_fit": annotation["ontology_fit"], "annotation_analysis": annotation["analysis"],
        "ambiguity_note": annotation["ambiguity_note"],
        "contextual_interpretation": annotation["contextual_interpretation"],
        "relevant_evidence": annotation["evidence"],
        "background_knowledge_metadata": annotation["background_knowledge"],
    }


def cache_identity(record: dict, api_model: str, prompt_hash: str, schema_hash: str) -> dict:
    value = enrichment_input(record)
    annotation_fields = {key: value[key] for key in (
        "utterance_status", "scores", "confidence", "ontology_fit", "annotation_analysis",
        "ambiguity_note", "contextual_interpretation", "relevant_evidence",
        "background_knowledge_metadata")}
    source_fields = {key: value[key] for key in (
        "title", "author", "language", "source_passage", "target_span", "source_location")}
    return {
        "occurrence_id": record["occurrence_id"],
        "report_occurrence_key": record["report_occurrence_key"],
        "api_model": api_model, "prompt_version": PROMPT_VERSION,
        "prompt_sha256": prompt_hash, "schema_version": PROMPT_VERSION,
        "schema_sha256": schema_hash, "source_input_sha256": canonical_hash(source_fields),
        "annotation_input_sha256": canonical_hash(annotation_fields),
    }


def validate_enrichment(value: dict, language: str) -> list[str]:
    errors = []
    required = {"translation_en", "larger_context_summary", "interpretive_commentary"}
    if not isinstance(value, dict) or set(value) != required:
        return [f"enrichment fields must be exactly {sorted(required)}"]
    translation = value["translation_en"]
    if language == "en" and translation is not None:
        errors.append("English occurrence must have translation_en null")
    if language != "en" and (not isinstance(translation, str) or not translation.strip()):
        errors.append("non-English occurrence must have a non-empty translation_en")
    for key in ("larger_context_summary", "interpretive_commentary"):
        if not isinstance(value[key], str) or not value[key].strip():
            errors.append(f"{key} must be a non-empty string")
    return errors


def request_payload(prompt: str, schema: dict, api_model: str, request_input: dict) -> dict:
    supplied = json.dumps(request_input, ensure_ascii=False, indent=2)
    combined = f"{prompt}\n\n## Input\n\n{supplied}"
    return {"model": api_model, "input": combined,
            "text": structured_output_format(schema, "corpus_report_enrichment_v0_1")}


def existing_cache(cache_dir: Path, identity: dict, language: str) -> tuple[dict | None, Path]:
    key = canonical_hash(identity)
    directory = cache_dir / identity["report_occurrence_key"] / key
    result_path = directory / "result.json"
    if not result_path.is_file():
        return None, directory
    wrapper = read_json(result_path)
    if wrapper.get("identity") != identity or validate_enrichment(wrapper.get("enrichment"), language):
        return None, directory
    return wrapper["enrichment"], directory


def recorded_cache_cost(cache_dir: Path) -> float:
    total = 0.0
    for cost_path in cache_dir.glob("*/*/attempt-*/cost.json"):
        try:
            total += float(read_json(cost_path).get("estimated_total_cost", 0.0))
        except (OSError, ValueError, TypeError, json.JSONDecodeError):
            continue
    return total


def next_attempt(directory: Path) -> Path:
    attempts = sorted(directory.glob("attempt-*"))
    number = max([int(path.name.split("-")[-1]) for path in attempts] or [0]) + 1
    attempt = directory / f"attempt-{number:03d}"
    attempt.mkdir(parents=True)
    return attempt


def call_model(payload: dict, api_key: str, endpoint: str) -> dict:
    request = urllib.request.Request(endpoint, data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                                     headers={"Authorization": f"Bearer {api_key}",
                                              "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(request, timeout=300) as response:
        return json.loads(response.read().decode("utf-8"))


def enrich_one(*, record: dict, identity: dict, directory: Path, payload: dict,
               api_key: str, endpoint: str, pricing: dict,
               caller=call_model, now=lambda: datetime.now(timezone.utc)) -> tuple[dict | None, float]:
    attempt = next_attempt(directory)
    write_json(attempt / "request.json", payload)
    write_json(attempt / "pricing_snapshot.json", pricing)
    write_json(attempt / "metadata.json", {"created_at": now().isoformat(), "attempt": attempt.name,
                                            "identity": identity, "model": payload["model"]})
    try:
        response = caller(payload, api_key, endpoint)
        write_json(attempt / "response.json", response)
        raw_text = output_text(response)
        (attempt / "output.txt").write_text(raw_text + ("\n" if raw_text else ""), encoding="utf-8")
        parsed, parsing_method = parse_json_output(raw_text)
        write_json(attempt / "parsed.json", parsed)
        errors = validate_enrichment(parsed, record["language"])
        write_json(attempt / "validation.json", {"valid": not errors, "errors": errors,
                                                  "parsing_method": parsing_method})
        cost = calculate_cost(response.get("usage", {}), pricing)
        write_json(attempt / "cost.json", cost)
        if errors:
            write_json(attempt / "status.json", {"state": "invalid"})
            return None, cost["estimated_total_cost"]
        write_json(attempt / "status.json", {"state": "valid"})
        write_json(directory / "result.json", {"identity": identity, "enrichment": parsed,
                                                "valid_attempt": attempt.name})
        return parsed, cost["estimated_total_cost"]
    except Exception as exc:  # Preserve every failed attempt and let remaining calls proceed.
        (attempt / "error.txt").write_text(f"{type(exc).__name__}: {exc}\n", encoding="utf-8")
        write_json(attempt / "status.json", {"state": "failed"})
        return None, 0.0


def slug(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return cleaned or "occurrence"


def anchors(records: list[dict]) -> list[str]:
    return [f"occ-{slug(record['occurrence_id'])}-{record['report_occurrence_key'][:8]}"
            for record in records]


def structural_categories(record: dict) -> set[str]:
    status = record["annotation"]["utterance_status"]["status"]
    categories = set()
    if status in {"embedded_or_reported", "embedded", "reported"}:
        categories.add("embedded/reported")
    if status in {"quoted_or_revoiced", "quoted", "revoiced"}:
        categories.add("quoted/revoiced")
    # Negation is intentionally not guessed from multilingual source strings.
    return categories


def build_indices(records: list[dict]) -> dict:
    result = {"by_work": [], "by_language": [], "interesting": {}}
    work_order, language_order = [], []
    for record in records:
        if record["work_id"] not in work_order:
            work_order.append(record["work_id"])
        if record["language"] not in language_order:
            language_order.append(record["language"])
    for work_id in work_order:
        subset = [r for r in records if r["work_id"] == work_id]
        result["by_work"].append({"work_id": work_id, "title": subset[0]["title"],
                                  "count": len(subset),
                                  "anchors": [r["anchor"] for r in subset]})
    for language in language_order:
        subset = [r for r in records if r["language"] == language]
        result["by_language"].append({"language": language, "count": len(subset),
                                      "anchors": [r["anchor"] for r in subset]})
    predicates = {
        "P >= 2": lambda r: r["annotation"]["scores"]["P"] >= 2,
        "E >= 2": lambda r: r["annotation"]["scores"]["E"] >= 2,
        "O > 0": lambda r: r["annotation"]["scores"]["O"] > 0,
        "ontology fit != natural": lambda r: r["annotation"]["ontology_fit"] != "natural",
        "low confidence (< 0.75)": lambda r: r["annotation"]["confidence"] < 0.75,
        "embedded/reported": lambda r: "embedded/reported" in structural_categories(r),
        "quoted/revoiced": lambda r: "quoted/revoiced" in structural_categories(r),
    }
    result["interesting"] = {name: [r["anchor"] for r in records if predicate(r)]
                             for name, predicate in predicates.items()}
    result["interesting"]["negated"] = None
    result["interesting_notes"] = {
        "negated": "unknown / not structurally represented",
        "status_policy": "Status indices use only structured utterance_status values; categories may be incomplete."
    }
    return result


def report_document(*, name: str, records: list[dict], batches: list[dict], model: str,
                    prompt_hash: str, schema_hash: str, reused: int, generated: int,
                    failures: int, invocation_cost: float, total_cost: float, complete: bool) -> dict:
    for record, anchor in zip(records, anchors(records)):
        record["anchor"] = anchor
    return {
        "report_schema_version": REPORT_SCHEMA_VERSION, "report_name": name,
        "complete": complete, "batches": batches,
        "summary": {"works": len({r["work_id"] for r in records}),
                    "occurrences": len(records), "enrichments_reused": reused,
                    "enrichments_generated": generated, "failures": failures,
                    "invocation_model_cost_usd": invocation_cost,
                    "total_recorded_model_cost_usd": total_cost,
                    "enrichment_model": model, "prompt_version": PROMPT_VERSION,
                    "prompt_sha256": prompt_hash, "schema_version": PROMPT_VERSION,
                    "schema_sha256": schema_hash},
        "indices": build_indices(records), "occurrences": records,
    }


def markdown_link_list(items: list[dict] | list[str]) -> str:
    if not items:
        return "None"
    if isinstance(items[0], str):
        return ", ".join(f"[{item}](#{item})" for item in items)
    return ", ".join(f"[{item['title']} ({item['count']})](#{item['anchors'][0]})" for item in items)


def render_markdown(report: dict) -> str:
    status = "complete" if report["complete"] else "INCOMPLETE — missing or failed enrichments"
    summary = report["summary"]
    lines = [f"# Corpus report: {report['report_name']}", "", f"> **Status: {status}**", "",
             "## Summary", "", f"- **Works:** {summary['works']}",
             f"- **Occurrences:** {summary['occurrences']}",
             f"- **Enrichment model:** `{summary['enrichment_model']}`",
             f"- **Invocation cost:** USD {summary['invocation_model_cost_usd']:.6f}", "",
             f"- **Total recorded enrichment cost:** USD {summary['total_recorded_model_cost_usd']:.6f}", "",
             "## Index", "", "### By work", "",
             markdown_link_list(report["indices"]["by_work"]), "", "### By language", ""]
    language_names = {"en": "English", "fr": "French", "no": "Norwegian",
                      "sv": "Swedish", "de": "German"}
    for item in report["indices"]["by_language"]:
        lines.append(f"- **{language_names.get(item['language'], item['language'])} ({item['count']}):** "
                     + markdown_link_list(item["anchors"]))
    lines.extend(["", "### Interesting cases", ""])
    for name, values in report["indices"]["interesting"].items():
        rendered = report["indices"].get("interesting_notes", {}).get(name) if values is None \
            else markdown_link_list(values)
        lines.append(f"- **{name}:** {rendered}")
    lines.extend(["", f"_{report['indices']['interesting_notes']['status_policy']}_", ""])
    for record in report["occurrences"]:
        annotation, enrichment = record["annotation"], record.get("enrichment")
        lines.extend([f"<a id=\"{record['anchor']}\"></a>", "",
                      f"## {record['title']} — occurrence {record['occurrence_index']}", "",
                      f"- **Occurrence ID:** `{record['occurrence_id']}`",
                      f"- **Author:** {record['author']}", f"- **Language:** `{record['language']}`",
                      f"- **Source:** `{record['source_id']}`",
                      f"- **Position:** {record['source_location'].get('relative_position', 'unknown')}",
                      f"- **Utterance status:** `{annotation['utterance_status']['status']}` — "
                      f"{annotation['utterance_status']['description']}", "", "### Original passage", "",
                      record["original_passage"], "", "### English translation", ""])
        if not enrichment:
            lines.append("**Missing enrichment. This report is incomplete.**")
        elif enrichment["translation_en"] is None:
            lines.append("Not required (source language is English).")
        else:
            lines.append(enrichment["translation_en"])
        lines.extend(["", "### Larger context", "",
                      enrichment["larger_context_summary"] if enrichment else "**Missing enrichment.**",
                      "", "### Annotation", ""])
        for key in "PTEO":
            lines.append(f"- **{key}:** {annotation['scores'][key]}")
        lines.extend([f"- **Confidence:** {annotation['confidence']}",
                      f"- **Ontology fit:** `{annotation['ontology_fit']}`",
                      f"- **Ambiguity:** {annotation['ambiguity_note'] or 'None recorded.'}", "",
                      "### Commentary", "",
                      enrichment["interpretive_commentary"] if enrichment else "**Missing enrichment.**",
                      "", "### Provenance", "",
                      f"- **Source record:** `{record['source_provenance']}`",
                      f"- **Batch/run:** `{record['batch_run']}`",
                      f"- **Annotation output:** `{record['annotation_provenance']['path']}`",
                      f"- **Annotation version/model:** `v{record['annotation_provenance']['annotation_version']}` / "
                      f"`{record['annotation_provenance']['model']}`",
                      f"- **Annotation prompt/schema:** `{record['annotation_provenance']['prompt_sha256']}` / "
                      f"`{record['annotation_provenance']['schema_sha256']}`", ""])
    return "\n".join(lines).rstrip() + "\n"


def write_text_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def build(*, repo_root: Path, name: str, batch_runs: list[Path], model_alias: str,
          output_root: Path, prompt_path: Path, schema_path: Path, catalog_path: Path,
          offline: bool, force_enrichment: bool, endpoint: str,
          caller=call_model) -> tuple[dict, int]:
    prompt_text = prompt_path.read_text(encoding="utf-8")
    schema_text = schema_path.read_text(encoding="utf-8")
    schema = json.loads(schema_text)
    prompt_hash, schema_hash = sha256_bytes(prompt_text.encode()), sha256_bytes(schema_text.encode())
    api_model, pricing = resolve_model(catalog_path, model_alias, date.today())
    records, batches = collect_occurrences(batch_runs, repo_root)
    work_dir = output_root / name / "work"
    request_dir, cache_dir = work_dir / "requests", output_root / "cache"
    reused = generated = failures = 0
    invocation_cost = 0.0
    pending = []
    for record in records:
        identity = cache_identity(record, api_model, prompt_hash, schema_hash)
        cached, directory = existing_cache(cache_dir, identity, record["language"])
        payload = request_payload(prompt_text, schema, api_model, enrichment_input(record))
        write_json(request_dir / f"{record['language']}--{record['report_occurrence_key']}--{record['occurrence_id']}.json",
                   {"cache_identity": identity, "request": payload})
        if cached is not None and not force_enrichment:
            record["enrichment"] = cached
            reused += 1
        else:
            pending.append((record, identity, directory, payload))
    expected = sum(batch["occurrences"] for batch in batches)
    print("Selected batch runs:")
    for batch in batches:
        print(f"  {batch['batch_id']}: {batch['path']} ({batch['occurrences']} occurrences)")
    print(f"Works: {len({r['work_id'] for r in records})}")
    print(f"Occurrences: {len(records)} (expected {expected}, unique {len(records)})")
    print(f"Languages: {', '.join(dict.fromkeys(r['language'] for r in records))}")
    print(f"Cache hits: {reused}")
    print(f"Cache misses: {len(pending)}")
    print(f"Model calls required: {len(pending)}")
    print("Invalid source records: 0")
    print(f"Estimated maximum output tokens: {len(pending) * 1200}")
    estimated_output_cost = len(pending) * 1200 * pricing["usd_per_million_tokens"]["output"] / 1_000_000
    print(f"Rough output-token-only maximum cost: USD {estimated_output_cost:.6f}")
    print(f"Expected JSON: {output_root / (name + '.json')}")
    print(f"Expected Markdown: {output_root / (name + '.md')}")
    if not offline and pending:
        api_key = os.environ.get("OPENAI_" + "API_KEY")
        if not api_key:
            raise ValueError("set the OpenAI API credential before a non-offline model run")
        for record, identity, directory, payload in pending:
            enrichment, cost = enrich_one(record=record, identity=identity, directory=directory,
                                           payload=payload, api_key=api_key, endpoint=endpoint,
                                           pricing=pricing, caller=caller)
            invocation_cost += cost
            if enrichment is None:
                failures += 1
            else:
                record["enrichment"] = enrichment
                generated += 1
    complete = all(record.get("enrichment") is not None for record in records)
    total_cost = recorded_cache_cost(cache_dir)
    report = report_document(name=name, records=records, batches=batches, model=api_model,
                             prompt_hash=prompt_hash, schema_hash=schema_hash, reused=reused,
                             generated=generated, failures=failures,
                             invocation_cost=invocation_cost, total_cost=total_cost, complete=complete)
    report_path, markdown_path = output_root / f"{name}.json", output_root / f"{name}.md"
    write_json(report_path, report)
    write_text_atomic(markdown_path, render_markdown(report))
    summary = {"report_name": name, **report["summary"], "json_path": str(report_path),
               "markdown_path": str(markdown_path),
               "completeness_status": "complete" if complete else "incomplete"}
    write_json(output_root / f"{name}.summary.json", summary)
    print(f"Enrichments reused: {reused}; newly generated: {generated}; failures: {failures}")
    print(f"Invocation model cost: USD {invocation_cost:.6f}")
    print(f"Total recorded enrichment cost: USD {total_cost:.6f}")
    print(f"Completeness: {summary['completeness_status']}")
    return report, 0 if complete else 2


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True, help="safe report basename")
    parser.add_argument("--batch-run", action="append", required=True, type=Path,
                        help="explicit completed batch-run directory; repeat in report order")
    parser.add_argument("--enrichment-model", required=True, help="alias in config/api_models.json")
    parser.add_argument("--offline", action="store_true", help="prepare and render without model calls")
    parser.add_argument("--force-enrichment", action="store_true",
                        help="regenerate all enrichments; unrelated to deterministic rendering")
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--prompt", type=Path, default=DEFAULT_PROMPT)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--model-catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--endpoint", default="https://api.openai.com/v1/responses")
    args = parser.parse_args(argv)
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", args.name):
        parser.error("--name must be a safe basename")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repo_root = REPOSITORY_ROOT
    try:
        _, status = build(
            repo_root=repo_root, name=args.name,
            batch_runs=[repository_path(path, repo_root).resolve() for path in args.batch_run],
            model_alias=args.enrichment_model,
            output_root=repository_path(args.output_root, repo_root),
            prompt_path=repository_path(args.prompt, repo_root),
            schema_path=repository_path(args.schema, repo_root),
            catalog_path=repository_path(args.model_catalog, repo_root),
            offline=args.offline, force_enrichment=args.force_enrichment, endpoint=args.endpoint,
        )
        return status
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
