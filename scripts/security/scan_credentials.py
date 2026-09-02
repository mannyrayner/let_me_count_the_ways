#!/usr/bin/env python3
"""Fail safely when likely API credentials occur in selected artifacts."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PATTERNS = [
    re.compile(rb"OPENAI_API_KEY"),
    re.compile(rb"Authorization\s*:\s*Bearer", re.IGNORECASE),
    re.compile(rb"sk-[A-Za-z0-9_-]{16,}"),
]


def files_under(paths: list[Path]) -> list[Path]:
    files = []
    for path in paths:
        if not path.exists():
            raise FileNotFoundError(path)
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(candidate for candidate in path.rglob("*") if candidate.is_file())
        else:
            raise ValueError(f"unsupported path type: {path}")
    return sorted(set(files))


def findings(paths: list[Path]) -> list[tuple[Path, int]]:
    found = []
    for path in files_under(paths):
        for line_number, line in enumerate(path.read_bytes().splitlines(), start=1):
            if any(pattern.search(line) for pattern in PATTERNS):
                found.append((path, line_number))
    return found


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", type=Path, nargs="+", help="files or directories to scan")
    args = parser.parse_args()
    try:
        found = findings(args.paths)
    except (OSError, ValueError) as exc:
        print(f"Credential scan could not run: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
    if found:
        print("Possible credential material found; matching content is redacted:", file=sys.stderr)
        for path, line_number in found:
            print(f"  {path}:{line_number}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Credential scan passed: {len(files_under(args.paths))} file(s) checked.")


if __name__ == "__main__":
    main()
