#!/usr/bin/env python3
"""Extract multilingual 'I love you' candidates from a normalized text."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path


def load_patterns(path: Path, language: str) -> tuple[str, list[dict[str, str]]]:
    config = json.loads(path.read_text(encoding="utf-8"))
    try:
        patterns = config["languages"][language]["patterns"]
    except KeyError as exc:
        raise ValueError(f"language {language!r} is absent from {path}") from exc
    return config["schema_version"], patterns


def paragraph_window(text: str, start: int, end: int, radius: int) -> tuple[int, int]:
    left_limit = max(0, start - radius)
    right_limit = min(len(text), end + radius)
    left_break = text.rfind("\n\n", left_limit, start)
    right_break = text.find("\n\n", end, right_limit)
    context_start = left_break + 2 if left_break >= 0 else left_limit
    context_end = right_break if right_break >= 0 else right_limit
    return context_start, context_end


def extract(
    text: str,
    language: str,
    work_id: str,
    source_id: str,
    pattern_version: str,
    patterns: list[dict[str, str]],
    radius: int,
) -> list[dict[str, object]]:
    text = unicodedata.normalize("NFC", text)
    matches: list[tuple[int, int, str, str]] = []
    for pattern in patterns:
        flags = 0 if pattern.get("case_sensitive", False) else re.IGNORECASE
        for match in re.finditer(pattern["regex"], text, flags):
            matches.append((match.start(), match.end(), pattern["id"], match.group(0)))
    matches.sort(key=lambda item: (item[0], item[1], item[2]))

    records = []
    seen_spans: set[tuple[int, int]] = set()
    extracted_at = datetime.now(timezone.utc).isoformat()
    for start, end, pattern_id, matched_text in matches:
        if (start, end) in seen_spans:
            continue
        seen_spans.add((start, end))
        context_start, context_end = paragraph_window(text, start, end, radius)
        identity = f"{source_id}:{start}:{end}:{matched_text}".encode()
        occurrence_id = f"{work_id}-{hashlib.sha256(identity).hexdigest()[:12]}"
        records.append(
            {
                "occurrence_id": occurrence_id,
                "work_id": work_id,
                "source_id": source_id,
                "language": language,
                "pattern_version": pattern_version,
                "pattern_id": pattern_id,
                "match": matched_text,
                "start": start,
                "end": end,
                "context_start": context_start,
                "context_end": context_end,
                "context": text[context_start:context_end],
                "extracted_at": extracted_at,
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="normalized UTF-8 text")
    parser.add_argument("output", type=Path, help="JSON Lines output")
    parser.add_argument("--language", required=True)
    parser.add_argument("--work-id", required=True)
    parser.add_argument("--source-id", required=True)
    parser.add_argument(
        "--patterns",
        type=Path,
        default=Path("data/development/search_patterns_v0_1.json"),
    )
    parser.add_argument("--context-chars", type=int, default=1000)
    args = parser.parse_args()

    version, patterns = load_patterns(args.patterns, args.language)
    text = args.input.read_text(encoding="utf-8")
    records = extract(
        text, args.language, args.work_id, args.source_id, version, patterns,
        args.context_chars,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as stream:
        for record in records:
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"wrote {len(records)} occurrence(s) to {args.output}")


if __name__ == "__main__":
    main()
