#!/usr/bin/env python3
"""Validate corpus-report completeness, provenance, and annotation immutability."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts.reporting.build_corpus_report import (  # noqa: E402
    collect_occurrences, repository_path, validate_enrichment,
)


def validate_report(report: dict, originals: list[dict], repo_root: Path) -> list[str]:
    errors = []
    records = report.get("occurrences", [])
    original_by_key = {item["report_occurrence_key"]: item for item in originals}
    report_keys = [item.get("report_occurrence_key") for item in records]
    if len(report_keys) != len(set(report_keys)):
        errors.append("report occurrence keys are not unique")
    if set(report_keys) != set(original_by_key):
        errors.append("report/source occurrence sets differ")
    anchors = [item.get("anchor") for item in records]
    if not all(anchors) or len(anchors) != len(set(anchors)):
        errors.append("anchors are missing or non-unique")
    for record in records:
        key = record.get("report_occurrence_key")
        original = original_by_key.get(key)
        if not original:
            continue
        if record.get("annotation") != original["annotation"]:
            errors.append(f"immutable annotation differs: {record.get('occurrence_id')}")
        errors.extend(f"{record.get('occurrence_id')}: {error}" for error in
                      validate_enrichment(record.get("enrichment"), record.get("language")))
        for pointer in (record.get("source_provenance"),
                        record.get("annotation_provenance", {}).get("path")):
            if not pointer or not repository_path(Path(pointer), repo_root).is_file():
                errors.append(f"unresolved provenance pointer for {record.get('occurrence_id')}: {pointer}")
    expected = sum(batch["occurrences"] for batch in report.get("batches", []))
    if len(records) != expected or report.get("summary", {}).get("occurrences") != expected:
        errors.append(f"occurrence count mismatch: expected {expected}, report has {len(records)}")
    should_complete = not errors and all(record.get("enrichment") for record in records)
    if report.get("complete") != should_complete:
        errors.append("report completeness flag is incorrect")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--batch-run", action="append", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        report = json.loads(args.report.read_text(encoding="utf-8"))
        originals, _ = collect_occurrences(
            [(path if path.is_absolute() else REPOSITORY_ROOT / path).resolve()
             for path in args.batch_run], REPOSITORY_ROOT)
        errors = validate_report(report, originals, REPOSITORY_ROOT)
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        errors = [str(exc)]
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"valid complete report: {len(report['occurrences'])} occurrences; annotations immutable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
