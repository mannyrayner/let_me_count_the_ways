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
    direct_manifest = root / source_id / "manifest.json"
    if direct_manifest.exists():
        manifest = read_json(direct_manifest)
        if manifest.get("annotation_version") == version and manifest.get("status") == "complete":
            matches.append(direct_manifest.parent)
    for manifest_path in (root / source_id).glob("*/manifest.json"):
        manifest = read_json(manifest_path)
        if manifest.get("annotation_version") == version and manifest.get("status") == "complete":
            matches.append(manifest_path.parent)
    return sorted(matches)[-1] if matches else None


def scores(output: dict, version: str) -> dict:
    container = output["core_love_content"] if version == "0.2" else output["core_classification"]
    return container["label_support"]


def context_summary(output: dict, version: str) -> str:
    if version != "0.2":
        return output["contextual_interpretation"]
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
            old_core = old_output["core_love_content"] if old_version == "0.2" else old_output["core_classification"]
            new_core = new_output["core_classification"]
            old_fit = (
                "natural" if old_version == "0.2" and old_output["ontology_assessment"]["adequate"]
                else "inadequate" if old_version == "0.2"
                else old_output["ontology_assessment"]["fit"]
            )
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
                "e_changed": differences["exclamatory_reflexive"] != 0,
                "conspicuous_e_change": abs(differences["exclamatory_reflexive"]) >= 2,
                "old_other_score": old_scores.get("other"),
                "other_score": new_scores["other"],
                "other_changed": old_scores.get("other") is not None and old_scores["other"] != new_scores["other"],
                "other_diagnosis": new_output["other_diagnosis"],
                "old_ontology_fit": old_fit,
                "ontology_fit": new_output["ontology_assessment"]["fit"],
                "ontology_fit_changed": old_fit != new_output["ontology_assessment"]["fit"],
                "old_confidence": old_core["confidence"],
                "new_confidence": new_core["confidence"],
                "confidence_difference": new_core["confidence"] - old_core["confidence"],
                "ambiguity": new_output["core_classification"]["ambiguity"],
                "old_context_summary": context_summary(old_output, old_version),
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
        "e_changes": sum(record["e_changed"] for record in records),
        "conspicuous_e_changes": sum(record["conspicuous_e_change"] for record in records),
        "other_changes": sum(record["other_changed"] for record in records),
        "ontology_fit_changes": sum(record["ontology_fit_changed"] for record in records),
        "conspicuous_confidence_changes": sum(
            abs(record["confidence_difference"]) >= 0.2 for record in records),
        "records": records,
    }
    lines = [
        f"# Annotation comparison: v{old_version} → v{batch['annotation_version']}", "",
        f"> This is a diagnostic comparison. v{old_version} is not treated as ground truth; changes may",
        "> reflect improvement, information loss, overclassification, instability, or ambiguity.", "",
        f"- **Batch:** `{batch['batch_id']}`", f"- **Matched occurrences:** {len(records)}",
        f"- **Unmatched occurrences:** {len(unmatched)}",
        f"- **Exact T/P/E agreement:** " + ", ".join(f"{k} {v}/{len(records)}" for k, v in agreements.items()),
        f"- **All three scores exact:** {result['all_dimension_exact_agreement']}/{len(records)}",
        f"- **O scores:** O=0: {o_counts['0']}; O=1: {o_counts['1']}; O≥2: {o_counts['2_or_more']}",
        f"- **E changes / magnitude ≥2:** {result['e_changes']} / {result['conspicuous_e_changes']}",
        f"- **O / ontology-fit changes:** {result['other_changes']} / {result['ontology_fit_changes']}",
        f"- **Confidence changes ≥0.20:** {result['conspicuous_confidence_changes']}",
        "- **Ontology fit:** " + ", ".join(f"{k}: {result['ontology_fit_counts'][k]}" for k in ("natural", "strained", "inadequate")),
        "", "## Cases requiring inspection", "",
    ]
    flagged = [
        r for r in records
        if r["conspicuous_change"] or r["other_changed"] or r["ontology_fit_changed"]
        or abs(r["confidence_difference"]) >= 0.2 or r["other_score"] > 0
        or r["ontology_fit"] != "natural" or r["ambiguity"]
    ]
    if not flagged:
        lines.append("No conspicuous score changes, O cases, non-natural fits, or explicit ambiguity.")
    for record in flagged:
        lines.extend([
            f"### `{record['occurrence_id']}`", "",
            f"- **T/P/E:** {list(record['old_scores'].values())} → {list(record['new_scores'].values())}",
            f"- **O / fit:** {record['other_score']} / `{record['ontology_fit']}`",
            f"- **Confidence:** {record['old_confidence']:.2f} → {record['new_confidence']:.2f}",
            f"- **Ambiguity:** {record['ambiguity'] or 'None recorded'}",
            f"- **O diagnosis:** {record['other_diagnosis']}", "",
        ])
    e_changes = [record for record in records if record["e_changed"]]
    lines.extend(["## All E changes", ""])
    if not e_changes:
        lines.append("No E scores changed.")
    for record in e_changes:
        marker = " **(magnitude ≥2)**" if record["conspicuous_e_change"] else ""
        lines.append(
            f"- `{record['occurrence_id']}`: "
            f"{record['old_scores']['exclamatory_reflexive']} → "
            f"{record['new_scores']['exclamatory_reflexive']}{marker}"
        )
    lines.append("")
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
