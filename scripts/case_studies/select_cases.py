#!/usr/bin/env python3
"""Select a deterministic union of annotated cases using configurable rules."""
from __future__ import annotations
import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.case_studies.common import dump, load, matches_criterion, portable

def select(batch_root: Path, review_path: Path, criteria: list[str], ids: list[str], top: list[str]) -> dict:
    unusual_path = batch_root / "unusual_cases.json"
    unusual = load(unusual_path) if unusual_path.exists() else {"cases": []}
    unusual_by_id = {c["occurrence_id"]: c for c in unusual["cases"]}
    reviews = {r["occurrence_id"]: r for r in load(review_path)["occurrences"]}
    candidates = []
    for output_path in batch_root.glob("texts/*/annotations/*/attempt-*/output.json"):
        out = load(output_path); oid = out["occurrence_id"]
        support = out["core_classification"]["label_support"]
        scores = {"P":support["performative"], "T":support["truth_conditional"], "E":support["exclamatory_reflexive"], "O":support["other"]}
        candidates.append({"occurrence_id":oid, "source_id": reviews.get(oid,{}).get("source_id", output_path.parts[-6]),
            "scores":scores, "confidence":out["core_classification"]["confidence"], "ontology_fit":out["ontology_assessment"]["fit"],
            "annotation_path":output_path.as_posix(), "unusual_case_path": unusual_path.as_posix() if oid in unusual_by_id else None})
    selected: dict[str,dict] = {}
    for case in candidates:
        reasons = [criterion for criterion in criteria if matches_criterion(case, criterion)]
        if case["occurrence_id"] in ids: reasons.append("explicit occurrence ID")
        if reasons: selected[case["occurrence_id"]] = {**case, "selection_reasons":reasons}
    for rule in top:
        dimension, count = rule.split(":", 1)
        for case in sorted(candidates, key=lambda c:(-c["scores"][dimension], c["occurrence_id"]))[:int(count)]:
            selected.setdefault(case["occurrence_id"], {**case, "selection_reasons":[]})["selection_reasons"].append(f"top-{count} by {dimension}")
    return {"schema_version":"1.0", "created_at":datetime.now(timezone.utc).isoformat(), "batch_root":batch_root.as_posix(),
            "review_path":review_path.as_posix(), "unusual_cases_path":unusual_path.as_posix(), "criteria":criteria,
            "explicit_occurrence_ids":ids, "top_n":top, "cases":sorted(selected.values(), key=lambda c:c["occurrence_id"])}

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("--batch-root",type=Path,required=True); p.add_argument("--review",type=Path,required=True)
    p.add_argument("--criterion",action="append",default=[]); p.add_argument("--occurrence-id",action="append",default=[]); p.add_argument("--top",action="append",default=[],metavar="DIMENSION:N"); p.add_argument("--output",type=Path,required=True)
    a=p.parse_args(); dump(a.output,select(a.batch_root,a.review,a.criterion,a.occurrence_id,a.top)); print(a.output)
if __name__=="__main__": main()
