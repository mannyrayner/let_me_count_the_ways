#!/usr/bin/env python3
"""Atomically acquire and derive Gutenberg or Runeberg literary texts."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from typing import Callable


GUTENBERG_START = re.compile(
    r"(?im)^\*\*\* START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.*?\*\*\*\s*$"
)
GUTENBERG_END = re.compile(
    r"(?im)^\*\*\* END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.*?\*\*\*\s*$"
)
RUNEBERG_OCR_START = "<!-- mode=normal -->"
RUNEBERG_OCR_END = "<!-- NEWIMAGE2 -->"
RUNEBERG_OCR_FALLBACK_END = "<!-- #### -->"
RUNEBERG_FORBIDDEN_TEXT = (
    "project runeberg",
    "on this page / på denna sida",
    "proofread the page now",
    "korrekturläs sidan nu",
    "table of contents / innehåll",
    "full resolution (jpeg)",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_download(url: str, destination: Path, force: bool = False) -> bool:
    """Download with curl to ``.part``; return False when a valid file is reused."""
    partial = destination.with_suffix(destination.suffix + ".part")
    if destination.is_file() and destination.stat().st_size and not force:
        return False
    if destination.exists() and not force:
        raise FileExistsError(f"refusing to replace empty or non-file path {destination}")
    if partial.exists():
        raise FileExistsError(f"refusing to overwrite stale partial file {partial}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            ["curl", "--fail", "--location", "--retry", "3", "--output", str(partial), url],
            check=True,
        )
        if not partial.is_file() or not partial.stat().st_size:
            raise OSError(f"empty response for {url}")
        partial.replace(destination)
    except Exception:
        partial.unlink(missing_ok=True)
        raise
    return True


class VisibleText(HTMLParser):
    BLOCKS = {"address", "article", "blockquote", "br", "div", "h1", "h2", "h3",
              "h4", "h5", "h6", "li", "p", "pre", "section", "table", "tr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.hidden = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style"}:
            self.hidden += 1
        elif not self.hidden and tag in self.BLOCKS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self.hidden:
            self.hidden -= 1
        elif not self.hidden and tag in self.BLOCKS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.hidden:
            self.parts.append(data)

    def text(self) -> str:
        value = html.unescape("".join(self.parts)).replace("\r\n", "\n").replace("\r", "\n")
        value = re.sub(r"[ \t]+", " ", value)
        value = re.sub(r" *\n *", "\n", value)
        value = re.sub(r"\n{3,}", "\n\n", value).strip()
        if not value:
            raise ValueError("HTML literary-content region is empty")
        return value + "\n"


def html_to_text(value: str) -> str:
    parser = VisibleText()
    parser.feed(value)
    parser.close()
    return parser.text()


class RunebergOCRLines(HTMLParser):
    """Decode OCR markup while treating only ``br`` as physical lineation."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.casefold() == "br":
            self.parts.append("\n")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)

    def handle_data(self, data: str) -> None:
        # Newlines in the HTML serialization merely follow <br> tags. Runeberg's
        # physical OCR lines are represented structurally by those tags.
        self.parts.append(data.replace("\r", "").replace("\n", ""))

    def text(self) -> str:
        return html.unescape("".join(self.parts))


def runeberg_ocr_lines(fragment: str) -> str:
    """Discard structural page furniture, then preserve each OCR ``br`` exactly."""
    first_break = re.search(r"(?is)<br\s*/?\s*>", fragment)
    if first_break is None:
        parser = RunebergOCRLines()
        parser.feed(fragment)
        parser.close()
        structural_field = parser.text().strip()
        # Some title/furniture-only scan pages have a mode marker but no OCR
        # line breaks. They contribute an intentionally empty mapped slice.
        if len(structural_field) <= 100:
            return ""
        raise ValueError("Runeberg OCR has substantial text but no structural <br>")
    # Everything before this first break is the structurally located printed-page
    # field, whether its OCR happens to be numeric, corrupt (for example Gi), or a
    # title-page label. It is not literary OCR.
    literary_fragment = fragment[first_break.end():]
    parser = RunebergOCRLines()
    parser.feed(literary_fragment)
    parser.close()
    value = parser.text().lstrip("\n").rstrip("\n")
    # A title-only range boundary can consist entirely of the structural field.
    # Preserve that page in the map as an empty slice rather than retaining its
    # furniture or inventing literary content.
    return value + "\n" if value else ""


