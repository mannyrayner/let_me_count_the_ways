#!/usr/bin/env python3
"""Resumably annotate an explicit calibration or the complete enriched KEEP set."""
from __future__ import annotations
import argparse, hashlib, json, os, sys, time, urllib.request
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Callable
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from scripts.api.call_responses import calculate_cost, output_text, parse_json_output, resolve_model, structured_output_format
from scripts.annotation.contracts import resolve_annotation_contract

def read_jsonl(path): return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x]
def write_json(path,value): path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def emit_progress(message): print(message,file=sys.stderr,flush=True)
def sha(value): return hashlib.sha256(value.encode()).hexdigest()

def prepare_annotation_input(row):
    occurrence=row['occurrence']; translation=row.get('translation'); language=row['work_metadata']['language']
    if language != 'en' and (not translation or translation.get('status') != 'provided' or not translation.get('text')):
        raise ValueError(f"{occurrence['occurrence_id']}: required translation is incomplete")
    return {'occurrence_id':occurrence['occurrence_id'],
      'SOURCE_TEXT':{'exact_match':occurrence['match'],'local_text':row['context']['local'],'wider_canonical_context':row['context']['wide']},
      'TRANSLATION_ANALYTICAL_AID':translation,
      'MODEL_GENERATED_SOURCE_GROUNDED_SUMMARY':row.get('narrative_context'),
      'METADATA':{'work':row['work_metadata'],'location':row['canonical_location'],
        'form':{k:occurrence.get(k) for k in ('form_family','polarity','tense_aspect','temporal_modifier','syntactic_family')},
        'pattern':{k:occurrence.get(k) for k in ('pattern_id','pattern_version')},'membership_review':row['review']},
      'background_knowledge':row.get('background_knowledge')}

def request_body(prompt,schema,prepared,model):
    return {'model':model,'input':prompt+'\n\n## Input\n\n'+json.dumps(prepared,ensure_ascii=False),'text':structured_output_format(schema,'classification_v0_3')}

def fingerprint(oid,model,prompt_hash,schema_hash,prepared_hash):
    value={'occurrence_id':oid,'annotation_version':'0.3.1','model':model,'prompt_sha256':prompt_hash,'schema_sha256':schema_hash,'prepared_input_sha256':prepared_hash}
    value['fingerprint_sha256']=sha(json.dumps(value,sort_keys=True,separators=(',',':'))); return value

def compatible(directory,validator,key):
    try:
        provenance=json.loads((directory/'provenance.json').read_text()); result=json.loads((directory/'output.json').read_text())
        if any(provenance.get(k)!=v for k,v in key.items()): return False
        validator(result,key['occurrence_id']); return True
    except (OSError,json.JSONDecodeError,ValueError,TypeError,KeyError): return False

def attempt_directory(output, key):
    return output/'annotations'/key['occurrence_id']/key['fingerprint_sha256']

def call_api(body,endpoint,key):
    req=urllib.request.Request(endpoint,data=json.dumps(body).encode(),headers={'Authorization':f'Bearer {key}','Content-Type':'application/json'},method='POST')
    with urllib.request.urlopen(req,timeout=300) as response: return json.loads(response.read().decode())

def selected_rows(enriched,calibration,all_records):
    rows=read_jsonl(enriched); by_id={r['occurrence']['occurrence_id']:r for r in rows}
    if all_records:
        if any(r.get('review',{}).get('decision')!='KEEP' for r in rows): raise ValueError('--all input contains non-KEEP records')
        return rows
    if calibration is None: raise ValueError('choose --calibration or --all')
    ids=[x['occurrence_id'] for x in json.loads(calibration.read_text())['cases']]
    if not 1<=len(ids)<=12 or len(ids)!=len(set(ids)): raise ValueError('calibration must contain 1-12 unique IDs')
    unknown=set(ids)-set(by_id)
    if unknown: raise ValueError(f'calibration IDs absent from enrichment: {sorted(unknown)}')
    return [by_id[x] for x in ids]

