#!/usr/bin/env python3
"""Run resumable, separately versioned literary enrichment calls."""
from __future__ import annotations
import argparse, json, os, sys, urllib.request
from datetime import date, datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.api.call_responses import calculate_cost, output_text, parse_json_output, resolve_model
from scripts.case_studies.common import dump, load, sha

COMPONENTS={"translation":Path("prompts/case_studies/literary_translation_v1.md"),"narrative_context":Path("prompts/case_studies/narrative_context_v1.md"),"ontology_note":Path("prompts/case_studies/ontology_relevance_v1.md")}
def payload_for(component, prepared):
    evidence={"occurrence_id":prepared["occurrence_id"],"language":prepared["bibliography"]["language"],"target_expression":prepared["target_expression"],"source_context":prepared["display_context"] if component=="translation" else prepared["source_context"]}
    if component=="ontology_note": evidence["frozen_annotation"]=prepared["frozen_annotation"]
    return evidence
def enrich_one(case_dir:Path, component:str, alias:str, catalog_path:Path, endpoint:str):
    prepared=load(case_dir/"prepared.json"); prompt_path=COMPONENTS[component]; prompt=prompt_path.read_text(encoding="utf-8"); evidence=payload_for(component,prepared); evidence_text=json.dumps(evidence,ensure_ascii=False); fingerprint=sha(prompt+"\n"+evidence_text+"\n"+alias)
    if component=="translation" and prepared["bibliography"]["language"].lower().startswith("en"): return "not_required"
    current=case_dir/f"{component}.json"
    if current.exists() and load(current).get("input_fingerprint")==fingerprint and load(current).get("status")=="complete": return "skipped"
    key=os.environ.get("OPENAI_API_KEY");
    if not key: raise RuntimeError("OPENAI_API_KEY is required for model enrichment")
    model,pricing=resolve_model(catalog_path,alias,date.today()); body={"model":model,"input":prompt+"\n\n## Evidence\n\n"+evidence_text}
    req=urllib.request.Request(endpoint,data=json.dumps(body).encode(),headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"},method="POST")
    with urllib.request.urlopen(req,timeout=300) as response: raw=json.load(response)
    parsed,_=parse_json_output(output_text(raw)); now=datetime.now(timezone.utc); cost=calculate_cost(raw.get("usage",{}),pricing)
    source_hash=prepared["source_provenance"]["display_sha256" if component=="translation" else "context_sha256"]
    artifact={"schema_version":"1.0","component":component,"status":parsed["status"],"model":model,"model_alias":alias,"generated_at":now.isoformat(),"prompt_path":prompt_path.as_posix(),"prompt_version":"v1","prompt_sha256":sha(prompt),"source_context_sha256":source_hash,"input_fingerprint":fingerprint,"input_evidence":evidence,"output":parsed,"usage":raw.get("usage",{}),"cost":cost,"attempt_history":[{"generated_at":now.isoformat(),"status":parsed["status"]}]}
    if component=="translation" and parsed["status"]=="complete": artifact["translation_sha256"]=sha(parsed["translation"])
    if current.exists():
        old=load(current); archive=case_dir/"attempts"/component/f'{old.get("generated_at","unknown").replace(":","")}.json'; dump(archive,old)
    dump(current,artifact); return parsed["status"]
def main():
 p=argparse.ArgumentParser(description=__doc__); p.add_argument("--case-root",type=Path,required=True); p.add_argument("--model",default="5.6"); p.add_argument("--model-catalog",type=Path,default=Path("config/api_models.json")); p.add_argument("--endpoint",default="https://api.openai.com/v1/responses"); p.add_argument("--component",action="append",choices=COMPONENTS)
 a=p.parse_args(); components=a.component or list(COMPONENTS)
 for case_dir in sorted(p.parent for p in a.case_root.glob("*/prepared.json")):
  for component in components: print(case_dir.name,component,enrich_one(case_dir,component,a.model,a.model_catalog,a.endpoint))
if __name__=="__main__":main()
