import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
import json

from call_responses import (
    calculate_cost, output_text, parse_json_output, resolve_model, structured_output_format,
)


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

    def test_parses_exact_and_markdown_fenced_json(self):
        self.assertEqual(parse_json_output('{"value": 1}'), ({"value": 1}, "exact_json"))
        self.assertEqual(
            parse_json_output('```json\n{"value": 1}\n```'),
            ({"value": 1}, "markdown_json_fence_removed"),
        )

    def test_does_not_silently_discard_arbitrary_trailing_text(self):
        with self.assertRaises(json.JSONDecodeError):
            parse_json_output('{"value": 1}\nHere is an explanation.')

    def test_structured_format_removes_local_conditional_keywords(self):
        result = structured_output_format({
            "$schema": "draft", "type": "object", "allOf": [{"if": {}}], "minLength": 1,
            "$defs": {"item": {"type": "object", "allOf": [{"then": {}}]}},
        }, "classification")
        schema = result["format"]["schema"]
        self.assertNotIn("$schema", schema)
        self.assertNotIn("allOf", schema)
        self.assertNotIn("minLength", schema)
        self.assertNotIn("allOf", schema["$defs"]["item"])
        self.assertTrue(result["format"]["strict"])

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
