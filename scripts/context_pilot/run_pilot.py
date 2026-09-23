#!/usr/bin/env python3
"""Prepare, run and report independent context judgments. Default: no API calls."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import date, datetime, timezone
import hashlib
import html
import json
import math
import os
from pathlib import Path
import random
import statistics
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.api.call_responses import calculate_cost, output_text, parse_json_output, resolve_model, structured_output_format
from scripts.annotation.annotate_canonical_candidates import call_api
from scripts.corpus_acquisition.prepare_commitment_extension import stable_write, json_bytes

VALIDATION_POLICY = 'literal_quote_whitespace_normalized_v1'
PUBLIC = {'PUBLIC_DOMAIN_FULL_CONTEXT_OK', 'PERMISSIONED_CONTEXT_OK'}
SELECTION = ROOT / 'data/context_pilot/selection_v1.json'
PROMPT = ROOT / 'prompts/context_pilot/classify_v1.md'
SCHEMA = ROOT / 'prompts/context_pilot/schema_v1.json'

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def sha(value):
    return hashlib.sha256(value).hexdigest()

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(json_bytes(value))

def source(case, config=None):
    manifest = read(ROOT / 'corpus/works' / case['work_id'] / 'work.json')
    if not manifest['rights']['analysis_allowed']:
        raise ValueError('Analysis not allowed: ' + case['work_id'])
    override = (config or {}).get('canonical_paths', {}).get(case['work_id'])
    if override:
        from scripts.reader.records import publication_approved, repository_path
        if not publication_approved(ROOT, config, manifest, {}):
            raise ValueError('Canonical override lacks matching publication decision')
        path = repository_path(ROOT, override)
    else:
        path = ROOT / (manifest.get('canonical_local_path') or 'corpus/works/' + case['work_id'] + '/canonical.txt')
    raw = path.read_bytes()
    if sha(raw) != case['canonical_sha256'] or sha(raw) != manifest['canonical_sha256']:
        raise ValueError('Canonical bytes changed: ' + case['case_id'])
    return path.read_text(encoding='utf-8'), manifest

def range_text(text, span):
    a, b = span
    if not (type(a) is int and type(b) is int and 0 <= a < b <= len(text)):
        raise ValueError('Invalid source span: ' + str(span))
    return text[a:b]

def inputs(case, scope, config=None):
    text, manifest = source(case, config)
    target = range_text(text, case['target'])
    a, b = case['scene']
    if not a <= case['target'][0] < case['target'][1] <= b:
        raise ValueError('Scene does not contain target')
    prior = case['prior'] if scope == 'dossier' else ([[0,a]] if a else [])
    later = case['later'] if scope == 'dossier' else ([[b,len(text)]] if b < len(text) else [])
    if any(y > a for x,y in prior) or any(x < b for x,y in later):
        raise ValueError('Prior/later evidence crosses scene boundary')
    for spans in [prior,later]:
        if spans != sorted(spans) or any(x[1] > y[0] for x,y in zip(spans,spans[1:])):
            raise ValueError('Overlapping/out-of-order excerpts')
    scene = {'block_id':'scene', 'text':range_text(text,case['scene'])}
    before = [{'block_id':f'prior_{i+1}', 'text':range_text(text,s)} for i,s in enumerate(prior)]
    after = [{'block_id':f'later_{i+1}', 'text':range_text(text,s)} for i,s in enumerate(later)]
    sequences = {'A':[], 'B':[scene], 'C':before+[scene], 'D':before+[scene]+after}
    prepared = {c:{'TARGET':target,'SOURCE_BLOCKS':blocks} for c,blocks in sequences.items()}
    if config and config['protocol_version'] in ('context_pilot_v2', 'context_pilot_v3'):
        from scripts.context_pilot.target_grounding import ground_inputs
        prepared = ground_inputs(prepared, case, text)
    return prepared, manifest

def validate_shape(value, schema, where='output'):
    types = schema.get('type'); types = types if isinstance(types,list) else [types]
    ok = any((t=='null' and value is None) or (t=='object' and isinstance(value,dict))
             or (t=='array' and isinstance(value,list)) or (t=='string' and isinstance(value,str))
             or (t=='boolean' and type(value) is bool) or (t=='integer' and type(value) is int)
             or (t=='number' and type(value) in (int,float) and math.isfinite(value)) for t in types)
    if not ok:
        raise ValueError(where + ': wrong type')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(where + ': invalid enum')
    if type(value) in (int,float):
        if value < schema.get('minimum',-math.inf) or value > schema.get('maximum',math.inf):
            raise ValueError(where + ': out of range')
    if isinstance(value,dict):
        if set(value) != set(schema['properties']):
            raise ValueError(where + ': missing or unexpected fields')
        for key, item in value.items():
            validate_shape(item,schema['properties'][key],where+'.'+key)
    if isinstance(value,list):
        for i,item in enumerate(value):
            validate_shape(item,schema['items'],where+f'[{i}]')

def quote_matches(quotation, block):
    # Ignore layout whitespace only. Preserve case, spelling, punctuation and word order.
    return bool(quotation.strip()) and ' '.join(quotation.split()) in ' '.join(block.split())

def validate(result, prepared, schema):
    validate_shape(result,schema)
    if 'TARGET_REFERENCE' in prepared:
        from scripts.context_pilot.target_grounding import validate_identification, unmark_inputs
        validate_identification(result, prepared)
        prepared = unmark_inputs(prepared)
    from scripts.context_pilot.quotation_matching import match
    audit = []
    blocks = {'target':prepared['TARGET'], **{b['block_id']:b['text'] for b in prepared['SOURCE_BLOCKS']}}
    for name, dim in result['dimensions'].items():
        insufficient = dim['evidence_status'] == 'insufficient'
        if insufficient != (dim['score'] is None):
            raise ValueError(name + ': null score must mean insufficient evidence')
        if not dim['reason'].strip() or (not insufficient and not dim['evidence']):
            raise ValueError(name + ': missing reason/evidence')
        for index, item in enumerate(dim['evidence']):
            found = match(item['quotation'], blocks.get(item['block_id'],''), allow_accents='TARGET_REFERENCE' in prepared)
            if found is None:
                raise ValueError(name + ': evidence does not match the named input block under the passage-matching policy')
            audit.append(dict(found, dimension=name, evidence_index=index, block_id=item['block_id']))
    return audit

def result_for(call, schema):
    directory = call['directory']
    output = directory / 'output.json'
    if not output.exists():
        return None
    result = read(output)
    if read(directory/'provenance.json')['fingerprint'] != call['fingerprint']:
        raise ValueError('Saved result fingerprint mismatch')
    audit = validate(result,call['prepared'],schema)
    audit_path = directory/'quotation_audit.json'
    if audit_path.exists() and read(audit_path) != audit:
        raise ValueError('Saved quotation audit differs from source alignment')
    return result

def prepare(scope, model_alias, only_cases=None, version='v1'):
    if version not in ('v1', 'v2', 'v3'):
        raise ValueError('Unknown protocol version')
    selection_path = SELECTION if version == 'v1' else ROOT/'data/context_pilot/selection_v2.json'
    prompt_path = PROMPT if version == 'v1' else ROOT/f'prompts/context_pilot/classify_{version}.md'
    schema_path = SCHEMA if version == 'v1' else ROOT/'prompts/context_pilot/schema_v2.json'
    config = read(selection_path)
    if version == 'v3':
        config['protocol_version'] = 'context_pilot_v3'
    prompt, schema = prompt_path.read_text(encoding='utf-8'), read(schema_path)
    # Protocol documents are text; v2 hashes ignore checkout newline conversion.
    # Retain the historical byte-hash contract for v1 resumption.
    def document_hash(path):
        return sha(path.read_text(encoding='utf-8').encode('utf-8')) if version in ('v2', 'v3') else sha(path.read_bytes())
    model, pricing = resolve_model(ROOT/'config/api_models.json',model_alias,date.today())
    base = ROOT / 'results/context_pilot' / (version+'_'+scope)
    calls, overview, pages = [], [], []
    wanted = set(only_cases or [c['case_id'] for c in config['cases']])
    if wanted - {c['case_id'] for c in config['cases']}:
        raise ValueError('Unknown case selection')
    for case in config['cases']:
        if case['case_id'] not in wanted:
            continue
        prepared, manifest = inputs(case,scope,config if version in ('v2', 'v3') else None)
        public = manifest['rights']['public_render_policy'] in PUBLIC
        if version in ('v2', 'v3') and not public:
            from scripts.reader.records import publication_approved
            public = publication_approved(ROOT, config, manifest, {})
        target_base = base if public else ROOT/'results/context_pilot_private'/(version+'_'+scope)
        overview.append({'case_id':case['case_id'],'work_id':case['work_id'],'label':case['label'],
                         'public_context':public,'dossier_note':case['dossier_note'],
                         'input_characters':{c:len(json.dumps(p,ensure_ascii=False)) for c,p in prepared.items()}})
        for condition,p in prepared.items():
            input_path = target_base/'inputs'/case['case_id']/(condition+'.json')
            stable_write(input_path,json_bytes(p))
            body = {'model':model,'input':prompt+'\n\n## Input\n\n'+json.dumps(p,ensure_ascii=False),
                    'store':False,'max_output_tokens':8000 if version in ('v2', 'v3') else 2400,'text':structured_output_format(schema,'context_pilot_v2' if version == 'v3' else config['protocol_version'])}
            review = '<!doctype html><meta charset="utf-8"><title>Context input</title><style>body{max-width:75ch;margin:3rem auto;padding:1rem;font:18px/1.6 Georgia}pre{white-space:pre-wrap}h2{font:1.1em system-ui}</style>'
            review += '<h1>'+html.escape(case['label'])+' — '+condition+'</h1><p>'+html.escape(config['conditions'][condition])+'</p>'
            review += '<p>Scope: '+scope+'. No scores or bibliographic labels are sent with the source input.</p><h2>Target</h2><pre>'+html.escape(p['TARGET'])+'</pre>'
            if p.get('TARGET_REFERENCE') is not None:
                review += '<h2>Reviewed target reference (sent to model)</h2><pre>'+html.escape(json.dumps(p['TARGET_REFERENCE'],ensure_ascii=False,indent=2))+'</pre>'
            for block in p['SOURCE_BLOCKS']:
                review += '<h2>'+block['block_id']+'</h2><pre>'+html.escape(block['text'])+'</pre>'
            stable_write(input_path.with_suffix('.html'),review.encode('utf-8'))
            for repeat in range(1,config['repetitions']+1):
                key = {'protocol_sha256':document_hash(selection_path),'request':body,'repeat':repeat}
                fingerprint = sha(json.dumps(key,ensure_ascii=False,sort_keys=True).encode('utf-8'))
                directory = target_base/'calls'/case['case_id']/condition/f'r{repeat}-{fingerprint[:16]}'
                calls.append({'case_id':case['case_id'],'condition':condition,'repeat':repeat,
                              'public':public,'prepared':p,'body':body,'fingerprint':fingerprint,'directory':directory})
    random.Random(config['order_seed']).shuffle(calls)
    protocol = {'protocol_version':config['protocol_version'],'scope':scope,'model_alias':model_alias,'api_model':model,
                'selection_sha256':document_hash(selection_path),'prompt_sha256':document_hash(prompt_path),'schema_sha256':document_hash(schema_path),
                'conditions':config['conditions'],'repetitions':config['repetitions'],'order_seed':config['order_seed'],
                'cases':overview,'call_order':[{'case_id':c['case_id'],'condition':c['condition'],'repeat':c['repeat'],'fingerprint':c['fingerprint']} for c in calls]}
    # A named scope/model plan has immutable inputs; subsets get their own manifest.
    manifest_name = 'protocol_'+model_alias+('_'+'-'.join(sorted(wanted)) if only_cases else '')+'.json'
    if version in ('v2', 'v3'):
        protocol['target_identification_policy'] = config['target_identification_policy']
        protocol['validation_policy'] = 'reviewed_target_identity_and_literal_quote_v2'
    stable_write(base/manifest_name,json_bytes(protocol))
    links=['# Context input review','',f'Scope: **{scope}**. Each letter opens the exact input as HTML.','',
           '| Case | Work / speaker | A | B | C | D |','|---|---|---|---|---|---|']
    for c in overview:
        cells=[f'[{x}](inputs/{c["case_id"]}/{x}.html)' if c['public_context'] else 'local only' for x in 'ABCD']
        links.append('| '+c['case_id']+' | '+c['label']+' | '+' | '.join(cells)+' |')
    links += ['','Private-case inputs are under results/context_pilot_private/'+(version+'_'+scope)+'/inputs/.',
              'Dossier inputs are selected source excerpts, not a complete-work condition. Full-text scope supplies all canonical text in D.',
              'No external background knowledge is requested. Recognition of famous works can still affect judgments.']
    (base/'README.md').write_text('\n'.join(links)+'\n',encoding='utf-8')
    return calls, base, pricing, schema, protocol

def report(calls, base, schema, protocol):
    rows=[]
    for call in calls:
        result=result_for(call,schema)
        if result is not None:
            rows.append({'case_id':call['case_id'],'condition':call['condition'],'repeat':call['repeat'],
                         'scores':{k:d['score'] for k,d in result['dimensions'].items()},
                         'recognised_work':result['recognised_work'],
                         'artifact':(call['directory']/'output.json').relative_to(ROOT).as_posix() if call['public'] else 'local-only'})
            if protocol.get('protocol_version') in ('context_pilot_v2', 'context_pilot_v3'):
                rows[-1]['target_identification'] = result['target_identification']
    cases=[]
    for case in protocol['cases']:
        by={c:[r for r in rows if r['case_id']==case['case_id'] and r['condition']==c] for c in 'ABCD'}
        groups={c:{'valid':len(rs),'P_distribution':dict(Counter(str(r['scores']['P']) for r in rs)),
                   'P_nontrivial':sum(r['scores']['P'] is not None and r['scores']['P']>=2 for r in rs),
                   'P_strong':sum(r['scores']['P'] is not None and r['scores']['P']>=3 for r in rs)} for c,rs in by.items()}
        b=[r['scores']['P'] for r in by['B'] if r['scores']['P'] is not None]
        d=[r['scores']['P'] for r in by['D'] if r['scores']['P'] is not None]
        # No partial-repeat comparison: missingness and instability stay visible.
        delta=statistics.median(d)-statistics.median(b) if len(b)==len(d)==protocol['repetitions'] else None
        cases.append({'case_id':case['case_id'],'label':case['label'],'conditions':groups,'median_P_D_minus_B':delta})
    result={'status':'complete' if len(rows)==len(calls) else 'not_run' if not rows else 'partial',
            'scope':protocol['scope'],'expected':len(calls),'valid':len(rows),'cases':cases,'judgments':rows,
            'interpretation':'Purposive diagnostic cases. Repeats are not independent literary occurrences. Differences measure model judgments under supplied evidence, not human population effects.'}
    if protocol.get('protocol_version') in ('context_pilot_v2', 'context_pilot_v3'):
        result['protocol_version'] = protocol['protocol_version']
        result['validation_note'] = 'Accepted outputs pass reference-identity and passage-matching checks. Long unique accent-only alignments are recorded separately; original responses are unchanged. Review explanations.'
    write(base/'summary.json',result)
    lines=['# Context pilot results','',f'Status: **{result["status"]}** — {len(rows)}/{len(calls)} valid judgments.','',
           'P distributions show score:count; null means insufficient evidence. No missing score is imputed as zero.','',
           '| Case | A | B | C | D | Median P: D − B |','|---|---|---|---|---|---|']
    for case in cases:
        cells=[', '.join(f'{k}:{v}' for k,v in sorted(case['conditions'][c]['P_distribution'].items())) or 'pending' for c in 'ABCD']
        lines.append('| '+case['label']+' | '+' | '.join(cells)+' | '+str(case['median_P_D_minus_B'] if case['median_P_D_minus_B'] is not None else 'not estimable')+' |')
    lines += ['',result['interpretation'],'','[Review context inputs](README.md)']
    (base/'summary.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return result

def compatible_attempt_request(actual, planned):
    """Only an explicitly increased output ceiling may differ from the frozen plan."""
    actual = dict(actual)
    budget = actual.get('max_output_tokens')
    minimum = planned.get('max_output_tokens')
    if type(budget) is not int or type(minimum) is not int or budget < minimum:
        return False
    actual['max_output_tokens'] = minimum
    return actual == planned

def require_complete_response(response):
    status = response.get('status', 'completed')
    if status != 'completed':
        reason = (response.get('incomplete_details') or {}).get('reason', status)
        if reason == 'max_output_tokens':
            raise ValueError('Response truncated at max_output_tokens. Original response saved; retry with a larger --max-output-tokens and --retry-failed. Completed judgments are preserved.')
        raise ValueError('API response is not complete: ' + str(reason))

def validation_policy(prepared):
    return 'reviewed_target_identity_and_long_unique_accent_alignment_v1' if 'TARGET_REFERENCE' in prepared else VALIDATION_POLICY

def recover_saved(calls, schema):
    recovered = 0
    for call in calls:
        if result_for(call, schema) is not None:
            continue
        for attempt in sorted(call['directory'].glob('attempt-*')):
            if not (attempt/'response.json').exists():
                continue
            # Recovery uses the identical original request, never a response from another condition.
            actual_request = read(attempt/'request.json')
            if not compatible_attempt_request(actual_request, call['body']):
                raise ValueError('Saved request differs from planned request: ' + str(attempt))
            response = read(attempt/'response.json')
            if response.get('status', 'completed') != 'completed':
                continue
            try:
                parsed, _ = parse_json_output(output_text(response))
                audit = validate(parsed, call['prepared'], schema)
            except (ValueError, KeyError, TypeError):
                continue
            stable_write(call['directory']/'quotation_audit.json', json_bytes(audit))
            stable_write(call['directory']/'provenance.json', json_bytes({
                'fingerprint':call['fingerprint'], 'attempt':attempt.name,
                'recorded_at':datetime.now(timezone.utc).isoformat(),
                'validation_policy':validation_policy(call['prepared']),
                'recovered_from_saved_response':True,
                'actual_request_sha256':sha(json_bytes(actual_request)),
                'max_output_tokens':actual_request['max_output_tokens'],
                'note':'Original response, request and any failure record retained unchanged; no API call.'}))
            stable_write(call['directory']/'output.json', json_bytes(parsed))
            recovered += 1
            print(f"Recovered: {call['case_id']} {call['condition']} repeat {call['repeat']}", flush=True)
            break
    return recovered

def audit_saved_quotes(calls, base, schema):
    rows=[]
    for call in calls:
        provenance_path=call['directory']/'provenance.json'
        selected=read(provenance_path)['attempt'] if provenance_path.exists() else None
        for attempt in sorted(call['directory'].glob('attempt-*')):
            if not (attempt/'response.json').exists():
                continue
            row={'case_id':call['case_id'],'condition':call['condition'],'repeat':call['repeat'],
                 'attempt':attempt.relative_to(ROOT).as_posix(),'selected':attempt.name==selected}
            try:
                request=read(attempt/'request.json')
                if not compatible_attempt_request(request,call['body']):
                    raise ValueError('Saved request differs from frozen plan')
                response=read(attempt/'response.json');require_complete_response(response)
                parsed,_=parse_json_output(output_text(response))
                row['quotation_matches']=validate(parsed,call['prepared'],schema)
                row['scores']={k:d['score'] for k,d in parsed['dimensions'].items()}
                row['status']='valid_under_current_policy'
            except (ValueError,KeyError,TypeError) as exc:
                row['status']='invalid';row['error']=str(exc)
            rows.append(row)
    write(base/'quotation_attempt_audit.json',{'policy':validation_policy(calls[0]['prepared']) if calls else None,
          'selection_policy':'Existing accepted judgments are preserved; superseded valid attempts are listed for sensitivity analysis, not substituted.',
          'attempts':rows})
    print('Audited retained attempts: '+str(len(rows)))

def run(args, caller=call_api):
    version = getattr(args, 'protocol', 'v1')
    calls,base,pricing,schema,protocol=prepare(args.scope,args.model,args.cases,version)
    if getattr(args, 'recover_saved', False):
        print('Recovered saved responses: ' + str(recover_saved(calls, schema)))
    if getattr(args, 'audit_saved_quotes', False):
        audit_saved_quotes(calls,base,schema)
    pending=[c for c in calls if result_for(c,schema) is None]
    minimum_budget = 8000 if version in ('v2', 'v3') else 2400
    output_budget = getattr(args, 'max_output_tokens', None) or minimum_budget
    if output_budget < minimum_budget:
        raise ValueError(f'Output budget must be at least the planned {minimum_budget}-token ceiling')
    estimated_input=sum(math.ceil(len(c['body']['input'].encode('utf-8'))/3) for c in pending)
    estimate=calculate_cost({'input_tokens':estimated_input,'output_tokens':output_budget*len(pending)},pricing)
    preflight={'status':'prepared','scope':args.scope,'cases':len(protocol['cases']),'planned_calls':len(calls),
               'resumable':len(calls)-len(pending),'calls_needed':len(pending),
               'largest_input_characters':max((len(c['body']['input']) for c in calls),default=0),
               'api_key_configured':bool(os.environ.get('OPENAI_API_KEY')),'api_model':protocol['api_model'],
               'pricing_verified_on':pricing['pricing_verified_on'],'estimate_usd':estimate['estimated_total_cost'],
               'max_output_tokens_for_new_attempts':output_budget,
               'estimate_method':f'UTF-8 bytes / 3 input tokens (heuristic), {output_budget} output tokens per remaining call (ceiling, not predicted usage); not a billing or context-capacity guarantee.'}
    if version in ('v2', 'v3'):
        preflight['protocol_version'] = protocol['protocol_version']
    write(base/'preflight.json',preflight);print(json.dumps(preflight,indent=2))
    report(calls,base,schema,protocol)
    if not args.run or not pending:
        return preflight
    if not os.environ.get('OPENAI_API_KEY'):
        raise ValueError('OPENAI_API_KEY is not configured; prepared inputs are ready, no API calls made')
    if preflight['largest_input_characters'] > args.max_input_chars:
        raise ValueError('Input exceeds --max-input-chars. Verify model capacity before changing the guard; no truncation is performed.')
    if estimate['estimated_total_cost'] > args.max_estimate_usd:
        raise ValueError('Remaining-call estimate exceeds --max-estimate-usd; no API calls made')
    completed=0
    for c in pending:
        directory=c['directory'];attempts=sorted(directory.glob('attempt-*'))
        if attempts and not args.retry_failed:
            raise ValueError('Unfinished/invalid earlier attempt in '+str(directory)+'. Inspect it; --retry-failed creates a new retained attempt and may incur another charge.')
        if args.max_calls is not None and completed >= args.max_calls:
            break
        attempt=directory/f'attempt-{len(attempts)+1:03d}'
        actual_request = dict(c['body'], max_output_tokens=output_budget)
        stable_write(attempt/'request.json',json_bytes(actual_request))
        write(attempt/'pricing_snapshot.json',pricing)
        print(f"{completed+1}: {c['case_id']} {c['condition']} repeat {c['repeat']} — started",flush=True)
        try:
            response=caller(actual_request,'https://api.openai.com/v1/responses',os.environ['OPENAI_API_KEY'],args.timeout)
            write(attempt/'response.json',response)
            write(attempt/'cost.json',calculate_cost(response.get('usage',{}),pricing))
            require_complete_response(response)
            parsed,_=parse_json_output(output_text(response));audit=validate(parsed,c['prepared'],schema)
            stable_write(directory/'quotation_audit.json',json_bytes(audit))
            stable_write(directory/'provenance.json',json_bytes({'fingerprint':c['fingerprint'],'attempt':attempt.name,
                         'recorded_at':datetime.now(timezone.utc).isoformat(),
                         'validation_policy':validation_policy(c['prepared']),
                         'actual_request_sha256':sha(json_bytes(actual_request)),
                         'max_output_tokens':output_budget}))
            stable_write(directory/'output.json',json_bytes(parsed))
            completed+=1
            print('  valid; P='+str(parsed['dimensions']['P']['score']),flush=True)
        except Exception as exc:
            write(attempt/'failure.json',{'error_type':type(exc).__name__,'message':str(exc),'automatic_retry':False})
            report(calls,base,schema,protocol)
            raise
        report(calls,base,schema,protocol)
    return report(calls,base,schema,protocol)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run',action='store_true');p.add_argument('--model',default='5.6')
    p.add_argument('--protocol',choices=['v1','v2','v3'],default='v1',help='v2: reviewed targets; v3: same inputs with clarified P instructions; separate result directories')
    p.add_argument('--scope',choices=['dossier','full_text'],default='dossier')
    p.add_argument('--cases',nargs='+',help='Optional case IDs; selection is recorded in the plan')
    p.add_argument('--max-estimate-usd',type=float,default=25)
    p.add_argument('--max-input-chars',type=int,default=250000)
    p.add_argument('--max-output-tokens',type=int,default=None,help='Default: 2400 for v1, 8000 for v2/v3. Output ceiling for new attempts only; completed judgments resume unchanged (minimum 2400)')
    p.add_argument('--max-calls',type=int);p.add_argument('--timeout',type=float,default=300)
    p.add_argument('--retry-failed',action='store_true')
    p.add_argument('--audit-saved-quotes',action='store_true',help='Audit all retained attempts, including superseded responses, without replacing accepted judgments')
    p.add_argument('--recover-saved',action='store_true',help='Validate retained responses under the whitespace-tolerant quote check; no API calls unless --run is also given')
    args=p.parse_args()
    if args.max_output_tokens is not None and args.max_output_tokens<2400:p.error('--max-output-tokens must be at least 2400')
    if args.max_estimate_usd<=0 or args.max_input_chars<=0 or args.timeout<=0 or (args.max_calls is not None and args.max_calls<=0):
        p.error('Limits must be positive')
    try:run(args)
    except (ValueError,FileNotFoundError) as exc:p.exit(1,str(exc)+'\n')

if __name__=='__main__':main()
