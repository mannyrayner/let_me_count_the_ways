#!/usr/bin/env python3
"""Audit a completed single-text pipeline run before it is committed."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts.pipeline.run_single_text_pipeline import read_json, read_jsonl, resolve_annotation_contract


REQUIRED_VALID_ATTEMPT_FILES = {
    "metadata.json", "request.json", "response.json", "output.txt", "output.json",
    "validation.json", "cost.json", "status.json",
}


def compatible_valid_attempts(annotation_root: Path, manifest: dict) -> list[Path]:
    found = []
    for status_path in sorted(annotation_root.glob("attempt-*/status.json")):
        status = read_json(status_path)
        combination = status.get("combination", {})
        if (
            status.get("state") == "valid"
            and combination.get("annotation_version") == manifest["annotation_version"]
            and combination.get("model") == manifest["api_model"]
            and combination.get("prompt_sha256") == manifest["prompt_sha256"]
            and combination.get("schema_sha256") == manifest["schema_sha256"]
        ):
            found.append(status_path.parent)
    return found


def audit_run(run_dir: Path, repo_root: Path, expected_occurrences: int | None = None) -> dict:
    run_dir = run_dir.resolve()
    manifest = read_json(run_dir / "manifest.json")
    summary = read_json(run_dir / "summary.json")
    passages = read_jsonl(run_dir / "extraction/passages.jsonl")
    occurrence_ids = [passage["occurrence_id"] for passage in passages]

    if manifest["status"] != "complete":
        raise ValueError(f"run status is {manifest['status']!r}, not 'complete'")
    if expected_occurrences is not None and len(passages) != expected_occurrences:
        raise ValueError(f"expected {expected_occurrences} passages, found {len(passages)}")
    if len(occurrence_ids) != len(set(occurrence_ids)):
        raise ValueError("extraction contains duplicate occurrence IDs")
    if manifest["extracted_occurrences"] != len(passages):
        raise ValueError("manifest extracted-occurrence count does not match extraction")
    if manifest["valid_occurrences"] != len(passages):
        raise ValueError("manifest does not report one valid result per occurrence")
    if summary["valid_occurrences"] != len(passages):
        raise ValueError("summary valid-occurrence count does not match extraction")
    if not (run_dir / "report.md").is_file():
        raise ValueError("report.md is missing")

    contract = resolve_annotation_contract(manifest["annotation_version"], repo_root)
    if contract.prompt_sha256 != manifest["prompt_sha256"]:
        raise ValueError("current prompt hash does not match the run manifest")
    if contract.schema_sha256 != manifest["schema_sha256"]:
        raise ValueError("current schema hash does not match the run manifest")

    for occurrence_id in occurrence_ids:
        input_path = run_dir / "inputs" / f"{occurrence_id}.json"
        if not input_path.is_file():
            raise ValueError(f"prepared input is missing: {input_path}")
        prepared = read_json(input_path)
        if prepared.get("annotation_version") != manifest["annotation_version"]:
            raise ValueError(f"input annotation version differs for {occurrence_id}")
        if prepared.get("occurrence", {}).get("occurrence_id") != occurrence_id:
            raise ValueError(f"input occurrence ID differs for {occurrence_id}")

        attempts = compatible_valid_attempts(run_dir / "annotations" / occurrence_id, manifest)
        if not attempts:
            raise ValueError(f"no compatible valid attempt for {occurrence_id}")
        selected = attempts[-1]
        missing = REQUIRED_VALID_ATTEMPT_FILES - {path.name for path in selected.iterdir()}
        if missing:
            raise ValueError(f"valid attempt {selected} lacks files: {sorted(missing)}")
        validation = read_json(selected / "validation.json")
        if validation.get("valid") is not True:
            raise ValueError(f"validation record is not valid: {selected}")
        output = read_json(selected / "output.json")
        contract.validator(output, occurrence_id)

    return {
        "run_id": manifest["run_id"],
        "work_id": manifest["work_id"],
        "source_id": manifest["source_id"],
        "annotation_version": manifest["annotation_version"],
        "model": manifest["api_model"],
        "occurrences": len(passages),
        "attempts": manifest["attempt_counts"]["attempts"],
        "failed_or_invalid_attempts": manifest["invalid_or_failed_attempts"],
        "unresolved_failed_occurrences": manifest.get("unresolved_failed_occurrences", 0),
        "estimated_total_cost_usd": manifest["usage_and_cost"]["estimated_total_cost_usd"],
        "status": manifest["status"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--expected-occurrences", type=int)
    args = parser.parse_args()
    try:
        result = audit_run(args.run_dir, REPOSITORY_ROOT, args.expected_occurrences)
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"Pipeline run audit failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
