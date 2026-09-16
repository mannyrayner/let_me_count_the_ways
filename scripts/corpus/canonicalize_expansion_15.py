#!/usr/bin/env python3
"""Safely canonicalize the expansion fifteen from the approved acquisition inventory."""

from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
from dataclasses import dataclass
from pathlib import Path

if __package__:
    from .build_canonical_work import build_work
else:
    from build_canonical_work import build_work


EXPECTED_METADATA = {
    "stendhal-le-rouge-et-le-noir": ("Le Rouge et le Noir", "Stendhal", "fr", "gutenberg_single", ["provenance/sources/gutenberg-798.json"]),
    "balzac-illusions-perdues": ("Illusions perdues", "Honoré de Balzac", "fr", "gutenberg_single", ["provenance/sources/gutenberg-54723.json"]),
    "colette-le-ble-en-herbe": ("Le blé en herbe", "Colette", "fr", "gutenberg_single", ["provenance/sources/gutenberg-59926.json"]),
    "sand-la-mare-au-diable": ("La Mare au Diable", "George Sand", "fr", "gutenberg_single", ["provenance/sources/gutenberg-23582.json"]),
    "stael-corinne": ("Corinne; ou, l'Italie", "Madame de Staël", "fr", "gutenberg_single", ["provenance/sources/gutenberg-60810.json"]),
    "fontane-effi-briest": ("Effi Briest", "Theodor Fontane", "de", "gutenberg_single", ["provenance/sources/gutenberg-5323.json"]),
    "zuccoli-lamore-di-loredana": ("L'amore di Loredana", "Luciano Zùccoli", "it", "gutenberg_single", ["provenance/sources/gutenberg-34346.json"]),
    "verona-colei-che-non-si-deve-amare": ("Colei che non si deve amare", "Guido da Verona", "it", "gutenberg_single", ["provenance/sources/gutenberg-69294.json"]),
    "bang-ved-vejen": ("Ved Vejen", "Herman Bang", "da", "gutenberg_single", ["provenance/sources/gutenberg-13175.json"]),
    "nansen-maria": ("Maria: En Bog om Kærlighed", "Peter Nansen", "da", "gutenberg_single", ["provenance/sources/gutenberg-41786.json"]),
    "bronte-tenant-of-wildfell-hall": ("The Tenant of Wildfell Hall", "Anne Brontë", "en", "gutenberg_single", ["provenance/sources/gutenberg-969.json"]),
    "austen-persuasion": ("Persuasion", "Jane Austen", "en", "gutenberg_single", ["provenance/sources/gutenberg-105.json"]),
    "eliot-middlemarch": ("Middlemarch", "George Eliot", "en", "gutenberg_single", ["provenance/sources/gutenberg-145.json"]),
    "lagerlof-gosta-berlings-saga": ("Gösta Berlings saga", "Selma Lagerlöf", "sv", "runeberg", ["provenance/sources/runeberg-berling.json", "data/raw/lagerlof-gosta-berlings-saga/page-map.json"]),
    "undset-kristin-lavransdatter": ("Kristin Lavransdatter", "Sigrid Undset", "no", "runeberg", ["provenance/sources/runeberg-kristin-kransen.json", "provenance/sources/runeberg-kristin-husfrue.json", "provenance/sources/runeberg-kristin-korset.json"]),
}
SPECIAL_IDS = {"balzac-illusions-perdues", "undset-kristin-lavransdatter"}
BALZAC_START = "ILLUSIONS PERDUES\n\n\n  A MONSIEUR VICTOR HUGO."
BALZAC_END = "\n\nFIN DU HUITIÈME VOLUME."
BALZAC_PARTS = ("LES DEUX POÈTES.", "UN GRAND HOMME DE PROVINCE A PARIS.", "ÈVE ET DAVID.")
UNDSET_REGRESSIONS = (
    "Ved skiftet efter Ivar unge Gjesling paa Sundbu i\naaret 1306",
    "ti Ragnfrid var noget sær og tungsindig",
    "Hun blir saa rusende, hun kan ikke gaa ned til\nsæteren,» sa Halvdan",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()


@dataclass(frozen=True)
class PlannedWork:
    work_id: str
    canonical: bytes
    source_path: str
    relationship: str
    derivation_files: dict[str, bytes]


def _read_verified(root: Path, path_text: str, expected_hash: str) -> bytes:
    path = root / path_text
    if not path.is_file():
        raise ValueError(f"missing acquisition input: {path_text}")
    data = path.read_bytes()
    try:
        data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"acquisition input is not UTF-8: {path_text}") from exc
    actual = sha256(data)
    if actual != expected_hash:
        raise ValueError(f"SHA-256 mismatch for {path_text}: expected {expected_hash}, got {actual}")
    return data


