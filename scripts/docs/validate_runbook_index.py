#!/usr/bin/env python3
"""Validate and inventory the authoritative docs/howto runbook table."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


TABLE_ROW = re.compile(
    r"^\|\s*(?P<step>\d+)\s*\|\s*\[[^]]+\]\((?P<link>[^)]+\.md)\)\s*\|"
)
NUMBERED_FILE = re.compile(r"^(?P<prefix>\d+)_.*\.md$")


@dataclass(frozen=True)
class RunbookEntry:
    step: int
    link: str


@dataclass(frozen=True)
class RunbookInventory:
    canonical: tuple[str, ...]
    unlinked: tuple[str, ...]
    errors: tuple[str, ...]


def parse_entries(readme: Path) -> list[RunbookEntry]:
    entries = []
    for line in readme.read_text(encoding="utf-8").splitlines():
        match = TABLE_ROW.match(line)
        if match:
            entries.append(RunbookEntry(int(match.group("step")), match.group("link")))
    if not entries:
        raise ValueError(f"no runbook rows found in {readme}")
    return entries


def validate_index(howto: Path) -> RunbookInventory:
    readme = howto / "README.md"
    if not readme.is_file():
        return RunbookInventory((), (), (f"missing authoritative index: {readme}",))
    try:
        entries = parse_entries(readme)
    except (OSError, ValueError) as exc:
        return RunbookInventory((), (), (str(exc),))

    errors = []
    links = [entry.link for entry in entries]
    steps = [entry.step for entry in entries]
    for link, count in Counter(links).items():
        if count > 1:
            errors.append(f"README links to {link!r} {count} times")
    for step, count in Counter(steps).items():
        if count > 1:
            errors.append(f"README claims step {step} {count} times")
    if steps:
        expected = list(range(steps[0], steps[-1] + 1))
        if steps != expected or steps[0] != 0:
            errors.append(f"README steps must be contiguous from 0; found {steps}")

    for entry in entries:
        if Path(entry.link).name != entry.link:
            errors.append(f"step {entry.step} link is not a direct filename: {entry.link!r}")
        match = NUMBERED_FILE.fullmatch(entry.link)
        if not match:
            errors.append(f"step {entry.step} link is not a numbered Markdown runbook: {entry.link!r}")
        elif int(match.group("prefix")) != entry.step:
            errors.append(
                f"step {entry.step} filename has numeric prefix {match.group('prefix')}: {entry.link}"
            )
        if not (howto / entry.link).is_file():
            errors.append(f"README link does not exist: {entry.link}")

    numbered_files = sorted(
        path.name
        for path in howto.iterdir()
        if path.is_file() and NUMBERED_FILE.fullmatch(path.name)
    )
    linked = set(links)
    filesystem = set(numbered_files)
    unlinked = tuple(sorted(filesystem - linked))
    missing = tuple(sorted(linked - filesystem))
    for name in unlinked:
        errors.append(f"unlinked numbered runbook in docs/howto: {name}")
    for name in missing:
        errors.append(f"README numbered runbook is absent from docs/howto: {name}")

    prefixes: dict[int, list[str]] = {}
    for name in numbered_files:
        match = NUMBERED_FILE.fullmatch(name)
        assert match is not None
        prefixes.setdefault(int(match.group("prefix")), []).append(name)
    for prefix, names in sorted(prefixes.items()):
        if len(names) > 1:
            errors.append(
                f"duplicate numbered runbook prefix {prefix}: {', '.join(names)}"
            )
    canonical = tuple(entry.link for entry in entries)
    return RunbookInventory(canonical, unlinked, tuple(errors))


def format_inventory(inventory: RunbookInventory) -> str:
    lines = ["README:", "  README.md", "", "Canonical:"]
    lines.extend(f"  {name}" for name in inventory.canonical)
    lines.extend(["", "Unlinked:"])
    if inventory.unlinked:
        lines.extend(f"  {name}" for name in inventory.unlinked)
    else:
        lines.append("  (none)")
    if inventory.errors:
        lines.extend(["", "Errors:"])
        lines.extend(f"  {error}" for error in inventory.errors)
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--howto", type=Path, default=Path("docs/howto"))
    args = parser.parse_args(argv)
    inventory = validate_index(args.howto)
    print(format_inventory(inventory), end="")
    if inventory.errors:
        print(f"Runbook index validation failed with {len(inventory.errors)} error(s).",
              file=sys.stderr)
        return 1
    print(f"Runbook index valid: {len(inventory.canonical)} canonical runbooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