def validate_runeberg_ocr_text(value: str) -> None:
    """Reject structural chrome; marker-bounded OCR may legitimately be short."""
    lowered = value.casefold()
    found = [phrase for phrase in RUNEBERG_FORBIDDEN_TEXT if phrase in lowered]
    if found:
        raise ValueError(f"Runeberg OCR contains forbidden navigation text: {found[0]}")


def extract_runeberg_ocr(value: str) -> tuple[str, str]:
    """Return raw OCR text and the deterministic end marker used."""
    starts = [match.start() for match in re.finditer(re.escape(RUNEBERG_OCR_START), value)]
    if not starts:
        raise ValueError("Runeberg OCR start marker not found")
    if len(starts) != 1:
        raise ValueError("ambiguous Runeberg OCR start markers")
    content_start = starts[0] + len(RUNEBERG_OCR_START)

    primary = [match.start() for match in re.finditer(re.escape(RUNEBERG_OCR_END), value)]
    if any(position < content_start for position in primary):
        raise ValueError("Runeberg OCR end marker occurs before start marker")
    primary_after = [position for position in primary if position >= content_start]
    if len(primary_after) > 1:
        raise ValueError("ambiguous Runeberg OCR end markers")
    if primary_after:
        content_end = primary_after[0]
        end_marker = "NEWIMAGE2"
    else:
        fallback = [match.start() for match in
                    re.finditer(re.escape(RUNEBERG_OCR_FALLBACK_END), value)]
        # Proofreading-status chrome can contain a #### marker before the OCR
        # start. Only markers after mode=normal can terminate literary OCR.
        fallback_after = [position for position in fallback if position >= content_start]
        if not fallback_after:
            raise ValueError("Runeberg OCR end marker not found")
        if len(fallback_after) > 1:
            raise ValueError("ambiguous Runeberg OCR fallback end markers")
        content_end = fallback_after[0]
        end_marker = "####"
    if content_end <= content_start:
        raise ValueError("Runeberg OCR markers are empty or out of order")

    text = runeberg_ocr_lines(value[content_start:content_end])
    validate_runeberg_ocr_text(text)
    return text, end_marker


def runeberg_html_to_text(value: str) -> str:
    return extract_runeberg_ocr(value)[0]


def extract_runeberg_proofread(value: str) -> str:
    """Extract an older Runeberg proofread page between navigation and scan links."""
    if RUNEBERG_OCR_START in value:
        raise ValueError("proofread-page extractor received raw OCR markup")
    if "project runeberg" not in value.casefold():
        raise ValueError("markerless page does not identify Project Runeberg")
    body = re.search(r"(?is)<body\b[^>]*>(.*)</body\s*>", value)
    if body is None:
        raise ValueError("Runeberg proofread page has no complete body element")
    body_html = body.group(1)
    navigation_end = re.search(r"(?is)</form\s*>", body_html)
    if navigation_end is None:
        raise ValueError("Runeberg proofread page has no navigation form boundary")
    rules = list(re.finditer(r"(?is)<hr\b[^>]*>", body_html[navigation_end.end():]))
    if len(rules) < 2:
        raise ValueError("Runeberg proofread page has fewer than two footer rules")
    # The old proofread template closes its navigation form immediately before
    # the chapter and places the first rule immediately after the literary text.
    # Scan links lie between the two footer rules and must not enter the output.
    literary_end = navigation_end.end() + rules[0].start()
    fragment = body_html[navigation_end.end():literary_end]
    text = html_to_text(fragment)
    validate_runeberg_ocr_text(text)
    if len(text.strip()) < 100:
        raise ValueError("Runeberg proofread literary region is implausibly short")
    return text


def extract_runeberg_page(value: str) -> tuple[str, str]:
    """Extract a raw-OCR or structurally bounded proofread Runeberg page."""
    if RUNEBERG_OCR_START in value:
        text, end_marker = extract_runeberg_ocr(value)
        return text, f"raw_ocr:{end_marker}"
    return extract_runeberg_proofread(value), "proofread_html:after_form_to_first_hr"


def trim_gutenberg(value: str) -> str:
    start = GUTENBERG_START.search(value)
    end = GUTENBERG_END.search(value, start.end() if start else 0)
    if not start or not end or start.end() >= end.start():
        raise ValueError("could not find ordered explicit Gutenberg START/END markers")
    return value[start.end():end.start()].strip() + "\n"


