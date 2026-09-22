#!/usr/bin/env python3
"""Preflight or run membership review, translation and v0.3.1 annotation for three new works."""
from __future__ import annotations
import argparse
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.api.call_responses import resolve_model
from scripts.annotation.private_output import require_ignored_output
from scripts.review.scholarly_candidate_review import candidates
from scripts.corpus.validate_canonical_corpus import validate_work

GROUPS=[{'name':'public','extraction':'results/extraction/context_extension_3_v0_13',
         'review':'results/review/context_extension_3_v0_13_ai_review_v1',
         'annotation_root':'results/annotation','private':False},
        {'name':'local','extraction':'results/extraction_private/context_extension_3_v0_13',
         'review':'results/review_private/context_extension_3_v0_13_ai_review_v1',
         'annotation_root':'results/annotation_private','private':True}]

def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def command(script,*args):subprocess.run([sys.executable,'-u',script,*map(str,args)],cwd=ROOT,check=True)
def checked_private(path):
    require_ignored_output(ROOT/path, ROOT)

def preflight(model):
    selection=read('data/acquisition/context_extension_3_v1/selection.json')
    summaries=read('results/extraction/context_extension_3_v0_13/summary.json')
    expected={w['work_id'] for w in selection['works']};all_rows=[];counts={}
    for group in GROUPS:
        rows=candidates(ROOT/group['extraction']);all_rows+=rows;counts[group['name']]=len(rows)
        if group['private']:
            checked_private(Path(group['review']));checked_private(Path(group['annotation_root']))
    if {r['work_id'] for r in all_rows} != expected or len(all_rows)!=summaries['total_candidates']:
        raise ValueError('Candidate inventory incomplete; run acquisition and extraction first')
    if len({r['occurrence_id'] for r in all_rows})!=len(all_rows):raise ValueError('Duplicate candidate IDs')
    for wid in expected:
        errors,m=validate_work(ROOT/'corpus/works'/wid,ROOT)
        if errors:raise ValueError(errors)
        p=ROOT/(m.get('canonical_local_path') or f'corpus/works/{wid}/canonical.txt')
        text=p.read_text(encoding='utf-8')
        for r in [x for x in all_rows if x['work_id']==wid]:
            if r['canonical_sha256']!=m['canonical_sha256'] or text[r['start']:r['end']]!=r['match'] or text[r['context_start']:r['context_end']]!=r['context']:
                raise ValueError('Stale extraction: '+r['occurrence_id'])
    api,pricing=resolve_model(ROOT/'config/api_models.json',model,date.today())
    return {'status':'ready_for_membership_review','candidate_count':len(all_rows),'groups':counts,
            'api_model':api,'api_key_configured':bool(os.environ.get('OPENAI_API_KEY')),
            'pricing_verified_on':pricing['pricing_verified_on'],'classification_version':'0.3.1',
            'note':'The context experiment uses a separate prompt and is not a replacement for these historical-method annotations.'}

def estimate_guard(directory,limit):
    estimate=read(directory/'estimate.json')
    if estimate['estimated_total_usd']>limit:raise ValueError('Stage estimate exceeds limit: '+str(directory))

def run(model,limit,timeout):
    checked=preflight(model)
    if not checked['api_key_configured']:raise ValueError('OPENAI_API_KEY is not configured; no API calls made')
    for group in GROUPS:
        extraction=Path(group['extraction']);review=Path(group['review']);kept=review/'kept_candidates/kept_candidates.jsonl'
        translations=Path(group['annotation_root'])/'context_extension_3_v0_13_translations_v1'
        annotation=Path(group['annotation_root'])/'context_extension_3_v0_13_v0_3_1'
        enriched=kept.parent/'enriched_full_v1.jsonl'
        reviewer='scripts/review/scholarly_candidate_review.py'
        command(reviewer,'run','--candidates',extraction,'--output',review,'--model',model)
        command(reviewer,'validate','--candidates',extraction,'--review',review,'--expected-total',checked['groups'][group['name']])
        command(reviewer,'render','--candidates',extraction,'--review',review,'--output',review)
        command(reviewer,'freeze','--candidates',extraction,'--review',review,'--output',kept.parent)
        n=sum(bool(l.strip()) for l in (ROOT/kept).read_text(encoding='utf-8').splitlines())
        if not n:
            print(group['name']+': no retained candidates; inspect membership decisions');continue
        private=['--private-output'] if group['private'] else []
        translator='scripts/annotation/generate_context_translations.py'
        args=['--reviewed',kept,'--all-reviewed','--output',translations,'--model',model,'--timeout',timeout,*private]
        command(translator,*args,'--estimate-only');estimate_guard(translations,limit);command(translator,*args)
        if read(translations/'summary.json')['status']!='complete':raise ValueError('Translations incomplete; inspect and resume')
        command('scripts/annotation/enrich_canonical_candidates.py','--reviewed',kept,'--generated',translations/'generated_enrichment.json','--output',enriched,*private)
        annotator='scripts/annotation/annotate_canonical_candidates.py'
        args=['--enriched',enriched,'--all','--output',annotation,'--model',model,'--timeout',timeout]
        command(annotator,*args,'--estimate-only');estimate_guard(annotation,limit);command(annotator,*args)
        summary=read(annotation/'summary.json')
        if summary['status']!='complete' or summary['valid']!=n:raise ValueError('Annotations incomplete; inspect and resume')
        print(json.dumps({'group':group['name'],'valid_annotations':n,'output':str(annotation)},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',action='store_true');p.add_argument('--model',default='5.6')
    p.add_argument('--max-stage-usd',type=float,default=25);p.add_argument('--timeout',type=int,default=300);a=p.parse_args()
    if a.max_stage_usd<=0 or a.timeout<=0:p.error('Limits must be positive')
    try:
        print(json.dumps(preflight(a.model),indent=2))
        if a.run:run(a.model,a.max_stage_usd,a.timeout)
    except (ValueError,FileNotFoundError) as e:p.exit(1,str(e)+'\n')
