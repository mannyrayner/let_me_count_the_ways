#!/usr/bin/env python3
"""Build offline HTML and GitHub-readable Markdown from frozen annotations."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import html
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.reader.records import load_collection, LANGUAGES, read

LABELS={"T":"Truth-conditional report / avowal","P":"Relational undertaking","E":"Expressive / reflexive force","O":"Other core function"}
def esc(value): return html.escape(str(value),quote=True)
def paragraphs(value):
    return "".join("<p>"+esc(p).replace("\n","<br>")+"</p>" for p in str(value or "").split("\n\n") if p.strip())
def target_text(record,block):
    start=record["location"]["source_start"]-block["context_start"]
    end=record["location"]["source_end"]-block["context_start"]
    text=block["text"]
    if not 0<=start<end<=len(text):raise ValueError("Target outside display context")
    return esc(text[:start])+"<mark>"+esc(text[start:end])+"</mark>"+esc(text[end:])
def shell(title,body,depth=0):
    base="../" if depth else ""
    return '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(title)+' · Let Me Count the Ways</title><link rel="stylesheet" href="'+base+'assets/reader.css"><script defer src="'+base+'assets/reader.js"></script></head><body><main class="wrap"><p class="brand"><a href="'+base+'index.html">Let Me Count the Ways</a> / Reading the evidence</p>'+body+'<footer>Saved AI annotations, shown without rescoring. Translations and interpretations are research aids. The corpus grew through successive selections of complete works.</footer></main></body></html>\n'
def chips(scores):
    return '<span class="chips">'+"".join('<span class="chip '+k+'">'+k+' '+str(v)+'</span>' for k,v in scores.items())+"</span>"
def case_html(r,prev_oid,next_oid):
    w,o=r["work"],r["output"];core=o["core_classification"]
    body='<p class="meta">'+esc(w["author"])+' · '+LANGUAGES[w["language"]]+' · '+esc(o["utterance_status"]["status"].replace("_"," "))+"</p>"
    body+="<h1>"+esc(w["title"])+"</h1>"
    if r["location"].get("chapter_or_section"):body+='<p class="meta">'+esc(r["location"]["chapter_or_section"])+"</p>"
    body+='<blockquote class="target" lang="'+w["language"]+'">'+esc(r["source"]["exact_match"])+"</blockquote>"
    body+='<div class="scores">'+"".join('<div class="score '+k+'"><strong>'+k+' '+str(v)+'<em> / 4</em></strong><span>'+LABELS[k]+"</span></div>" for k,v in r["scores"].items())+"</div>"
    body+='<p class="notice">Scores are independent levels of support, not probabilities or exclusive categories. T concerns an avowal, not its truth; P concerns an undertaking, not whether it is honoured.</p>'
    body+="<h2>The utterance in its passage</h2><div class=\"source\" lang=\""+w["language"]+'">'+target_text(r,r["source"]["local_text"])+"</div>"
    if r.get('translation'): body+='<p class="small"><a href="#translation">Read the supplied English translation ↓</a></p>'
    body+='<span class="badge">ORIGINAL TEXT</span><p class="small">The highlighted span is the extracted target. Spelling and OCR are preserved from the text supplied to the annotator.</p>'
    body+="<h2>How the scores were assigned</h2><div class=\"panel\">"+paragraphs(core["analysis"])+"</div>"
    body+='<p class="small">Original AI explanation · '+esc(r["provenance"]["model"])+' · prompt '+esc(r["provenance"]["annotation_version"])+"</p>"
    if core.get("ambiguity"):
        body+="<h3>Ambiguity noted by the annotator</h3>"+paragraphs(core["ambiguity"])
    body+="<h2>Narrative situation</h2><p class=\"small\">The original annotator’s interpretation of the supplied context.</p>"+paragraphs(o["contextual_interpretation"])
    wide=r["source"].get("wider_canonical_context") or r["source"]["local_text"];tr=r.get("translation")
    body+="<h2>Context supplied for this judgment</h2><p class=\"notice\">This is the actual saved input window. It is not a reconstruction of the entire work.</p>"
    body+='<div class="columns'+("" if tr else " single")+'"><section><h3>Original · '+LANGUAGES[w["language"]]+'</h3><div class="source" lang="'+w["language"]+'">'+target_text(r,wide)+'</div></section>'
    if tr:
        body+='<section id="translation"><h3>English translation</h3><p class="small">AI-generated analytical aid, supplied to the annotator; scope: '+esc(tr.get("scope","unspecified").replace("_"," "))+'.</p><div class="source" lang="en">'+esc(tr["text"])+"</div></section>"
    body+="</div>"
    if not tr:body+='<p class="notice">The original is English; no translation was supplied.</p>'
    body+="<h2>Evidence cited for the judgment</h2><p class=\"notice\">Quotations and descriptions below reproduce the annotator’s evidence entries. Check the original above for exact wording.</p><ol class=\"evidence\">"
    for e in o["evidence"]:
        body+='<li><span class="badge">'+esc(e["source"].replace("_"," "))+'</span><blockquote>'+esc(e["quotation_or_description"])+"</blockquote>"+paragraphs(e["supports"])+"</li>"
    body+="</ol>"
    bg=o["background_knowledge"]
    body+='<details><summary>Background knowledge, uncertainty and source records</summary>'
    body+=paragraphs(o["utterance_status"]["description"])
    body+="<p>Background knowledge reported as used: <strong>"+("Yes" if bg["used"] else "No")+"</strong>. Familiarity reported by the model: "+esc(bg["familiarity"])+".</p>"
    if bg.get("contribution"):body+=paragraphs(bg["contribution"])
    body+="<p>Self-reported confidence: "+esc(core["confidence"])+". This is not a calibrated accuracy estimate.</p>"
    body+="<p>Fit of the scheme: "+esc(o["ontology_assessment"]["fit"])+". "+esc(o["ontology_assessment"]["diagnosis"])+"</p>"
    for v in o.get("other_diagnosis",{}).values():
        if v:body+=paragraphs(v)
    if o.get("notes"):body+=paragraphs(o["notes"])
    body+='<p><a href="'+r["request_url"]+'">Saved input</a> · <a href="'+r["output_url"]+'">Saved annotation</a> · <a href="'+r["canonical_url"]+'">Canonical work</a> · <a href="../records/'+r["occurrence_id"]+'.md">Markdown record</a></p><p>Occurrence: <code>'+esc(r["occurrence_id"])+"</code></p>"
    body+="<p>Source offsets: "+str(r["location"]["source_start"])+"–"+str(r["location"]["source_end"])+". Canonical SHA-256: <code>"+w["canonical_sha256"]+"</code>.</p>"
    body+="<p>Historical run: <code>"+esc(r["run"])+"</code>. Model request fingerprint: <code>"+r["provenance"]["fingerprint_sha256"]+"</code>.</p></details>"
    body+='<nav class="nav" aria-label="Occurrence navigation">'+('<a href="'+prev_oid+'.html">← Previous occurrence</a>' if prev_oid else "<span></span>")+('<a href="'+next_oid+'.html">Next occurrence →</a>' if next_oid else "<span></span>")+"</nav>"
    return shell(w["title"],body,1)
def quoted(value):
    return "\n".join("> "+line for line in str(value).splitlines())+"\n"
def case_markdown(r):
    w,o=r["work"],r["output"];s=r["scores"];wide=r["source"].get("wider_canonical_context") or r["source"]["local_text"]
    lines=["# "+w["title"],"",w["author"]+" · "+LANGUAGES[w["language"]],"",
      "[All records](../README.md) · [HTML reading copy](../cases/"+r["occurrence_id"]+".html)","",
      "## Target","",quoted(r["source"]["exact_match"]),"",
      "| T: report / avowal | P: undertaking | E: expressive/reflexive | O: other |","|---:|---:|---:|---:|",
      "| "+" | ".join(str(s[k])+" / 4" for k in "TPEO")+" |","",
      "Scores are independent support judgments. T is not a sincerity score.","",
      "## Original passage","",quoted(r["source"]["local_text"]["text"]),"",
      "## Original AI explanation","",o["core_classification"]["analysis"],"",
      "## Ambiguity","",o["core_classification"].get("ambiguity") or "None recorded.","",
      "## Narrative situation (AI interpretation)","",o["contextual_interpretation"],"",
      "## Original context supplied to the annotator","",quoted(wide["text"]),"",
      "## English translation supplied to the annotator","",
      quoted(r["translation"]["text"]) if r["translation"] else "Original text is English; no translation was supplied.","",
      "Translation, where present, is an AI-generated analytical aid, not an authoritative edition.","",
      "## Evidence cited by the annotator",""]
    for e in o["evidence"]:
        lines.extend(["### "+e["evidence_id"]+" — "+e["source"].replace("_"," "),"",
            quoted(e["quotation_or_description"]),e["supports"],""])
    bg=o["background_knowledge"]
    lines+=["## Background, status and source records","",
        "Utterance status: **"+o["utterance_status"]["status"].replace("_"," ")+"**. "+o["utterance_status"]["description"],"",
        "Background knowledge reported as used: **"+str(bg["used"])+"**. "+(bg.get("contribution") or ""),"",
        "Self-reported confidence: "+str(o["core_classification"]["confidence"])+". Not a calibrated accuracy estimate.","",
        "Ontology fit: "+o["ontology_assessment"]["fit"]+". "+o["ontology_assessment"]["diagnosis"],"",
        "- [Saved input]("+r["request_url"]+")","- [Saved annotation]("+r["output_url"]+")",
        "- [Canonical source]("+r["canonical_url"]+")",
        "- Occurrence: "+r["occurrence_id"],"- Model: "+r["provenance"]["model"],
        "- Classification prompt: "+r["provenance"]["annotation_version"],
        "- Historical run: "+r["run"],"- Canonical SHA-256: "+w["canonical_sha256"],"",
        "Rendered deterministically from the saved record. No rescoring or replacement explanation."]
    for value in o.get("other_diagnosis",{}).values():
        if value: lines += ["", "Other-function diagnosis: "+value]
    if o.get("notes"):lines+=["","Saved notes: "+o["notes"]]
    return "\n".join(lines)+"\n"
def generate(root,config):
    records,inventory,hashes=load_collection(root,config)
    workcounts=Counter(r["work"]["work_id"] for r in records);statuses=sorted({r["output"]["utterance_status"]["status"] for r in records})
    body='<h1>What do the words do?</h1><p class="lead">Read the passages, translations and reasoning behind our study of “I love you” across literary works.</p>'
    body+='<div class="stats">'+''.join('<div class="stat"><strong>'+str(n)+'</strong>'+label+"</div>" for n,label in [(len(records),"annotated occurrences"),(len(inventory),"complete works searched"),(len({w['language'] for w in inventory.values()}),"languages")])+"</div>"
    body+='<p class="notice">One corpus, assembled over successive revisions. The reader shows the saved judgments; it does not resolve every interpretive disagreement. <a href="#about">How to read the scores</a>.</p>'
    body+='<form id="filters" class="filters"><label>Search<input id="query" type="search" placeholder="Words, work, author, interpretation…"></label><label>Work<select id="work"><option value="">All works</option>'
    for wid,w in sorted(inventory.items(),key=lambda x:x[1]["title"].casefold()):
        body+='<option value="'+wid+'">'+esc(w["title"])+" ("+str(workcounts[wid])+")</option>"
    body+='</select></label><label>Utterance status<select id="status"><option value="">All statuses</option>'+''.join('<option value="'+s+'">'+s.replace("_"," ")+"</option>" for s in statuses)+'</select></label><label>Minimum P<select id="p-min">'+''.join('<option value="'+str(n)+'">'+str(n)+(' · all scores' if n==0 else '')+"</option>" for n in range(5))+'</select></label><button type="reset">Reset</button></form>'
    body+='<p id="visible-count" class="small" role="status" aria-live="polite">'+str(len(records))+' occurrences</p><div class="table-scroll"><table id="case-table"><thead><tr><th>Work</th><th>Target expression</th><th>T / P / E / O</th><th>Status</th></tr></thead><tbody>'
    md=["# Reading the evidence","",
        f"{len(records)} annotated occurrences from {len(inventory)} complete works in {len({w['language'] for w in inventory.values()})} languages.","",
        "These are human-readable versions of the original annotations, including context, translation, explanation and evidence. No model calls or new scoring were used.","",
        "Open [index.html](index.html) in a browser after downloading the reader for search and filters. GitHub renders the Markdown records below directly.","",
        "| Work | Target | T/P/E/O | Record |","|---|---|---|---|"]
    outputs={}
    for i,r in enumerate(records):
        oid=r["occurrence_id"];w=r["work"];status=r["output"]["utterance_status"]["status"]
        search=" ".join([w["title"],w["author"],r["source"]["exact_match"],r["output"]["core_classification"]["analysis"],r["output"]["contextual_interpretation"]]).casefold()
        body+='<tr data-work="'+w["work_id"]+'" data-status="'+status+'" data-p="'+str(r["scores"]["P"])+'" data-search="'+esc(search)+'"><td>'+esc(w["title"])+'<span class="work-author">'+esc(w["author"])+" · "+LANGUAGES[w["language"]]+'</span></td><td><a href="cases/'+oid+'.html">'+esc(r["source"]["exact_match"])+"</a></td><td>"+chips(r["scores"])+"</td><td>"+status.replace("_"," ")+"</td></tr>"
        md.append("| "+w["title"].replace("|","\\|")+" | "+r["source"]["exact_match"].replace("\n"," ").replace("|","\\|")+" | "+"/".join(str(r["scores"][k]) for k in "TPEO")+" | [Read](records/"+oid+".md) |")
        outputs["cases/"+oid+".html"]=case_html(r,records[i-1]["occurrence_id"] if i else None,records[i+1]["occurrence_id"] if i+1<len(records) else None)
        outputs["records/"+oid+".md"]=case_markdown(r)
    body+='</tbody></table></div><p id="no-results" hidden>No occurrences match these filters. A work with zero extracted occurrences, such as <i>Pengar</i>, remains part of the searched corpus.</p>'
    body+='<section id="about"><h2>Reading the scores</h2><p>The four dimensions can coexist. Support is scored from 0 to 4; these are ordinal judgments, not measured probabilities.</p><ul>'
    body+=''.join("<li><strong>"+k+"</strong> — "+v+"</li>" for k,v in LABELS.items())+"</ul><p>T concerns presenting a loving state as true, even if the avowal is false. P concerns undertaking, renewing or invoking a commitment. E requires evidence about expressive or reflex-like production of the words; intensity alone does not establish it. O records a core function inadequately represented by T/P/E.</p><p>Cases include actual speech as well as written, imagined, hypothetical and narrated occurrences. The original annotation explains which event is being classified.</p></section>"
    body+='<details><summary>Sources and reproduction</summary><p>Data snapshot: <code>'+config["data_commit"]+'</code>. Full model inputs, outputs and canonical sources are linked from each case. Historical run identifiers remain available there.</p><p>Build: <code>python scripts/reader/build_reader.py</code>. Verify: <code>python scripts/reader/build_reader.py --check</code>. The build uses no API and runs offline.</p></details>'
    outputs["index.html"]=shell("Reading the evidence",body)
    outputs["README.md"]="\n".join(md)+"\n"
    for name in ["reader.css","reader.js"]:outputs["assets/"+name]=(root/"scripts/reader"/name).read_text(encoding="utf-8")
    outputs["manifest.json"]=json.dumps({"schema_version":"1.0","data_commit":config["data_commit"],
        "occurrences":len(records),"works_searched":len(inventory),"work_counts":dict(sorted(workcounts.items())),
        "source_hash_normalization":"UTF-8 JSON text after universal-newline decoding; canonical source hashes retain original bytes",
        "source_hashes":hashes,"output_sha256":{k:hashlib.sha256(v.encode()).hexdigest() for k,v in sorted(outputs.items())}},
        ensure_ascii=False,indent=2)+"\n"
    return outputs
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--output",type=Path,default=ROOT/"docs/reader")
    p.add_argument("--config",type=Path,default=ROOT/"data/reader/collection_v1.json");p.add_argument("--check",action="store_true")
    args=p.parse_args();outputs=generate(ROOT,read(args.config));differences=[]
    for name,content in outputs.items():
        path=args.output/name
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8")!=content:differences.append(name)
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            with path.open("w",encoding="utf-8",newline="\n") as stream:stream.write(content)
    if differences:raise SystemExit("Reader differs: "+", ".join(differences[:10]))
    print(json.dumps({"status":"verified" if args.check else "built","files":len(outputs),
        "occurrences":json.loads(outputs["manifest.json"])["occurrences"],"output":str(args.output)}))
if __name__=="__main__":main()
