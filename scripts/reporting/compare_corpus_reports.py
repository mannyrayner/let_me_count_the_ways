#!/usr/bin/env python3
"""Build the deterministic canonical-versus-indie descriptive comparison."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

SCORES = "PTEO"
STATUS_GROUPS = {
    "embedded_or_reported": {"embedded", "embedded_or_reported", "reported"},
    "quoted_or_revoiced": {"quoted", "quoted_or_revoiced", "revoiced"},
    "hypothetical_or_other_marked": {
        "hypothetical", "imagined", "written", "nonverbal_verbalised", "other",
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction(count: int, denominator: int) -> dict:
    return {
        "count": count,
        "denominator": denominator,
        "proportion": round(count / denominator, 6) if denominator else None,
    }


def unavailable(reason: str) -> dict:
    return {"count": None, "denominator": None, "proportion": None, "reason": reason}


def summarize(records: list[dict]) -> dict:
    total = len(records)
    score_distributions = {
        score: {str(value): 0 for value in range(5)} for score in SCORES
    }
    fits: Counter[str] = Counter()
    statuses: Counter[str] = Counter()
    missing_scores = missing_fit = missing_status = 0
    p_high = e_high = mixed = 0
    interesting = {"P >= 2": [], "E >= 2": [], "O > 0": [],
                   "ontology fit != natural": [], "low confidence (< 0.75)": []}

    for record in records:
        annotation = record.get("annotation", {})
        scores = annotation.get("scores")
        if not isinstance(scores, dict) or any(
            not isinstance(scores.get(label), int) or scores[label] not in range(5)
            for label in SCORES
        ):
            missing_scores += 1
        else:
            for label in SCORES:
                score_distributions[label][str(scores[label])] += 1
            p_high += scores["P"] >= 2
            e_high += scores["E"] >= 2
            mixed += sum(scores[label] >= 2 for label in "PTE") >= 2
            occurrence_id = record.get("occurrence_id")
            if scores["P"] >= 2:
                interesting["P >= 2"].append(occurrence_id)
            if scores["E"] >= 2:
                interesting["E >= 2"].append(occurrence_id)
            if scores["O"] > 0:
                interesting["O > 0"].append(occurrence_id)

        fit = annotation.get("ontology_fit")
        if isinstance(fit, str):
            fits[fit] += 1
            if fit != "natural":
                interesting["ontology fit != natural"].append(record.get("occurrence_id"))
        else:
            missing_fit += 1
        confidence = annotation.get("confidence")
        if isinstance(confidence, (int, float)) and confidence < 0.75:
            interesting["low confidence (< 0.75)"].append(record.get("occurrence_id"))

        status = annotation.get("utterance_status", {}).get("status")
        if isinstance(status, str):
            statuses[status] += 1
        else:
            missing_status += 1

    score_denominator = total - missing_scores
    fit_denominator = total - missing_fit
    status_denominator = total - missing_status
    structural = {
        name: fraction(sum(count for status, count in statuses.items() if status in members),
                       status_denominator)
        for name, members in STATUS_GROUPS.items()
    }
    structural["direct_status"] = fraction(statuses["direct"], status_denominator)
    reason = "affirmation/negation is not structurally represented in v0.3.1 annotations"
    structural["direct_affirmative"] = unavailable(reason)
    structural["negated"] = unavailable(reason)
    return {
        "works": len({record.get("work_id") for record in records}),
        "occurrences": total,
        "score_distributions": score_distributions,
        "P_at_least_2": fraction(p_high, score_denominator),
        "E_at_least_2": fraction(e_high, score_denominator),
        "mixed_PTE": fraction(mixed, score_denominator),
        "ontology_fit": {
            "distribution": dict(sorted(fits.items())), "denominator": fit_denominator,
        },
        "utterance_status": {
            "distribution": dict(sorted(statuses.items())), "denominator": status_denominator,
            "categories": structural,
        },
        "missing_data": {
            "scores": missing_scores, "ontology_fit": missing_fit,
            "utterance_status": missing_status,
            "negation": total, "direct_affirmative": total,
        },
        "interesting_occurrence_ids": interesting,
    }


def work_summaries(records: list[dict]) -> list[dict]:
    identities = sorted({(record["title"], record["work_id"]) for record in records})
    return [
        {"work_id": work_id, "title": title,
         **summarize([record for record in records if record["work_id"] == work_id])}
        for title, work_id in identities
    ]


def validate_report(report: dict, label: str) -> list[dict]:
    if report.get("complete") is not True:
        raise ValueError(f"{label} report is not complete")
    records = report.get("occurrences")
    if not isinstance(records, list):
        raise ValueError(f"{label} report has no occurrence list")
    if report.get("summary", {}).get("occurrences") != len(records):
        raise ValueError(f"{label} report occurrence total does not reconcile")
    return records


def build_comparison(canonical: dict, pilot: dict, canonical_path: Path,
                     pilot_path: Path) -> dict:
    canonical_records = validate_report(canonical, "canonical")
    pilot_records = validate_report(pilot, "pilot")
    if len({record["work_id"] for record in canonical_records}) != 8:
        raise ValueError("canonical report must contain exactly eight works")
    pilot_works = {(record["work_id"], record["title"]) for record in pilot_records}
    if len(pilot_works) != 1 or {title for _, title in pilot_works} != {"Nikki's Touch"}:
        raise ValueError("pilot report must contain only Nikki's Touch")
    groups = []
    for group_id, label, records in (
        ("canonical_eight", "Canonical literary fiction/drama", canonical_records),
        ("indie_romance_pilot", "Contemporary indie romance pilot", pilot_records),
    ):
        groups.append({"group_id": group_id, "label": label,
                       **summarize(records), "by_work": work_summaries(records)})
    return {
        "comparison_schema_version": "1.0",
        "comparison_name": "canonical_vs_indie_romance_pilot_v1",
        "method": {
            "design": "descriptive exploratory contrast; no significance testing",
            "mixed_PTE_definition": "at least two of P, T, and E have scores >= 2",
            "category_overlap": "structural categories may overlap",
            "negation_policy": "unknown: negation is not structurally represented in v0.3.1",
            "independence_caution": (
                "Occurrences are corpus units, not independent scenes; the two P=3 pilot "
                "occurrences in the short final exchange are not two scene-level confirmations."
            ),
            "genre_inference_caution": (
                "The indie-romance group contains one work and cannot support broad genre inference."
            ),
        },
        "inputs": {
            "canonical_report": str(canonical_path).replace("\\", "/"),
            "canonical_sha256": sha256(canonical_path),
            "pilot_report": str(pilot_path).replace("\\", "/"),
            "pilot_sha256": sha256(pilot_path),
        },
        "groups": groups,
    }


def metric_text(metric: dict) -> str:
    if metric["count"] is None:
        return f"unknown ({metric['reason']})"
    proportion = "unknown" if metric["proportion"] is None else f"{metric['proportion']:.3f}"
    return f"{metric['count']}/{metric['denominator']} ({proportion})"


def render_markdown(comparison: dict) -> str:
    lines = ["# Canonical eight vs. indie-romance pilot", "",
             "> Descriptive exploratory contrast only; no significance testing.", "",
             comparison["method"]["genre_inference_caution"], "",
             f"**Mixed P/T/E:** {comparison['method']['mixed_PTE_definition']}.", "",
             "## Group comparison", "",
             "| Group | Works | Occurrences | P ≥ 2 | E ≥ 2 | Mixed P/T/E |",
             "| --- | ---: | ---: | ---: | ---: | ---: |"]
    for group in comparison["groups"]:
        lines.append("| {label} | {works} | {occurrences} | {p} | {e} | {mixed} |".format(
            label=group["label"], works=group["works"], occurrences=group["occurrences"],
            p=metric_text(group["P_at_least_2"]), e=metric_text(group["E_at_least_2"]),
            mixed=metric_text(group["mixed_PTE"])))
    for group in comparison["groups"]:
        lines.extend(["", f"## {group['label']}", "", "### Score distributions", "",
                      "| Dimension | 0 | 1 | 2 | 3 | 4 |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
        for label in SCORES:
            distribution = group["score_distributions"][label]
            lines.append(f"| {label} | " + " | ".join(str(distribution[str(i)]) for i in range(5)) + " |")
        lines.extend(["", "### Ontology fit", ""])
        fits = group["ontology_fit"]["distribution"]
        lines.append(", ".join(f"{key}: {value}" for key, value in fits.items()) or "None")
        lines.extend(["", "### Utterance status", ""])
        statuses = group["utterance_status"]["distribution"]
        lines.append(", ".join(f"{key}: {value}" for key, value in statuses.items()) or "None")
        lines.extend(["", "### Structural categories", ""])
        for name, metric in group["utterance_status"]["categories"].items():
            lines.append(f"- **{name}:** {metric_text(metric)}")
        lines.extend(["", "### Missing-data inventory", ""])
        for name, count in group["missing_data"].items():
            lines.append(f"- **{name}:** {count}")
        lines.extend(["", "### By work", "",
                      "| Work | Occurrences | P ≥ 2 | E ≥ 2 | Mixed P/T/E |",
                      "| --- | ---: | ---: | ---: | ---: |"])
        for work in group["by_work"]:
            lines.append(f"| {work['title']} | {work['occurrences']} | "
                         f"{metric_text(work['P_at_least_2'])} | "
                         f"{metric_text(work['E_at_least_2'])} | "
                         f"{metric_text(work['mixed_PTE'])} |")
    lines.extend(["", "## Interpretation cautions", "",
                  f"- {comparison['method']['independence_caution']}",
                  f"- {comparison['method']['genre_inference_caution']}",
                  "- Counts with a zero denominator use a null/unknown proportion.", ""])
    return "\n".join(lines)


def write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--canonical-report", required=True, type=Path)
    parser.add_argument("--pilot-report", required=True, type=Path)
    parser.add_argument("--output-json", required=True, type=Path)
    parser.add_argument("--output-markdown", required=True, type=Path)
    args = parser.parse_args()
    try:
        canonical = json.loads(args.canonical_report.read_text(encoding="utf-8"))
        pilot = json.loads(args.pilot_report.read_text(encoding="utf-8"))
        comparison = build_comparison(canonical, pilot, args.canonical_report, args.pilot_report)
        write_atomic(args.output_json, json.dumps(comparison, indent=2, ensure_ascii=False) + "\n")
        write_atomic(args.output_markdown, render_markdown(comparison))
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {args.output_json} and {args.output_markdown}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
