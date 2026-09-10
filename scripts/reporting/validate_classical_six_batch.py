#!/usr/bin/env python3
"""Validate the completed classical-six annotation checkpoint."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts.pipeline.run_batch import markdown_summary

EXCLUDED_ID = "dumas-fils-la-dame-aux-camelias-dec42bc1687b"
EXPECTED_SUMMARY = {
    "batch_id": "classical_six_v1",
    "annotation_version": "0.3.1",
    "model_alias": "5.6",
    "dry_run": False,
    "status": "complete",
    "texts_requested": 6,
    "texts_completed": 6,
    "texts_partial_or_failed": 0,
    "occurrences": 37,
    "valid_annotations": 37,
    "failures": 0,
    "historical_failed_attempts": 0,
    "model_calls_needed": 0,
}
EXPECTED_TEXT_COUNTS = {
    "gutenberg-541": 1,
    "gutenberg-4240": 9,
    "runeberg-hamsun-victoria": 8,
    "runeberg-hamsun-pan": 4,
    "gutenberg-2419": 14,
    "gutenberg-13861": 1,
}
EXPECTED_STATISTICS = {
    "score_distributions": {
        "P": {"0": 27, "1": 5, "2": 5, "3": 0, "4": 0},
        "T": {"0": 1, "1": 0, "2": 0, "3": 0, "4": 36},
        "E": {"0": 36, "1": 0, "2": 0, "3": 1, "4": 0},
        "O": {"0": 36, "1": 0, "2": 0, "3": 0, "4": 1},
    },
    "ontology_fit": {"natural": 37, "strained": 0, "inadequate": 0},
    "o_above_zero": 1,
    "e_at_least_two": 1,
    "p_at_least_two": 5,
    "balanced_core": 6,
}
ALLOWED_UNUSUAL_REASONS = {
    "O > 0", "ontology_fit = strained", "ontology_fit = inadequate",
    "E >= 2", "P >= 2", "confidence < 0.75", "two or more of P/T/E >= 2",
}
EXPECTED_UNUSUAL_CRITERIA = [
    "O > 0", "ontology_fit != natural", "E >= 2", "P >= 2",
    "confidence < 0.75", "two or more of P/T/E >= 2",
]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def scores_from_output(output: dict) -> tuple[dict[str, int], str, float]:
    core = output.get("core_love_content", output.get("core_classification"))
    if not isinstance(core, dict):
        raise ValueError("annotation lacks core love classification")
    support = core["label_support"]
    scores = {
        "P": support["performative"],
        "T": support["truth_conditional"],
        "E": support["exclamatory_reflexive"],
        "O": support["other"],
    }
    return scores, output["ontology_assessment"]["fit"], core["confidence"]


def expected_reasons(scores: dict[str, int], fit: str, confidence: float) -> set[str]:
    reasons = set()
    if scores["O"] > 0:
        reasons.add("O > 0")
    if fit != "natural":
        reasons.add(f"ontology_fit = {fit}")
    if scores["E"] >= 2:
        reasons.add("E >= 2")
    if scores["P"] >= 2:
        reasons.add("P >= 2")
    if confidence < 0.75:
        reasons.add("confidence < 0.75")
    if sum(scores[key] >= 2 for key in "PTE") >= 2:
        reasons.add("two or more of P/T/E >= 2")
    return reasons


def validate(batch_root: Path, reconnaissance_root: Path) -> list[str]:
    errors: list[str] = []

    def check(label: str, actual, expected) -> None:
        if actual != expected:
            errors.append(f"{label}: expected {expected!r}, found {actual!r}")

    summary_path = batch_root / "summary.json"
    report_path = batch_root / "report.md"
    unusual_path = batch_root / "unusual_cases.json"
    for path in (summary_path, report_path, unusual_path):
        if not path.is_file():
            errors.append(f"required artifact missing: {path}")
    if errors:
        return errors

    summary = read_json(summary_path)
    for field, expected in EXPECTED_SUMMARY.items():
        check(f"summary.{field}", summary.get(field), expected)
    cost = summary.get("estimated_total_cost_usd")
    if not isinstance(cost, (int, float)) or abs(cost - 1.4321) > 0.0000005:
        errors.append(f"summary.estimated_total_cost_usd: expected 1.432100, found {cost!r}")
    check("summary.ontology_statistics", summary.get("ontology_statistics"), EXPECTED_STATISTICS)
    check("report.md generated content", report_path.read_text(encoding="utf-8"), markdown_summary(summary))

    texts = summary.get("texts", [])
    check("summary text source IDs", {item.get("source_id") for item in texts}, set(EXPECTED_TEXT_COUNTS))
    for item in texts:
        source_id = item.get("source_id")
        if source_id not in EXPECTED_TEXT_COUNTS:
            continue
        check(f"{source_id}.status", item.get("status"), "complete")
        check(f"{source_id}.extracted_occurrences", item.get("extracted_occurrences"),
              EXPECTED_TEXT_COUNTS[source_id])
        check(f"{source_id}.valid_occurrences", item.get("valid_occurrences"),
              EXPECTED_TEXT_COUNTS[source_id])
        check(f"{source_id}.failures", item.get("failures"), 0)

    with (reconnaissance_root / "occurrence_inventory.tsv").open(
            encoding="utf-8", newline="") as stream:
        inventory = list(csv.DictReader(stream, delimiter="\t"))
    reviewed = read_json(reconnaissance_root / "reviewed_occurrences.json")["occurrences"]
    inventory_ids = [item["occurrence_id"] for item in inventory]
    keep_ids = {item["occurrence_id"] for item in reviewed if item["decision"] == "KEEP"}
    excluded_ids = {item["occurrence_id"] for item in reviewed if item["decision"] == "EXCLUDE"}
    check("raw reconnaissance occurrence count", len(inventory_ids), 38)
    check("unique raw reconnaissance IDs", len(set(inventory_ids)), 38)
    check("reviewed KEEP count", len(keep_ids), 37)
    check("reviewed EXCLUDE IDs", excluded_ids, {EXCLUDED_ID})
    check("reviewed IDs versus raw inventory", keep_ids | excluded_ids, set(inventory_ids))
    reviewed_sources = {item["occurrence_id"]: item["source_id"] for item in reviewed}

    outputs: dict[str, tuple[dict[str, int], str, float]] = {}
    valid_status_ids: set[str] = set()
    output_paths = sorted((batch_root / "texts").glob("*/annotations/*/attempt-*/output.json"))
    for output_path in output_paths:
        occurrence_id = output_path.parents[1].name
        source_id = output_path.parents[3].name
        if occurrence_id in outputs:
            errors.append(f"duplicate final output occurrence ID: {occurrence_id}")
            continue
        status_path = output_path.with_name("status.json")
        required_attempt_files = {
            "cost.json", "metadata.json", "output.json", "output.txt", "parsing.json",
            "request.json", "response.json", "status.json", "validation.json",
        }
        present_attempt_files = {path.name for path in output_path.parent.iterdir() if path.is_file()}
        missing_attempt_files = sorted(required_attempt_files - present_attempt_files)
        if missing_attempt_files:
            errors.append(f"{occurrence_id}: missing attempt provenance {missing_attempt_files}")
        input_path = output_path.parents[3] / "inputs" / f"{occurrence_id}.json"
        if not input_path.is_file():
            errors.append(f"{occurrence_id}: annotation input missing: {input_path}")
        if reviewed_sources.get(occurrence_id) != source_id:
            errors.append(
                f"{occurrence_id}: annotated under {source_id!r}, reviewed under "
                f"{reviewed_sources.get(occurrence_id)!r}"
            )
        if not status_path.is_file():
            errors.append(f"status missing for output: {output_path}")
            continue
        if read_json(status_path).get("state") != "valid":
            errors.append(f"output does not have valid status: {output_path}")
            continue
        valid_status_ids.add(occurrence_id)
        try:
            outputs[occurrence_id] = scores_from_output(read_json(output_path))
        except (KeyError, TypeError, ValueError) as exc:
            errors.append(f"invalid output {output_path}: {exc}")
    check("final valid output count", len(outputs), 37)
    check("unique annotated IDs versus reviewed KEEP set", set(outputs), keep_ids)
    excluded_dirs = list((batch_root / "texts").glob(f"*/annotations/{EXCLUDED_ID}"))
    if EXCLUDED_ID in valid_status_ids or excluded_dirs:
        errors.append(f"excluded occurrence has annotation artifacts: {EXCLUDED_ID}")

    unusual = read_json(unusual_path)
    check("unusual_cases.criteria", unusual.get("criteria"), EXPECTED_UNUSUAL_CRITERIA)
    cases = unusual.get("cases")
    if not isinstance(cases, list):
        errors.append("unusual_cases.cases must be an array")
        cases = []
    unusual_ids = [case.get("occurrence_id") for case in cases]
    duplicates = sorted(oid for oid, count in Counter(unusual_ids).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate unusual-case IDs: {duplicates}")
    expected_unusual_ids = {oid for oid, values in outputs.items() if expected_reasons(*values)}
    check("unusual-case occurrence IDs", set(unusual_ids), expected_unusual_ids)
    for case in cases:
        oid = case.get("occurrence_id")
        if oid not in outputs:
            errors.append(f"unusual case lacks valid KEEP annotation: {oid}")
            continue
        scores, fit, confidence = outputs[oid]
        reasons = set(case.get("reasons", []))
        check(f"{oid}.scores", case.get("scores"), scores)
        check(f"{oid}.ontology_fit", case.get("ontology_fit"), fit)
        check(f"{oid}.confidence", case.get("confidence"), confidence)
        check(f"{oid}.reasons", reasons, expected_reasons(scores, fit, confidence))
        if not reasons or not reasons <= ALLOWED_UNUSUAL_REASONS:
            errors.append(f"{oid}: undocumented unusual-case reason(s): {sorted(reasons)}")

    notable = {
        "lawrence-women-in-love-5ab672887915": {"P": 0, "T": 0, "E": 0, "O": 4},
        "hamsun-victoria-be00bbdbf853": {"P": 0, "T": 4, "E": 3, "O": 0},
    }
    for oid, expected in notable.items():
        check(f"noteworthy result {oid}", outputs.get(oid, (None,))[0], expected)
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-root", type=Path, required=True)
    parser.add_argument("--reconnaissance-root", type=Path, required=True)
    args = parser.parse_args()
    errors = validate(args.batch_root, args.reconnaissance_root)
    if errors:
        raise SystemExit("classical-six validation failed:\n- " + "\n- ".join(errors))
    print("Classical-six checkpoint valid: 6/6 texts, 37/37 valid annotations, "
          "1 reviewed exclusion, 0 failures, USD 1.432100.")


if __name__ == "__main__":
    main()