def derive_balzac(source: bytes) -> bytes:
    text = source.decode("utf-8")
    if text.count(BALZAC_START) != 1 or text.count(BALZAC_END) != 1:
        raise ValueError("Balzac boundary anchors must each occur exactly once")
    start = text.index(BALZAC_START)
    end = text.index(BALZAC_END, start)
    output = text[start:end].rstrip() + "\n"
    positions = [output.find(part) for part in BALZAC_PARTS]
    if any(position < 0 for position in positions) or positions != sorted(positions):
        raise ValueError("Balzac derivation does not contain the three ordered part headings")
    return output.encode("utf-8")


def derive_undset(parts: list[bytes]) -> bytes:
    # Preserve all non-terminal bytes and normalize only the join to two newlines.
    output = b"\n\n".join(part.rstrip(b"\r\n") for part in parts) + b"\n"
    text = output.decode("utf-8")
    for required in UNDSET_REGRESSIONS:
        if required not in text:
            raise ValueError(f"Undset repaired regression text missing: {required!r}")
    return output


def load_plan(root: Path) -> list[PlannedWork]:
    inventory_path = root / "data/acquisition/expansion_15_v1/manifest.json"
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    works = inventory.get("works", [])
    ids = [item.get("work_id") for item in works]
    if len(ids) != 15 or set(ids) != set(EXPECTED_METADATA) or len(set(ids)) != 15:
        raise ValueError("acquisition inventory must contain exactly the expected 15 work IDs")

    plan = []
    for item in works:
        work_id = item["work_id"]
        if work_id == "undset-kristin-lavransdatter":
            parts_meta = item.get("constituent_parts", [])
            if [part.get("title") for part in parts_meta] != ["Kransen", "Husfrue", "Korset"]:
                raise ValueError("Undset constituents must be ordered Kransen, Husfrue, Korset")
            parts = [_read_verified(root, p["derived_text_path"], p["derived_sha256"]) for p in parts_meta]
            canonical = derive_undset(parts)
            derived_path = "data/derived/undset-kristin-lavransdatter/canonical-source.txt"
            inputs = [{"title": p["title"], "path": p["derived_text_path"], "sha256": p["derived_sha256"], "order": n, "character_count": len(data.decode("utf-8"))} for n, (p, data) in enumerate(zip(parts_meta, parts), 1)]
            derivation = {"schema_version": "1.0", "work_id": work_id, "inputs": inputs, "separator_rule": "Remove only terminal CR/LF bytes from each volume, join volumes with exactly one blank line, and end the trilogy with one LF; insert no editorial prose.", "output_path": derived_path, "output_sha256": sha256(canonical), "character_count": len(canonical.decode("utf-8"))}
            files = {derived_path: canonical, "data/derived/undset-kristin-lavransdatter/derivation.json": json_bytes(derivation)}
            plan.append(PlannedWork(work_id, canonical, derived_path, "deterministic-derived", files))
        else:
            source_path = item["derived_text_path"]
            source = _read_verified(root, source_path, item["derived_sha256"])
            if work_id == "balzac-illusions-perdues":
                canonical = derive_balzac(source)
                derived_path = "data/derived/balzac-illusions-perdues/canonical-source.txt"
                derivation = {"schema_version": "1.0", "work_id": work_id, "input_path": source_path, "input_sha256": item["derived_sha256"], "boundary_anchors": {"start_inclusive": BALZAC_START, "end_exclusive": BALZAC_END}, "required_ordered_part_headings": list(BALZAC_PARTS), "output_path": derived_path, "output_sha256": sha256(canonical), "character_count": len(canonical.decode("utf-8"))}
                files = {derived_path: canonical, "data/derived/balzac-illusions-perdues/derivation.json": json_bytes(derivation)}
                plan.append(PlannedWork(work_id, canonical, derived_path, "deterministic-derived", files))
            else:
                plan.append(PlannedWork(work_id, source, source_path, "byte-identical", {}))
    return plan