def result_row(oid,source,result):
    core=result.get('core_classification',{}); scores=core.get('label_support',{})
    flags=[]
    conditions=((scores.get('other',0)>0,'O>0'),(scores.get('exclamatory_reflexive',0)>=2,'E>=2'),(scores.get('performative',0)>=2,'P>=2'),(core.get('confidence',1)<.75,'confidence<0.75'),(result.get('ontology_assessment',{}).get('fit')!='natural','fit!=natural'),(sum(scores.get(x,0)>=2 for x in ('truth_conditional','performative','exclamatory_reflexive'))>=2,'mixed T/P/E'))
    for yes,label in conditions:
        if yes: flags.append(label)
    return {'occurrence_id':oid,'work_id':source['occurrence']['work_id'],'language':source['work_metadata']['language'],'scores':scores,'confidence':core.get('confidence'),'utterance_status':result.get('utterance_status',{}).get('status'),'ontology_fit':result.get('ontology_assessment',{}).get('fit'),'background_knowledge_used':result.get('background_knowledge',{}).get('used',False),'flags':flags}

def render_reports(output,rows,keys,stats):
    cases=[]
    for source,key in zip(rows,keys):
        oid=source['occurrence']['occurrence_id']; path=attempt_directory(output,key)/'output.json'
        if path.exists(): cases.append(result_row(oid,source,json.loads(path.read_text())))
    distributions={name:dict(Counter(r['scores'].get(key,0) for r in cases)) for name,key in [('T','truth_conditional'),('P','performative'),('E','exclamatory_reflexive'),('O','other')]}
    distributions.update({'ontology_fit':dict(Counter(r['ontology_fit'] for r in cases)),'utterance_status':dict(Counter(r['utterance_status'] for r in cases)),'background_knowledge_used':dict(Counter(str(r['background_knowledge_used']).lower() for r in cases))})
    summary={'annotation_version':'0.3.1',**stats,'distributions':distributions,'cases':cases}; write_json(output/'summary.json',summary)
    review=[r for r in cases if r['flags']]; write_json(output/'review_cases.json',review)
    header='| Occurrence | Work | Language | T/P/E/O | Confidence | Status | Fit | Background | Flags |\n|---|---|---|---|---:|---|---|---|---|\n'
    def line(r):
        s=r['scores']; scores='/'.join(str(s.get(k,0)) for k in ('truth_conditional','performative','exclamatory_reflexive','other'))
        return f"| `{r['occurrence_id']}` | {r['work_id']} | {r['language']} | {scores} | {r['confidence']} | {r['utterance_status']} | {r['ontology_fit']} | {r['background_knowledge_used']} | {', '.join(r['flags'])} |"
    (output/'summary.md').write_text('# Canonical annotation run\n\n'+header+'\n'.join(map(line,cases))+'\n',encoding='utf-8')
    (output/'review_cases.md').write_text('# Priority review cases\n\n'+header+'\n'.join(map(line,review))+'\n',encoding='utf-8')
    return summary

