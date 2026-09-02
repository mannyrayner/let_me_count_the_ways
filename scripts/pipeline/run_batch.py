#!/usr/bin/env python3
"""Run a resumable, manifest-defined corpus through the single-text pipeline."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts.pipeline.compare_annotation_versions import compare
from scripts.pipeline.run_single_text_pipeline import (
    ANNOTATION_FILES, read_json, resolve_source, run_pipeline, sha256_file, write_json,
)


def load_batch_manifest(path: Path) -> dict:
    value = read_json(path)
    required = {"schema_version", "batch_id", "description", "sources"}
    if not isinstance(value, dict) or set(value) != required:
        raise ValueError(f"batch manifest must contain exactly {sorted(required)}")
    if value["schema_version"] != "0.1" or not value["batch_id"]:
        raise ValueError("unsupported batch schema or empty batch_id")
    if not isinstance(value["sources"], list) or not value["sources"]:
        raise ValueError("batch sources must be a non-empty array")
    paths = []
    for item in value["sources"]:
        if not isinstance(item, dict) or set(item) != {"provenance"} or not item["provenance"]:
            raise ValueError("each source must contain only a non-empty provenance path")
        paths.append(item["provenance"])
    if len(paths) != len(set(paths)):
        raise ValueError("batch provenance paths must be unique")
    return value


def find_reusable_extraction(*, source_id: str, source_sha256: str, context_chars: int,
                             extractor_sha256: str, extraction_root: Path) -> Path | None:
    candidates = []
    for metadata_path in (extraction_root / source_id).glob("*/extraction/metadata.json"):
        passages = metadata_path.parent / "passages.jsonl"
        fingerprint = read_json(metadata_path).get("fingerprint", {})
        if (passages.exists() and fingerprint.get("source_sha256") == source_sha256
                and fingerprint.get("context_characters") == context_chars
                and fingerprint.get("extractor_sha256") == extractor_sha256):
            manifest_path = metadata_path.parents[1] / "manifest.json"
            complete = manifest_path.exists() and read_json(manifest_path).get("status") == "complete"
            candidates.append((complete, metadata_path.parent))
    return sorted(candidates, key=lambda item: (item[0], str(item[1])))[-1][1] if candidates else None


def pattern_for_extraction(extraction: Path, candidates: list[Path]) -> Path:
    expected = read_json(extraction / "metadata.json")["fingerprint"]["patterns_sha256"]
    for candidate in candidates:
        if candidate.exists() and sha256_file(candidate) == expected:
            return candidate
    raise ValueError(f"no supplied search-pattern file matches reused extraction hash {expected}")


def seed_extraction(source: Path, destination_run: Path) -> bool:
    destination = destination_run / "extraction"
    if destination.exists() or source is None:
        return False
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    return True


def markdown_summary(summary: dict) -> str:
    lines = [
        f"# Batch report: {summary['batch_id']}", "", "## Configuration", "",
        f"- **Annotation:** v{summary['annotation_version']}",
        f"- **Model alias:** `{summary['model_alias']}`",
        f"- **Status:** `{summary['status']}`",
        f"- **Dry run:** `{summary['dry_run']}`", "", "## Totals", "",
        f"- **Texts requested:** {summary['texts_requested']}",
        f"- **Texts completed:** {summary['texts_completed']}",
        f"- **Texts partial/failed:** {summary['texts_partial_or_failed']}",
        f"- **Texts with valid outputs resumed/skipped:** {summary['texts_resumed_or_skipped']}",
        f"- **Occurrences:** {summary['occurrences']}",
        f"- **Attempted this invocation:** {summary['occurrences_attempted_this_invocation']}",
        f"- **Valid annotations:** {summary['valid_annotations']}",
        f"- **Model calls still needed:** {summary['model_calls_needed']}",
        f"- **Unresolved failed occurrences:** {summary['failures']}",
        f"- **Historical failed/invalid attempts:** {summary['historical_failed_attempts']}",
        f"- **Estimated recorded cost:** USD {summary['estimated_total_cost_usd']:.6f}", "",
        "## Texts", "",
    ]
    for text in summary["texts"]:
        lines.extend([
            f"### {text.get('title', text['source_id'])}", "",
            f"- **Source:** `{text['source_id']}`", f"- **Status:** `{text['status']}`",
            f"- **Occurrences / valid:** {text['extracted_occurrences']} / {text['valid_occurrences']}",
            f"- **Attempted / unresolved failures:** {text['attempted_this_invocation']} / {text['failures']}",
            f"- **Historical failed/invalid attempts:** {text['historical_failed_attempts']}",
            f"- **Cost:** USD {text['estimated_total_cost_usd']:.6f}",
            f"- **Recorded cost per valid annotation:** USD {text['cost_per_valid_annotation_usd']:.6f}",
            f"- **Result:** `{text['result_location']}`",
        ])
        if text.get("error"):
            lines.append(f"- **Error:** {text['error']}")
        lines.append("")
    return "\n".join(lines)


def run_batch(*, repo_root: Path, manifest_path: Path, annotation_version: str,
              model_alias: str, patterns_paths: list[Path], output_root: Path,
              extraction_root: Path, context_chars: int = 1000, dry_run: bool = False,
              force: bool = False, compare_with: str | None = None,
              now=lambda: datetime.now(timezone.utc)) -> Path:
    repo_root = repo_root.resolve()
    manifest_path = (repo_root / manifest_path).resolve() if not manifest_path.is_absolute() else manifest_path
    batch = load_batch_manifest(manifest_path)
    output_root = (repo_root / output_root).resolve() if not output_root.is_absolute() else output_root
    extraction_root = (repo_root / extraction_root).resolve() if not extraction_root.is_absolute() else extraction_root
    patterns_paths = [
        (repo_root / path).resolve() if not path.is_absolute() else path for path in patterns_paths
    ]
    batch_dir = output_root / batch["batch_id"] / f"v{annotation_version}-{model_alias}"
    batch_dir.mkdir(parents=True, exist_ok=True)
    started = now().isoformat()
    texts = []
    for source in batch["sources"]:
        provenance_path = repo_root / source["provenance"]
        provenance, _, _ = resolve_source(provenance_path, repo_root)
        source_id = provenance["source_id"]
        run_dir = batch_dir / "texts" / source_id
        seeded = False
        try:
            reusable = find_reusable_extraction(
                source_id=source_id, source_sha256=provenance["sha256"],
                context_chars=context_chars,
                extractor_sha256=sha256_file(repo_root / "scripts/extraction/extract_passages.py"),
                extraction_root=extraction_root,
            )
            if reusable is None:
                raise ValueError("no compatible existing extraction; refusing implicit re-extraction")
            patterns_path = pattern_for_extraction(reusable, patterns_paths)
            seeded = seed_extraction(reusable, run_dir)
            run_pipeline(
                repo_root=repo_root, provenance_path=provenance_path, patterns_path=patterns_path,
                annotation_version=annotation_version, model_alias=model_alias,
                output_root=batch_dir / "unused", run_dir=run_dir, context_chars=context_chars,
                dry_run=dry_run, force=force,
            )
            text_manifest = read_json(run_dir / "manifest.json")
            texts.append({
                "source_id": source_id, "title": provenance["title"],
                "status": text_manifest["status"],
                "extraction_seeded_this_invocation": seeded,
                "extracted_occurrences": text_manifest["extracted_occurrences"],
                "attempted_this_invocation": text_manifest["attempted_this_invocation"],
                "valid_occurrences": text_manifest["valid_occurrences"],
                "failures": text_manifest.get("unresolved_failed_occurrences", 0),
                "historical_failed_attempts": text_manifest["invalid_or_failed_attempts"],
                "skipped_valid_this_invocation": text_manifest["skipped_valid_this_invocation"],
                "recovered_without_model_call_this_invocation": text_manifest.get(
                    "recovered_without_model_call_this_invocation", 0),
                "estimated_total_cost_usd": text_manifest["usage_and_cost"]["estimated_total_cost_usd"],
                "cost_per_valid_annotation_usd": (
                    text_manifest["usage_and_cost"]["estimated_total_cost_usd"] /
                    text_manifest["valid_occurrences"] if text_manifest["valid_occurrences"] else 0.0
                ),
                "result_location": str(run_dir.relative_to(repo_root)),
            })
        except Exception as exc:  # A failed text must not prevent other texts from completing.
            existing = read_json(run_dir / "manifest.json") if (run_dir / "manifest.json").exists() else {}
            texts.append({
                "source_id": source_id, "title": provenance["title"], "status": "error",
                "extraction_seeded_this_invocation": seeded,
                "extracted_occurrences": existing.get("extracted_occurrences", 0),
                "attempted_this_invocation": 0,
                "valid_occurrences": existing.get("valid_occurrences", 0),
                "failures": existing.get("unresolved_failed_occurrences", 0) + 1,
                "historical_failed_attempts": existing.get("invalid_or_failed_attempts", 0),
                "skipped_valid_this_invocation": 0,
                "recovered_without_model_call_this_invocation": 0,
                "estimated_total_cost_usd": existing.get("usage_and_cost", {}).get(
                    "estimated_total_cost_usd", 0.0),
                "cost_per_valid_annotation_usd": (
                    existing.get("usage_and_cost", {}).get("estimated_total_cost_usd", 0.0) /
                    existing.get("valid_occurrences", 1) if existing.get("valid_occurrences") else 0.0
                ),
                "result_location": str(run_dir.relative_to(repo_root)),
                "error": f"{type(exc).__name__}: {exc}",
            })
    summary = {
        "batch_id": batch["batch_id"], "batch_manifest": str(manifest_path.relative_to(repo_root)),
        "annotation_version": annotation_version, "model_alias": model_alias,
        "started_at": started, "ended_at": now().isoformat(), "dry_run": dry_run,
        "force": force, "texts_requested": len(texts),
        "texts_completed": sum(t["status"] == "complete" for t in texts),
        "texts_partial_or_failed": sum(t["status"] in {"partial", "error"} for t in texts),
        "texts_resumed_or_skipped": sum(t["skipped_valid_this_invocation"] > 0 for t in texts),
        "annotations_recovered_without_model_call": sum(
            t["recovered_without_model_call_this_invocation"] for t in texts),
        "occurrences": sum(t["extracted_occurrences"] for t in texts),
        "occurrences_attempted_this_invocation": sum(t["attempted_this_invocation"] for t in texts),
        "valid_annotations": sum(t["valid_occurrences"] for t in texts),
        "model_calls_needed": sum(
            max(0, t["extracted_occurrences"] - t["valid_occurrences"]) for t in texts),
        "failures": sum(t["failures"] for t in texts),
        "historical_failed_attempts": sum(t["historical_failed_attempts"] for t in texts),
        "estimated_total_cost_usd": sum(t["estimated_total_cost_usd"] for t in texts),
        "status": "complete" if all(t["status"] == "complete" for t in texts) else
                  ("prepared" if dry_run and all(t["status"] == "prepared" for t in texts) else "partial"),
        "batch_result_location": str(batch_dir.relative_to(repo_root)), "texts": texts,
    }
    write_json(batch_dir / "summary.json", summary)
    (batch_dir / "report.md").write_text(markdown_summary(summary), encoding="utf-8")
    if compare_with:
        comparison, report = compare(
            batch_summary_path=batch_dir / "summary.json", reference_root=extraction_root,
            old_version=compare_with,
        )
        write_json(batch_dir / "comparison.json", comparison)
        (batch_dir / "comparison.md").write_text(report, encoding="utf-8")
    return batch_dir


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--annotation-version", choices=sorted(ANNOTATION_FILES), required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument(
        "--patterns", type=Path, action="append", dest="patterns",
        help="candidate search-pattern file; repeat when reused texts used different versions",
    )
    parser.add_argument("--output-root", type=Path, default=Path("results/batch_runs"))
    parser.add_argument("--extraction-root", type=Path, default=Path("results/pipeline_runs"))
    parser.add_argument("--context-chars", type=int, default=1000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--compare-with")
    args = parser.parse_args()
    result = run_batch(
        repo_root=REPOSITORY_ROOT, manifest_path=args.manifest,
        annotation_version=args.annotation_version, model_alias=args.model,
        patterns_paths=args.patterns or [
            Path("data/development/search_patterns_v0_1.json"),
            Path("data/development/search_patterns_v0_2.json"),
        ], output_root=args.output_root,
        extraction_root=args.extraction_root, context_chars=args.context_chars,
        dry_run=args.dry_run, force=args.force, compare_with=args.compare_with,
    )
    print(result)


if __name__ == "__main__":
    main()
