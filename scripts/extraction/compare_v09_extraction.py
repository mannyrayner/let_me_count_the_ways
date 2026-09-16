#!/usr/bin/env python3
"""Build deterministic v0.9-versus-historical extraction diagnostics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def run(output: Path) -> None:
    baselines = (("canonical_16_v0_7", ROOT / "results/extraction/canonical_16_v0_7"),
                 ("expansion_15_v0_8", ROOT / "results/extraction/expansion_15_v0_8"))
    rows, recovered = [], []
    for baseline_name, baseline in baselines:
        for summary_path in sorted((baseline / "works").glob("*/summary.json")):
            old_summary = json.loads(summary_path.read_text(encoding="utf-8"))
            work_id = old_summary["work_id"]
            new_summary = json.loads((output / "works" / work_id / "summary.json").read_text(encoding="utf-8"))
            old_count, new_count = old_summary.get("candidate_count"), new_summary.get("candidate_count")
            rows.append({"baseline": baseline_name, "work_id": work_id,
                         "old_count": old_count, "v0_9_count": new_count,
                         "delta": new_count - old_count if isinstance(old_count, int) and isinstance(new_count, int) else None})
            old = read_jsonl(summary_path.parent / "candidates.jsonl")
            old_spans = {(r["start"], r["end"], r["match"]) for r in old}
            for record in read_jsonl(output / "works" / work_id / "candidates.jsonl"):
                if (record["start"], record["end"], record["match"]) not in old_spans:
                    recovered.append({key: record[key] for key in
                                      ("work_id", "language", "start", "end", "match", "pattern_id")})
    comparison = {"comparison": "historical extraction to canonical_31_v0_9",
                  "works": rows, "newly_recovered_candidates": recovered}
    (output / "historical_comparison.json").write_text(
        json.dumps(comparison, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Historical extraction comparison", "",
             "| Baseline | Work | Old | v0.9 | Delta |", "| --- | --- | ---: | ---: | ---: |"]
    lines += [f"| {r['baseline']} | {r['work_id']} | {r['old_count']} | {r['v0_9_count']} | {r['delta']} |" for r in rows]
    lines += ["", "## Newly recovered candidates", "",
              "| Work | Language | Offset | Pattern | Surface |", "| --- | --- | ---: | --- | --- |"]
    lines += [f"| {r['work_id']} | {r['language']} | {r['start']} | {r['pattern_id']} | {r['match']} |" for r in recovered]
    (output / "historical_comparison.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    exclusive = [r for r in recovered if r["pattern_id"].startswith(tuple(
        f"{language}_exclusive" for language in ("en", "fr", "de", "no", "sv", "da", "it")))]
    (output / "exclusive_target_candidates.json").write_text(
        json.dumps(exclusive, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    exclusive_lines = ["# Corpus candidates from new exclusive-target patterns", "",
                       "| Work | Language | Pattern | Match |", "| --- | --- | --- | --- |"]
    exclusive_lines += [f"| {r['work_id']} | {r['language']} | {r['pattern_id']} | {r['match']} |" for r in exclusive]
    if not exclusive:
        exclusive_lines.append("| — | — | — | None |")
    (output / "exclusive_target_candidates.md").write_text("\n".join(exclusive_lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "results/extraction/canonical_31_v0_9")
    args = parser.parse_args()
    run(args.output.resolve())


if __name__ == "__main__":
    main()
