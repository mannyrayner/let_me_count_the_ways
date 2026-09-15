#!/usr/bin/env python3
"""Copy an approved UTF-8 text into a canonical work and write its manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def build_work(source: Path, works_root: Path, metadata: dict) -> Path:
    """Copy *source* byte-for-byte and create a deterministic work manifest."""
    source_bytes = source.read_bytes()
    source_bytes.decode("utf-8")
    work_dir = works_root / metadata["work_id"]
    work_dir.mkdir(parents=True, exist_ok=True)
    canonical = work_dir / "canonical.txt"
    canonical.write_bytes(source_bytes)

    manifest = {
        "schema_version": "1.0",
        "work_id": metadata["work_id"],
        "title": metadata["title"],
        "author": metadata["author"],
        "language": metadata["language"],
        "source_type": metadata["source_type"],
        "canonical_text": "canonical.txt",
        "canonical_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "source_references": metadata["source_references"],
        "rights": {
            "analysis_allowed": metadata["analysis_allowed"],
            "public_render_policy": metadata["public_render_policy"],
        },
        "notes": metadata.get("notes", ""),
    }
    manifest_path = work_dir / "work.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return manifest_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="approved existing UTF-8 literary text")
    parser.add_argument("--works-root", type=Path, default=Path("corpus/works"))
    parser.add_argument("--work-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--author", required=True)
    parser.add_argument("--language", required=True)
    parser.add_argument(
        "--source-type", required=True,
        choices=("gutenberg_single", "gutenberg_multi", "runeberg", "local_permissioned"),
    )
    parser.add_argument("--source-reference", action="append", required=True)
    parser.add_argument("--public-render-policy", required=True)
    parser.add_argument("--analysis-allowed", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--notes", default="")
    args = parser.parse_args()
    metadata = vars(args)
    source = metadata.pop("source")
    works_root = metadata.pop("works_root")
    metadata["source_references"] = metadata.pop("source_reference")
    path = build_work(source, works_root, metadata)
    print(f"Wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
