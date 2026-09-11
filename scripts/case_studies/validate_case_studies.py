#!/usr/bin/env python3
"""Validate selections, prepared evidence, enrichments, and rendered dossiers."""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.case_studies.common import annotation_scores, load, matches_criterion, sha
def validate(selection_path:Path,case_root:Path,dossier:Path):
 sel=load(selection_path); review={x["occurrence_id"]:x for x in load(Path(sel["review_path"]))["occurrences"]}; errors=[]; ids=[]; md=dossier.read_text(encoding="utf-8")
 for case in sel["cases"]:
  oid=case["occurrence_id"]; ids.append(oid); d=case_root/oid; p=load(d/"prepared.json"); r=review.get(oid)
  if not r or r["decision"]!="KEEP": errors.append(f"{oid}: not reviewed KEEP")
  if p["scene_cluster"]!=r.get("scene_cluster"): errors.append(f"{oid}: scene cluster mismatch")
  source=Path(p["source_provenance"]["source_file"]).read_text(encoding="utf-8"); sp=p["source_provenance"]
  if source[sp["context_start"]:sp["context_end"]]!=p["source_context"]: errors.append(f"{oid}: context offsets do not resolve")
  if source[sp["display_start"]:sp["display_end"]]!=p["display_context"]: errors.append(f"{oid}: display offsets do not resolve")
  if source[sp["target_start"]:sp["target_end"]]!=p["target_expression"] or p["target_expression"] not in p["source_context"]: errors.append(f"{oid}: target does not resolve")
  ann=load(Path(case["annotation_path"]));
  if annotation_scores(ann)!=p["frozen_annotation"]["scores"] or case["scores"]!=p["frozen_annotation"]["scores"]: errors.append(f"{oid}: frozen scores mismatch")
  for name in ("narrative_context","ontology_note") + (() if p["bibliography"]["language"].startswith("en") else ("translation",)):
   a=load(d/f"{name}.json")
   for key in ("model","prompt_version","prompt_sha256","source_context_sha256","usage","cost","status","output"):
    if key not in a: errors.append(f"{oid}/{name}: missing {key}")
   expected_hash=sp["display_sha256"] if name=="translation" else sp["context_sha256"]
   if a.get("source_context_sha256")!=expected_hash: errors.append(f"{oid}/{name}: source hash mismatch")
  n=load(d/"narrative_context.json")
  if n.get("context_basis") not in {"LOCAL_CONTEXT_ONLY","WIDER_SOURCE_READ","WHOLE_TEXT_READ"} or not n.get("source_ranges"): errors.append(f"{oid}: narrative evidence missing")
  tr=d/"translation.json"
  if tr.exists() and load(tr).get("translation_sha256")!=sha(load(tr)["output"]["translation"]): errors.append(f"{oid}: translation hash mismatch")
  if md.count(f"## {p['bibliography']['title']} — `{oid}`")!=1: errors.append(f"{oid}: missing or duplicate dossier section")
 for criterion in sel["criteria"]:
  if not any(matches_criterion(c,criterion) and criterion in c["selection_reasons"] for c in sel["cases"]): errors.append(f"criterion uncovered: {criterion}")
 if len(ids)!=len(set(ids)): errors.append("duplicate selected IDs")
 if errors: raise SystemExit("VALIDATION FAILED\n- "+"\n- ".join(errors))
 print(f"VALID: {len(ids)} distinct case studies; {len(sel['criteria'])} criteria covered")
def main():
 p=argparse.ArgumentParser(description=__doc__); p.add_argument("--selection",type=Path,required=True); p.add_argument("--case-root",type=Path,required=True); p.add_argument("--dossier",type=Path,required=True); a=p.parse_args(); validate(a.selection,a.case_root,a.dossier)
if __name__=="__main__":main()
