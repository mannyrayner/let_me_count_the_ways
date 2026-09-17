import json
import re
import unittest
from pathlib import Path


V010 = Path("data/development/search_patterns_v0_10.json")
V011 = Path("data/development/search_patterns_v0_11.json")


class PatternV011Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v010 = json.loads(V010.read_text(encoding="utf-8"))
        cls.v011 = json.loads(V011.read_text(encoding="utf-8"))

    def pattern(self, language, pattern_id):
        return next(
            pattern
            for pattern in self.v011["languages"][language]["patterns"]
            if pattern["id"] == pattern_id
        )

    def matches(self, language, pattern_id, text):
        pattern = self.pattern(language, pattern_id)
        flags = 0 if pattern.get("case_sensitive") else re.IGNORECASE
        return bool(re.search(pattern["regex"], text, flags))

    def test_only_german_and_french_change(self):
        self.assertEqual(self.v011["schema_version"], "0.11")
        for language in set(self.v010["languages"]) - {"de", "fr"}:
            self.assertEqual(self.v011["languages"][language], self.v010["languages"][language])

    def test_german_second_person_targets_and_case(self):
        positive = {
            "de_main": ["Ich liebe dich.", "Ich liebe euch.", "Ich liebe Sie."],
            "de_subordinate": [
                "dass ich dich liebe",
                "daß ich euch liebe",
                "dass ich Sie liebe",
            ],
        }
        for pattern_id, examples in positive.items():
            for example in examples:
                with self.subTest(pattern_id=pattern_id, example=example):
                    self.assertTrue(self.matches("de", pattern_id, example))

        for example in (
            "Ich liebe sie.",
            "Ich liebe meine Frau; ich liebe sie noch.",
            "Sie weiß, wie ich sie liebe.",
        ):
            with self.subTest(example=example):
                self.assertFalse(any(
                    self.matches("de", pattern["id"], example)
                    for pattern in self.v011["languages"]["de"]["patterns"]
                ))

    def test_german_target_fix_covers_every_pattern(self):
        for pattern in self.v011["languages"]["de"]["patterns"]:
            self.assertIn("(?:dich|euch|(?-i:Sie))", pattern["regex"])
            self.assertNotIn("(?:dich|euch|Sie)", pattern["regex"])

    def test_french_future_metadata(self):
        pattern = self.pattern("fr", "fr_future")
        self.assertEqual(pattern["tense_aspect"], "future")
        for example in ("Je t'aimerai.", "Je vous aimerai."):
            self.assertTrue(self.matches("fr", "fr_future", example))
            self.assertFalse(self.matches("fr", "fr_conditional", example))

    def test_french_conditional_metadata(self):
        pattern = self.pattern("fr", "fr_conditional")
        self.assertEqual(pattern["tense_aspect"], "modal")
        self.assertEqual(pattern["modality"], "conditional")
        for example in ("Je t'aimerais.", "Je vous aimerais à la folie."):
            self.assertTrue(self.matches("fr", "fr_conditional", example))
            self.assertFalse(self.matches("fr", "fr_future", example))


if __name__ == "__main__":
    unittest.main()
