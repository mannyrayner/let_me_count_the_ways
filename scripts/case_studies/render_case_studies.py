#!/usr/bin/env python3
"""Render auditable enrichment artifacts as a reader-facing Markdown dossier."""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.case_studies.common import dump, load

def artifact(case_dir, name): return load(case_dir/f"{name}.json")
def render(case_root:Path, output:Path, title:str):
    cases=[(p.parent,load(p)) for p in sorted(case_root.glob("*/prepared.json"))]
    blocked=[c["occurrence_id"] for _,c in cases if c["rights"]["policy"] in {"LIMITED_QUOTATION_ONLY","NO_PUBLIC_RENDER"}]
    if blocked:
        raise ValueError("public rendering blocked by rights policy for: " + ", ".join(blocked))
    lines=[f"# {title}","","> **Evidence labels.** ORIGINAL SOURCE TEXT is verbatim primary evidence. AI-GENERATED sections are working research aids. FROZEN ANNOTATION RESULT reproduces the completed annotation and is not revised here.","","## Overview","","| Work | Occurrence | Language | Scene | Selected because | P/T/E/O |","|---|---|---:|---|---|---|"]
    clusters={}
    for _,c in cases: clusters.setdefault(c.get("scene_cluster"),[]).append(c["occurrence_id"])
    for _,c in cases:
        s=c["frozen_annotation"]["scores"]; lines.append(f'| {c["bibliography"]["title"]} | `{c["occurrence_id"]}` | {c["bibliography"]["language"]} | {c.get("scene_cluster") or "—"} | {", ".join(c["selection_reasons"])} | {s["P"]}/{s["T"]}/{s["E"]}/{s["O"]} |')
    for d,c in cases:
        b=c["bibliography"]; s=c["frozen_annotation"]["scores"]; n=artifact(d,"narrative_context"); o=artifact(d,"ontology_note"); tr=(artifact(d,"translation") if (d/"translation.json").exists() else None)
        related=[x for x in clusters.get(c.get("scene_cluster"),[]) if x!=c["occurrence_id"]]
        lines += ["",f'## {b["title"]} — `{c["occurrence_id"]}`',"",f'- **Author:** {b["author"]}',f'- **Language:** {b["language"]}',f'- **Scene cluster:** {c.get("scene_cluster") or "not supplied"}',f'- **Selected because:** {", ".join(c["selection_reasons"])}']
        if related: lines += [f'- **Scene dependence:** Shares this scene with selected case(s) {", ".join(f"`{x}`" for x in related)}; these are not independent confirmations.']
        lines += ["","### ORIGINAL SOURCE TEXT","",c["display_context"]]
        if tr: lines += ["","### AI-GENERATED TRANSLATION","","> AI-generated working translation for this study; not a published or authoritative translation.","",tr["output"]["translation"]]
        lines += ["","### AI-GENERATED NARRATIVE CONTEXT","",f'**Immediate narrative situation.** {n["output"]["immediate_situation"]}',"",f'**Broader relationship/plot context.** {n["output"]["broader_context"]}',"",f'**Why here.** {n["output"]["why_here"]}']
        if n["output"].get("ambiguities"): lines += ["",f'**Ambiguities.** {n["output"]["ambiguities"]}']
        lines += ["","### FROZEN ANNOTATION RESULT","",f'**P={s["P"]}; T={s["T"]}; E={s["E"]}; O={s["O"]}; fit={c["frozen_annotation"]["ontology_fit"]}; confidence={c["frozen_annotation"]["confidence"]}.**',"","#### Original annotation rationale","",c["frozen_annotation"]["rationale"],"","#### Scholarly review note","",c["structural_note"],"","### AI-GENERATED INTERPRETIVE NOTE","",o["output"]["note"],"","### Provenance","",f'- Source: `{c["source_provenance"]["source_file"]}` (`{c["source_provenance"]["source_sha256"]}`)',f'- Source offsets: context {c["source_provenance"]["context_start"]}–{c["source_provenance"]["context_end"]}; target {c["source_provenance"]["target_start"]}–{c["source_provenance"]["target_end"]}',f'- Context selection: {c["source_provenance"]["selection_method"]}',f'- Rights policy: `{c["rights"]["policy"]}`',f'- Annotation: `{c["paths"]["annotation"]}`',f'- Review: `{c["paths"]["review"]}`',f'- Narrative evidence basis: `{n["context_basis"]}`; source ranges {n["source_ranges"]}',f'- Enrichment: `{n["model"]}`; translation `{tr["prompt_version"] if tr else "not required"}`, narrative `{n["prompt_version"]}`, ontology `{o["prompt_version"]}`.']
        if c["source_provenance"]["page_identifiers"]: lines += [f'- Runeberg page-map identifiers: {", ".join(str(x["url_index"]) for x in c["source_provenance"]["page_identifiers"])}']
        (d/"case.md").write_text("\n".join(lines[lines.index(next(x for x in reversed(lines) if x.startswith("## "))):])+"\n",encoding="utf-8")
    output.parent.mkdir(parents=True,exist_ok=True); output.write_text("\n".join(lines)+"\n",encoding="utf-8")
    costs=[sum(artifact(d,x).get("cost",{}).get("estimated_total_cost",0) for x in ("translation","narrative_context","ontology_note") if (d/f"{x}.json").exists()) for d,_ in cases]
    summary={"schema_version":"1.0","distinct_cases":len(cases),"languages":sorted({c["bibliography"]["language"] for _,c in cases}),"source_characters_read":sum(len(c["source_context"]) for _,c in cases),"source_characters_rendered":sum(len(c["display_context"]) for _,c in cases),"approximate_source_tokens_read":sum((len(c["source_context"])+3)//4 for _,c in cases),"context_escalations":sum(len(artifact(d,"narrative_context").get("escalation_steps",[]))-1 for d,_ in cases),"translations_generated":sum((d/"translation.json").exists() for d,_ in cases),"narrative_summaries_generated":len(cases),"total_enrichment_cost_usd":sum(costs),"cost_per_case_usd":sum(costs)/len(cases) if cases else 0,"cost_note":"Interactive-agent generation was not separately metered; recorded component costs are zero."}
    dump(output.with_name("cost_coverage_summary.json"),summary)
def main():
 p=argparse.ArgumentParser(description=__doc__); p.add_argument("--case-root",type=Path,required=True); p.add_argument("--output",type=Path,required=True); p.add_argument("--title",default="Critical literary case studies"); a=p.parse_args(); render(a.case_root,a.output,a.title); print(a.output)
if __name__=="__main__":main()
