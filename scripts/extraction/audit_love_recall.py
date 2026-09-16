#!/usr/bin/env python3
"""Audit broad first-person LOVE cues against the narrower v0.8 extractor."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.extraction.extract_canonical_corpus import extract_candidates, resolve_canonical

DEFAULT_PATTERNS = ROOT / "data/development/search_patterns_v0_8.json"
DEFAULT_OUTPUT = ROOT / "results/extraction_audit/canonical_31_pre_v0_9"

# These deliberately broad, first-person lexical cues are diagnostic only.  They
# are not production templates and need not mention a second-person target.
AUDIT_RULES = {
    "en": ("en_first_person_love_lexeme", r"\bI(?:\s+(?:have|had|do|did|shall|will|would|could|can|never|always|still|really|truly|not)){0,4}\s+love(?:d)?\b|\bI[’'](?:ve|d|ll)\s+(?:\w+\s+){0,2}love(?:d)?\b"),
    "fr": ("fr_first_person_aimer_lexeme", r"\bje\s+(?:n[’']aim(?:e|ais|erai|erais)|(?:ne\s+)?(?:\w+\s+){0,4}aim(?:e|ais|ai|é|ée|erai|erais))\b|\bj[’']aim(?:e|ais|erai|erais)\b"),
    "de": ("de_first_person_lieben_lexeme", r"\bich(?:\s+\w+){0,5}\s+(?:lieb(?:e|te|en)|geliebt)\b"),
    "no": ("no_first_person_elske_lexeme", r"\bjeg(?:\s+\w+){0,5}\s+elsk(?:er|et|e)\b"),
    "sv": ("sv_first_person_alska_lexeme", r"\bjag(?:\s+\w+){0,5}\s+älsk(?:ar|ade|at|a)\b"),
    "da": ("da_first_person_elske_lexeme", r"\bjeg(?:\s+\w+){0,5}\s+elsk(?:er|ede|et|e)\b"),
    "it": ("it_first_person_amare_lexeme", r"\b(?:io\s+)?(?:non\s+)?(?:ti|t[’']|vi\s+)?(?:ho\s+|avevo\s+)?(?:sempre\s+|mai\s+)?(?:amo|amavo|amai|amerò|amerei|amato|amata)\b"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def cue_matches(language: str, text: str):
    rule_id, regex = AUDIT_RULES[language]
    return rule_id, list(re.finditer(regex, text, re.IGNORECASE))


def run(pattern_path: Path, output: Path, context_chars: int = 100) -> dict:
    config = json.loads(pattern_path.read_text(encoding="utf-8"))
    output.mkdir(parents=True, exist_ok=True)
    works, language_counts = [], Counter()
    for manifest_path in sorted((ROOT / "corpus/works").glob("*/work.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        work_id, language = manifest["work_id"], manifest["language"]
        source, _ = resolve_canonical(manifest_path, manifest)
        row = {"work_id": work_id, "language": language}
        if not source.is_file():
            row.update(status="unavailable", broad_lexical_cues=None, captured_by_v0_8=None,
                       unmatched=None)
            works.append(row)
            continue
        if sha256(source) != manifest["canonical_sha256"]:
            raise RuntimeError(f"canonical hash mismatch for {work_id}")
        text = source.read_text(encoding="utf-8")
        production = extract_candidates(text, manifest, config["schema_version"],
                                        config["languages"][language]["patterns"], 0)
        spans = [(record["start"], record["end"]) for record in production]
        audit_rule, cues = cue_matches(language, text)
        unmatched, captured = [], 0
        for cue in cues:
            is_captured = any(cue.start() < end and cue.end() > start for start, end in spans)
            if is_captured:
                captured += 1
                continue
            left, right = max(0, cue.start() - context_chars), min(len(text), cue.end() + context_chars)
            unmatched.append({
                "work_id": work_id, "language": language, "cue": cue.group(0),
                "start": cue.start(), "end": cue.end(), "short_context": text[left:right],
                "audit_rule": audit_rule, "captured_by_v0_8": False,
            })
        artifact = output / "works" / work_id / "unmatched_cues.jsonl"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in unmatched),
                            encoding="utf-8")
        row.update(status="audited", broad_lexical_cues=len(cues), captured_by_v0_8=captured,
                   unmatched=len(unmatched))
        works.append(row)
        language_counts[(language, "broad")] += len(cues)
        language_counts[(language, "captured")] += captured
        language_counts[(language, "unmatched")] += len(unmatched)

    by_language = {language: {
        "broad_lexical_cues": language_counts[(language, "broad")],
        "captured_by_v0_8": language_counts[(language, "captured")],
        "unmatched": language_counts[(language, "unmatched")],
    } for language in sorted(AUDIT_RULES)}
    available = [w for w in works if w["status"] == "audited"]
    summary = {
        "run_id": output.name, "production_baseline": config["schema_version"],
        "offset_unit": "Unicode code points in unmodified decoded canonical text",
        "diagnostic_only": True, "works_discovered": len(works),
        "works_audited": len(available), "works_unavailable": len(works) - len(available),
        "by_language": by_language, "works": works,
        "zero_yield_works_v0_8": [w["work_id"] for w in available if w["captured_by_v0_8"] == 0],
        "very_low_yield_works_v0_8": [w["work_id"] for w in available if w["captured_by_v0_8"] == 1],
        "many_unmatched_works": [w["work_id"] for w in available if w["unmatched"] >= 10],
    }
    (output / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
                                         encoding="utf-8")
    lines = ["# Pre-v0.9 deterministic LOVE recall audit", "",
             "Broad cues are diagnostics, not a scholarly occurrence inventory.", "",
             "| Language | Broad cues | Captured by v0.8 | Unmatched |", "| --- | ---: | ---: | ---: |"]
    lines += [f"| {k} | {v['broad_lexical_cues']} | {v['captured_by_v0_8']} | {v['unmatched']} |"
              for k, v in by_language.items()]
    lines += ["", "## Work-level unmatched counts", "", "| Work | Language | Unmatched |", "| --- | --- | ---: |"]
    lines += [f"| {w['work_id']} | {w['language']} | {w['unmatched'] if w['unmatched'] is not None else 'unavailable'} |" for w in works]
    for label, key in (("Zero-yield works", "zero_yield_works_v0_8"),
                       ("Very-low-yield works", "very_low_yield_works_v0_8"),
                       ("Works with many unmatched cues", "many_unmatched_works")):
        lines += ["", f"**{label}:** {', '.join(summary[key]) or 'none'}"]
    (output / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--patterns", type=Path, default=DEFAULT_PATTERNS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--context-chars", type=int, default=100)
    args = parser.parse_args()
    result = run(args.patterns.resolve(), args.output.resolve(), args.context_chars)
    print(f"audited {result['works_audited']} works; {result['works_unavailable']} unavailable")


if __name__ == "__main__":
    main()
