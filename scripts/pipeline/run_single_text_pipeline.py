#!/usr/bin/env python3
"""Run the staged, resumable pipeline for one approved text source."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import unicodedata
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Callable

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts.annotation.validate_classification import validate, validate_v0_2
from scripts.api.call_responses import calculate_cost, output_text, resolve_model
from scripts.extraction.extract_passages import extract, load_patterns


ANNOTATION_FILES = {
    "0.1": (
        Path("prompts/annotation/classify_passage_v0_1.md"),
        Path("prompts/annotation/classification_schema_v0_1.json"),
        validate,
    ),
    "0.2": (
        Path("prompts/annotation/classify_passage_v0_2.md"),
        Path("prompts/annotation/classification_schema_v0_2.json"),
        validate_v0_2,
    ),
}
APPROVED_STATUSES = {"approved_for_development_processing"}
CHAPTER_PATTERN = re.compile(r"(?m)^CHAPTER ([^\n]+?)\s*$")


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as stream:
        for record in records:
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")


def git_commit() -> str | None:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


@dataclass(frozen=True)
class AnnotationContract:
    version: str
    prompt_path: Path
    schema_path: Path
    validator: Callable[[dict, str | None], None]
    prompt: str
    schema: str
    prompt_sha256: str
    schema_sha256: str


def resolve_annotation_contract(version: str, repo_root: Path) -> AnnotationContract:
    try:
        prompt_relative, schema_relative, validator = ANNOTATION_FILES[version]
    except KeyError as exc:
        raise ValueError(f"unsupported annotation version {version!r}") from exc
    prompt_path = repo_root / prompt_relative
    schema_path = repo_root / schema_relative
    prompt = prompt_path.read_text(encoding="utf-8")
    schema = schema_path.read_text(encoding="utf-8")
    return AnnotationContract(
        version=version,
        prompt_path=prompt_relative,
        schema_path=schema_relative,
        validator=validator,
        prompt=prompt,
        schema=schema,
        prompt_sha256=sha256_bytes(prompt.encode()),
        schema_sha256=sha256_bytes(schema.encode()),
    )


def resolve_source(provenance_path: Path, repo_root: Path) -> tuple[dict, Path, bytes]:
    provenance = read_json(provenance_path)
    if provenance.get("review_status") not in APPROVED_STATUSES:
        raise ValueError(f"source is not approved: {provenance.get('review_status')!r}")
    required = {"work_id", "source_id", "author", "title", "language", "sha256", "local_path"}
    missing = required - set(provenance)
    if missing:
        raise ValueError(f"provenance record lacks required fields: {sorted(missing)}")
    source_path = repo_root / provenance["local_path"]
    source_bytes = source_path.read_bytes()
    actual_hash = sha256_bytes(source_bytes)
    if actual_hash != provenance["sha256"]:
        raise ValueError(
            f"source hash mismatch: provenance has {provenance['sha256']}, found {actual_hash}"
        )
    return provenance, source_path, source_bytes


def chapter_locations(text: str) -> list[tuple[int, str]]:
    return [(match.start(), f"CHAPTER {match.group(1).strip()}") for match in CHAPTER_PATTERN.finditer(text)]


def chapter_at(locations: list[tuple[int, str]], offset: int) -> str | None:
    preceding = [label for position, label in locations if position <= offset]
    return preceding[-1] if preceding else None


def enrich_occurrence(record: dict, provenance: dict, source_text: str) -> dict:
    start = record["start"]
    source_length = len(source_text)
    locations = chapter_locations(source_text)
    return {
        "annotation_version": None,
        "occurrence": record,
        "metadata": {
            "title": provenance["title"],
            "author": provenance["author"],
            "language": provenance["language"],
            "work_id": provenance["work_id"],
            "source_id": provenance["source_id"],
            "edition_source": {
                "repository": provenance.get("repository"),
                "repository_ebook_id": provenance.get("repository_ebook_id"),
                "source_url": provenance.get("source_url"),
                "retrieved_at": provenance.get("retrieved_at"),
            },
            "location": {
                "source_start": start,
                "source_end": record["end"],
                "source_length_characters": source_length,
                "relative_position": round(start / source_length, 6) if source_length else 0.0,
                "chapter_or_section": chapter_at(locations, start),
            },
            "supplied_context": {
                "context_start": record["context_start"],
                "context_end": record["context_end"],
                "characters": record["context_end"] - record["context_start"],
                "characters_before_match": start - record["context_start"],
                "characters_after_match": record["context_end"] - record["end"],
            },
        },
    }


def extraction_fingerprint(source_hash: str, patterns_path: Path, pattern_version: str,
                           context_chars: int, extractor_path: Path) -> dict:
    return {
        "source_sha256": source_hash,
        "patterns_sha256": sha256_file(patterns_path),
        "pattern_version": pattern_version,
        "context_characters": context_chars,
        "extractor_sha256": sha256_file(extractor_path),
    }


def next_attempt_directory(annotation_root: Path) -> Path:
    existing = [
        int(path.name.split("-")[1])
        for path in annotation_root.glob("attempt-*")
        if path.is_dir() and path.name.split("-")[-1].isdigit()
    ]
    return annotation_root / f"attempt-{max(existing, default=0) + 1:03d}"


def valid_completion(annotation_root: Path, fingerprint: dict) -> bool:
    for status_path in sorted(annotation_root.glob("attempt-*/status.json"), reverse=True):
        status = read_json(status_path)
        if status.get("state") == "valid" and status.get("combination") == fingerprint:
            return True
    return False


class ApiAnnotator:
    """Minimal Responses API transport; orchestration and persistence remain in the runner."""

    def __init__(self, api_key: str, endpoint: str = "https://api.openai.com/v1/responses"):
        self.api_key = api_key
        self.endpoint = endpoint

    def __call__(self, request_payload: dict) -> dict:
        request = urllib.request.Request(
            self.endpoint,
            data=json.dumps(request_payload, ensure_ascii=False).encode(),
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=300) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"API HTTP {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"API network error: {exc}") from exc


def summarize_attempts(run_dir: Path, occurrence_ids: list[str]) -> tuple[dict, dict]:
    states = {"valid": 0, "invalid": 0, "api_failure": 0, "parse_failure": 0}
    usage = {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0}
    total_cost = 0.0
    attempts = 0
    for occurrence_id in occurrence_ids:
        for attempt in (run_dir / "annotations" / occurrence_id).glob("attempt-*"):
            status_path = attempt / "status.json"
            if not status_path.exists():
                continue
            attempts += 1
            state = read_json(status_path).get("state")
            if state in states:
                states[state] += 1
            cost_path = attempt / "cost.json"
            if cost_path.exists():
                cost = read_json(cost_path)
                usage["input_tokens"] += cost.get("input_tokens", 0)
                usage["cached_input_tokens"] += cost.get("cached_input_tokens", 0)
                usage["output_tokens"] += cost.get("output_tokens", 0)
                total_cost += cost.get("estimated_total_cost", 0.0)
    return {"attempts": attempts, **states}, {**usage, "estimated_total_cost_usd": total_cost}


def failure_record(occurrence_id: str, state: str, error: Exception, attempt: int,
                   timestamp: str) -> dict:
    stages = {"api_failure": "annotation", "parse_failure": "parsing", "invalid": "validation"}
    return {
        "occurrence_id": occurrence_id,
        "stage": stages[state],
        "error_type": type(error).__name__,
        "error_message": str(error),
        "attempt_number": attempt,
        "timestamp": timestamp,
        "retry_appropriate": True,
        "retry_state": "pending_manual_or_resume",
        "state": state,
    }


def run_pipeline(*, repo_root: Path, provenance_path: Path, patterns_path: Path,
                 annotation_version: str, model_alias: str, output_root: Path,
                 run_dir: Path | None = None, context_chars: int = 1000,
                 dry_run: bool = False, force: bool = False,
                 annotator: Callable[[dict], dict] | None = None,
                 now: Callable[[], datetime] = utc_now) -> Path:
    repo_root = repo_root.resolve()
    provenance_path = (repo_root / provenance_path).resolve() if not provenance_path.is_absolute() else provenance_path
    patterns_path = (repo_root / patterns_path).resolve() if not patterns_path.is_absolute() else patterns_path
    output_root = (repo_root / output_root).resolve() if not output_root.is_absolute() else output_root
    contract = resolve_annotation_contract(annotation_version, repo_root)
    provenance, source_path, source_bytes = resolve_source(provenance_path, repo_root)
    # Match the extraction CLI's text-mode universal-newline behavior so offsets
    # and occurrence IDs remain compatible with existing inventories.
    source_text = unicodedata.normalize("NFC", source_path.read_text(encoding="utf-8"))
    pattern_version, patterns = load_patterns(patterns_path, provenance["language"])
    model_catalog = repo_root / "config/api_models.json"
    api_model, pricing = resolve_model(model_catalog, model_alias, now().date())
    started = now()
    run_id = started.strftime("%Y%m%dT%H%M%SZ")
    if run_dir is None:
        run_dir = output_root / provenance["source_id"] / run_id
        suffix = 1
        while run_dir.exists():
            run_dir = output_root / provenance["source_id"] / f"{run_id}-{suffix}"
            suffix += 1
    elif not run_dir.is_absolute():
        run_dir = (repo_root / run_dir).resolve()
    run_dir.mkdir(parents=True, exist_ok=True)

    previous_manifest_path = run_dir / "manifest.json"
    previous_manifest = read_json(previous_manifest_path) if previous_manifest_path.exists() else None
    if previous_manifest:
        expected = {
            "source_id": provenance["source_id"],
            "source_sha256": provenance["sha256"],
            "search_pattern_version": pattern_version,
            "annotation_version": annotation_version,
            "model_alias": model_alias,
            "prompt_sha256": contract.prompt_sha256,
            "schema_sha256": contract.schema_sha256,
        }
        incompatible = {
            key: {"existing": previous_manifest.get(key), "requested": value}
            for key, value in expected.items()
            if previous_manifest.get(key) != value
        }
        if incompatible:
            raise ValueError(f"run directory is incompatible with requested configuration: {incompatible}")

    extractor_path = repo_root / "scripts/extraction/extract_passages.py"
    extraction_meta = extraction_fingerprint(
        provenance["sha256"], patterns_path, pattern_version, context_chars, extractor_path,
    )
    extraction_path = run_dir / "extraction/passages.jsonl"
    extraction_metadata_path = run_dir / "extraction/metadata.json"
    extraction_reused = False
    if extraction_path.exists() and extraction_metadata_path.exists():
        if read_json(extraction_metadata_path)["fingerprint"] != extraction_meta:
            raise ValueError("existing extraction is incompatible with this run configuration")
        records = read_jsonl(extraction_path)
        extraction_reused = True
    else:
        records = extract(
            source_text, provenance["language"], provenance["work_id"],
            provenance["source_id"], pattern_version, patterns, context_chars,
        )
        write_jsonl(extraction_path, records)
        write_json(extraction_metadata_path, {
            "fingerprint": extraction_meta,
            "inventory_sha256": sha256_file(extraction_path),
            "occurrence_count": len(records),
        })

    source_reference = {
        "provenance_path": str(provenance_path.relative_to(repo_root)),
        "local_source_path": str(source_path.relative_to(repo_root)),
        "work_id": provenance["work_id"],
        "source_id": provenance["source_id"],
        "source_sha256": provenance["sha256"],
        "review_status": provenance["review_status"],
        "rights_note": provenance.get("rights_note"),
    }
    write_json(run_dir / "source_reference.json", source_reference)
    write_json(run_dir / "pricing_snapshot.json", pricing)

    inputs = []
    for record in records:
        prepared = enrich_occurrence(record, provenance, source_text)
        prepared["annotation_version"] = annotation_version
        input_path = run_dir / "inputs" / f"{record['occurrence_id']}.json"
        if input_path.exists():
            if read_json(input_path) != prepared:
                raise ValueError(f"existing prepared input is incompatible: {input_path}")
        else:
            write_json(input_path, prepared)
        inputs.append((record["occurrence_id"], prepared, input_path))

    combination = {
        "annotation_version": annotation_version,
        "model": api_model,
        "prompt_sha256": contract.prompt_sha256,
        "schema_sha256": contract.schema_sha256,
        "input_policy": "metadata-enriched-v0.1",
    }
    attempted_this_invocation = 0
    skipped_valid = 0
    if not dry_run:
        if annotator is None:
            api_key = os.environ.get("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY is required unless --dry-run is used")
            annotator = ApiAnnotator(api_key)
        for occurrence_id, prepared, _ in inputs:
            annotation_root = run_dir / "annotations" / occurrence_id
            if not force and valid_completion(annotation_root, combination):
                skipped_valid += 1
                continue
            attempt_dir = next_attempt_directory(annotation_root)
            attempt_dir.mkdir(parents=True)
            attempt_number = int(attempt_dir.name.split("-")[1])
            attempt_time = now().isoformat()
            combined_input = (
                f"{contract.prompt}\n\n## Input\n\n"
                f"{json.dumps(prepared, indent=2, ensure_ascii=False)}\n\n"
                f"## JSON Schema\n\n{contract.schema}"
            )
            request_payload = {"model": api_model, "input": combined_input}
            write_json(attempt_dir / "request.json", request_payload)
            write_json(attempt_dir / "metadata.json", {
                "occurrence_id": occurrence_id,
                "attempt_number": attempt_number,
                "created_at": attempt_time,
                "combination": combination,
                "parameters": {},
            })
            attempted_this_invocation += 1
            try:
                response = annotator(request_payload)
                write_json(attempt_dir / "response.json", response)
            except Exception as exc:  # Preserve per-occurrence transport failures and continue.
                failure = failure_record(occurrence_id, "api_failure", exc, attempt_number, now().isoformat())
                write_json(attempt_dir / "failure.json", failure)
                write_json(attempt_dir / "status.json", {"state": "api_failure", "combination": combination})
                write_json(run_dir / "failures" / f"{occurrence_id}-attempt-{attempt_number:03d}.json", failure)
                continue

            parsed_text = output_text(response)
            (attempt_dir / "output.txt").write_text(parsed_text + ("\n" if parsed_text else ""), encoding="utf-8")
            usage = response.get("usage", {})
            write_json(attempt_dir / "cost.json", calculate_cost(usage, pricing))
            try:
                parsed = json.loads(parsed_text)
            except (json.JSONDecodeError, TypeError) as exc:
                failure = failure_record(occurrence_id, "parse_failure", exc, attempt_number, now().isoformat())
                write_json(attempt_dir / "failure.json", failure)
                write_json(attempt_dir / "status.json", {"state": "parse_failure", "combination": combination})
                write_json(run_dir / "failures" / f"{occurrence_id}-attempt-{attempt_number:03d}.json", failure)
                continue
            write_json(attempt_dir / "output.json", parsed)
            try:
                contract.validator(parsed, occurrence_id)
            except (ValueError, TypeError) as exc:
                failure = failure_record(occurrence_id, "invalid", exc, attempt_number, now().isoformat())
                write_json(attempt_dir / "validation.json", {"valid": False, "error": str(exc)})
                write_json(attempt_dir / "failure.json", failure)
                write_json(attempt_dir / "status.json", {"state": "invalid", "combination": combination})
                write_json(run_dir / "failures" / f"{occurrence_id}-attempt-{attempt_number:03d}.json", failure)
                continue
            write_json(attempt_dir / "validation.json", {"valid": True, "schema_version": annotation_version})
            write_json(attempt_dir / "status.json", {"state": "valid", "combination": combination})

    occurrence_ids = [record["occurrence_id"] for record in records]
    attempt_counts, totals = summarize_attempts(run_dir, occurrence_ids)
    valid_occurrences = sum(
        valid_completion(run_dir / "annotations" / occurrence_id, combination)
        for occurrence_id in occurrence_ids
    )
    ended = now()
    if dry_run:
        status = "prepared"
    elif valid_occurrences == len(records):
        status = "complete"
    elif attempt_counts["attempts"]:
        status = "partial"
    else:
        status = "not_started"
    manifest = {
        "run_id": run_dir.name,
        "started_at": previous_manifest["started_at"] if previous_manifest else started.isoformat(),
        "ended_at": ended.isoformat(),
        "work_id": provenance["work_id"],
        "source_id": provenance["source_id"],
        "source_sha256": provenance["sha256"],
        "title": provenance["title"],
        "author": provenance["author"],
        "language": provenance["language"],
        "search_pattern_version": pattern_version,
        "annotation_version": annotation_version,
        "model_alias": model_alias,
        "api_model": api_model,
        "prompt_path": str(contract.prompt_path),
        "prompt_sha256": contract.prompt_sha256,
        "schema_path": str(contract.schema_path),
        "schema_sha256": contract.schema_sha256,
        "extraction_fingerprint": extraction_meta,
        "extraction_reused": extraction_reused,
        "extracted_occurrences": len(records),
        "attempted_this_invocation": attempted_this_invocation,
        "skipped_valid_this_invocation": skipped_valid,
        "valid_occurrences": valid_occurrences,
        "invalid_or_failed_attempts": (
            attempt_counts["invalid"] + attempt_counts["api_failure"] + attempt_counts["parse_failure"]
        ),
        "attempt_counts": attempt_counts,
        "usage_and_cost": totals,
        "software": {
            "git_commit": git_commit(),
            "runner_sha256": sha256_file(Path(__file__)),
            "extractor_sha256": extraction_meta["extractor_sha256"],
            "validator_sha256": sha256_file(repo_root / "scripts/annotation/validate_classification.py"),
            "model_catalog_sha256": sha256_file(model_catalog),
        },
        "dry_run": dry_run,
        "context_expansion_policy": "record_only_no_automatic_rerun",
        "status": status,
    }
    write_json(run_dir / "manifest.json", manifest)
    write_json(run_dir / "summary.json", {
        "run_id": run_dir.name,
        "text": f"{provenance['title']} by {provenance['author']}",
        "annotation_version": annotation_version,
        "model": api_model,
        "extracted_occurrences": len(records),
        "valid_occurrences": valid_occurrences,
        "failed_attempts": manifest["invalid_or_failed_attempts"],
        "estimated_total_cost_usd": totals["estimated_total_cost_usd"],
        "model_calls_needed": len(records) - valid_occurrences,
        "status": status,
        "artifacts": {
            "run_directory": str(run_dir.relative_to(repo_root)),
            "extraction": str(extraction_path.relative_to(repo_root)),
            "inputs": str((run_dir / "inputs").relative_to(repo_root)),
            "annotations": str((run_dir / "annotations").relative_to(repo_root)),
            "failures": str((run_dir / "failures").relative_to(repo_root)),
        },
    })
    return run_dir


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("provenance", type=Path, help="approved provenance JSON record")
    parser.add_argument("--patterns", type=Path, required=True, help="versioned search-pattern JSON")
    parser.add_argument("--annotation-version", required=True, choices=sorted(ANNOTATION_FILES))
    parser.add_argument("--model", required=True, help="alias in config/api_models.json")
    parser.add_argument("--output-root", type=Path, default=Path("results/pipeline_runs"))
    parser.add_argument("--run-dir", type=Path, help="resume a specific run directory")
    parser.add_argument("--context-chars", type=int, default=1000)
    parser.add_argument("--dry-run", action="store_true", help="prepare artifacts without API calls")
    parser.add_argument("--force", action="store_true", help="rerun completed annotations")
    args = parser.parse_args()
    if args.context_chars < 0:
        parser.error("--context-chars must be non-negative")
    repo_root = REPOSITORY_ROOT
    try:
        run_dir = run_pipeline(
            repo_root=repo_root,
            provenance_path=args.provenance,
            patterns_path=args.patterns,
            annotation_version=args.annotation_version,
            model_alias=args.model,
            output_root=args.output_root,
            run_dir=args.run_dir,
            context_chars=args.context_chars,
            dry_run=args.dry_run,
            force=args.force,
        )
    except ValueError as exc:
        parser.error(str(exc))
    print(run_dir)


if __name__ == "__main__":
    main()
