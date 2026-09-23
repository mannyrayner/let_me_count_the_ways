#!/usr/bin/env python3
"""Validate and compare frozen v2 and clarified-P v3 judgments; no API calls."""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
import statistics
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.context_pilot import run_pilot as p


def load_run(scope, version, model='5.6', root=ROOT):
    base = root/'results/context_pilot'/f'{version}_{scope}'
    suffix = '_C05-C06' if scope == 'full_text' else ''
    plan = p.read(base/f'protocol_{model}{suffix}.json')
    prompt_path = root/f'prompts/context_pilot/classify_{version}.md'
    schema_path = root/'prompts/context_pilot/schema_v2.json'
    selection_path = root/'data/context_pilot/selection_v2.json'
    for key,path in [('prompt_sha256',prompt_path),('schema_sha256',schema_path),('selection_sha256',selection_path)]:
        if p.sha(path.read_text(encoding='utf-8').encode('utf-8')) != plan[key]:
            raise ValueError('Frozen protocol document changed: '+str(path))
    if plan['protocol_version'] != 'context_pilot_'+version or plan['scope'] != scope:
        raise ValueError('Unexpected protocol or scope')
    schema = p.read(schema_path)
    prompt = prompt_path.read_text(encoding='utf-8')
    records = {}
    for item in plan['call_order']:
        cid,condition,repeat = item['case_id'],item['condition'],item['repeat']
        key = (cid,condition,repeat)
        if key in records:
            raise ValueError('Duplicate call identity')
        prepared = p.read(base/'inputs'/cid/(condition+'.json'))
        body = {'model':plan['api_model'],'input':prompt+'\n\n## Input\n\n'+json.dumps(prepared,ensure_ascii=False),
                'store':False,'max_output_tokens':8000,'text':p.structured_output_format(schema,'context_pilot_v2')}
        fingerprint = p.sha(json.dumps({'protocol_sha256':plan['selection_sha256'],'request':body,'repeat':repeat},ensure_ascii=False,sort_keys=True).encode('utf-8'))
        if fingerprint != item['fingerprint']:
            raise ValueError('Request fingerprint mismatch: '+str(key))
        directory = base/'calls'/cid/condition/f'r{repeat}-{fingerprint[:16]}'
        call = dict(item,directory=directory,prepared=prepared,body=body)
        result = p.result_for(call,schema)
        if result is not None:
            provenance=p.read(directory/'provenance.json')
            attempt_name=provenance['attempt']
            if Path(attempt_name).name != attempt_name or not attempt_name.startswith('attempt-'):
                raise ValueError('Invalid attempt path')
            attempt=directory/attempt_name
            request=p.read(attempt/'request.json')
            if not p.compatible_attempt_request(request,body) or p.sha(p.json_bytes(request)) != provenance['actual_request_sha256']:
                raise ValueError('Actual request differs from frozen plan')
            response=p.read(attempt/'response.json');p.require_complete_response(response)
            parsed,_=p.parse_json_output(p.output_text(response))
            if parsed != result:
                raise ValueError('Saved output differs from retained API response')
        records[key]={'prepared':prepared,'body':body,'result':result,
                      'artifact':(directory/'output.json').relative_to(root).as_posix() if result is not None else None}
    expected={(case['case_id'],condition,repeat) for case in plan['cases'] for condition in 'ABCD' for repeat in range(1,plan['repetitions']+1)}
    if set(records) != expected:
        raise ValueError('Incomplete or unexpected call plan')
    return plan,records


def describe(results, repetitions):
    values=[r for r in results if r is not None]
    dimensions={}
    for name in 'TPEO':
        scores=[r['dimensions'][name]['score'] for r in values]
        assessable=[s for s in scores if s is not None]
        dimensions[name]={'scores':scores,'distribution':dict(Counter('null' if s is None else str(s) for s in scores)),
                          'median':statistics.median(assessable) if len(assessable)==repetitions else None}
    return {'valid':len(values),'dimensions':dimensions}


def compare(scope, model='5.6', root=ROOT):
    old_plan,old=load_run(scope,'v2',model,root)
    new_plan,new=load_run(scope,'v3',model,root)
    if set(old)!=set(new) or old_plan['repetitions']!=new_plan['repetitions']:
        raise ValueError('Comparison requires identical cases, conditions and repetitions')
    for key in old:
        if old[key]['prepared'] != new[key]['prepared']:
            raise ValueError('Source evidence or target metadata changed: '+str(key))
        a={k:v for k,v in old[key]['body'].items() if k!='input'}
        b={k:v for k,v in new[key]['body'].items() if k!='input'}
        if a!=b:
            raise ValueError('Non-prompt request parameters changed: '+str(key))
    repetitions=old_plan['repetitions']
    rows=[]
    for case in old_plan['cases']:
        cid=case['case_id']
        for condition in 'ABCD':
            keys=[(cid,condition,r) for r in range(1,repetitions+1)]
            a=describe([old[k]['result'] for k in keys],repetitions)
            b=describe([new[k]['result'] for k in keys],repetitions)
            delta={d:(b['dimensions'][d]['median']-a['dimensions'][d]['median'])
                   if a['dimensions'][d]['median'] is not None and b['dimensions'][d]['median'] is not None else None for d in 'TPEO'}
            rows.append({'case_id':cid,'label':case['label'],'condition':condition,'v2':a,'v3':b,'median_v3_minus_v2':delta,
                         'artifacts':{'v2':[old[k]['artifact'] for k in keys],'v3':[new[k]['artifact'] for k in keys]}})
    old_count=sum(v['result'] is not None for v in old.values())
    new_count=sum(v['result'] is not None for v in new.values())
    status='complete' if old_count==new_count==len(old) else 'partial' if new_count else 'awaiting_v3'
    result={'status':status,'scope':scope,'expected_per_prompt':len(old),'v2_valid':old_count,'v3_valid':new_count,
            'input_and_non_prompt_parameters_identical':True,'rows':rows,
            'interpretation':'Exploratory prompt-sensitivity comparison selected after inspecting v2. Old and new calls are not interleaved; alias/backend drift and sampling variation remain possible. Repeats are not independent literary cases. Score increases alone do not establish better validity.'}
    base=root/'results/context_pilot/comparison_v2_v3'/scope
    p.write(base/'summary.json',result)
    lines=['# P-instruction comparison: v2 versus v3','',f'Scope: {scope}. Status: {status}. v2: {old_count}/{len(old)}; v3: {new_count}/{len(new)}.','',
           'Scores are listed in repeat order. Missing or insufficient results do not become zero.','',
           '| Case | Context | P, v2 | P, v3 | Median difference |','|---|---|---|---|---|']
    for row in rows:
        vals=[]
        for version in ('v2','v3'):
            scores=row[version]['dimensions']['P']['scores']
            vals.append(', '.join('null' if x is None else str(x) for x in scores) if scores else 'pending')
        delta=row['median_v3_minus_v2']['P']
        lines.append(f"| {row['label']} | {row['condition']} | {vals[0]} | {vals[1]} | {delta if delta is not None else 'not estimable'} |")
    lines+=['',result['interpretation'],'','JSON includes all T/P/E/O scores, distributions and links to original explanations.']
    (base/'summary.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('scope','status','expected_per_prompt','v2_valid','v3_valid')},indent=2))
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scope',choices=['dossier','full_text','both'],default='both')
    parser.add_argument('--model',default='5.6')
    args=parser.parse_args()
    for scope in ('dossier','full_text') if args.scope=='both' else (args.scope,):
        compare(scope,args.model)

if __name__=='__main__':main()
