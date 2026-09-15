#!/usr/bin/env python3
"""Deterministically extract broadened LOVE(I,YOU) candidates from the corpus."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PATTERNS = ROOT / "data/development/search_patterns_v0_7.json"
DEFAULT_OUTPUT = ROOT / "results/extraction/canonical_16_v0_7"
DEFAULT_PRIVATE_OUTPUT = ROOT / "results/extraction_private/canonical_16_v0_7"
PUBLIC_POLICIES = {"PUBLIC_DOMAIN_FULL_CONTEXT_OK", "PERMISSIONED_CONTEXT_OK"}
PRIVATE_POLICIES = {"LIMITED_QUOTATION_ONLY", "NO_PUBLIC_RENDER"}
TOOL_VERSION = "1.0"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def resolve_canonical(manifest_path: Path, manifest: dict) -> tuple[Path, str]:
    storage = manifest.get("canonical_storage", "repository")
    if storage == "repository":
        return manifest_path.parent / (manifest.get("canonical_text") or "canonical.txt"), storage
    if storage == "local_private":
        configured = Path(manifest["canonical_local_path"])
        return (configured if configured.is_absolute() else ROOT / configured), storage
    raise ValueError(f"unsupported canonical_storage {storage!r}")


def paragraph_window(text: str, start: int, end: int, radius: int) -> tuple[int, int]:
    left_limit, right_limit = max(0, start - radius), min(len(text), end + radius)
    left_break, right_break = text.rfind("\n\n", left_limit, start), text.find("\n\n", end, right_limit)
    return (left_break + 2 if left_break >= 0 else left_limit,
            right_break if right_break >= 0 else right_limit)


def extract_candidates(text: str, manifest: dict, version: str,
                       patterns: list[dict], radius: int) -> list[dict]:
    """Match unmodified canonical text; all offsets are Unicode code-point indices."""
    hits = []
    for order, pattern in enumerate(patterns):
        flags = 0 if pattern.get("case_sensitive", False) else re.IGNORECASE
        for match in re.finditer(pattern["regex"], text, flags):
            hits.append((match.start(), match.end(), order, pattern, match.group(0)))
    # Prefer the broadest match where patterns overlap, making form metadata specific.
    hits.sort(key=lambda hit: (hit[0], -(hit[1] - hit[0]), hit[2]))
    selected = []
    for hit in hits:
        if any(hit[0] < prior[1] and hit[1] > prior[0] for prior in selected):
            continue
        selected.append(hit)
    selected.sort(key=lambda hit: (hit[0], hit[1]))

    records = []
    canonical_hash = manifest["canonical_sha256"]
    metadata_fields = ("form_family", "polarity", "tense_aspect", "modality",
                       "temporal_modifier", "syntactic_family")
    for start, end, _, pattern, surface in selected:
        context_start, context_end = paragraph_window(text, start, end, radius)
        identity = "\0".join((manifest["work_id"], canonical_hash, str(start), str(end),
                              surface, version)).encode("utf-8")
        record = {
            "occurrence_id": f"{manifest['work_id']}-{hashlib.sha256(identity).hexdigest()[:16]}",
            "work_id": manifest["work_id"], "language": manifest["language"],
            "canonical_sha256": canonical_hash, "pattern_version": version,
            "pattern_id": pattern["id"], "match": surface, "start": start, "end": end,
            "context_start": context_start, "context_end": context_end,
            "context": text[context_start:context_end], "candidate_status": "candidate",
            "extraction_tool_version": TOOL_VERSION,
        }
        record.update({key: pattern[key] for key in metadata_fields if key in pattern})
        records.append(record)
    return records


def counts(records: list[dict], key: str) -> dict[str, int]:
    return dict(sorted(Counter(str(record.get(key, "unspecified")) for record in records).items()))


def historical_count(work_id: str) -> int | None:
    """Return the largest prior checked-in inventory count as a descriptive baseline."""
    values = []
    for path in ROOT.glob("results/**/extraction/passages.jsonl"):
        try:
            lines = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
        except (OSError, json.JSONDecodeError):
            continue
        if lines and lines[0].get("work_id") == work_id:
            values.append(len(lines))
    return max(values) if values else None


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records), encoding="utf-8")


def assert_known_cases(all_public: dict[str, list[dict]]) -> dict[str, bool]:
    surfaces = {work: [" ".join(r["match"].casefold().split()) for r in records]
                for work, records in all_public.items()}
    checks = {
        "nora_negative_cessation": any("jeg elsker deg ikke mer" in s for s in surfaces.get("ibsen-et-dukkehjem", [])),
        "rank_perfect_formal": any("jeg har elsket dem" in s for s in surfaces.get("ibsen-et-dukkehjem", [])),
        "lawrence_surface_formula": any("i love you" in s for s in surfaces.get("lawrence-women-in-love", [])),
    }
    missing = [name for name, found in checks.items() if not found]
    if missing:
        raise RuntimeError("known-case assertion(s) failed: " + ", ".join(missing))
    return checks


def run(pattern_path: Path, output: Path, private_output: Path, radius: int) -> dict:
    config = read_json(pattern_path)
    version = config["schema_version"]
    manifests = sorted((ROOT / "corpus/works").glob("*/work.json"))
    output.mkdir(parents=True, exist_ok=True)
    public_records, summaries = {}, []
    attempted = 0
    for manifest_path in manifests:
        manifest, attempted = read_json(manifest_path), attempted + 1
        work_id, rights = manifest["work_id"], manifest["rights"]
        policy = rights["public_render_policy"]
        work_summary = {"work_id": work_id, "language": manifest["language"],
                        "canonical_sha256": manifest["canonical_sha256"],
                        "public_render_policy": policy, "analysis_allowed": rights["analysis_allowed"]}
        if not rights["analysis_allowed"]:
            work_summary.update(status="skipped_analysis_not_allowed", candidate_count=0,
                                candidate_artifact="none")
            write_json(output / "works" / work_id / "summary.json", work_summary)
            summaries.append(work_summary); continue
        source, storage = resolve_canonical(manifest_path, manifest)
        work_summary["canonical_storage"] = storage
        if not source.is_file():
            print(f"WARNING: canonical source unavailable for {work_id}: {source}", file=sys.stderr)
            work_summary.update(status="unavailable", candidate_count=None,
                                candidate_artifact="unavailable", private_output_available=False)
            write_json(output / "works" / work_id / "summary.json", work_summary)
            summaries.append(work_summary); continue
        actual_hash = sha256(source)
        if actual_hash != manifest["canonical_sha256"]:
            raise RuntimeError(f"canonical hash mismatch for {work_id}: {actual_hash}")
        if manifest["language"] not in config["languages"]:
            raise RuntimeError(f"no {version} patterns for {manifest['language']} ({work_id})")
        text = source.read_text(encoding="utf-8")  # Deliberately no Unicode normalization.
        records = extract_candidates(text, manifest, version,
                                     config["languages"][manifest["language"]]["patterns"], radius)
        if policy in PUBLIC_POLICIES:
            artifact = output / "works" / work_id / "candidates.jsonl"
            write_jsonl(artifact, records); public_records[work_id] = records
            artifact_status, private_available = "public", False
        elif policy in PRIVATE_POLICIES:
            artifact = private_output / "works" / work_id / "candidates.jsonl"
            write_jsonl(artifact, records)
            artifact_status, private_available = "private_local", True
        else:
            raise RuntimeError(f"unsupported public_render_policy {policy!r} for {work_id}")
        work_summary.update(status="extracted", candidate_count=len(records),
                            candidate_artifact=artifact_status,
                            private_output_available=private_available,
                            counts_by_pattern=counts(records, "pattern_id"),
                            counts_by_form_family=counts(records, "form_family"),
                            historical_candidate_count=historical_count(work_id))
        write_json(output / "works" / work_id / "summary.json", work_summary)
        summaries.append(work_summary)

    known = assert_known_cases(public_records)
    aggregate = {
        "run_id": output.name, "pattern_version": version, "extraction_tool_version": TOOL_VERSION,
        "canonical_offset_unit": "Unicode code points in the unmodified decoded canonical text",
        "occurrence_identity": "SHA-256 prefix of NUL-joined work_id, canonical_sha256, start, end, matched surface, pattern version",
        "works_discovered": len(manifests), "works_attempted": attempted,
        "works_extracted": sum(w["status"] == "extracted" for w in summaries),
        "works_unavailable": sum(w["status"] == "unavailable" for w in summaries),
        "total_candidates": sum(w["candidate_count"] or 0 for w in summaries),
        "known_case_assertions": known, "works": summaries,
    }
    write_json(output / "summary.json", aggregate)
    write_json(output / "manifest.json", {key: aggregate[key] for key in (
        "run_id", "pattern_version", "extraction_tool_version", "canonical_offset_unit",
        "occurrence_identity", "works_discovered", "works_attempted")})
    rows = ["# Canonical corpus extraction v0.7", "", f"Total candidates: **{aggregate['total_candidates']}**", "",
            "| Work | Lang | Candidates | Artifact | Historical max | Form-family counts |",
            "| --- | --- | ---: | --- | ---: | --- |"]
    for w in summaries:
        families = ", ".join(f"{k}: {v}" for k, v in w.get("counts_by_form_family", {}).items()) or "—"
        old = w.get("historical_candidate_count")
        rows.append(f"| {w['work_id']} | {w['language']} | {w['candidate_count'] if w['candidate_count'] is not None else 'unavailable'} | {w['candidate_artifact']} | {old if old is not None else '—'} | {families} |")
    (output / "summary.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    return aggregate


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--patterns", type=Path, default=DEFAULT_PATTERNS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--private-output", type=Path, default=DEFAULT_PRIVATE_OUTPUT)
    parser.add_argument("--context-chars", type=int, default=1000)
    args = parser.parse_args()
    result = run(args.patterns.resolve(), args.output.resolve(), args.private_output.resolve(), args.context_chars)
    print(f"attempted {result['works_attempted']} works; extracted {result['total_candidates']} candidates")


if __name__ == "__main__":
    main()
