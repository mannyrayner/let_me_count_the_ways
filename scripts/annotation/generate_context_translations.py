#!/usr/bin/env python3
"""Generate resumable API translations of selected non-English wide contexts."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.annotation.enrich_canonical_candidates import enrich, read_jsonl, sha256_text
from scripts.api.call_responses import (
    calculate_cost,
    output_text,
    parse_json_output,
    resolve_model,
    structured_output_format,
)

PROMPT_VERSION = "translate_context_v1"
PROMPT_PATH = Path("prompts/annotation/translate_context_v1.md")
SCHEMA_PATH = Path("prompts/annotation/translation_schema_v1.json")
NOTICE = "Analytical aid; not source text."


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def validate_output(value: object) -> str:
    if not isinstance(value, dict) or set(value) != {"text"}:
        raise ValueError("translation output must contain only the text field")
    text = value["text"]
    if not isinstance(text, str) or not text.strip():
        raise ValueError("translation text must be a non-empty string")
    return text


def resumption_key(occurrence_id: str, source_hash: str, model: str) -> dict:
    return {"occurrence_id": occurrence_id,
            "source_language_text_sha256": source_hash,
            "model": model, "prompt_version": PROMPT_VERSION}


def artifact_path(output: Path, key: dict) -> Path:
    digest = sha256_text(json.dumps(key, sort_keys=True, separators=(",", ":")))
    return output / "translations" / key["occurrence_id"] / f"{digest}.json"


def valid_artifact(value: object, key: dict, prompt_hash: str, schema_hash: str) -> bool:
    if not isinstance(value, dict):
        return False
    artifact_key = {"occurrence_id": value.get("source_occurrence_id"),
                    "source_language_text_sha256": value.get("source_language_text_sha256"),
                    "model": value.get("model"),
                    "prompt_version": value.get("prompt_version")}
    if artifact_key != key:
        return False
    required = {"status", "text", "source_occurrence_id", "source_language",
                "source_language_text_sha256", "scope", "model", "model_alias",
                "prompt_version", "prompt_sha256", "schema_sha256", "translated_at",
                "model_usage", "estimated_cost_usd", "notice"}
    if not required <= set(value):
        return False
    if value.get("status") != "provided" or value.get("source_occurrence_id") != key["occurrence_id"]:
        return False
    if value.get("scope") != "wide_context" or value.get("notice") != NOTICE:
        return False
    if value.get("prompt_sha256") != prompt_hash or value.get("schema_sha256") != schema_hash:
        return False
    if not isinstance(value.get("model_usage"), dict) or not isinstance(value.get("estimated_cost_usd"), (int, float)):
        return False
    try:
        validate_output({"text": value.get("text")})
    except ValueError:
        return False
    return True


def call_api(prompt: str, schema: dict, payload: dict, model: str,
             endpoint: str, api_key: str) -> tuple[dict, dict]:
    body = {"model": model,
            "input": prompt + "\n\n## Canonical context\n\n" + json.dumps(payload, ensure_ascii=False),
            "text": structured_output_format(schema, "canonical_context_translation")}
    request = urllib.request.Request(endpoint, data=json.dumps(body).encode(), headers={
        "Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            raw = json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"API error {exc.code}: {exc.read().decode(errors='replace')}") from exc
    parsed, _ = parse_json_output(output_text(raw))
    return parsed, raw.get("usage", {})


def generate(*, reviewed: Path, calibration: Path, output: Path, corpus: Path,
             model_alias: str, model_catalog: Path, endpoint: str,
             estimate_only: bool = False, api_key: str | None = None,
             caller: Callable = call_api) -> dict:
    prompt = (ROOT / PROMPT_PATH).read_text(encoding="utf-8")
    schema_text = (ROOT / SCHEMA_PATH).read_text(encoding="utf-8")
    schema = json.loads(schema_text)
    prompt_hash, schema_hash = sha256_text(prompt), sha256_text(schema_text)
    model, pricing = resolve_model(model_catalog, model_alias, date.today())
    rows = {row.get("candidate", row.get("occurrence", row))["occurrence_id"]: row
            for row in read_jsonl(reviewed)}
    selected = [case["occurrence_id"] for case in json.loads(
        calibration.read_text(encoding="utf-8"))["cases"]]
    missing = sorted(set(selected) - set(rows))
    if missing:
        raise ValueError(f"calibration cases are not in reviewed KEEP set: {missing}")
    sources = [enrich(rows[oid], corpus) for oid in selected]
    pending = [row for row in sources if row["work_metadata"]["language"].lower() != "en"]
    estimated_pending = []
    for row in pending:
        oid = row["occurrence"]["occurrence_id"]
        source_hash = sha256_text(row["context"]["wide"]["text"])
        key = resumption_key(oid, source_hash, model)
        path = artifact_path(output, key)
        existing = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
        if not valid_artifact(existing, key, prompt_hash, schema_hash):
            estimated_pending.append(row)
    estimated_usage = {"input_tokens": sum((len(prompt) + len(row["context"]["wide"]["text"])) // 4
                                            for row in estimated_pending),
                       "output_tokens": sum(max(1, len(row["context"]["wide"]["text"]) // 4)
                                            for row in estimated_pending)}
    if estimate_only:
        result = {"selected_cases": len(sources), "non_english_cases": len(pending),
                  "translation_calls": len(estimated_pending),
                  "assumptions": "4 characters per input/output token; excludes resumed records",
                  **calculate_cost(estimated_usage, pricing)}
        print(json.dumps(result, indent=2))
        return result
    if not api_key:
        raise ValueError("set OPENAI_API_KEY before generating translations")

    generated, resumed, called = {}, 0, 0
    totals = {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0,
              "estimated_total_cost_usd": 0.0}
    for row in pending:
        oid = row["occurrence"]["occurrence_id"]
        source_text = row["context"]["wide"]["text"]
        source_hash = sha256_text(source_text)
        key = resumption_key(oid, source_hash, model)
        path = artifact_path(output, key)
        artifact = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
        if valid_artifact(artifact, key, prompt_hash, schema_hash):
            resumed += 1
        else:
            answer, usage = caller(prompt, schema, {
                "occurrence_id": oid, "source_language": row["work_metadata"]["language"],
                "scope": "wide_context", "text": source_text}, model, endpoint, api_key)
            text = validate_output(answer)
            cost = calculate_cost(usage, pricing)
            artifact = {"status": "provided", "text": text,
                        "source_occurrence_id": oid,
                        "source_language": row["work_metadata"]["language"],
                        "source_language_text_sha256": source_hash, "scope": "wide_context",
                        "model": model, "model_alias": model_alias,
                        "prompt_version": PROMPT_VERSION, "prompt_sha256": prompt_hash,
                        "schema_sha256": schema_hash,
                        "translated_at": datetime.now(timezone.utc).isoformat(),
                        "model_usage": {name: cost[name] for name in (
                            "input_tokens", "cached_input_tokens", "output_tokens")},
                        "estimated_cost_usd": cost["estimated_total_cost"], "notice": NOTICE}
            write_json(path, artifact)
            called += 1
        generated[oid] = {"translation": artifact}
        for name in ("input_tokens", "cached_input_tokens", "output_tokens"):
            totals[name] += artifact["model_usage"].get(name, 0)
        totals["estimated_total_cost_usd"] += artifact["estimated_cost_usd"]
    write_json(output / "generated_enrichment.json", generated)
    summary = {"model": model, "model_alias": model_alias, "prompt_version": PROMPT_VERSION,
               "selected_cases": len(sources), "translations": len(generated),
               "api_calls_this_run": called, "resumed": resumed, **totals}
    write_json(output / "usage.json", summary)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reviewed", type=Path, required=True)
    parser.add_argument("--calibration", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--corpus", type=Path, default=Path("corpus"))
    parser.add_argument("--model", default="5.6")
    parser.add_argument("--model-catalog", type=Path, default=Path("config/api_models.json"))
    parser.add_argument("--endpoint", default="https://api.openai.com/v1/responses")
    parser.add_argument("--estimate-only", action="store_true")
    args = parser.parse_args()
    generate(reviewed=args.reviewed, calibration=args.calibration, output=args.output,
             corpus=args.corpus, model_alias=args.model, model_catalog=args.model_catalog,
             endpoint=args.endpoint, estimate_only=args.estimate_only,
             api_key=os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
