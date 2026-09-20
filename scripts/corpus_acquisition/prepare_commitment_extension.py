#!/usr/bin/env python3
"""Acquire the five-work commitment extension without changing frozen results.

Sources are preserved verbatim. Existing derived files must reproduce exactly;
divergent files are never overwritten. No model API calls are made here.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.corpus_acquisition.acquire_public_domain_text import (
    extract_runeberg_page, trim_gutenberg,
)
from scripts.corpus.build_canonical_work import build_work
from scripts.corpus.validate_canonical_corpus import validate_work

DEFAULT_SELECTION = Path("data/acquisition/commitment_extension_5_v1/selection.json")
DERIVATION_VERSION = "commitment_extension_sources_v1"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def stable_write(path: Path, data: bytes) -> None:
    if path.exists():
        if path.read_bytes() != data:
            raise ValueError(f"refusing to overwrite divergent artifact: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def json_bytes(data: object) -> bytes:
    return (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def download(url: str, path: Path) -> bytes:
    if path.exists():
        data = path.read_bytes()
        if not data:
            raise ValueError(f"empty cached source: {path}")
        return data
    request = urllib.request.Request(url, headers={"User-Agent": "LMCW-research/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
    if not data:
        raise ValueError(f"empty source response: {url}")
    stable_write(path, data)
    return data


def alto_text(raw: bytes, page_label: str) -> str:
    """Retain ALTO word/line order; remove only the first page-number line.

    No spelling correction, inferred dehyphenation, or confidence filtering.
    Empty pages are allowed and remain represented in the page map.
    """
    root = ET.fromstring(raw)
    if root.tag.rsplit("}", 1)[-1] != "alto":
        raise ValueError("expected ALTO XML")
    paragraphs = []
    first_line = True
    for block in root.findall(".//{*}TextBlock"):
        lines = []
        for line in block.findall("{*}TextLine"):
            words = [word.get("CONTENT", "") for word in line.findall("{*}String")]
            text = " ".join(word for word in words if word)
            if first_line and text.strip() == page_label:
                first_line = False
                continue
            if text:
                lines.append(text)
                first_line = False
        if lines:
            paragraphs.append("\n".join(lines))
    return "\n\n".join(paragraphs).strip()


def correct_page(text: str, raw: bytes, corrections: list[dict]) -> str:
    """Apply only exact, scan-verified errata to the expected source bytes."""
    for correction in corrections:
        if digest(raw) != correction["source_sha256"]:
            raise ValueError(f"OCR correction source changed: {correction['correction_id']}")
        if text.count(correction["before"]) != 1:
            raise ValueError(f"OCR correction is not unique: {correction['correction_id']}")
        text = text.replace(correction["before"], correction["after"], 1)
    return text


def assemble(parts: list[tuple[str, bytes, str, Path]], root: Path) -> tuple[bytes, list[dict]]:
    chunks, page_map, offset = [], [], 0
    for label, raw, text, path in parts:
        separator = "\n\n" if chunks else ""
        start = offset + len(separator)
        chunks.append(separator + text)
        offset = start + len(text)
        page_map.append({"page": label, "source_path": str(path.relative_to(root)),
                         "source_sha256": digest(raw), "output_start": start,
                         "output_end": offset})
    return ("".join(chunks) + "\n").encode("utf-8"), page_map


def acquire(work: dict, root: Path) -> tuple[bytes, dict]:
    raw_dir = root / "data/raw" / work["work_id"]
    kind = work["source_type"]
    if kind == "gutenberg_single":
        path = raw_dir / "source-download.txt"
        raw = download(work["download_url"], path)
        text = trim_gutenberg(raw.decode("utf-8-sig")).encode("utf-8")
        return text, {"download_url": work["download_url"],
                      "download_path": str(path.relative_to(root)),
                      "download_sha256": digest(raw),
                      "processing_note": "Removed only the explicit Gutenberg START/END wrapper."}
    if kind == "runeberg":
        parts, methods = [], []
        for name in work["page_names"]:
            path = raw_dir / "pages" / f"{name}.html"
            raw = download(work["catalogue_url"] + name + ".html", path)
            text, method = extract_runeberg_page(raw.decode("utf-8-sig"))
            parts.append((name, raw, text.rstrip("\n"), path))
            methods.append(method)
        text, page_map = assemble(parts, root)
        map_path = raw_dir / "page-map.json"
        stable_write(map_path, json_bytes(page_map))
        return text, {"page_map_path": str(map_path.relative_to(root)),
                      "page_names": work["page_names"], "page_count": len(parts),
                      "processing_note": "Existing Runeberg parser; chapters in explicit order, separated by two newlines; no OCR/spelling correction.",
                      "derivation_methods": sorted(set(methods))}
    if kind != "nb_public_domain_ocr":
        raise ValueError(f"unsupported extension source: {kind}")
    query_url = "https://api.nb.no/catalog/v1/items?" + urllib.parse.urlencode(
        {"q": f'urn:"{work["urn"]}"'})
    catalogue_path = raw_dir / "catalogue.json"
    catalogue_raw = download(query_url, catalogue_path)
    items = json.loads(catalogue_raw)["_embedded"]["items"]
    if len(items) != 1 or items[0]["metadata"]["identifiers"]["urn"] != work["urn"]:
        raise ValueError("National Library catalogue does not identify exactly the selected URN")
    item = items[0]
    access = item["accessInfo"]
    if not (access.get("isPublicDomain") is True and access.get("license") == "publicdomain"
            and access.get("accessAllowedFrom") == "EVERYWHERE" and access.get("viewability") == "ALL"):
        raise ValueError("National Library edition is not confirmed freely accessible public domain")
    manifest_path = raw_dir / "iiif-manifest.json"
    manifest_raw = download(item["_links"]["presentation"]["href"], manifest_path)
    manifest = json.loads(manifest_raw)
    first, last = work["printed_page_range"]
    canvases = [c for c in manifest["sequences"][0]["canvases"]
                if re.search(r"_[0-9]+$", c["@id"]) and c["label"].isdigit()
                and first <= int(c["label"]) <= last]
    labels = [int(c["label"]) for c in canvases]
    if labels != list(range(first, last + 1)):
        raise ValueError("selected printed-page range is incomplete, duplicated, or out of order")
    corrections_path = root / work["ocr_corrections"]
    corrections = [c for c in json.loads(corrections_path.read_text(encoding="utf-8"))["corrections"]
                   if c["work_id"] == work["work_id"]]
    if any(c["printed_page"] not in labels for c in corrections):
        raise ValueError("OCR correction falls outside acquired page range")

    def get_page(canvas):
        path = raw_dir / "alto" / f"{int(canvas['label']):04d}.xml"
        raw = download(canvas["@seeAlso"]["@id"], path)
        errata = [c for c in corrections if c["printed_page"] == int(canvas["label"])]
        text = correct_page(alto_text(raw, canvas["label"]), raw, errata)
        return canvas["label"], raw, text, path

    parts = []
    with ThreadPoolExecutor(max_workers=12) as pool:
        for index, part in enumerate(pool.map(get_page, canvases), 1):
            parts.append(part)
            if index % 25 == 0 or index == len(canvases):
                print(f"  {work['work_id']}: {index}/{len(canvases)} OCR pages", flush=True)
    text, page_map = assemble(parts, root)
    for entry, canvas in zip(page_map, canvases):
        entry.update(source_url=canvas["@seeAlso"]["@id"], canvas_url=canvas["@id"],
                     image_url=canvas["images"][0]["resource"]["@id"],
                     correction_ids=[c["correction_id"] for c in corrections
                                     if c["printed_page"] == int(canvas["label"])])
    map_path = raw_dir / "page-map.json"
    stable_write(map_path, json_bytes(page_map))
    return text, {"urn": work["urn"], "national_library_id": item["id"],
                  "catalogue_path": str(catalogue_path.relative_to(root)),
                  "catalogue_sha256": digest(catalogue_raw),
                  "iiif_manifest_path": str(manifest_path.relative_to(root)),
                  "iiif_manifest_sha256": digest(manifest_raw),
                  "license_url": manifest["license"], "access_info": access,
                  "printed_page_range": [first, last], "page_count": len(parts),
                  "page_map_path": str(map_path.relative_to(root)),
                  "ocr_corrections_path": str(corrections_path.relative_to(root)),
                  "ocr_correction_ids": [c["correction_id"] for c in corrections],
                  "processing_note": "Original-edition ALTO OCR in IIIF reading order; first page-number line removed when exact; block/line order retained; only explicitly logged scan-verified corrections; no inferred dehyphenation; non-narrative front/back matter excluded by reviewed printed-page range.",
                  "quality_note": "OCR with limited documented correction, not a fully proofread edition. Inspect matched passages against linked page images before interpreting scores; remaining OCR errors can affect extraction recall."}


def prepare(selection_path: Path, root: Path) -> dict:
    selection = json.loads(selection_path.read_text(encoding="utf-8"))
    rows = []
    for work in selection["works"]:
        print(f"Preparing {work['title']}", flush=True)
        text, details = acquire(work, root)
        derived = root / "data/raw" / work["work_id"] / "literary.txt"
        stable_write(derived, text)
        reference = Path("provenance/sources") / f"{work['source_id']}.json"
        provenance = {key: work[key] for key in ("work_id", "source_id", "title", "author",
                      "author_death_year", "first_publication_year", "language", "source_type", "catalogue_url")}
        provenance.update(details)
        provenance.update(local_path=str(derived.relative_to(root)), sha256=digest(text),
                          retrieved_on=selection["selected_on"], derivation_version=DERIVATION_VERSION,
                          review_status="approved_for_exploratory_processing",
                          rights_note="Historical original-language work published before 1931; author died more than 70 years ago. National Library editions additionally carry an explicit public-domain designation; Gutenberg catalogues designate their editions public domain in the USA. Modern translations are not used.",
                          rights_reference="https://www.ag.gov.au/rights-and-protections/copyright/copyright-basics",
                          source_note=work.get("source_note", ""))
        stable_write(root / reference, json_bytes(provenance))
        metadata = {key: work[key] for key in ("work_id", "title", "author", "language", "source_type")}
        metadata.update(source_references=[str(reference), str(selection_path.relative_to(root))],
                        analysis_allowed=True, public_render_policy="PUBLIC_DOMAIN_FULL_CONTEXT_OK",
                        notes=f"Targeted exploratory commitment extension, {selection['inventory_id']}. "
                              + work["selection_reason"] + " " + work.get("source_note", ""))
        work_dir = root / "corpus/works" / work["work_id"]
        if work_dir.exists():
            errors, existing = validate_work(work_dir, root)
            if errors or existing["canonical_sha256"] != digest(text):
                raise ValueError(f"divergent or invalid existing canonical work: {work['work_id']}: {errors}")
            for key in ("title", "author", "language", "source_type", "source_references", "notes"):
                if existing[key] != metadata[key]:
                    raise ValueError(f"existing work metadata differs: {work['work_id']} / {key}")
        else:
            build_work(derived, root / "corpus/works", metadata)
        errors, _ = validate_work(work_dir, root)
        if errors:
            raise ValueError("; ".join(errors))
        rows.append({"work_id": work["work_id"], "language": work["language"],
                     "canonical_sha256": digest(text), "canonical_characters": len(text.decode("utf-8")),
                     "provenance_path": str(reference), "status": "VALID"})
        print(f"  VALID: {len(text):,} UTF-8 bytes", flush=True)
    result = {"schema_version": "1.0", "inventory_id": selection["inventory_id"],
              "research_role": selection["research_role"], "work_count": len(rows), "works": rows}
    stable_write(selection_path.parent / "manifest.json", json_bytes(result))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selection", type=Path, default=DEFAULT_SELECTION)
    args = parser.parse_args()
    result = prepare((ROOT / args.selection).resolve(), ROOT)
    print(f"Prepared {result['work_count']} canonical works; no annotation API calls made.")


if __name__ == "__main__":
    main()
