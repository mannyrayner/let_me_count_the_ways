#!/usr/bin/env python3
"""Add or update a human-verified model alias and token prices."""

from __future__ import annotations

import argparse
import json
from datetime import date
from decimal import Decimal
from pathlib import Path


def nonnegative(value: str) -> float:
    number = Decimal(value)
    if number < 0:
        raise argparse.ArgumentTypeError("price must be nonnegative")
    return float(number)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=Path("config/api_models.json"))
    parser.add_argument("--alias", required=True, help="short runbook name, e.g. 5.6")
    parser.add_argument("--api-model", required=True, help="exact API model identifier")
    parser.add_argument("--input", type=nonnegative, required=True,
                        help="USD per million uncached input tokens")
    parser.add_argument("--cached-input", type=nonnegative, required=True,
                        help="USD per million cached input tokens; use 0 if documented free")
    parser.add_argument("--output", type=nonnegative, required=True,
                        help="USD per million output tokens")
    parser.add_argument("--verified-on", default=date.today().isoformat())
    parser.add_argument("--source", default="https://openai.com/api/pricing/")
    args = parser.parse_args()

    date.fromisoformat(args.verified_on)
    catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
    catalog["pricing_source"] = args.source
    catalog["models"][args.alias] = {
        "api_model": args.api_model,
        "pricing_verified_on": args.verified_on,
        "pricing_source": args.source,
        "usd_per_million_tokens": {
            "input": args.input,
            "cached_input": args.cached_input,
            "output": args.output
        }
    }
    args.catalog.write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"updated {args.alias} -> {args.api_model} in {args.catalog}")


if __name__ == "__main__":
    main()
