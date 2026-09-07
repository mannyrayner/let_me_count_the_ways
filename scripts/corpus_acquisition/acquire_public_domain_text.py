#!/usr/bin/env python3
"""Atomically acquire and derive Gutenberg or Runeberg literary texts."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Callable


USER_AGENT = "Let-Me-Count-the-Ways/1.0 (literary research acquisition)"
GUTENBERG_START = re.compile(
    r"(?im)^\*\*\* START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.*?\*\*\*\s*$"
)
GUTENBERG_END = re.compile(
    r"(?im)^\*\*\* END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.*?\*\*\*\s*$"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_download(url: str, destination: Path) -> None:
    """Download *url* without exposing a partial or empty completed file."""
    if destination.exists() or destination.with_suffix(destination.suffix + ".part").exists():
        raise FileExistsError(f"refusing to overwrite {destination} or its .part file")
    destination.parent.mkdir(parents=True, exist_ok=True)
    partial = destination.with_suffix(destination.suffix + ".part")
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=60) as response, partial.open("wb") as output:
            if getattr(response, "status", 200) != 200:
                raise OSError(f"HTTP {response.status} for {url}")
            while chunk := response.read(1024 * 128):
                output.write(chunk)
        if not partial.stat().st_size:
            raise OSError(f"empty response for {url}")
        partial.replace(destination)
    except Exception:
        partial.unlink(missing_ok=True)
        raise


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
        return re.sub(r"\n{3,}", "\n\n", value).strip() + "\n"


def html_to_text(value: str) -> str:
    parser = VisibleText()
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
                       downloader: Callable[[str, Path], None] = atomic_download) -> dict:
    if output.exists():
        raise FileExistsError(f"refusing to overwrite {output}")
    downloader(url, raw)
    downloaded = raw.read_text(encoding="utf-8-sig")
    literary = html_to_text(downloaded) if raw.suffix.lower() in {".htm", ".html"} else downloaded
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(trim_gutenberg(literary), encoding="utf-8", newline="\n")
    return {"source_url": url, "download_path": str(raw), "download_sha256": sha256(raw),
            "local_path": str(output), "sha256": sha256(output)}


def page_urls(volume_url: str, first_url_index: int, last_url_index: int) -> list[str]:
    if first_url_index < 0 or last_url_index < first_url_index:
        raise ValueError("invalid Runeberg URL-index range")
    base = volume_url.rstrip("/") + "/"
    return [f"{base}{index:04d}.html" for index in range(first_url_index, last_url_index + 1)]


def acquire_runeberg(volume_url: str, first_url_index: int, last_url_index: int,
                      printed_first: int, printed_last: int, raw_dir: Path, output: Path,
                      downloader: Callable[[str, Path], None] = atomic_download) -> dict:
    """Acquire a verified contiguous Runeberg URL range; never infer its print offset."""
    if output.exists() or raw_dir.exists():
        raise FileExistsError(f"refusing to overwrite {output} or {raw_dir}")
    if printed_last < printed_first:
        raise ValueError("invalid printed-page range")
    urls = page_urls(volume_url, first_url_index, last_url_index)
    paths: list[Path] = []
    try:
        for index, url in zip(range(first_url_index, last_url_index + 1), urls):
            path = raw_dir / f"source-page-{index:04d}.html"
            downloader(url, path)
            paths.append(path)
        pages = [html_to_text(path.read_text(encoding="utf-8-sig")) for path in paths]
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text("\n\n".join(page.rstrip() for page in pages) + "\n", encoding="utf-8", newline="\n")
    except Exception:
        if raw_dir.exists() and not any(raw_dir.iterdir()):
            raw_dir.rmdir()
        raise
    return {
        "volume_url": volume_url, "printed_page_range": [printed_first, printed_last],
        "url_index_range": [first_url_index, last_url_index], "source_urls": urls,
        "download_paths": [str(path) for path in paths],
        "download_sha256": {path.name: sha256(path) for path in paths},
        "local_path": str(output), "sha256": sha256(output),
    }


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
    runeberg.add_argument("--printed-first", type=int, required=True)
    runeberg.add_argument("--printed-last", type=int, required=True)
    runeberg.add_argument("--raw-dir", type=Path, required=True)
    runeberg.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "gutenberg":
        metadata = acquire_gutenberg(args.url, args.raw, args.output)
    else:
        metadata = acquire_runeberg(args.volume_url, args.first_url_index,
                                    args.last_url_index, args.printed_first,
                                    args.printed_last, args.raw_dir, args.output)
    print(json.dumps(metadata, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
