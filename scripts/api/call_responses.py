#!/usr/bin/env python3
"""Call the OpenAI Responses API and retain a reproducible run directory."""

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


def output_text(response: dict) -> str:
    parts = []
    for item in response.get("output", []):
        for content in item.get("content", []):
            if content.get("type") == "output_text" and isinstance(content.get("text"), str):
                parts.append(content["text"])
    return "\n".join(parts)


def resolve_model(catalog_path: Path, alias: str, today: date) -> tuple[str, dict]:
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    try:
        entry = catalog["models"][alias]
    except KeyError as exc:
        raise ValueError(
            f"model alias {alias!r} is not priced in {catalog_path}; "
            "run scripts/api/update_model_pricing.py first"
        ) from exc
    verified = date.fromisoformat(entry["pricing_verified_on"])
    age = (today - verified).days
    if age > catalog["stale_after_days"]:
        print(
            f"WARNING: pricing for {alias} is {age} days old; verify it against "
            f"{catalog['pricing_source']}", file=sys.stderr,
        )
    return entry["api_model"], entry


def calculate_cost(usage: dict, pricing: dict) -> dict:
    input_tokens = usage.get("input_tokens", 0)
    cached_tokens = usage.get("input_tokens_details", {}).get("cached_tokens", 0)
    output_tokens = usage.get("output_tokens", 0)
    uncached_tokens = max(0, input_tokens - cached_tokens)
    rates = pricing["usd_per_million_tokens"]
    input_cost = uncached_tokens * rates["input"] / 1_000_000
    cached_cost = cached_tokens * rates["cached_input"] / 1_000_000
    output_cost = output_tokens * rates["output"] / 1_000_000
    return {
        "currency": "USD",
        "input_tokens": input_tokens,
        "cached_input_tokens": cached_tokens,
        "uncached_input_tokens": uncached_tokens,
        "output_tokens": output_tokens,
        "input_cost": input_cost,
        "cached_input_cost": cached_cost,
        "output_cost": output_cost,
        "estimated_total_cost": input_cost + cached_cost + output_cost,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt", type=Path, required=True)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--schema", type=Path)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--model", required=True, help="alias in the model catalogue")
    parser.add_argument("--model-catalog", type=Path, default=Path("config/api_models.json"))
    parser.add_argument("--endpoint", default="https://api.openai.com/v1/responses")
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        parser.error("set OPENAI_API_KEY before running this command")
    try:
        api_model, pricing = resolve_model(args.model_catalog, args.model, date.today())
    except (ValueError, KeyError) as exc:
        parser.error(str(exc))

    prompt = args.prompt.read_text(encoding="utf-8")
    supplied_input = args.input.read_text(encoding="utf-8") if args.input else ""
    combined = prompt if not supplied_input else f"{prompt}\n\n## Input\n\n{supplied_input}"
    schema = args.schema.read_text(encoding="utf-8") if args.schema else ""
    if schema:
        combined = f"{combined}\n\n## JSON Schema\n\n{schema}"
    payload = {"model": api_model, "input": combined}
    request_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    now = datetime.now(timezone.utc)
    run_id = now.strftime("%Y%m%dT%H%M%SZ")
    run_dir = args.output_root / run_id
    suffix = 1
    while run_dir.exists():
        run_dir = args.output_root / f"{run_id}-{suffix}"
        suffix += 1
    run_dir.mkdir(parents=True)

    metadata = {
        "created_at": now.isoformat(),
        "endpoint": args.endpoint,
        "model_alias": args.model,
        "api_model": api_model,
        "prompt_path": str(args.prompt),
        "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "input_path": str(args.input) if args.input else None,
        "input_sha256": (
            hashlib.sha256(supplied_input.encode("utf-8")).hexdigest()
            if args.input else None
        ),
        "schema_path": str(args.schema) if args.schema else None,
        "schema_sha256": (
            hashlib.sha256(schema.encode("utf-8")).hexdigest()
            if args.schema else None
        ),
    }
    (run_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (run_dir / "request.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    request = urllib.request.Request(
        args.endpoint,
        data=request_bytes,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        error = exc.read().decode("utf-8", errors="replace")
        (run_dir / "error.txt").write_text(error, encoding="utf-8")
        print(f"API error {exc.code}; details saved in {run_dir / 'error.txt'}", file=sys.stderr)
        raise SystemExit(1) from exc
    except urllib.error.URLError as exc:
        (run_dir / "error.txt").write_text(str(exc), encoding="utf-8")
        print(f"network error; details saved in {run_dir / 'error.txt'}", file=sys.stderr)
        raise SystemExit(1) from exc

    parsed = json.loads(raw)
    (run_dir / "response.json").write_text(
        json.dumps(parsed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    text = output_text(parsed)
    (run_dir / "output.txt").write_text(text + ("\n" if text else ""), encoding="utf-8")
    (run_dir / "pricing_snapshot.json").write_text(
        json.dumps(pricing, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    cost = calculate_cost(parsed.get("usage", {}), pricing)
    (run_dir / "cost.json").write_text(
        json.dumps(cost, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(run_dir)


if __name__ == "__main__":
    main()
