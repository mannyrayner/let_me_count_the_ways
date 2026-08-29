import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
import json

from call_responses import calculate_cost, output_text, resolve_model


class OutputTextTests(unittest.TestCase):
    def test_collects_output_text_parts(self):
        response = {
            "output": [
                {"content": [{"type": "output_text", "text": "first"}]},
                {"content": [{"type": "output_text", "text": "second"}]},
            ]
        }
        self.assertEqual(output_text(response), "first\nsecond")

    def test_ignores_non_text_content(self):
        response = {"output": [{"content": [{"type": "refusal", "refusal": "no"}]}]}
        self.assertEqual(output_text(response), "")

    def test_calculates_cached_and_uncached_cost(self):
        usage = {
            "input_tokens": 1000,
            "input_tokens_details": {"cached_tokens": 400},
            "output_tokens": 200,
        }
        pricing = {
            "usd_per_million_tokens": {
                "input": 2.0, "cached_input": 0.5, "output": 8.0
            }
        }
        cost = calculate_cost(usage, pricing)
        self.assertEqual(cost["uncached_input_tokens"], 600)
        self.assertAlmostEqual(cost["estimated_total_cost"], 0.003)

    def test_resolves_catalog_alias(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "models.json"
            path.write_text(json.dumps({
                "stale_after_days": 30,
                "pricing_source": "https://example.test",
                "models": {"test": {
                    "api_model": "gpt-test",
                    "pricing_verified_on": "2026-08-29"
                }}
            }))
            model, entry = resolve_model(path, "test", date(2026, 8, 29))
            self.assertEqual(model, "gpt-test")
            self.assertEqual(entry["api_model"], "gpt-test")


if __name__ == "__main__":
    unittest.main()