def acquire_gutenberg(url: str, raw: Path, output: Path,
                       downloader: Callable[[str, Path], object] = atomic_download) -> dict:
    if output.exists():
        raise FileExistsError(f"refusing to overwrite {output}")
    downloader(url, raw)
    downloaded = raw.read_text(encoding="utf-8-sig")
    literary = html_to_text(downloaded) if raw.suffix.lower() in {".htm", ".html"} else downloaded
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(trim_gutenberg(literary), encoding="utf-8", newline="\n")
    return {"download_url": url, "download_path": str(raw), "download_sha256": sha256(raw),
            "local_path": str(output), "sha256": sha256(output)}


def page_urls(volume_url: str, first_url_index: int, last_url_index: int) -> list[str]:
    if first_url_index < 0 or last_url_index < first_url_index:
        raise ValueError("invalid Runeberg URL-index range")
    base = volume_url.rstrip("/") + "/"
    return [f"{base}{index:04d}.html" for index in range(first_url_index, last_url_index + 1)]


def named_page_urls(volume_url: str, page_names: list[str]) -> list[str]:
    """Build Runeberg URLs for a reviewed, explicitly ordered nonnumeric page list."""
    if not page_names:
        raise ValueError("Runeberg named-page list is empty")
    if len(page_names) != len(set(page_names)):
        raise ValueError("Runeberg named-page list contains duplicates")
    if any(not re.fullmatch(r"[A-Za-z0-9_-]+", name) for name in page_names):
        raise ValueError("invalid Runeberg page name")
    base = volume_url.rstrip("/") + "/"
    return [f"{base}{name}.html" for name in page_names]


def acquire_runeberg(volume_url: str, first_url_index: int, last_url_index: int,
                      raw_dir: Path, output: Path, page_map: Path,
                      printed_first: int | None = None, printed_last: int | None = None,
                      force: bool = False,
                      downloader: Callable[[str, Path], object] = atomic_download) -> dict:
    """Acquire and deterministically assemble a verified contiguous Runeberg range."""
    if first_url_index < 0 or last_url_index < first_url_index:
        raise ValueError("invalid Runeberg URL-index range")
    indices = list(range(first_url_index, last_url_index + 1))
    metadata = acquire_runeberg_pages(
        volume_url, [f"{index:04d}" for index in indices], raw_dir, output, page_map,
        printed_first, printed_last, force, downloader,
    )
    metadata["runeberg_url_index_range"] = [first_url_index, last_url_index]
    metadata["ordered_url_indices"] = indices
    metadata["fallback_end_marker_url_indices"] = [
        int(name) for name in metadata.pop("fallback_end_marker_page_names")
    ]
    metadata.pop("runeberg_page_names")
    return metadata


