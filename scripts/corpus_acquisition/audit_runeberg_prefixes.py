#!/usr/bin/env python3
"""Audit the field before the first Runeberg raw-OCR ``br`` tag."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.corpus_acquisition.acquire_public_domain_text import (
    RUNEBERG_OCR_END, RUNEBERG_OCR_FALLBACK_END, RUNEBERG_OCR_START,
    RunebergOCRLines,
)


BREAK = re.compile(r"(?is)<br\s*/?\s*>")


def page_prefix(source: str) -> tuple[str, str | None]:
    """Return the extraction classification and normalized prefix, if applicable."""
    start = source.find(RUNEBERG_OCR_START)
    if start < 0:
        return "NOT_RAW_OCR", None
    content_start = start + len(RUNEBERG_OCR_START)
    ends = [position for marker in (RUNEBERG_OCR_END, RUNEBERG_OCR_FALLBACK_END)
            if (position := source.find(marker, content_start)) >= 0]
    if not ends:
        return "AMBIGUOUS", None
    fragment = source[content_start:min(ends)]
    first_break = BREAK.search(fragment)
    if first_break is None:
        return "EMPTY" if not html.unescape(fragment).strip() else "AMBIGUOUS", None
    parser = RunebergOCRLines()
    parser.feed(fragment[:first_break.start()])
    parser.close()
    prefix = parser.text().strip()
    if not prefix:
        return "EMPTY", ""
    if re.fullmatch(r"[0-9]+", prefix):
        return "NUMERIC_PAGE_FIELD", prefix
    return "PRESERVED_TEXT", prefix


def audit_directory(path: Path) -> dict:
    counts = {key: 0 for key in
              ("NUMERIC_PAGE_FIELD", "EMPTY", "PRESERVED_TEXT", "AMBIGUOUS", "NOT_RAW_OCR")}
    affected: list[str] = []
    for page in sorted(path.glob("*.html")):
        classification, _ = page_prefix(page.read_text(encoding="utf-8-sig"))
        counts[classification] += 1
        if classification == "PRESERVED_TEXT":
            affected.append(page.stem)
    return {
        "pages_examined": sum(counts.values()),
        "classifications": counts,
        "potentially_affected_pages_under_old_parser": len(affected),
        "potentially_affected_page_names_sample": affected[:20],
    }


def build_report(root: Path) -> dict:
    locations = {
        "hamsun-pan": [root / "data/raw/hamsun-pan/source-pages"],
        "hamsun-victoria": [root / "data/raw/hamsun-victoria/source-pages"],
        "lagerlof-gosta-berlings-saga": [
            root / "data/raw/lagerlof-gosta-berlings-saga/source-pages"
        ],
        "undset-kristin-lavransdatter": sorted(
            (root / "data/raw/undset-kristin-lavransdatter").glob("*/source-pages")
        ),
    }
    works = {}
    for work_id, directories in locations.items():
        parts = {directory.parent.name: audit_directory(directory) for directory in directories}
        works[work_id] = {"raw_pages_available": True, "parts": parts}
    for work_id in ("ibsen-et-dukkehjem", "strindberg-froken-julie"):
        works[work_id] = {
            "raw_pages_available": False,
            "applicability": "No stored source-pages directory; acquisition predates this auditable path.",
        }
    return {
        "schema_version": "1.0",
        "rule": "EMPTY is discarded; ^[0-9]+$ is NUMERIC_PAGE_FIELD; all other prefixes are preserved.",
        "historical_canonical_action": (
            "No canonical text was changed. PRESERVED_TEXT pages in existing Hamsun acquisitions "
            "are reported for human review rather than silently replacing frozen texts."
        ),
        "works": works,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = build_report(args.root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
