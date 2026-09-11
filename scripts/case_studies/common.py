#!/usr/bin/env python3
"""Shared, dependency-free case-study helpers."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

RIGHTS_POLICIES = {"PUBLIC_DOMAIN_FULL_CONTEXT_OK", "PERMISSIONED_CONTEXT_OK", "LIMITED_QUOTATION_ONLY", "NO_PUBLIC_RENDER"}

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def portable(path: str | Path) -> Path:
    return Path(str(path).replace("\\", "/"))

def annotation_scores(output: dict) -> dict:
    support = output["core_classification"]["label_support"]
    return {"P": support["performative"], "T": support["truth_conditional"],
            "E": support["exclamatory_reflexive"], "O": support["other"]}

_CRITERION = re.compile(r"^(P|T|E|O|confidence|ontology_fit)\s*(>=|<=|!=|=|>|<)\s*(.+)$")
def matches_criterion(case: dict, criterion: str) -> bool:
    match = _CRITERION.fullmatch(criterion.strip())
    if not match:
        raise ValueError(f"unsupported criterion: {criterion!r}")
    field, op, raw = match.groups()
    value = case["scores"].get(field) if field in "PTEO" and len(field) == 1 else case[field]
    expected = raw.strip().strip("'\"")
    if field != "ontology_fit": expected = float(expected)
    operations = {">": lambda a,b:a>b, ">=":lambda a,b:a>=b, "<":lambda a,b:a<b,
                  "<=":lambda a,b:a<=b, "=":lambda a,b:a==b, "!=":lambda a,b:a!=b}
    return operations[op](value, expected)

def latest_attempt(annotation_dir: Path) -> Path:
    attempts = sorted(p for p in annotation_dir.glob("attempt-*") if (p / "output.json").exists())
    if not attempts: raise FileNotFoundError(f"no valid annotation attempt in {annotation_dir}")
    return attempts[-1]

def page_ids(page_map: Path, start: int, end: int) -> list[dict]:
    if not page_map.exists(): return []
    return [{"url_index": p["url_index"], "url": p["url"], "output_start": p["output_start"], "output_end": p["output_end"]}
            for p in load(page_map) if p["output_end"] > start and p["output_start"] < end]

def natural_window(text: str, target_start: int, target_end: int, before: int=6500, after: int=3500) -> tuple[int,int,str]:
    """Expand a page-like fallback window to paragraph boundaries."""
    rough_start, rough_end = max(0, target_start-before), min(len(text), target_end+after)
    start = text.rfind("\n\n", 0, rough_start)
    start = 0 if start < 0 else start + 2
    end = text.find("\n\n", rough_end)
    end = len(text) if end < 0 else end
    return start, end, text[start:end]