def metadata_for(work: PlannedWork) -> dict:
    title, author, language, source_type, references = EXPECTED_METADATA[work.work_id]
    relationship_note = "Byte-for-byte copy of the approved acquisition-derived text." if work.relationship == "byte-identical" else "Canonical text copied byte-for-byte from the recorded deterministic derived source."
    return {"work_id": work.work_id, "title": title, "author": author, "language": language, "source_type": source_type, "source_references": references, "analysis_allowed": True, "public_render_policy": "PUBLIC_DOMAIN_FULL_CONTEXT_OK", "notes": relationship_note}


def expected_work_files(work: PlannedWork) -> dict[str, bytes]:
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        source = root / "source.txt"
        source.write_bytes(work.canonical)
        manifest = build_work(source, root / "works", metadata_for(work))
        directory = manifest.parent
        return {path.name: path.read_bytes() for path in directory.iterdir()}


def _check_target(root: Path, relative_dir: str, expected: dict[str, bytes]) -> str:
    target = root / relative_dir
    if not target.exists():
        return "CREATE"
    if not target.is_dir():
        raise ValueError(f"output target is not a directory: {relative_dir}")
    actual_names = {p.name for p in target.iterdir()}
    if actual_names != set(expected) or any((target / name).read_bytes() != data for name, data in expected.items()):
        raise ValueError(f"divergent existing output; refusing to overwrite: {relative_dir}")
    return "VALID/UNCHANGED"


def _inventory_files(plan: list[PlannedWork]) -> dict[str, bytes]:
    entries = [{"work_id": w.work_id, "canonical_path": f"corpus/works/{w.work_id}/canonical.txt", "canonical_sha256": sha256(w.canonical), "source_relationship": w.relationship, "source_or_derived_path": w.source_path, "validation_status": "VALID"} for w in plan]
    manifest = {"schema_version": "1.0", "inventory_id": "expansion_15_v1", "status": "15/15 canonicalized", "canonicalized_work_count": 15, "target_work_count": 15, "works": entries}
    readme = "# Expansion 15 canonicalization checkpoint\n\nGenerated deterministically by `scripts/corpus/canonicalize_expansion_15.py`.\n\nStatus: **15/15 canonicalized**. See `manifest.json` for paths, relationships, and hashes.\n"
    return {"manifest.json": json_bytes(manifest), "README.md": readme.encode()}


def execute(root: Path, check: bool = False) -> list[str]:
    plan = load_plan(root)  # Every input and derivation is validated before output checks/writes.
    work_files = {w.work_id: expected_work_files(w) for w in plan}
    statuses = []
    for work in plan:
        statuses.append(f"{work.work_id}: {_check_target(root, f'corpus/works/{work.work_id}', work_files[work.work_id])}")
        for path, data in work.derivation_files.items():
            parent = str(Path(path).parent)
            expected = {p.name: d for p, d in ((Path(name), value) for name, value in work.derivation_files.items())}
            _check_target(root, parent, expected)
            break
    inventory_files = _inventory_files(plan)
    _check_target(root, "data/canonicalization/expansion_15_v1", inventory_files)
    if check:
        return statuses

    for work in plan:
        for path, data in work.derivation_files.items():
            destination = root / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
        directory = root / "corpus/works" / work.work_id
        if not directory.exists():
            directory.mkdir(parents=True)
            for name, data in work_files[work.work_id].items():
                (directory / name).write_bytes(data)
        if (directory / "canonical.txt").read_bytes() != work.canonical:
            raise AssertionError(f"post-write byte identity failed: {work.work_id}")
    inventory_dir = root / "data/canonicalization/expansion_15_v1"
    inventory_dir.mkdir(parents=True, exist_ok=True)
    for name, data in inventory_files.items():
        (inventory_dir / name).write_bytes(data)
    return statuses


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate and plan without writing outputs")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        statuses = execute(args.root.resolve(), args.check)
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    for status in statuses:
        print(status)
    print("Preflight valid; no files written." if args.check else "Canonicalized 15/15 expansion works.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
