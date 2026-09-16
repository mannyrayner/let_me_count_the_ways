#!/usr/bin/env python3
"""Atomically rederive the three Undset volumes without network access."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.corpus_acquisition.acquire_public_domain_text import acquire_runeberg, sha256


VOLUMES = {
    "kransen": ("1", 5, 370, "runeberg-kristin-kransen.txt"),
    "husfrue": ("2", 9, 505, "runeberg-kristin-husfrue.txt"),
    "korset": ("3", 7, 527, "runeberg-kristin-korset.txt"),
}


def reuse_only(_url: str, destination: Path) -> bool:
    if not destination.is_file() or not destination.stat().st_size:
        raise FileNotFoundError(f"stored Runeberg page is missing: {destination}")
    return False


def raw_digest(raw_dir: Path) -> str:
    digest = hashlib.sha256()
    for page in sorted(raw_dir.glob("*.html")):
        digest.update(page.name.encode("utf-8") + b"\0" + page.read_bytes())
    return digest.hexdigest()


def main() -> None:
    base = Path("data/raw/undset-kristin-lavransdatter")
    for name, (part, first, last, filename) in VOLUMES.items():
        directory = base / name
        raw_dir = directory / "source-pages"
        output = directory / filename
        page_map = directory / "page-map.json"
        metadata_path = directory / "acquisition-metadata.json"
        prior_metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        old_sha = prior_metadata.get("derivation_repair", {}).get(
            "old_derived_sha256", sha256(output)
        )
        before_raw = raw_digest(raw_dir)
        with tempfile.TemporaryDirectory(dir=directory, prefix="rederive-") as temporary:
            temporary = Path(temporary)
            staged_output = temporary / filename
            staged_map = temporary / "page-map.json"
            metadata = acquire_runeberg(
                f"https://runeberg.org/kristin/{part}/", first, last, raw_dir,
                staged_output, staged_map, downloader=reuse_only,
            )
            if raw_digest(raw_dir) != before_raw:
                raise RuntimeError(f"raw Runeberg pages changed while deriving {name}")
            old_map = json.loads(page_map.read_text(encoding="utf-8"))
            new_map = json.loads(staged_map.read_text(encoding="utf-8"))
            if [row["raw_sha256"] for row in old_map] != [row["raw_sha256"] for row in new_map]:
                raise RuntimeError(f"raw SHA-256 lineage changed for {name}")
            # Retain this acquisition's established Cygwin/Windows JSON path
            # spelling so the rebuild changes offsets, not every path line.
            for row in new_map:
                row["raw_path"] = row["raw_path"].replace("/", "\\")
            staged_map.write_text(
                json.dumps(new_map, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
            metadata["local_path"] = str(output).replace("/", "\\")
            metadata["page_map"] = str(page_map).replace("/", "\\")
            metadata["download_paths"] = [path.replace("/", "\\")
                                          for path in metadata["download_paths"]]
            metadata["derivation_repair"] = {
                "version": "runeberg-prefix-v1",
                "reason": "Preserve nonnumeric text before the first OCR <br>; strip digits-only pagination.",
                "raw_source_pages_unchanged": True,
                "old_derived_sha256": old_sha,
                "new_derived_sha256": metadata["sha256"],
            }
            staged_metadata = temporary / "acquisition-metadata.json"
            staged_metadata.write_text(
                json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
            staged_output.replace(output)
            staged_map.replace(page_map)
            staged_metadata.replace(metadata_path)
        print(f"{name}: {old_sha} -> {sha256(output)}")


if __name__ == "__main__":
    main()
