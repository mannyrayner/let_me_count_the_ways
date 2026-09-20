#!/usr/bin/env python3
"""Check, or explicitly run, the existing API pipeline for the five-work extension.

Default is a read-only preflight. --run uses the configured OPENAI_API_KEY and
existing 5.6 model alias, membership prompt, translation prompt, and v0.3.1
classification. All output paths belong to this exploratory extension.
"""
from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.api.call_responses import resolve_model
from scripts.corpus.validate_canonical_corpus import validate_work
from scripts.review.scholarly_candidate_review import candidates

SELECTION = Path("data/acquisition/commitment_extension_5_v1/selection.json")
EXTRACTION = Path("results/extraction/commitment_extension_5_v0_12")
REVIEW = Path("results/review/commitment_extension_5_v0_12_ai_review_v1")
KEPT = REVIEW / "kept_candidates/kept_candidates.jsonl"
TRANSLATIONS = Path("results/annotation/commitment_extension_5_v0_12_translations_v1")
ENRICHED = REVIEW / "kept_candidates/enriched_full_v1.jsonl"
ANNOTATION = Path("results/annotation/commitment_extension_5_v0_12_v0_3_1")


def read_json(path: Path) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def preflight(model: str) -> dict:
    selection = read_json(SELECTION)
    wanted = {row["work_id"] for row in selection["works"]}
    summary = read_json(EXTRACTION / "summary.json")
    if summary["pattern_version"] != "0.12":
        raise ValueError("extension must use versioned v0.12 extraction")
    if {row["work_id"] for row in summary["works"]} != wanted:
        raise ValueError("extraction work set differs from the selection")
    records = candidates(ROOT / EXTRACTION)
    if len(records) != summary["total_candidates"] or len({r['occurrence_id'] for r in records}) != len(records):
        raise ValueError("extraction count or uniqueness check failed")
    for work_id in sorted(wanted):
        directory = ROOT / "corpus/works" / work_id
        errors, manifest = validate_work(directory, ROOT)
        if errors:
            raise ValueError("; ".join(errors))
        text = (directory / "canonical.txt").read_text(encoding="utf-8")
        for record in [row for row in records if row["work_id"] == work_id]:
            if record["canonical_sha256"] != manifest["canonical_sha256"]:
                raise ValueError(f"stale extraction: {record['occurrence_id']}")
            if text[record["start"]:record["end"]] != record["match"]:
                raise ValueError(f"invalid match offsets: {record['occurrence_id']}")
            if text[record["context_start"]:record["context_end"]] != record["context"]:
                raise ValueError(f"invalid context offsets: {record['occurrence_id']}")
    api_model, pricing = resolve_model(ROOT / "config/api_models.json", model, date.today())
    return {"status": "ready_for_membership_review", "work_count": len(wanted),
            "candidate_count": len(records), "model_alias": model, "api_model": api_model,
            "pricing_verified_on": pricing["pricing_verified_on"],
            "api_key_configured": bool(os.environ.get("OPENAI_API_KEY")),
            "pattern_sha256": hashlib.sha256((ROOT / selection['extraction_patterns']).read_bytes()).hexdigest(),
            "classification_prompt_sha256": hashlib.sha256((ROOT / selection['classification_prompt']).read_bytes()).hexdigest(),
            "annotation_status": "complete" if (ROOT / ANNOTATION / "summary.json").exists()
                and read_json(ANNOTATION / "summary.json").get("status") == "complete" else "not_complete"}


def command(script: str, *args: object) -> None:
    subprocess.run([sys.executable, "-u", script, *map(str, args)], cwd=ROOT, check=True)


def check_estimate(directory: Path, max_usd: float) -> None:
    estimate = read_json(directory / "estimate.json")
    cost = estimate["estimated_total_usd"]
    if cost > max_usd:
        raise ValueError(f"{directory}: estimate USD {cost:.2f} exceeds stage limit USD {max_usd:.2f}")


def run(model: str, max_usd: float, timeout: int) -> None:
    checked = preflight(model)
    if not checked["api_key_configured"]:
        raise ValueError("OPENAI_API_KEY is not configured; preflight passed, but no API calls were made")
    reviewer = "scripts/review/scholarly_candidate_review.py"
    command(reviewer, "run", "--candidates", EXTRACTION, "--output", REVIEW, "--model", model)
    command(reviewer, "validate", "--candidates", EXTRACTION, "--review", REVIEW,
            "--expected-total", checked["candidate_count"])
    command(reviewer, "render", "--candidates", EXTRACTION, "--review", REVIEW, "--output", REVIEW)
    command(reviewer, "freeze", "--candidates", EXTRACTION, "--review", REVIEW,
            "--output", KEPT.parent)
    kept_count = sum(bool(line.strip()) for line in (ROOT / KEPT).read_text(encoding="utf-8").splitlines())
    if not kept_count:
        raise ValueError("membership review retained no cases; inspect its decisions before proceeding")
    translator = "scripts/annotation/generate_context_translations.py"
    translation_args = ("--reviewed", KEPT, "--all-reviewed", "--output", TRANSLATIONS,
                        "--model", model, "--timeout", timeout)
    command(translator, *translation_args, "--estimate-only")
    check_estimate(TRANSLATIONS, max_usd)
    command(translator, *translation_args)
    translations = read_json(TRANSLATIONS / "summary.json")
    if translations.get("status") != "complete" or translations.get("failed") != 0:
        raise ValueError("translation stage incomplete; compatible successful calls will resume")
    command("scripts/annotation/enrich_canonical_candidates.py", "--reviewed", KEPT,
            "--generated", TRANSLATIONS / "generated_enrichment.json", "--output", ENRICHED)
    annotator = "scripts/annotation/annotate_canonical_candidates.py"
    annotation_args = ("--enriched", ENRICHED, "--all", "--output", ANNOTATION,
                       "--model", model, "--timeout", timeout)
    command(annotator, *annotation_args, "--estimate-only")
    check_estimate(ANNOTATION, max_usd)
    command(annotator, *annotation_args)
    summary = read_json(ANNOTATION / "summary.json")
    if not (summary.get("status") == "complete" and summary.get("failed") == 0
            and summary.get("requested") == summary.get("valid") == kept_count):
        raise ValueError("annotation stage incomplete; inspect failure inventory and resume")
    print(json.dumps(summary["distributions"], ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="store_true", help="make the resumable model API calls")
    parser.add_argument("--model", default="5.6")
    parser.add_argument("--max-stage-usd", type=float, default=25,
                        help="estimate limit for each translation and classification stage; membership review is separately metered")
    parser.add_argument("--timeout", type=int, default=300)
    args = parser.parse_args()
    if args.max_stage_usd <= 0 or args.timeout <= 0:
        parser.error("cost limit and timeout must be positive")
    print(json.dumps(preflight(args.model), ensure_ascii=False, indent=2))
    if args.run:
        run(args.model, args.max_stage_usd, args.timeout)


if __name__ == "__main__":
    main()
