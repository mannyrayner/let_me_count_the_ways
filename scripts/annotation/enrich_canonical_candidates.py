#!/usr/bin/env python3
"""Create annotation-ready records from reviewed canonical offsets (no extraction)."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

VERSION = "canonical_annotation_input_v1"
WIDE_RADIUS = 3000
PUBLIC_POLICIES = {
    "PUBLIC_DOMAIN_FULL_CONTEXT_OK",
    "PUBLIC_FULL_CONTEXT_OK",
    "PERMISSIONED_CONTEXT_OK",
}
CHAPTER_PATTERN = re.compile(r"(?m)^(CHAPTER|CHAPITRE)\s+([^\n]+?)\s*$", re.IGNORECASE)

def chapter_locations(text: str) -> list[tuple[int, str]]:
    return [(m.start(), f"{m.group(1).upper()} {m.group(2).strip()}") for m in CHAPTER_PATTERN.finditer(text)]

def chapter_at(locations: list[tuple[int, str]], offset: int) -> str | None:
    labels=[label for position,label in locations if position <= offset]
    return labels[-1] if labels else None


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def validate_generated_enrichment(generated: dict) -> None:
    """Reject translation templates that have not yet been curated."""
    incomplete = [
        occurrence_id
        for occurrence_id, item in generated.items()
        if "translation" in item
        and (item["translation"].get("status") != "provided"
             or not item["translation"].get("text"))
    ]
    if incomplete:
        raise ValueError(
            "generated enrichment has incomplete translations: " + ", ".join(incomplete)
        )


def wide_bounds(text: str, start: int, end: int, radius: int = WIDE_RADIUS) -> tuple[int, int]:
    """Return a stable radius window, expanding outward to paragraph boundaries."""
    left, right = max(0, start - radius), min(len(text), end + radius)
    boundary = text.rfind("\n\n", 0, left)
    if boundary >= 0:
        left = boundary + 2
    boundary = text.find("\n\n", right)
    if boundary >= 0:
        right = boundary
    return left, right


def enrich(record: dict, corpus_root: Path, generated: dict | None = None,
           allow_private_output: bool = False) -> dict:
    occurrence = record.get("candidate", record.get("occurrence", record))
    review = record.get("review", {})
    work_dir = corpus_root / "works" / occurrence["work_id"]
    work = json.loads((work_dir / "work.json").read_text(encoding="utf-8"))
    canonical_bytes = (work_dir / work.get("canonical_text", "canonical.txt")).read_bytes()
    # Extraction used Path.read_text (universal-newline decoding); reproduce
    # that exact character coordinate system after hashing original bytes.
    text = (work_dir / work.get("canonical_text", "canonical.txt")).read_text(encoding="utf-8")
    actual_hash = hashlib.sha256(canonical_bytes).hexdigest()
    expected_hash = occurrence["canonical_sha256"]
    if actual_hash != expected_hash or work.get("canonical_sha256") != actual_hash:
        raise ValueError(f"{occurrence['occurrence_id']}: canonical hash mismatch")
    policy = work.get("rights", {}).get("public_render_policy")
    if policy not in PUBLIC_POLICIES and not allow_private_output:
        raise ValueError(f"{occurrence['work_id']}: rights policy forbids public context output")
    start, end = occurrence["start"], occurrence["end"]
    cs, ce = occurrence["context_start"], occurrence["context_end"]
    if text[start:end] != occurrence["match"] or text[cs:ce] != occurrence["context"]:
        raise ValueError(f"{occurrence['occurrence_id']}: canonical offsets do not reproduce candidate")
    ws, we = wide_bounds(text, start, end)
    language = work["language"]
    supplied = (generated or {}).get(occurrence["occurrence_id"], {})
    translation = supplied.get("translation") if language != "en" else None
    if language != "en" and translation is None:
        translation = {"status": "required", "text": None,
                       "source_occurrence_id": occurrence["occurrence_id"],
                       "source_language_text_sha256": sha256_text(text[ws:we]),
                       "scope": "wide_context", "notice": "Analytical aid; not source text."}
    narrative = supplied.get("narrative_context")
    locations = chapter_locations(text)
    metadata = {k: work.get(k) for k in ("work_id", "title", "author", "language", "source_type")}
    metadata["rights"] = {"public_render_policy": policy}
    return {
        "annotation_input_version": VERSION, "occurrence": occurrence, "review": review,
        "work_metadata": metadata,
        "canonical_location": {"chapter_or_section": chapter_at(locations, start),
            "relative_position": round(start / len(text), 6) if text else 0.0,
            "source_start": start, "source_end": end, "source_length": len(text)},
        "context": {"local": {"context_start": cs, "context_end": ce, "text": occurrence["context"]},
                    "wide": {"context_start": ws, "context_end": we, "text": text[ws:we],
                             "policy": f"radius_{WIDE_RADIUS}_expanded_outward_to_paragraph_boundaries"}},
        "translation": translation, "narrative_context": narrative,
        "background_knowledge": None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reviewed", type=Path, required=True)
    parser.add_argument("--corpus", type=Path, default=Path("corpus"))
    parser.add_argument("--generated", type=Path, help="optional keyed translation/summary JSON")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--private-output", action="store_true")
    args = parser.parse_args()
    generated = json.loads(args.generated.read_text(encoding="utf-8")) if args.generated else {}
    if args.generated:
        validate_generated_enrichment(generated)
    rows = [enrich(row, args.corpus, generated, args.private_output) for row in read_jsonl(args.reviewed)]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    print(f"enriched {len(rows)} reviewed canonical candidates")


if __name__ == "__main__":
    main()