def run(args,caller:Callable=call_api):
    output=args.output; output.mkdir(parents=True,exist_ok=True); contract=resolve_annotation_contract('0.3.1',ROOT)
    rows=selected_rows(args.enriched,getattr(args,'calibration',None),getattr(args,'all',False)); prepared=[prepare_annotation_input(r) for r in rows]
    model,pricing=resolve_model(args.model_catalog,args.model,date.today()); prompt_hash=sha(contract.prompt); schema_hash=sha(contract.schema); schema=json.loads(contract.schema)
    keys=[]
    for p in prepared: keys.append(fingerprint(p['occurrence_id'],model,prompt_hash,schema_hash,sha(json.dumps(p,sort_keys=True,ensure_ascii=False,separators=(',',':')))))
    resumable=sum(compatible(attempt_directory(output,k),contract.validator,k) for p,k in zip(prepared,keys))
    pending=len(rows)-resumable; chars=sum(len(contract.prompt)+len(json.dumps(p,ensure_ascii=False)) for p,k in zip(prepared,keys) if not compatible(attempt_directory(output,k),contract.validator,k))
    estimate={'total_candidates':len(rows),'already_valid_resumable':resumable,'api_calls_needed':pending,'estimated_input_tokens':chars//4,'estimated_output_tokens':pending*900}
    estimate.update(calculate_cost({'input_tokens':estimate['estimated_input_tokens'],'output_tokens':estimate['estimated_output_tokens']},pricing)); estimate['estimated_total_usd']=estimate['estimated_total_cost']; write_json(output/'estimate.json',estimate)
    if args.estimate_only: print(json.dumps(estimate,indent=2)); return estimate
    api_key=os.environ.get('OPENAI_API_KEY')
    if not api_key and pending: raise ValueError('set OPENAI_API_KEY before annotation')
    emit_progress(f'Annotations: {len(rows)} KEEP candidates; {resumable} existing valid; {pending} API calls needed.')
    totals=Counter(); resumed=valid=failed=calls=0; failures=[]
    for index,(source,p,keydata) in enumerate(zip(rows,prepared,keys),1):
        oid=p['occurrence_id']; directory=attempt_directory(output,keydata); directory.mkdir(parents=True,exist_ok=True)
        if compatible(directory,contract.validator,keydata): resumed+=1; valid+=1; emit_progress(f'Annotations [{index}/{len(rows)}] {oid} : existing valid annotation; skipped')
        else:
            emit_progress(f'Annotations [{index}/{len(rows)}] {oid} : API call started'); started=time.monotonic(); body=request_body(contract.prompt,schema,p,model); write_json(directory/'request.json',body); calls+=1
            try:
                raw=caller(body,args.endpoint,api_key); write_json(directory/'response.json',raw); raw_text=output_text(raw); (directory/'raw_output.txt').write_text(raw_text,encoding='utf-8'); parsed,method=parse_json_output(raw_text); contract.validator(parsed,oid); write_json(directory/'output.json',parsed); write_json(directory/'provenance.json',keydata)
                cost=calculate_cost(raw.get('usage',{}),pricing); [totals.update({k:cost[k]}) for k in ('input_tokens','cached_input_tokens','output_tokens')]; totals['estimated_total_cost_usd']+=cost['estimated_total_cost']; valid+=1
                s=parsed['core_classification']['label_support']; vals=[s.get(k,0) for k in ('truth_conditional','performative','exclamatory_reflexive','other')]
                status={'state':'valid','parse_method':method,'timestamp':datetime.now(timezone.utc).isoformat(),'cost':cost}; emit_progress(f"Annotations [{index}/{len(rows)}] {oid} : valid, T/P/E/O={'/'.join(map(str,vals))}, {time.monotonic()-started:.1f}s, USD {cost['estimated_total_cost']:.4f}")
            except Exception as exc:
                failed+=1; failure={'occurrence_id':oid,'failure_stage':'annotation','error':f'{type(exc).__name__}: {exc}','timestamp':datetime.now(timezone.utc).isoformat(),'request':body}; failures.append(failure); status={'state':'failure',**failure}; emit_progress(f'Annotations [{index}/{len(rows)}] {oid} : FAILED {failure["error"]}; continuing')
            write_json(directory/'status.json',status)
        if index%10==0 or index==len(rows): emit_progress(f'Annotation progress: {index}/{len(rows)} processed; {valid} valid, {resumed} resumed, {failed} failed; {len(rows)-index} remaining; USD {totals["estimated_total_cost_usd"]:.2f} this run')
    stats={'status':'complete' if not failed else 'partial','requested':len(rows),'valid':valid,'failed':failed,'resumed':resumed,'api_calls_this_run':calls,**dict(totals)}; write_json(output/'usage.json',stats); write_json(output/'failures.json',failures); return render_reports(output,rows,keys,stats)

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--enriched',type=Path,required=True); mode=p.add_mutually_exclusive_group(required=True); mode.add_argument('--calibration',type=Path); mode.add_argument('--all',action='store_true'); p.add_argument('--output',type=Path,required=True); p.add_argument('--model',default='5.6'); p.add_argument('--model-catalog',type=Path,default=Path('config/api_models.json')); p.add_argument('--endpoint',default='https://api.openai.com/v1/responses'); p.add_argument('--estimate-only',action='store_true'); run(p.parse_args())
if __name__=='__main__': main()
