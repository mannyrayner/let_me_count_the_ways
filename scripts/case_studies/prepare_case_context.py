#!/usr/bin/env python3
"""Prepare verbatim, rights-aware evidence packages without model calls."""
from __future__ import annotations
import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.case_studies.common import *

def prepare(selection_path:Path, output_root:Path, provenance_root:Path, rights_policy:str, before:int, after:int):
    if rights_policy not in RIGHTS_POLICIES: raise ValueError(f"invalid rights policy {rights_policy}")
    selection=load(selection_path); reviews_doc=load(portable(selection["review_path"])); reviews={x["occurrence_id"]:x for x in reviews_doc["occurrences"]}
    for case in selection["cases"]:
        oid=case["occurrence_id"]; review=reviews[oid]
        if review["decision"] != "KEEP": raise ValueError(f"{oid} is not reviewed KEEP")
        prov_path=provenance_root/f'{case["source_id"]}.json'; prov=load(prov_path); source_path=portable(prov["local_path"]); text=source_path.read_text(encoding="utf-8")
        actual_sha=sha(text)
        if actual_sha != prov["sha256"]: raise ValueError(f"source hash mismatch: {source_path}")
        start,end,context=natural_window(text,review["start"],review["end"],before,after); target=text[review["start"]:review["end"]]
        display_start,display_end,display_context=natural_window(text,review["start"],review["end"],1800,1400)
        annotation=load(portable(case["annotation_path"])); input_path=portable(case["annotation_path"]).parents[3]/"inputs"/f"{oid}.json"; annotation_input=load(input_path)
        pages=page_ids(portable(prov.get("page_map_path","")),start,end) if prov.get("page_map_path") else []
        prepared={"schema_version":"1.0", "prepared_at":datetime.now(timezone.utc).isoformat(), "occurrence_id":oid,
          "bibliography":{k:prov.get(k) for k in ("source_id","work_id","author","title","language","repository","edition") if prov.get(k) is not None},
          "target_expression":target, "selection_reasons":case["selection_reasons"], "scene_cluster":review.get("scene_cluster"), "structural_note":review.get("structural_note"),
          "local_annotation_context":annotation_input["occurrence"]["context"], "source_context":context, "display_context":display_context,
          "source_provenance":{"source_file":source_path.as_posix(),"source_sha256":actual_sha,"context_start":start,"context_end":end,"target_start":review["start"],"target_end":review["end"],
             "context_sha256":sha(context),"chapter_or_section":annotation_input["metadata"]["location"].get("chapter_or_section"),"page_identifiers":pages,
             "display_start":display_start,"display_end":display_end,"display_sha256":sha(display_context),
             "selection_method":"paragraph boundaries around asymmetric fallback window", "requested_characters_before":before,"requested_characters_after":after,"ocr_note":prov.get("editorial_note")},
          "rights":{"policy":rights_policy,"source_note":prov.get("rights_note")},
          "frozen_annotation":{"scores":annotation_scores(annotation),"ontology_fit":annotation["ontology_assessment"]["fit"],"confidence":annotation["core_classification"]["confidence"],"rationale":annotation["core_classification"]["analysis"]},
          "paths":{"selection":selection_path.as_posix(),"annotation":case["annotation_path"],"annotation_input":input_path.as_posix(),"review":portable(selection["review_path"]).as_posix(),"provenance":prov_path.as_posix()}}
        dump(output_root/oid/"prepared.json",prepared)

def main():
 p=argparse.ArgumentParser(description=__doc__); p.add_argument("--selection",type=Path,required=True); p.add_argument("--output-root",type=Path,required=True); p.add_argument("--provenance-root",type=Path,default=Path("provenance/sources")); p.add_argument("--rights-policy",default="PUBLIC_DOMAIN_FULL_CONTEXT_OK"); p.add_argument("--before",type=int,default=6500); p.add_argument("--after",type=int,default=3500)
 a=p.parse_args(); prepare(a.selection,a.output_root,a.provenance_root,a.rights_policy,a.before,a.after); print(a.output_root)
if __name__=="__main__":main()
