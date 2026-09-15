#!/usr/bin/env python3
"""Validate canonical work manifests and optionally regenerate corpus/index.md."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

SCHEMA_VERSION = "1.0"
SOURCE_TYPES = {"gutenberg_single", "gutenberg_multi", "runeberg", "local_permissioned"}
RIGHTS_POLICIES = {
    "PUBLIC_DOMAIN_FULL_CONTEXT_OK", "PERMISSIONED_CONTEXT_OK",
    "LIMITED_QUOTATION_ONLY", "NO_PUBLIC_RENDER",
}
STORAGE_MODES = {"repository", "local_private"}
RIGHTS_REVIEW_STATUSES = {"CLEAR", "REVIEW_REQUIRED", "BLOCKED"}
WORK_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
REQUIRED = {
    "schema_version", "work_id", "title", "author", "language", "source_type",
    "canonical_text", "canonical_sha256", "source_references", "rights", "notes",
}


def validate_work(work_dir: Path, repo_root: Path, warnings: list[str] | None = None) -> tuple[list[str], dict | None]:
    errors: list[str] = []
    manifest_path = work_dir / "work.json"
    if not manifest_path.is_file():
        return [f"{work_dir}: missing work.json"], None
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        return [f"{manifest_path}: invalid UTF-8 JSON: {exc}"], None
    if not isinstance(manifest, dict):
        return [f"{manifest_path}: manifest must be a JSON object"], None

    missing = sorted(REQUIRED - manifest.keys())
    if missing:
        errors.append(f"{manifest_path}: missing fields: {', '.join(missing)}")
    optional = {"canonical_storage", "canonical_local_path"}
    unexpected = sorted(manifest.keys() - REQUIRED - optional)
    if unexpected:
        errors.append(f"{manifest_path}: unexpected fields: {', '.join(unexpected)}")
    if manifest.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"{manifest_path}: unrecognized schema_version {manifest.get('schema_version')!r}")
    work_id = manifest.get("work_id")
    if not isinstance(work_id, str) or not WORK_ID.fullmatch(work_id):
        errors.append(f"{manifest_path}: invalid or missing work_id")
    elif work_id != work_dir.name:
        errors.append(f"{manifest_path}: work_id does not match directory {work_dir.name!r}")
    for field in ("title", "author", "language"):
        if not isinstance(manifest.get(field), str) or not manifest[field].strip():
            errors.append(f"{manifest_path}: {field} must be a nonempty string")
    if manifest.get("source_type") not in SOURCE_TYPES:
        errors.append(f"{manifest_path}: unsupported source_type {manifest.get('source_type')!r}")

    storage = manifest.get("canonical_storage", "repository")
    if storage not in STORAGE_MODES:
        errors.append(f"{manifest_path}: invalid canonical_storage {storage!r}")
    canonical_name = manifest.get("canonical_text")
    local_path = manifest.get("canonical_local_path")
    if storage == "repository":
        canonical = work_dir / canonical_name if canonical_name == "canonical.txt" else None
        if canonical is None:
            errors.append(f"{manifest_path}: repository canonical_text must be 'canonical.txt'")
        if local_path is not None:
            errors.append(f"{manifest_path}: repository canonical_local_path must be null or absent")
    else:
        canonical = repo_root / local_path if isinstance(local_path, str) and local_path else None
        if canonical_name is not None:
            errors.append(f"{manifest_path}: local_private canonical_text must be null")
        if canonical is None:
            errors.append(f"{manifest_path}: local_private canonical_local_path must be a nonempty string")
    if canonical is not None and not canonical.is_file():
        if storage == "local_private":
            if warnings is not None:
                warnings.append(f"{manifest['work_id']}: private canonical source unavailable locally: {local_path}")
        else:
            errors.append(f"{work_dir}: missing canonical.txt")
    elif canonical is not None:
        content = canonical.read_bytes()
        try:
            content.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{canonical}: not valid UTF-8: {exc}")
        actual_hash = hashlib.sha256(content).hexdigest()
        expected_hash = manifest.get("canonical_sha256")
        if not isinstance(expected_hash, str) or not SHA256.fullmatch(expected_hash):
            errors.append(f"{manifest_path}: invalid canonical_sha256")
        elif actual_hash != expected_hash:
            errors.append(f"{canonical}: SHA-256 mismatch (expected {expected_hash}, got {actual_hash})")

    references = manifest.get("source_references")
    if not isinstance(references, list) or not references or not all(
        isinstance(reference, str) and reference for reference in references
    ):
        errors.append(f"{manifest_path}: source_references must be a nonempty string list")
    else:
        for reference in references:
            path = Path(reference)
            if not path.is_absolute() and not (repo_root / path).exists():
                errors.append(f"{manifest_path}: source reference does not exist: {reference}")
    rights = manifest.get("rights")
    if not isinstance(rights, dict) or not isinstance(rights.get("analysis_allowed"), bool) or not (
        rights.get("public_render_policy") in RIGHTS_POLICIES
    ):
        errors.append(f"{manifest_path}: invalid rights metadata")
    elif "rights_review" in rights:
        review = rights["rights_review"]
        if not isinstance(review, dict) or set(review) != {"status", "issue", "note"} or not (
            review.get("status") in RIGHTS_REVIEW_STATUSES
            and isinstance(review.get("issue"), str) and review["issue"]
            and isinstance(review.get("note"), str) and review["note"]
        ):
            errors.append(f"{manifest_path}: invalid rights_review metadata")
    if not isinstance(manifest.get("notes"), str):
        errors.append(f"{manifest_path}: notes must be a string")
    return errors, manifest


def validate_corpus(works_root: Path, repo_root: Path, warnings: list[str] | None = None) -> tuple[list[str], list[dict]]:
    errors: list[str] = []
    manifests: list[dict] = []
    if not works_root.is_dir():
        return [f"{works_root}: works root does not exist"], manifests
    for work_dir in sorted(path for path in works_root.iterdir() if path.is_dir()):
        work_errors, manifest = validate_work(work_dir, repo_root, warnings)
        errors.extend(work_errors)
        if manifest is not None:
            manifests.append(manifest)
    if not manifests:
        errors.append(f"{works_root}: no work manifests found")
    return errors, manifests


def render_index(manifests: list[dict]) -> str:
    lines = [
        "# Canonical corpus", "",
        "Generated from the canonical work manifests. Do not edit this table by hand.", "",
        "| Work ID | Title | Author | Language | Source type | Canonical status | Rights/rendering policy |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in sorted(manifests, key=lambda value: value["work_id"]):
        values = [
            f"`{item['work_id']}`", item["title"], item["author"], item["language"],
            f"`{item['source_type']}`", "local/private" if item.get("canonical_storage", "repository") == "local_private" else "available",
            f"`{item['rights']['public_render_policy']}`",
        ]
        lines.append("| " + " | ".join(value.replace("|", "\\|") for value in values) + " |")
    return "\n".join(lines) + "\n"


def rights_review_lines(manifests: list[dict]) -> list[str]:
    """Return stable, tab-separated records for unresolved rights reviews."""
    lines = []
    for manifest in sorted(manifests, key=lambda item: item["work_id"]):
        review = manifest["rights"].get("rights_review")
        if review and review["status"] != "CLEAR":
            lines.append(f"{review['status']}\t{manifest['work_id']}\t{review['issue']}")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("works_root", nargs="?", type=Path, default=Path("corpus/works"))
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--write-index", type=Path)
    parser.add_argument("--report-rights-review", action="store_true")
    args = parser.parse_args()
    warnings: list[str] = []
    errors, manifests = validate_corpus(args.works_root, args.repo_root, warnings)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Canonical corpus validation failed with {len(errors)} error(s).")
        return 1
    for warning in warnings:
        print(f"WARNING: {warning}")
    if args.report_rights_review:
        for line in rights_review_lines(manifests):
            print(line)
    if args.write_index:
        args.write_index.write_text(render_index(manifests), encoding="utf-8")
        print(f"Wrote {args.write_index}")
    print(f"Canonical corpus valid: {len(manifests)} work(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
