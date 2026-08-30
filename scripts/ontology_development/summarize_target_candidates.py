#!/usr/bin/env python3
"""Validate and summarize a target-discovery JSON document."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

REQUIRED_FIELDS = {
    "candidate_id",
    "author",
    "title",
    "original_language",
    "original_publication_year",
    "genre",
    "why_contextually_useful",
    "likely_phrase_forms",
    "possible_repositories",
    "rights_notes",
    "familiarity",
    "selection_dimensions",
    "verification_needed",
}


def validate(document: dict) -> list[dict]:
    if document.get("prompt_version") != "0.1":
        raise ValueError("expected prompt_version 0.1")
    candidates = document.get("candidates")
    if not isinstance(candidates, list):
        raise ValueError("candidates must be an array")
    ids = []
    for index, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            raise ValueError(f"candidate {index} is not an object")
        missing = REQUIRED_FIELDS - candidate.keys()
        if missing:
            raise ValueError(
                f"candidate {index} is missing: {', '.join(sorted(missing))}"
            )
        ids.append(candidate["candidate_id"])
    duplicates = sorted(key for key, count in Counter(ids).items() if count > 1)
    if duplicates:
        raise ValueError(f"duplicate candidate_id values: {', '.join(duplicates)}")
    return candidates


def format_counts(label: str, values: list[str]) -> str:
    counts = Counter(values)
    rendered = ", ".join(f"{key}={counts[key]}" for key in sorted(counts))
    return f"{label}: {rendered}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    document = json.loads(args.input.read_text(encoding="utf-8"))
    candidates = validate(document)
    print(f"prompt_version: {document['prompt_version']}")
    print(f"candidate_count: {len(candidates)}")
    print(format_counts("languages", [item["original_language"] for item in candidates]))
    print(format_counts("genres", [item["genre"] for item in candidates]))
    print(format_counts("familiarity", [item["familiarity"] for item in candidates]))
    print("candidate_ids:")
    for candidate in candidates:
        print(f"- {candidate['candidate_id']}")


if __name__ == "__main__":
    main()
