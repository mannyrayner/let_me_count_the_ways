#!/usr/bin/env python3
"""Compare scientifically relevant fields across two annotation batch versions."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from scripts.pipeline.run_single_text_pipeline import read_json, write_json


DIMENSIONS = ("truth_conditional", "performative", "exclamatory_reflexive")


def completed_output(run_dir: Path, occurrence_id: str) -> tuple[dict, Path] | None:
    """Return the preferred valid output, independent of annotation fingerprint."""
    candidates = []
    for status_path in (run_dir / "annotations" / occurrence_id).glob("attempt-*/status.json"):
        status = read_json(status_path)
        output_path = status_path.parent / "output.json"
        if status.get("state") == "valid" and output_path.exists():
            candidates.append((status_path.parent, output_path))
    if not candidates:
        return None
    attempt_dir, output_path = sorted(candidates, reverse=True)[0]
    return read_json(output_path), attempt_dir


def latest_reference_run(root: Path, source_id: str, version: str) -> Path | None:
    matches = []
    for manifest_path in (root / source_id).glob("*/manifest.json"):
        manifest = read_json(manifest_path)
        if manifest.get("annotation_version") == version and manifest.get("status") == "complete":
            matches.append(manifest_path.parent)
    return sorted(matches)[-1] if matches else None


def scores(output: dict, version: str) -> dict:
    container = output["core_love_content"] if version == "0.2" else output["core_classification"]
    return container["label_support"]


def old_context_summary(output: dict) -> str:
    parts = [output["core_love_content"]["analysis"]]
    for name in ("realisation", "current_discourse_act", "contextual_modification"):
        layer = output.get(name, {})
        if layer.get("analysis"):
            parts.append(layer["analysis"])
    supported = [
        name for name, value in output.get("assessments", {}).items()
        if value.get("status") == "supported"
    ]
    if supported:
        parts.append("Supported assessments: " + ", ".join(supported) + ".")
    return " ".join(parts)


def compare(*, batch_summary_path: Path, reference_root: Path,
            old_version: str = "0.2") -> tuple[dict, str]:
    batch = read_json(batch_summary_path)
    records = []
    unmatched = []
    for text in batch["texts"]:
        source_id = text["source_id"]
        new_run = Path(text["result_location"])
        old_run = latest_reference_run(reference_root, source_id, old_version)
        if old_run is None:
            unmatched.append({"source_id": source_id, "reason": "no complete reference run"})
            continue
        old_occurrences = read_json(old_run / "summary.json")["extracted_occurrences"]
        for input_path in sorted((old_run / "inputs").glob("*.json")):
            occurrence_id = input_path.stem
            old = completed_output(old_run, occurrence_id)
            new = completed_output(new_run, occurrence_id)
            if old is None or new is None:
                unmatched.append({
                    "source_id": source_id, "occurrence_id": occurrence_id,
                    "reason": "missing valid old or new annotation",
                })
                continue
            old_output, old_attempt = old
            new_output, new_attempt = new
            old_scores, new_scores = scores(old_output, old_version), scores(new_output, batch["annotation_version"])
            differences = {name: new_scores[name] - old_scores[name] for name in DIMENSIONS}
            records.append({
                "source_id": source_id,
                "occurrence_id": occurrence_id,
                "old_attempt": str(old_attempt),
                "new_attempt": str(new_attempt),
                "old_scores": {name: old_scores[name] for name in DIMENSIONS},
                "new_scores": {name: new_scores[name] for name in DIMENSIONS},
                "differences": differences,
                "exact_tpe_agreement": all(value == 0 for value in differences.values()),
                "conspicuous_change": any(abs(value) >= 2 for value in differences.values()),
                "other_score": new_scores["other"],
                "other_diagnosis": new_output["other_diagnosis"],
                "ontology_fit": new_output["ontology_assessment"]["fit"],
                "ambiguity": new_output["core_classification"]["ambiguity"],
                "old_context_summary": old_context_summary(old_output),
                "new_contextual_interpretation": new_output["contextual_interpretation"],
            })
        if old_occurrences == 0:
            unmatched.append({"source_id": source_id, "reason": "reference run has no occurrences"})

    agreements = {name: sum(r["differences"][name] == 0 for r in records) for name in DIMENSIONS}
    o_counts = {"0": 0, "1": 0, "2_or_more": 0}
    for record in records:
        score = record["other_score"]
        o_counts[str(score) if score < 2 else "2_or_more"] += 1
    fit_counts = Counter(record["ontology_fit"] for record in records)
    result = {
        "batch_id": batch["batch_id"],
        "old_annotation_version": old_version,
        "new_annotation_version": batch["annotation_version"],
        "comparison_is_diagnostic_not_ground_truth": True,
        "matched_occurrences": len(records),
        "unmatched": unmatched,
        "tpe_exact_agreement": agreements,
        "all_dimension_exact_agreement": sum(r["exact_tpe_agreement"] for r in records),
        "other_score_counts": o_counts,
        "ontology_fit_counts": {name: fit_counts.get(name, 0) for name in ("natural", "strained", "inadequate")},
        "records": records,
    }
    lines = [
        f"# Annotation comparison: v{old_version} → v{batch['annotation_version']}", "",
        "> This is a diagnostic comparison. v0.2 is not treated as ground truth; changes may",
        "> reflect improvement, information loss, overclassification, instability, or ambiguity.", "",
        f"- **Batch:** `{batch['batch_id']}`", f"- **Matched occurrences:** {len(records)}",
        f"- **Unmatched occurrences:** {len(unmatched)}",
        f"- **Exact T/P/E agreement:** " + ", ".join(f"{k} {v}/{len(records)}" for k, v in agreements.items()),
        f"- **All three scores exact:** {result['all_dimension_exact_agreement']}/{len(records)}",
        f"- **O scores:** O=0: {o_counts['0']}; O=1: {o_counts['1']}; O≥2: {o_counts['2_or_more']}",
        "- **Ontology fit:** " + ", ".join(f"{k}: {result['ontology_fit_counts'][k]}" for k in ("natural", "strained", "inadequate")),
        "", "## Cases requiring inspection", "",
    ]
    flagged = [r for r in records if r["conspicuous_change"] or r["other_score"] > 0 or r["ontology_fit"] != "natural" or r["ambiguity"]]
    if not flagged:
        lines.append("No conspicuous score changes, O cases, non-natural fits, or explicit ambiguity.")
    for record in flagged:
        lines.extend([
            f"### `{record['occurrence_id']}`", "",
            f"- **T/P/E:** {list(record['old_scores'].values())} → {list(record['new_scores'].values())}",
            f"- **O / fit:** {record['other_score']} / `{record['ontology_fit']}`",
            f"- **Ambiguity:** {record['ambiguity'] or 'None recorded'}",
            f"- **O diagnosis:** {record['other_diagnosis']}", "",
        ])
    lines.extend(["## Qualitative preservation review", "",
                  "The paired summaries below support human/AI review; lexical similarity is not treated as proof of preservation.", ""])
    for record in records:
        lines.extend([
            f"### `{record['occurrence_id']}`", "",
            f"- **v{old_version}:** {record['old_context_summary']}",
            f"- **v{batch['annotation_version']}:** {record['new_contextual_interpretation']}", "",
        ])
    if unmatched:
        lines.extend(["## Unmatched cases", "", "```json", json.dumps(unmatched, indent=2), "```", ""])
    return result, "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch_summary", type=Path)
    parser.add_argument("--reference-root", type=Path, default=Path("results/pipeline_runs"))
    parser.add_argument("--old-version", default="0.2")
    parser.add_argument("--output-directory", type=Path)
    args = parser.parse_args()
    output_dir = args.output_directory or args.batch_summary.parent
    result, report = compare(batch_summary_path=args.batch_summary, reference_root=args.reference_root,
                             old_version=args.old_version)
    output_dir.mkdir(parents=True, exist_ok=True)
    write_json(output_dir / "comparison.json", result)
    (output_dir / "comparison.md").write_text(report, encoding="utf-8")
    print(output_dir / "comparison.md")


if __name__ == "__main__":
    main()
