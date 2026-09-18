#!/usr/bin/env python3
"""Resumably annotate an explicit calibration manifest of enriched candidates."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.api.call_responses import calculate_cost, output_text, parse_json_output, resolve_model, structured_output_format
from scripts.annotation.contracts import resolve_annotation_contract


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def prepare_annotation_input(row: dict) -> dict:
    """Expose source and generated layers explicitly to the v0.3.1 contract."""
    occurrence = row["occurrence"]
    translation = row.get("translation")
    language = row["work_metadata"]["language"]
    if language != "en" and translation and translation.get("status") == "required" and translation.get("text") is None:
        raise ValueError(
            f"{occurrence['occurrence_id']}: required translation is incomplete"
        )
    return {
        "occurrence_id": occurrence["occurrence_id"],
        "SOURCE_TEXT": {"exact_match": occurrence["match"],
            "local_text": row["context"]["local"], "wider_canonical_context": row["context"]["wide"]},
        "TRANSLATION_ANALYTICAL_AID": translation,
        "MODEL_GENERATED_SOURCE_GROUNDED_SUMMARY": row.get("narrative_context"),
        "METADATA": {"work": row["work_metadata"], "location": row["canonical_location"],
            "form": {key: occurrence.get(key) for key in ("form_family", "polarity", "tense_aspect", "temporal_modifier", "syntactic_family")},
            "pattern": {key: occurrence.get(key) for key in ("pattern_id", "pattern_version")},
            "membership_review": row["review"]},
        "background_knowledge": row.get("background_knowledge"),
    }


def request_body(prompt: str, schema: dict, prepared: dict, model: str) -> dict:
    return {"model": model, "input": prompt + "\n\n## Input\n\n" + json.dumps(prepared, ensure_ascii=False),
            "text": structured_output_format(schema, "classification_v0_3")}


def valid_result(directory: Path, validator, occurrence_id: str) -> bool:
    path = directory / "output.json"
    if not path.exists(): return False
    try: validator(json.loads(path.read_text(encoding="utf-8")), occurrence_id)
    except (ValueError, TypeError, KeyError): return False
    return True


def render_summary(output: Path, enriched: dict[str, dict]) -> dict:
    rows = []
    for oid, source in enriched.items():
        result_path = output / "annotations" / oid / "output.json"
        if not result_path.exists(): continue
        result = json.loads(result_path.read_text(encoding="utf-8"))
        core = result.get("core_classification", {})
        scores = core.get("label_support", {})
        confidence = core.get("confidence")
        utterance_status = result.get("utterance_status", {}).get("status")
        ontology_fit = result.get("ontology_assessment", {}).get("fit")
        background_used = result.get("background_knowledge", {}).get("used", False)
        flags = []
        for condition, label in ((scores.get("other", 0) > 0, "O>0"),
            (scores.get("exclamatory_reflexive", 0) >= 2, "E>=2"),
            (scores.get("performative", 0) >= 2, "P>=2"),
            (confidence is not None and confidence < .75, "confidence<0.75"),
            (ontology_fit != "natural", "fit!=natural")):
            if condition: flags.append(label)
        rows.append({"occurrence_id": oid, "work_id": source["occurrence"]["work_id"],
            "language": source["work_metadata"]["language"], "scores": scores,
            "confidence": confidence, "utterance_status": utterance_status,
            "ontology_fit": ontology_fit,
            "background_knowledge_used": background_used, "flags": flags})
    summary = {"annotation_version": "0.3.1", "completed": len(rows), "cases": rows}
    (output / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    lines = ["# Canonical annotation calibration", "", "| Occurrence | Work | Language | Scores | Confidence | Status | Fit | Background | Flags |", "|---|---|---|---|---:|---|---|---|---|"]
    for r in rows: lines.append(f"| `{r['occurrence_id']}` | {r['work_id']} | {r['language']} | `{json.dumps(r['scores'])}` | {r['confidence']} | {r['utterance_status']} | {r['ontology_fit']} | {r['background_knowledge_used']} | {', '.join(r['flags'])} |")
    (output / "summary.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    return summary


def run(args) -> None:
    contract = resolve_annotation_contract("0.3.1", ROOT)
    all_rows = {r["occurrence"]["occurrence_id"]: r for r in read_jsonl(args.enriched)}
    manifest = json.loads(args.calibration.read_text(encoding="utf-8"))
    ids = [case["occurrence_id"] for case in manifest["cases"]]
    if not 1 <= len(ids) <= 12 or len(ids) != len(set(ids)): raise ValueError("calibration must contain 1-12 unique IDs")
    unknown = set(ids) - set(all_rows)
    if unknown: raise ValueError(f"calibration IDs absent from enrichment: {sorted(unknown)}")
    prepared_rows = {oid: prepare_annotation_input(all_rows[oid]) for oid in ids}
    model, pricing = resolve_model(args.model_catalog, args.model, date.today())
    if args.estimate_only:
        chars = sum(len(json.dumps(prepared_rows[x], ensure_ascii=False)) for x in ids)
        estimate = calculate_cost({"input_tokens": chars//4, "output_tokens": len(ids)*900}, pricing)
        print(json.dumps({"cases": len(ids), "assumptions": "4 chars/input token; 900 output tokens/case", **estimate}, indent=2)); return
    key = os.environ.get("OPENAI_API_KEY")
    if not key: raise ValueError("set OPENAI_API_KEY before annotation")
    usage = Counter()
    schema = json.loads(contract.schema)
    for oid in ids:
        directory = args.output / "annotations" / oid; directory.mkdir(parents=True, exist_ok=True)
        if valid_result(directory, contract.validator, oid): continue
        body = request_body(contract.prompt, schema, prepared_rows[oid], model)
        (directory / "request.json").write_text(json.dumps(body, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
        try:
            req = urllib.request.Request(args.endpoint, data=json.dumps(body).encode(), headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"}, method="POST")
            with urllib.request.urlopen(req, timeout=300) as response: raw = json.loads(response.read().decode())
            (directory / "response.json").write_text(json.dumps(raw, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
            parsed, method = parse_json_output(output_text(raw)); contract.validator(parsed, oid)
            (directory / "output.json").write_text(json.dumps(parsed, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
            cost = calculate_cost(raw.get("usage", {}), pricing)
            for k in ("input_tokens","cached_input_tokens","output_tokens"): usage[k] += cost[k]
            usage["estimated_total_cost_usd"] += cost["estimated_total_cost"]
            status = {"state":"valid","parse_method":method,"timestamp":datetime.now(timezone.utc).isoformat(),"cost":cost}
        except Exception as exc:
            status = {"state":"failure","error":f"{type(exc).__name__}: {exc}","timestamp":datetime.now(timezone.utc).isoformat()}
            (directory / "status.json").write_text(json.dumps(status, indent=2)+"\n", encoding="utf-8"); raise
        (directory / "status.json").write_text(json.dumps(status, indent=2)+"\n", encoding="utf-8")
    (args.output / "usage.json").write_text(json.dumps(dict(usage), indent=2)+"\n", encoding="utf-8")
    render_summary(args.output, {x: all_rows[x] for x in ids})


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("--enriched",type=Path,required=True); p.add_argument("--calibration",type=Path,required=True); p.add_argument("--output",type=Path,required=True); p.add_argument("--model",default="5.6"); p.add_argument("--model-catalog",type=Path,default=Path("config/api_models.json")); p.add_argument("--endpoint",default="https://api.openai.com/v1/responses"); p.add_argument("--estimate-only",action="store_true"); args=p.parse_args(); args.output.mkdir(parents=True,exist_ok=True); run(args)

if __name__ == "__main__": main()
