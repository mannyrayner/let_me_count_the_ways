#!/usr/bin/env python3
"""Audit and summarize the completed Step 17 pilot comparison artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_metric(metric: dict, expected_denominator: int, label: str) -> list[str]:
    errors = []
    count, denominator, proportion = (metric.get(key) for key in
                                       ("count", "denominator", "proportion"))
    if denominator != expected_denominator:
        errors.append(f"{label}: denominator is {denominator}, expected {expected_denominator}")
    if not isinstance(count, int) or not 0 <= count <= denominator:
        errors.append(f"{label}: invalid count {count!r}")
    expected = round(count / denominator, 6) if denominator else None
    if proportion != expected:
        errors.append(f"{label}: proportion is {proportion!r}, expected {expected!r}")
    return errors


def audit_summary(summary: dict, label: str) -> list[str]:
    errors = []
    total = summary.get("occurrences")
    if not isinstance(total, int) or total < 0:
        return [f"{label}: invalid occurrence total {total!r}"]
    missing_scores = summary.get("missing_data", {}).get("scores")
    score_denominator = total - missing_scores if isinstance(missing_scores, int) else -1
    for dimension in "PTEO":
        distribution = summary.get("score_distributions", {}).get(dimension, {})
        if set(distribution) != {str(value) for value in range(5)}:
            errors.append(f"{label}: incomplete {dimension} distribution")
        elif sum(distribution.values()) != score_denominator:
            errors.append(f"{label}: {dimension} distribution does not reconcile")
    for name in ("P_at_least_2", "E_at_least_2", "mixed_PTE"):
        errors.extend(audit_metric(summary.get(name, {}), score_denominator,
                                   f"{label}/{name}"))
    if sum(summary.get("ontology_fit", {}).get("distribution", {}).values()) != \
            summary.get("ontology_fit", {}).get("denominator"):
        errors.append(f"{label}: ontology-fit distribution does not reconcile")
    if sum(summary.get("utterance_status", {}).get("distribution", {}).values()) != \
            summary.get("utterance_status", {}).get("denominator"):
        errors.append(f"{label}: utterance-status distribution does not reconcile")
    return errors


def audit(pilot: dict, comparison: dict, canonical_path: Path,
          pilot_path: Path) -> list[str]:
    errors = []
    if pilot.get("complete") is not True or pilot.get("summary", {}).get("occurrences") != 10:
        errors.append("pilot report must be complete with 10 occurrences")
    records = pilot.get("occurrences", [])
    if len(records) != 10 or {record.get("title") for record in records} != {"Nikki's Touch"}:
        errors.append("pilot occurrences must contain only 10 Nikki's Touch records")
    versions = {record.get("annotation_provenance", {}).get("annotation_version")
                for record in records}
    if versions != {"0.3.1"}:
        errors.append(f"pilot annotation versions are {sorted(str(item) for item in versions)}")
    if comparison.get("comparison_name") != "canonical_vs_indie_romance_pilot_v1":
        errors.append("unexpected comparison name")
    inputs = comparison.get("inputs", {})
    if inputs.get("canonical_sha256") != sha256(canonical_path):
        errors.append("canonical input hash does not match comparison")
    if inputs.get("pilot_sha256") != sha256(pilot_path):
        errors.append("pilot input hash does not match comparison")
    groups = comparison.get("groups", [])
    if [(group.get("group_id"), group.get("works"), group.get("occurrences"))
            for group in groups] != [("canonical_eight", 8, 41),
                                     ("indie_romance_pilot", 1, 10)]:
        errors.append("comparison groups must be canonical 8/41 and pilot 1/10")
    for group in groups:
        errors.extend(audit_summary(group, group.get("group_id", "unknown group")))
        if sum(work.get("occurrences", 0) for work in group.get("by_work", [])) != \
                group.get("occurrences"):
            errors.append(f"{group.get('group_id')}: work totals do not reconcile")
        for work in group.get("by_work", []):
            errors.extend(audit_summary(work, f"work/{work.get('work_id')}"))
    return errors


def review_inventory(pilot: dict, comparison: dict) -> dict:
    records = pilot["occurrences"]
    selected = []
    for record in records:
        annotation, scores = record["annotation"], record["annotation"]["scores"]
        substantial = [label for label in "PTE" if scores[label] >= 2]
        if (scores["P"] >= 2 or scores["E"] >= 2 or scores["O"] > 0 or
                len(substantial) >= 2 or annotation["ontology_fit"] != "natural" or
                annotation["confidence"] < 0.75):
            selected.append({
                "occurrence_id": record["occurrence_id"], "scores": scores,
                "confidence": annotation["confidence"],
                "ontology_fit": annotation["ontology_fit"],
                "utterance_status": annotation["utterance_status"]["status"],
            })
    return {
        "pilot_report_summary": pilot["summary"],
        "comparison_groups": [
            {key: group[key] for key in ("group_id", "works", "occurrences",
                                         "P_at_least_2", "E_at_least_2", "mixed_PTE",
                                         "missing_data")}
            for group in comparison["groups"]
        ],
        "pilot_cases_requiring_review": selected,
        "interpretation_cautions": comparison["method"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--canonical-report", required=True, type=Path)
    parser.add_argument("--pilot-report", required=True, type=Path)
    parser.add_argument("--comparison", required=True, type=Path)
    args = parser.parse_args()
    try:
        canonical = json.loads(args.canonical_report.read_text(encoding="utf-8"))
        pilot = json.loads(args.pilot_report.read_text(encoding="utf-8"))
        comparison = json.loads(args.comparison.read_text(encoding="utf-8"))
        errors = audit(pilot, comparison, args.canonical_report, args.pilot_report)
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        errors = [str(exc)]
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Step 17 audit passed: canonical 8/41 vs pilot 1/10")
    print(json.dumps(review_inventory(pilot, comparison), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
