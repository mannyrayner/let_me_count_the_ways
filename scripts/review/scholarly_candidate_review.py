#!/usr/bin/env python3
"""Run, validate, and render the provisional AI candidate-membership review."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts.api.call_responses import calculate_cost, output_text, resolve_model, structured_output_format

DECISIONS = {"KEEP", "EXCLUDE", "UNCERTAIN"}
REASONS = {
    "VALID_EXPLICIT_LOVE_I_YOU",
    "EXCLUDE_NOT_LOVE_SENSE", "EXCLUDE_SECOND_PERSON_NOT_TARGET",
    "EXCLUDE_FIRST_PERSON_NOT_EXPERIENCER", "EXCLUDE_SYNTACTIC_FALSE_POSITIVE",
    "EXCLUDE_TEXT_CORRUPTION", "EXCLUDE_OTHER",
    "UNCERTAIN_NEEDS_WIDER_CONTEXT", "UNCERTAIN_OTHER",
}
REASON_PREFIX = {"KEEP": "VALID_", "EXCLUDE": "EXCLUDE_", "UNCERTAIN": "UNCERTAIN_"}
PROMPT_VERSION = "scholarly_candidate_review_v1"
SCHEMA_VERSION = "1.0"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def candidates(root: Path) -> list[dict]:
    rows = []
    for path in sorted((root / "works").glob("*/candidates.jsonl")):
        rows.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line)
    return rows


def review_paths(root: Path) -> list[Path]:
    return sorted((root / "works").glob("*/review.jsonl"))


def reviews(root: Path) -> list[dict]:
    rows = []
    for path in review_paths(root):
        rows.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line)
    return rows


def candidate_input(row: dict, work: dict | None = None) -> dict:
    return {
        "work_metadata": work or {"work_id": row["work_id"]},
        "language": row["language"], "matched_text": row["match"],
        "local_extracted_context": row["context"],
        "form_metadata": {key: row.get(key) for key in (
            "form_family", "polarity", "tense_aspect", "temporal_modifier", "syntactic_family")},
        "pattern_metadata": {key: row.get(key) for key in (
            "pattern_version", "pattern_id", "extraction_tool_version")},
    }


def validate_record(row: dict) -> list[str]:
    oid = row.get("occurrence_id", "<missing>")
    required = {"occurrence_id", "work_id", "decision", "reason_code", "confidence",
                "review_note", "review_model", "review_prompt_version", "reviewed_at"}
    errors = [f"{oid}: missing {sorted(required - set(row))}"] if required - set(row) else []
    if row.get("decision") not in DECISIONS:
        errors.append(f"{oid}: invalid decision")
    if row.get("reason_code") not in REASONS:
        errors.append(f"{oid}: invalid reason code")
    elif row.get("decision") in DECISIONS and not row["reason_code"].startswith(REASON_PREFIX[row["decision"]]):
        errors.append(f"{oid}: reason code is incompatible with decision")
    confidence = row.get("confidence")
    if isinstance(confidence, bool) or not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
        errors.append(f"{oid}: confidence must be a number from 0 through 1")
    if row.get("review_prompt_version") != PROMPT_VERSION:
        errors.append(f"{oid}: wrong prompt version")
    for field in ("work_id", "review_note", "review_model", "reviewed_at"):
        if not isinstance(row.get(field), str) or not row[field].strip():
            errors.append(f"{oid}: {field} must be a nonempty string")
    return errors


def validate(candidate_roots: list[Path], review_roots: list[Path], expected_total: int | None = None) -> tuple[list[dict], list[dict]]:
    source = [row for root in candidate_roots for row in candidates(root)]
    reviewed = [row for root in review_roots for row in reviews(root)]
    source_ids = [row["occurrence_id"] for row in source]
    review_ids = [row.get("occurrence_id") for row in reviewed]
    errors = []
    for label, ids in (("candidate", source_ids), ("review", review_ids)):
        duplicates = sorted(key for key, count in Counter(ids).items() if count > 1)
        if duplicates:
            errors.append(f"duplicate {label} IDs: {duplicates}")
    unknown = sorted(set(review_ids) - set(source_ids))
    missing = sorted(set(source_ids) - set(review_ids))
    if unknown: errors.append(f"unknown review IDs: {unknown}")
    if missing: errors.append(f"missing review IDs: {missing}")
    by_id = {row["occurrence_id"]: row for row in source}
    for row in reviewed:
        errors.extend(validate_record(row))
        if row.get("occurrence_id") in by_id and row.get("work_id") != by_id[row["occurrence_id"]]["work_id"]:
            errors.append(f"{row['occurrence_id']}: work_id does not match candidate")
    if expected_total is not None and len(source) != expected_total:
        errors.append(f"expected {expected_total} candidates, found {len(source)}")
    if errors:
        raise ValueError("invalid scholarly review:\n- " + "\n- ".join(errors))
    return source, reviewed


def call_model(*, prompt: str, schema: dict, payload_input: dict, model: str, endpoint: str, api_key: str) -> tuple[dict, dict]:
    body = {
        "model": model, "temperature": 0,
        "input": prompt + "\n\n## Candidate\n\n" + json.dumps(payload_input, ensure_ascii=False),
        "text": structured_output_format(schema, "scholarly_candidate_review"),
    }
    request = urllib.request.Request(endpoint, data=json.dumps(body).encode(), headers={
        "Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            raw = json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"API error {exc.code}: {exc.read().decode(errors='replace')}") from exc
    return json.loads(output_text(raw)), raw.get("usage", {})


def run(candidate_root: Path, output_root: Path, prompt_path: Path, schema_path: Path,
        model_alias: str, catalog_path: Path, endpoint: str) -> None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("set OPENAI_API_KEY before running review")
    api_model, pricing = resolve_model(catalog_path, model_alias, date.today())
    prompt, schema = prompt_path.read_text(encoding="utf-8"), read_json(schema_path)
    existing = {row["occurrence_id"]: row for row in reviews(output_root)}
    for candidate in candidates(candidate_root):
        oid = candidate["occurrence_id"]
        if oid in existing:
            old = existing[oid]
            if old["review_model"] == api_model and old["review_prompt_version"] == PROMPT_VERSION:
                continue
            raise ValueError(f"{oid}: earlier review exists with a different model or prompt")
        answer, usage = call_model(prompt=prompt, schema=schema, payload_input=candidate_input(candidate),
                                   model=api_model, endpoint=endpoint, api_key=api_key)
        record = {"occurrence_id": oid, "work_id": candidate["work_id"], **answer,
                  "review_model": api_model, "review_prompt_version": PROMPT_VERSION,
                  "reviewed_at": datetime.now(timezone.utc).isoformat()}
        cost = calculate_cost(usage, pricing)
        record["model_usage"] = {key: cost[key] for key in (
            "input_tokens", "cached_input_tokens", "output_tokens")}
        record["estimated_cost_usd"] = cost["estimated_total_cost"]
        errors = validate_record(record)
        if errors: raise ValueError("; ".join(errors))
        path = output_root / "works" / candidate["work_id"] / "review.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
    complete = reviews(output_root)
    totals = {key: sum(row.get("model_usage", {}).get(key, 0) for row in complete)
              for key in ("input_tokens", "cached_input_tokens", "output_tokens")}
    totals["estimated_total_cost_usd"] = sum(row.get("estimated_cost_usd", 0) for row in complete)
    write_json(output_root / "usage.json", {"model": api_model, "model_alias": model_alias,
        "prompt_version": PROMPT_VERSION, "temperature": 0, "candidates_reviewed": len(complete), **totals})
    write_json(output_root / "manifest.json", {
        "schema_version": SCHEMA_VERSION,
        "status": "provisional_ai_review_pending_human_review",
        "candidate_input": str(candidate_root), "candidate_count": len(candidates(candidate_root)),
        "review_count": len(complete), "model": api_model, "model_alias": model_alias,
        "prompt_version": PROMPT_VERSION, "temperature": 0,
        "resumption_key": ["occurrence_id", "model", "prompt_version"],
    })


def render(candidate_roots: list[Path], review_roots: list[Path], public_output: Path,
           private_work_id: str | None = "mcmillan-error-of-understanding") -> dict:
    source, reviewed = validate(candidate_roots, review_roots)
    source_by_id = {row["occurrence_id"]: row for row in source}
    counts = Counter(row["decision"] for row in reviewed)
    reasons = Counter(row["reason_code"] for row in reviewed if row["decision"] == "EXCLUDE")
    works = []
    for work_id in sorted({row["work_id"] for row in source}):
        candidates_for_work = [row for row in source if row["work_id"] == work_id]
        reviews_for_work = [row for row in reviewed if row["work_id"] == work_id]
        wc = Counter(row["decision"] for row in reviews_for_work)
        works.append({"work_id": work_id, "raw_candidate_count": len(candidates_for_work),
                      **{key: wc[key] for key in ("KEEP", "EXCLUDE", "UNCERTAIN")}})
    summary = {"schema_version": SCHEMA_VERSION, "status": "provisional_ai_review_pending_human_review",
               "prompt_version": PROMPT_VERSION, "candidate_count": len(source),
               **{key: counts[key] for key in ("KEEP", "EXCLUDE", "UNCERTAIN")},
               "exclusions_by_reason_code": dict(sorted(reasons.items())), "works": works}
    write_json(public_output / "summary.json", summary)
    lines = ["# Provisional AI scholarly review", "", "**Status:** AI first pass; pending human review.", "",
             "| Work | Raw | KEEP | EXCLUDE | UNCERTAIN |", "| --- | ---: | ---: | ---: | ---: |"]
    lines += [f"| `{w['work_id']}` | {w['raw_candidate_count']} | {w['KEEP']} | {w['EXCLUDE']} | {w['UNCERTAIN']} |" for w in works]
    lines += [f"| **Total** | **{len(source)}** | **{counts['KEEP']}** | **{counts['EXCLUDE']}** | **{counts['UNCERTAIN']}** |", "", "## Exclusions by reason", ""]
    lines += [f"- `{key}`: {value}" for key, value in sorted(reasons.items())] or ["- None"]
    (public_output / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    rank = {"UNCERTAIN": 0, "EXCLUDE": 1, "KEEP": 2}
    ordered = sorted(reviewed, key=lambda row: (rank[row["decision"]], row["confidence"], row["work_id"], row["occurrence_id"]))
    sheet = public_output / "human_inspection.tsv"
    sheet.parent.mkdir(parents=True, exist_ok=True)
    with sheet.open("w", encoding="utf-8", newline="") as stream:
        fields = ["occurrence_id", "work", "language", "match", "short_context", "ai_decision", "confidence", "reason_code", "review_note"]
        writer = csv.DictWriter(stream, fields, delimiter="\t", lineterminator="\n"); writer.writeheader()
        for review in ordered:
            candidate = source_by_id[review["occurrence_id"]]
            if private_work_id and candidate["work_id"] == private_work_id: continue
            writer.writerow({"occurrence_id": review["occurrence_id"], "work": review["work_id"],
                "language": candidate["language"], "match": candidate["match"].replace("\n", " "),
                "short_context": " ".join(candidate["context"].split()), "ai_decision": review["decision"],
                "confidence": review["confidence"], "reason_code": review["reason_code"], "review_note": review["review_note"]})
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    run_parser = sub.add_parser("run")
    run_parser.add_argument("--candidates", type=Path, required=True); run_parser.add_argument("--output", type=Path, required=True)
    run_parser.add_argument("--prompt", type=Path, default=Path("prompts/review/scholarly_candidate_review_v1.md"))
    run_parser.add_argument("--schema", type=Path, default=Path("prompts/review/scholarly_candidate_review_schema_v1.json"))
    run_parser.add_argument("--model", default="5.6"); run_parser.add_argument("--model-catalog", type=Path, default=Path("config/api_models.json"))
    run_parser.add_argument("--endpoint", default="https://api.openai.com/v1/responses")
    validate_parser = sub.add_parser("validate"); validate_parser.add_argument("--candidates", type=Path, action="append", required=True)
    validate_parser.add_argument("--review", type=Path, action="append", required=True); validate_parser.add_argument("--expected-total", type=int)
    render_parser = sub.add_parser("render"); render_parser.add_argument("--candidates", type=Path, action="append", required=True)
    render_parser.add_argument("--review", type=Path, action="append", required=True); render_parser.add_argument("--output", type=Path, required=True)
    render_parser.add_argument("--include-private-in-sheet", action="store_true",
                               help="only for a Git-ignored private output tree")
    args = parser.parse_args()
    if args.command == "run": run(args.candidates, args.output, args.prompt, args.schema, args.model, args.model_catalog, args.endpoint)
    elif args.command == "validate":
        source, reviewed = validate(args.candidates, args.review, args.expected_total)
        print(f"valid: {len(reviewed)}/{len(source)} candidates have exactly one provisional AI review")
    else: render(args.candidates, args.review, args.output,
                 private_work_id=None if args.include_private_in_sheet else "mcmillan-error-of-understanding")


if __name__ == "__main__":
    main()