def acquire_runeberg_pages(volume_url: str, page_names: list[str], raw_dir: Path,
                           output: Path, page_map: Path,
                           printed_first: int | None = None,
                           printed_last: int | None = None, force: bool = False,
                           downloader: Callable[[str, Path], object] = atomic_download) -> dict:
    """Acquire a reviewed ordered Runeberg page list, including nonnumeric names."""
    if output.exists() or page_map.exists():
        raise FileExistsError(f"refusing to overwrite {output} or {page_map}")
    if (printed_first is None) != (printed_last is None):
        raise ValueError("printed page metadata requires both first and last")
    if printed_first is not None and printed_last < printed_first:
        raise ValueError("invalid printed-page range")
    urls = named_page_urls(volume_url, page_names)
    paths = [raw_dir / f"{name}.html" for name in page_names]
    downloaded = 0
    for url, path in zip(urls, paths):
        if downloader is atomic_download:
            downloaded += bool(downloader(url, path, force))
        else:
            downloaded += bool(downloader(url, path) is not False)

    expected_names = sorted(f"{name}.html" for name in page_names)
    actual_names = sorted(path.name for path in raw_dir.glob("*.html"))
    if actual_names != expected_names:
        raise ValueError("raw page directory has missing, duplicate, or unexpected HTML pages")
    if any(not path.is_file() or not path.stat().st_size for path in paths):
        raise ValueError("raw page range contains an empty or missing page")

    chunks: list[str] = []
    records: list[dict] = []
    fallback_end_marker_pages: list[str] = []
    offset = 0
    for page_name, url, path in zip(page_names, urls, paths):
        source_html = path.read_text(encoding="utf-8-sig")
        try:
            text, derivation_method = extract_runeberg_page(source_html)
        except ValueError as error:
            marker_counts = {
                "mode=normal": source_html.count(RUNEBERG_OCR_START),
                "NEWIMAGE2": source_html.count(RUNEBERG_OCR_END),
                "####": source_html.count(RUNEBERG_OCR_FALLBACK_END),
            }
            raise ValueError(
                f"Runeberg page {page_name!r} could not be parsed from {path} "
                f"(source URL {url}; {len(source_html.encode('utf-8'))} UTF-8 bytes; "
                f"marker counts {marker_counts}): {error}. Raw pages were preserved; "
                "inspect this page before changing source boundaries or parser rules"
            ) from error
        text = text.rstrip("\n")
        if derivation_method == "raw_ocr:####":
            fallback_end_marker_pages.append(page_name)
        # A physical page transition prevents line merging but is not a paragraph.
        separator = "" if not text or offset == 0 else "\n"
        start = offset + len(separator)
        chunks.append(separator + text)
        offset += len(separator) + len(text)
        record = {"url": url, "output_start": start,
                        "output_end": offset, "raw_path": str(path),
                        "raw_sha256": sha256(path), "facsimile_available": True,
                        "derivation_method": derivation_method}
        if derivation_method.startswith("raw_ocr:"):
            record["ocr_end_marker"] = derivation_method.removeprefix("raw_ocr:")
        if page_name.isdigit():
            record["url_index"] = int(page_name)
        else:
            record["url_name"] = page_name
        records.append(record)
    assembled = "".join(chunks) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(assembled, encoding="utf-8", newline="\n")
    page_map.parent.mkdir(parents=True, exist_ok=True)
    page_map.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    derivation_methods = sorted({record["derivation_method"] for record in records})
    metadata = {
        "volume_url": volume_url.rstrip("/") + "/",
        "pages_requested": len(urls), "pages_downloaded": downloaded,
        "pages_nonempty": sum(path.stat().st_size > 0 for path in paths),
        "runeberg_page_names": page_names,
        "source_urls": urls, "download_paths": [str(path) for path in paths],
        "page_map": str(page_map), "local_path": str(output),
        "assembled_character_count": len(assembled),
        "assembled_word_count": len(assembled.split()), "sha256": sha256(output),
        "fallback_end_marker_page_names": fallback_end_marker_pages,
        "page_derivation_methods": derivation_methods,
        "facsimile_available": True,
    }
    if all(method.startswith("raw_ocr:") for method in derivation_methods):
        metadata["ocr_status"] = "not proofread / uncorrected OCR"
    elif derivation_methods == ["proofread_html:after_form_to_first_hr"]:
        metadata["text_status"] = "proofread electronic text"
    else:
        metadata["text_status"] = "mixed Runeberg page derivations"
    if printed_first is not None:
        metadata["printed_page_range"] = [printed_first, printed_last]
    return metadata


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    gutenberg = subparsers.add_parser("gutenberg")
    gutenberg.add_argument("--url", required=True)
    gutenberg.add_argument("--raw", type=Path, required=True)
    gutenberg.add_argument("--output", type=Path, required=True)
    runeberg = subparsers.add_parser("runeberg-range")
    runeberg.add_argument("--volume-url", required=True)
    runeberg.add_argument("--first-url-index", type=int)
    runeberg.add_argument("--last-url-index", type=int)
    runeberg.add_argument(
        "--page-name", action="append", dest="page_names",
        help="Reviewed page basename, repeated in source order; alternative to numeric indices",
    )
    runeberg.add_argument("--printed-first", type=int)
    runeberg.add_argument("--printed-last", type=int)
    runeberg.add_argument("--raw-dir", type=Path, required=True)
    runeberg.add_argument("--output", type=Path, required=True)
    runeberg.add_argument("--page-map", type=Path, required=True)
    runeberg.add_argument("--force", action="store_true")
    args = parser.parse_args()
    if args.command == "gutenberg":
        metadata = acquire_gutenberg(args.url, args.raw, args.output)
    else:
        numeric = args.first_url_index is not None or args.last_url_index is not None
        if numeric == bool(args.page_names):
            parser.error("runeberg-range requires either both numeric indices or --page-name")
        if numeric:
            if args.first_url_index is None or args.last_url_index is None:
                parser.error("both --first-url-index and --last-url-index are required")
            metadata = acquire_runeberg(args.volume_url, args.first_url_index,
                                        args.last_url_index, args.raw_dir, args.output,
                                        args.page_map, args.printed_first,
                                        args.printed_last, args.force)
        else:
            metadata = acquire_runeberg_pages(
                args.volume_url, args.page_names, args.raw_dir, args.output,
                args.page_map, args.printed_first, args.printed_last, args.force,
            )
    print(json.dumps(metadata, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
