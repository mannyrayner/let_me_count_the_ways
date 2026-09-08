#!/usr/bin/env python3
"""Fill reviewed acquisition provenance from local literary and raw files."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from datetime import UTC, date, datetime
from pathlib import Path


SUMMARY_FIELDS = (
    "pages_requested",
    "pages_downloaded",
    "pages_nonempty",
    "assembled_character_count",
    "assembled_word_count",
    "sha256",
)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc_mtime(path: Path) -> str:
    value = datetime.fromtimestamp(path.stat().st_mtime, UTC).replace(microsecond=0)
    return value.isoformat().replace("+00:00", "Z")


def atomic_json_write(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".part", dir=path.parent
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as output:
            json.dump(value, output, indent=2, ensure_ascii=False)
            output.write("\n")
        Path(temporary_name).replace(path)
    except Exception:
        Path(temporary_name).unlink(missing_ok=True)
        raise


def raw_paths(record: dict) -> list[Path]:
    if record.get("download_path"):
        return [Path(record["download_path"])]
    page_map_path = record.get("page_map_path")
    if not page_map_path:
        raise ValueError(f"{record.get('source_id')}: no download_path or page_map_path")
    pages = json.loads(Path(page_map_path).read_text(encoding="utf-8"))
    paths = [Path(page["raw_path"]) for page in pages]
    if not paths:
        raise ValueError(f"{record.get('source_id')}: page map is empty")
    return paths


def finalized_record(record: dict, reviewed_on: str, approve: bool) -> dict:
    source_id = record.get("source_id", "unknown source")
    source = Path(record["local_path"])
    if not source.is_file() or not source.stat().st_size:
        raise ValueError(f"{source_id}: literary source is missing or empty: {source}")
    raws = raw_paths(record)
    for raw in raws:
        if not raw.is_file() or not raw.stat().st_size:
            raise ValueError(f"{source_id}: raw source is missing or empty: {raw}")

    result = dict(record)
    result["sha256"] = file_sha256(source)
    result["retrieved_at"] = result.get("retrieved_at") or max(utc_mtime(raw) for raw in raws)
    result["reviewed_on"] = reviewed_on
    if len(raws) == 1 and result.get("download_path"):
        result["download_sha256"] = file_sha256(raws[0])
    else:
        result["download_paths"] = [str(raw) for raw in raws]
        result["download_sha256"] = {raw.name: file_sha256(raw) for raw in raws}

    metadata_path = source.parent / "acquisition-metadata.json"
    if metadata_path.is_file():
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        if metadata.get("sha256") != result["sha256"]:
            raise ValueError(
                f"{source_id}: acquisition metadata hash {metadata.get('sha256')!r} "
                f"does not match literary source {result['sha256']}"
            )
        if all(field in metadata for field in SUMMARY_FIELDS):
            result["acquisition_summary"] = {
                field: metadata[field] for field in SUMMARY_FIELDS
            }

    if approve:
        rights_note = result.get("rights_note", "")
        if not rights_note or "PENDING" in rights_note.upper():
            raise ValueError(f"{source_id}: cannot approve a missing or pending rights_note")
        result["review_status"] = "approved_for_development_processing"
    return result


def finalize_batch(batch_path: Path, reviewed_on: str, approve: bool = False) -> list[Path]:
    date.fromisoformat(reviewed_on)
    batch = json.loads(batch_path.read_text(encoding="utf-8"))
    updates: list[tuple[Path, dict]] = []
    for member in batch["sources"]:
        path = Path(member["provenance"])
        record = json.loads(path.read_text(encoding="utf-8"))
        updates.append((path, finalized_record(record, reviewed_on, approve)))
    # Compute and validate the whole batch before replacing any provenance file.
    for path, record in updates:
        atomic_json_write(path, record)
    return [path for path, _ in updates]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", type=Path, required=True)
    parser.add_argument("--reviewed-on", required=True, help="Review date in YYYY-MM-DD form")
    parser.add_argument(
        "--approve", action="store_true",
        help="Mark every member approved after rejecting pending rights notes",
    )
    args = parser.parse_args()
    for path in finalize_batch(args.batch, args.reviewed_on, args.approve):
        print(path)


if __name__ == "__main__":
    main()
