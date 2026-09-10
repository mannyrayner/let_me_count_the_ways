#!/usr/bin/env python3
"""Validate and apply reviewed occurrence decisions with optional overrides."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
from collections import Counter
from pathlib import Path

DECISIONS = {"KEEP", "EXCLUDE"}
REQUIRED = {
    "occurrence_id", "source_id", "pattern_id", "start", "end", "decision",
    "scene_cluster", "structural_note", "reviewer", "review_version",
}


def inventory_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    required = {"source_id", "occurrence_id", "pattern_id", "start", "end"}
    if not rows or not required <= set(rows[0]):
        raise ValueError(f"inventory lacks columns {sorted(required)} or has no occurrences")
    return rows


def load_review(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("schema_version") != "1.0":
        raise ValueError("review schema_version must be '1.0'")
    if not isinstance(value.get("occurrences"), list):
        raise ValueError("review occurrences must be an array")
    return value


def load_overrides(path: Path | None) -> list[dict]:
    if path is None or not path.exists():
        return []
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("schema_version") != "1.0":
        raise ValueError("override schema_version must be '1.0'")
    if not isinstance(value.get("overrides"), list):
        raise ValueError("overrides must be an array")
    return value["overrides"]


def validate(inventory: Path, review_path: Path, overrides_path: Path | None = None
             ) -> tuple[list[dict[str, str]], dict, list[dict]]:
    rows = inventory_rows(inventory)
    review = load_review(review_path)
    expected = {row["occurrence_id"]: row for row in rows}
    ids = [item.get("occurrence_id") for item in review["occurrences"]]
    duplicates = sorted(key for key, count in Counter(ids).items() if count > 1)
    unknown = sorted(set(ids) - set(expected))
    missing = sorted(set(expected) - set(ids))
    errors: list[str] = []
    if "PENDING" in json.dumps(review, ensure_ascii=False).upper():
        errors.append("review contains PENDING")
    if duplicates:
        errors.append(f"duplicate occurrence IDs: {duplicates}")
    if unknown:
        errors.append(f"unknown occurrence IDs: {unknown}")
    if missing:
        errors.append(f"missing occurrence IDs: {missing}")
    for item in review["occurrences"]:
        oid = item.get("occurrence_id", "<missing>")
        absent = REQUIRED - set(item)
        if absent:
            errors.append(f"{oid}: missing fields {sorted(absent)}")
        if item.get("decision") not in DECISIONS:
            errors.append(f"{oid}: decision must be KEEP or EXCLUDE")
        if item.get("decision") == "KEEP" and "scene_cluster" not in item:
            errors.append(f"{oid}: KEEP must have scene_cluster (a string or explicit null)")
        if item.get("scene_cluster") is not None and not isinstance(item.get("scene_cluster"), str):
            errors.append(f"{oid}: scene_cluster must be a string or null")
        for field in ("structural_note", "reviewer", "review_version"):
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{oid}: {field} must be a nonempty string")
        source = expected.get(oid)
        if source:
            for field in ("source_id", "pattern_id", "start", "end"):
                if str(item.get(field)) != source[field]:
                    errors.append(f"{oid}: {field} does not match inventory")

    overrides = load_overrides(overrides_path)
    override_ids = [item.get("occurrence_id") for item in overrides]
    for oid, count in Counter(override_ids).items():
        if count > 1:
            errors.append(f"duplicate override occurrence ID: {oid}")
    reviewed = {item.get("occurrence_id"): item for item in review["occurrences"]}
    for override in overrides:
        oid = override.get("occurrence_id")
        required = {"occurrence_id", "ai_decision", "override_decision", "reason", "reviewer", "date"}
        if required - set(override):
            errors.append(f"{oid}: override missing fields {sorted(required - set(override))}")
            continue
        if oid not in expected:
            errors.append(f"unknown override occurrence ID: {oid}")
            continue
        if override["ai_decision"] != reviewed[oid].get("decision"):
            errors.append(f"{oid}: ai_decision does not match reviewed occurrence")
        if override["override_decision"] not in DECISIONS:
            errors.append(f"{oid}: override_decision must be KEEP or EXCLUDE")
        if override["override_decision"] == override["ai_decision"]:
            errors.append(f"{oid}: override must change the occurrence-validity decision")
        for field in ("reason", "reviewer", "date"):
            if not isinstance(override[field], str) or not override[field].strip():
                errors.append(f"{oid}: override {field} must be nonempty")

    effective = [dict(item) for item in review["occurrences"]]
    override_map = {item["occurrence_id"]: item for item in overrides if item.get("occurrence_id") in expected}
    for item in effective:
        if item["occurrence_id"] in override_map:
            item["decision"] = override_map[item["occurrence_id"]]["override_decision"]
            item["human_override"] = override_map[item["occurrence_id"]]
    if errors:
        raise ValueError("invalid occurrence review:\n- " + "\n- ".join(errors))
    return rows, review, effective


def filter_runs(inventory: Path, review_path: Path, selected: Path, output: Path,
                overrides_path: Path | None = None) -> None:
    rows, _, effective = validate(inventory, review_path, overrides_path)
    keep = {item["occurrence_id"] for item in effective if item["decision"] == "KEEP"}
    expected = {row["occurrence_id"]: row for row in rows}
    selections = json.loads(selected.read_text(encoding="utf-8"))
    found: dict[str, dict] = {}
    for selection in selections:
        source = Path(selection["run_directory"]) / "extraction"
        destination = output / selection["source_id"] / "reviewed" / "extraction"
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(source, destination)
        passages = destination / "passages.jsonl"
        records = [json.loads(line) for line in passages.read_text(encoding="utf-8").splitlines() if line]
        for record in records:
            oid = record["occurrence_id"]
            if oid in found:
                raise ValueError(f"duplicate selected occurrence ID: {oid}")
            found[oid] = record
            inventory_row = expected.get(oid)
            if inventory_row:
                for field in ("source_id", "pattern_id", "start", "end"):
                    if str(record.get(field)) != inventory_row[field]:
                        raise ValueError(f"{oid}: selected {field} does not match inventory")
        retained = [record for record in records if record["occurrence_id"] in keep]
        passages.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in retained), encoding="utf-8")
        metadata = json.loads((destination / "metadata.json").read_text(encoding="utf-8"))
        metadata["inventory_sha256"] = hashlib.sha256(passages.read_bytes()).hexdigest()
        metadata["occurrence_review"] = str(review_path)
        metadata["reviewed_from_occurrences"] = len(records)
        metadata["retained_occurrences"] = len(retained)
        (destination / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    if set(found) != set(expected):
        raise ValueError(
            f"selected runs do not match inventory; missing={sorted(set(expected)-set(found))}, "
            f"unknown={sorted(set(found)-set(expected))}"
        )
    excluded = sorted(set(expected) - keep)
    print(f"prepared {len(keep)} KEEP occurrences in {output}")
    print(f"filtered {len(excluded)} EXCLUDE occurrence(s): {', '.join(excluded) or 'none'}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "filter"))
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--overrides", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--selected-runs", type=Path)
    args = parser.parse_args()
    if args.command == "validate":
        rows, _, effective = validate(args.inventory, args.review, args.overrides)
        counts = Counter(item["decision"] for item in effective)
        print(f"valid: {len(rows)} occurrences; KEEP={counts['KEEP']}; EXCLUDE={counts['EXCLUDE']}")
        print(f"human overrides applied: {sum('human_override' in item for item in effective)}")
    else:
        if not args.output or not args.selected_runs:
            parser.error("filter requires --output and --selected-runs")
        filter_runs(args.inventory, args.review, args.selected_runs, args.output, args.overrides)


if __name__ == "__main__":
    main()
