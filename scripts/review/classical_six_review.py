#!/usr/bin/env python3
"""Validate, render, and apply the authoritative classical-six adjudication."""

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
    "structural_status", "scene_cluster", "adjudication",
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


def validate(inventory: Path, review_path: Path) -> tuple[list[dict], dict]:
    rows = inventory_rows(inventory)
    review = load_review(review_path)
    expected = {row["occurrence_id"]: row for row in rows}
    ids = [item.get("occurrence_id") for item in review["occurrences"]]
    duplicates = sorted(key for key, count in Counter(ids).items() if count > 1)
    unknown = sorted(set(ids) - set(expected))
    missing = sorted(set(expected) - set(ids))
    errors = []
    if "PENDING" in json.dumps(review, ensure_ascii=False).upper():
        errors.append("review contains PENDING")
    if duplicates: errors.append(f"duplicate occurrence IDs: {duplicates}")
    if unknown: errors.append(f"unknown occurrence IDs: {unknown}")
    if missing: errors.append(f"missing occurrence IDs: {missing}")
    for item in review["occurrences"]:
        oid = item.get("occurrence_id", "<missing>")
        absent = REQUIRED - set(item)
        if absent: errors.append(f"{oid}: missing fields {sorted(absent)}")
        if item.get("decision") not in DECISIONS:
            errors.append(f"{oid}: decision must be KEEP or EXCLUDE")
        for field in ("structural_status", "scene_cluster", "adjudication"):
            value = item.get(field)
            if not isinstance(value, str) or not value.strip() or "PENDING" in value.upper():
                errors.append(f"{oid}: {field} must be nonempty and not PENDING")
        source = expected.get(oid)
        if source:
            for field in ("source_id", "pattern_id", "start", "end"):
                if str(item.get(field)) != source[field]:
                    errors.append(f"{oid}: {field} does not match inventory")
    decisions = Counter(item.get("decision") for item in review["occurrences"])
    if decisions["KEEP"] + decisions["EXCLUDE"] != len(rows):
        errors.append("KEEP + EXCLUDE does not equal extracted occurrence count")
    if errors:
        raise ValueError("invalid adjudication:\n- " + "\n- ".join(errors))
    return rows, review


def render(inventory: Path, review_path: Path, output: Path) -> None:
    _, review = validate(inventory, review_path)
    lines = ["# Adjudicated classical-six occurrence review", "",
             "This document is rendered from the authoritative `review_adjudicated.json`.", ""]
    for item in review["occurrences"]:
        lines += [f"## {item['occurrence_id']}", "", f"- source: `{item['source_id']}`",
                  f"- pattern: `{item['pattern_id']}`", f"- offsets: {item['start']}–{item['end']}",
                  f"- final decision: {item['decision']}",
                  f"- structural status: {item['structural_status']}",
                  f"- scene cluster: {item['scene_cluster']}",
                  f"- adjudication: {item['adjudication']}"]
        if item.get("reason"): lines.append(f"- reason: {item['reason']}")
        lines.append("")
    output.write_text("\n".join(lines), encoding="utf-8")


def filter_runs(inventory: Path, review_path: Path, selected: Path, output: Path) -> None:
    rows, review = validate(inventory, review_path)
    keep = {item["occurrence_id"] for item in review["occurrences"] if item["decision"] == "KEEP"}
    expected = {row["occurrence_id"] for row in rows}
    selections = json.loads(selected.read_text(encoding="utf-8"))
    found: set[str] = set()
    for selection in selections:
        source = Path(selection["run_directory"]) / "extraction"
        destination = output / selection["source_id"] / "adjudicated" / "extraction"
        if destination.exists(): shutil.rmtree(destination)
        shutil.copytree(source, destination)
        passages = destination / "passages.jsonl"
        records = [json.loads(line) for line in passages.read_text(encoding="utf-8").splitlines() if line]
        found.update(row["occurrence_id"] for row in records)
        retained = [row for row in records if row["occurrence_id"] in keep]
        passages.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in retained), encoding="utf-8")
        metadata = json.loads((destination / "metadata.json").read_text(encoding="utf-8"))
        metadata["inventory_sha256"] = hashlib.sha256(passages.read_bytes()).hexdigest()
        metadata["adjudication_review"] = str(review_path)
        metadata["adjudicated_from_occurrences"] = len(records)
        metadata["retained_occurrences"] = len(retained)
        (destination / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    if found != expected:
        raise ValueError(
            f"selected runs do not match inventory; missing={sorted(expected-found)}, "
            f"unknown={sorted(found-expected)}"
        )
    print(f"prepared {len(keep)} KEEP occurrences in {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "render", "filter"))
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--selected-runs", type=Path)
    args = parser.parse_args()
    if args.command == "validate":
        rows, review = validate(args.inventory, args.review)
        counts = Counter(item["decision"] for item in review["occurrences"])
        print(f"valid: {len(rows)} occurrences; KEEP={counts['KEEP']}; EXCLUDE={counts['EXCLUDE']}")
    elif args.command == "render":
        if not args.output: parser.error("render requires --output")
        render(args.inventory, args.review, args.output)
    else:
        if not args.output or not args.selected_runs:
            parser.error("filter requires --output and --selected-runs")
        filter_runs(args.inventory, args.review, args.selected_runs, args.output)


if __name__ == "__main__":
    main()
