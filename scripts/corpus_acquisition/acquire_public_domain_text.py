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


class RunebergOCRParser(VisibleText):
    """Extract content between Runeberg's navigation form and footer rule."""

    def __init__(self) -> None:
        super().__init__()
        self.in_body = False
        self.form_depth = 0
        self.saw_navigation = False
        self.in_content = False
        self.saw_footer = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "body":
            self.in_body = True
            return
        if self.in_body and not self.in_content:
            if tag == "form":
                self.form_depth += 1
                self.saw_navigation = True
            return
        if self.in_content and tag == "hr" and "noshade" in attributes:
            # Runeberg separates OCR from its generated revision/navigation footer
            # with an HR (normally ``<hr noshade>``).
            self.in_content = False
            self.saw_footer = True
            return
        if self.in_content:
            super().handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if tag == "form" and self.form_depth:
            self.form_depth -= 1
            if not self.form_depth:
                self.in_content = True
            return
        if self.in_content:
            super().handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        if self.in_content:
            super().handle_data(data)

    def text(self) -> str:
        if not self.in_body or not self.saw_navigation or not self.saw_footer:
            raise ValueError("HTML lacks expected Runeberg body/navigation/footer structure")
        return super().text()


def html_to_text(value: str) -> str:
    parser = VisibleText()
    parser.feed(value)
    parser.close()
    return parser.text()


def runeberg_html_to_text(value: str) -> str:
    parser = RunebergOCRParser()
    parser.feed(value)
    parser.close()
    return parser.text()


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


def acquire_runeberg(volume_url: str, first_url_index: int, last_url_index: int,
                      raw_dir: Path, output: Path, page_map: Path,
                      printed_first: int | None = None, printed_last: int | None = None,
                      force: bool = False,
                      downloader: Callable[[str, Path], object] = atomic_download) -> dict:
    """Acquire and deterministically assemble a verified contiguous Runeberg range."""
    if output.exists() or page_map.exists():
        raise FileExistsError(f"refusing to overwrite {output} or {page_map}")
    if (printed_first is None) != (printed_last is None):
        raise ValueError("printed page metadata requires both first and last")
    if printed_first is not None and printed_last < printed_first:
        raise ValueError("invalid printed-page range")
    urls = page_urls(volume_url, first_url_index, last_url_index)
    paths = [raw_dir / f"{index:04d}.html"
             for index in range(first_url_index, last_url_index + 1)]
    downloaded = 0
    for url, path in zip(urls, paths):
        if downloader is atomic_download:
            downloaded += bool(downloader(url, path, force))
        else:
            downloaded += bool(downloader(url, path) is not False)

    expected_names = [f"{index:04d}.html" for index in range(first_url_index, last_url_index + 1)]
    actual_names = sorted(path.name for path in raw_dir.glob("*.html"))
    if actual_names != expected_names:
        raise ValueError("raw page directory has missing, duplicate, or unexpected HTML pages")
    if any(not path.is_file() or not path.stat().st_size for path in paths):
        raise ValueError("raw page range contains an empty or missing page")

    chunks: list[str] = []
    records: list[dict] = []
    offset = 0
    for index, url, path in zip(range(first_url_index, last_url_index + 1), urls, paths):
        text = runeberg_html_to_text(path.read_text(encoding="utf-8-sig")).rstrip()
        separator = "" if not chunks else "\n\n"
        start = offset + len(separator)
        chunks.append(separator + text)
        offset += len(separator) + len(text)
        records.append({"url_index": index, "url": url, "output_start": start,
                        "output_end": offset, "raw_path": str(path),
                        "raw_sha256": sha256(path), "facsimile_available": True})
    assembled = "".join(chunks) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(assembled, encoding="utf-8", newline="\n")
    page_map.parent.mkdir(parents=True, exist_ok=True)
    page_map.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    metadata = {
        "volume_url": volume_url.rstrip("/") + "/",
        "runeberg_url_index_range": [first_url_index, last_url_index],
        "pages_requested": len(urls), "pages_downloaded": downloaded,
        "pages_nonempty": sum(path.stat().st_size > 0 for path in paths),
        "ordered_url_indices": list(range(first_url_index, last_url_index + 1)),
        "source_urls": urls, "download_paths": [str(path) for path in paths],
        "page_map": str(page_map), "local_path": str(output),
        "assembled_character_count": len(assembled),
        "assembled_word_count": len(assembled.split()), "sha256": sha256(output),
        "ocr_status": "not proofread / uncorrected OCR", "facsimile_available": True,
    }
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
    runeberg.add_argument("--first-url-index", type=int, required=True)
    runeberg.add_argument("--last-url-index", type=int, required=True)
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
        metadata = acquire_runeberg(args.volume_url, args.first_url_index,
                                    args.last_url_index, args.raw_dir, args.output,
                                    args.page_map, args.printed_first,
                                    args.printed_last, args.force)
    print(json.dumps(metadata, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
