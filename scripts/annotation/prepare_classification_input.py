#!/usr/bin/env python3
"""Select one occurrence from JSONL as a classification input document."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def select_occurrence(source: Path, occurrence_id: str) -> dict:
    records = [
        json.loads(line)
        for line in source.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    selected = [record for record in records if record.get("occurrence_id") == occurrence_id]
    if len(selected) != 1:
        raise ValueError(
            f"expected one {occurrence_id} record, found {len(selected)}"
        )
    return selected[0]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="source occurrence JSONL")
    parser.add_argument("output", type=Path, help="classification input JSON")
    parser.add_argument("--occurrence-id", required=True)
    args = parser.parse_args()

    selected = select_occurrence(args.input, args.occurrence_id)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(selected, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Prepared classification input: {args.output}")


if __name__ == "__main__":
    main()
