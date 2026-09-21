#!/usr/bin/env python3
"""Record old-span changes and an intentionally broad Russian recall screen."""
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from scripts.extraction.extract_canonical_corpus import extract_candidates
from scripts.reader.records import load_collection

def main():
    old=json.loads((ROOT/'data/development/search_patterns_v0_12.json').read_text())
    new=json.loads((ROOT/'data/development/search_patterns_v0_13.json').read_text())
    _,inventory,_=load_collection();changed=[];totals=[0,0]
    for wid in sorted(inventory):
        m=json.loads((ROOT/f'corpus/works/{wid}/work.json').read_text());t=(ROOT/f'corpus/works/{wid}/canonical.txt').read_text(encoding='utf-8')
        sets=[]
        for i,p in enumerate([old,new]):
            rows=extract_candidates(t,m,p['schema_version'],p['languages'][m['language']]['patterns'],1000)
            sets.append({(r['start'],r['end'],r['match']) for r in rows});totals[i]+=len(rows)
        added,removed=sets[1]-sets[0],sets[0]-sets[1]
        if added or removed:changed.append({'work_id':wid,'added':[list(x) for x in sorted(added)],'removed':[list(x) for x in sorted(removed)]})
    wid='tolstoy-war-and-peace';text=(ROOT/f'corpus/works/{wid}/canonical.txt').read_text(encoding='utf-8')
    rows=[json.loads(l) for l in (ROOT/f'results/extraction/context_extension_3_v0_13/works/{wid}/candidates.jsonl').read_text().splitlines()]
    uncovered=[]
    for m in re.finditer(r'\b(?:люблю|любил[а]?|любить)\b',text,re.I):
        a,b=max(0,m.start()-80),m.end()+80;near=text[a:b]
        if re.search(r'\b(?:вас|тебя)\b',near,re.I) and not any(r['start']<=m.start()<r['end'] for r in rows):
            uncovered.append({'start':m.start(),'context_start':a,'context_end':min(b,len(text)),'context':near})
    out=ROOT/'results/extraction_audit/context_extension_3_v0_13';out.mkdir(parents=True,exist_ok=True)
    result={'status':'deterministic_screen_not_exhaustive_recall_validation','legacy_works_compared':len(inventory),
            'v0_12_span_count':totals[0],'v0_13_span_count':totals[1],'changed_works':changed,
            'uncovered_nearby_Russian_address_screen':uncovered,
            'interpretation':'Version 0.13 adds Russian/French dialogue, royal address and obligation modals. Old annotations are not changed. New matches in old works require separate review before entering a later corpus snapshot. The residual screen includes third-person, coordinated and anaphoric material outside the explicit first-person/second-person pattern contract; it is not evidence of complete recall.'}
    (out/'audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'legacy_works':len(inventory),'old_spans':totals[0],'new_spans':totals[1],'changed_works':len(changed),'uncovered_Russian_screens':len(uncovered)},indent=2))

if __name__=='__main__':main()
