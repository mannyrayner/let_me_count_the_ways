#!/usr/bin/env python3
"""Build the expansion-15 acquisition inventory from finalized provenance."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def build_inventory(batch_path: Path, manifest_path: Path) -> dict:
    batch = json.loads(batch_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    records = [
        json.loads(Path(member["provenance"]).read_text(encoding="utf-8"))
        for member in batch["sources"]
    ]
    by_work: dict[str, list[dict]] = {}
    for record in records:
        if record.get("review_status") != "approved_for_development_processing":
            raise ValueError(f"{record['source_id']}: provenance is not approved")
        source = Path(record["local_path"])
        if not source.is_file() or not source.stat().st_size:
            raise ValueError(f"{record['source_id']}: derived text is missing or empty")
        if not record.get("sha256"):
            raise ValueError(f"{record['source_id']}: finalized SHA-256 is missing")
        by_work.setdefault(record["work_id"], []).append(record)

    works = manifest["works"]
    if set(by_work) != {work["work_id"] for work in works}:
        raise ValueError("batch and inventory work IDs do not match")
    for work in works:
        members = by_work[work["work_id"]]
        work["acquisition_status"] = "acquired"
        if len(members) == 1:
            record = members[0]
            work["derived_text_path"] = record["local_path"]
            work["derived_sha256"] = record["sha256"]
        else:
            work["derived_text_path"] = None
            work["derived_sha256"] = None
            parts = []
            for record in members:
                parts.append({
                    "title": record["title"].split(": ", 1)[-1],
                    "volume_url": record["volume_url"],
                    "derived_text_path": record["local_path"],
                    "derived_sha256": record["sha256"],
                    "acquisition_status": "acquired",
                })
            work["constituent_parts"] = parts
    manifest["status"] = "acquired"
    manifest["successful_work_count"] = len(works)
    manifest["blocking_reason"] = None
    return manifest


def summary_markdown(manifest: dict) -> str:
    lines = [
        "# Expansion 15 acquisition status", "",
        f"**Status: {manifest['successful_work_count']}/{manifest['target_work_count']} acquired.**",
        "", "| Work | Source | Language | Status | Characters | Warning |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for work in manifest["works"]:
        identity = work["source_identity"]
        if work["source_type"] == "gutenberg":
            source = f"Gutenberg {identity['ebook_number']}"
            paths = [Path(work["derived_text_path"])]
        else:
            source = f"Runeberg `{identity['volume_url'].removeprefix('https://runeberg.org')}`"
            paths = [Path(part["derived_text_path"]) for part in work.get("constituent_parts", [])]
            if not paths:
                paths = [Path(work["derived_text_path"])]
        characters = sum(len(path.read_text(encoding="utf-8")) for path in paths)
        warning = "—"
        if work["work_id"] == "balzac-illusions-perdues":
            warning = "Acquired as the reviewed containing volume"
        elif work["work_id"] == "undset-kristin-lavransdatter":
            warning = "Three separately preserved parts; uncorrected OCR"
        lines.append(
            f"| {work['title']} | {source} | {work['language']} | acquired | "
            f"{characters} | {warning} |"
        )
    lines.extend(["", "Hashes and source-level details are recorded in finalized provenance.", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args()
    manifest = build_inventory(args.batch, args.manifest)
    args.manifest.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    args.summary.write_text(summary_markdown(manifest), encoding="utf-8")


if __name__ == "__main__":
    main()
