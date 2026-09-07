#!/usr/bin/env python3
"""Extract local-only candidates without weakening the production rights gate."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts.extraction.extract_passages import extract, load_patterns

LOCAL_STATUS = "local_triage_only"
TRIAGE_LABELS = (
    "potentially interesting",
    "ordinary avowal",
    "embedded",
    "repeated/clustered",
    "unclear",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require_ignored(path: Path, repo_root: Path) -> None:
    try:
        relative = path.resolve().relative_to(repo_root.resolve())
    except ValueError:
        return
    check = subprocess.run(
        ["git", "check-ignore", "--quiet", "--", str(relative)],
        cwd=repo_root,
        check=False,
    )
    if check.returncode != 0:
        raise ValueError(f"local triage path is not ignored by Git: {relative}")


def load_local_source(provenance_path: Path, repo_root: Path) -> tuple[dict, Path, str]:
    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    if provenance.get("review_status") != LOCAL_STATUS:
        raise ValueError(
            f"review_status must be {LOCAL_STATUS!r}; local triage never grants rights approval"
        )
    required = {
        "source_id", "work_id", "title", "author", "language",
        "local_path", "sha256", "original_source_path", "original_source_sha256",
    }
    missing = required - provenance.keys()
    if missing:
        raise ValueError(f"local provenance record lacks required fields: {sorted(missing)}")
    if provenance["language"] != "en":
        raise ValueError("this three-book triage requires the 'en' pattern family")
    source_path = Path(provenance["local_path"]).expanduser()
    if not source_path.is_absolute():
        source_path = repo_root / source_path
    require_ignored(provenance_path, repo_root)
    require_ignored(source_path, repo_root)
    actual_hash = sha256_file(source_path)
    if actual_hash != provenance["sha256"]:
        raise ValueError(
            f"derived-text hash mismatch: expected {provenance['sha256']}, found {actual_hash}"
        )
    text = source_path.read_text(encoding="utf-8")
    return provenance, source_path, text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("provenance", type=Path)
    parser.add_argument("--patterns", type=Path,
                        default=Path("data/development/search_patterns_v0_5.json"))
    parser.add_argument("--output-root", type=Path,
                        default=Path("results/local_candidate_triage"))
    parser.add_argument("--context-chars", type=int, default=1000)
    args = parser.parse_args()

    repo_root = REPOSITORY_ROOT
    provenance_path = args.provenance.resolve()
    output_root = args.output_root
    if not output_root.is_absolute():
        output_root = repo_root / output_root
    require_ignored(output_root, repo_root)
    provenance, source_path, text = load_local_source(provenance_path, repo_root)
    version, patterns = load_patterns(args.patterns, "en")
    records = extract(
        text, "en", provenance["work_id"], provenance["source_id"],
        version, patterns, args.context_chars,
    )

    work_root = output_root / provenance["work_id"]
    work_root.mkdir(parents=True, exist_ok=True)
    occurrence_path = work_root / "occurrences.jsonl"
    with occurrence_path.open("w", encoding="utf-8") as stream:
        for record in records:
            record["relative_position"] = round(record["start"] / len(text), 6) if text else 0.0
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")

    review_path = work_root / "manual_review.tsv"
    with review_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t")
        writer.writerow(("occurrence_id", "start", "end", "relative_position",
                         "pattern_id", "triage_label", "scene_cluster", "notes"))
        for record in records:
            writer.writerow((record["occurrence_id"], record["start"], record["end"],
                             record["relative_position"], record["pattern_id"], "", "", ""))

    manifest = {
        "review_status": LOCAL_STATUS,
        "annotation_model_calls": 0,
        "work_id": provenance["work_id"],
        "title": provenance["title"],
        "author": provenance["author"],
        "derived_text_path": str(source_path),
        "derived_text_sha256": provenance["sha256"],
        "pattern_version": version,
        "pattern_manifest_sha256": sha256_file(args.patterns),
        "context_characters": args.context_chars,
        "candidate_occurrences": len(records),
        "allowed_triage_labels": TRIAGE_LABELS,
        "manual_review_complete": False,
    }
    (work_root / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"wrote {len(records)} occurrence(s) to ignored local directory {work_root}")
    print(f"complete every row in {review_path}; no annotation calls were made")


if __name__ == "__main__":
    main()
