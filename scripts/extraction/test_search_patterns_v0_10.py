import json
import re
import unittest
from pathlib import Path


V09 = Path("data/development/search_patterns_v0_9.json")
V010 = Path("data/development/search_patterns_v0_10.json")


class PatternV010Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v09 = json.loads(V09.read_text(encoding="utf-8"))
        cls.v010 = json.loads(V010.read_text(encoding="utf-8"))

    def pattern(self, language, pattern_id):
        return next(
            pattern
            for pattern in self.v010["languages"][language]["patterns"]
            if pattern["id"] == pattern_id
        )

    def matches(self, language, pattern_id, text):
        pattern = self.pattern(language, pattern_id)
        flags = 0 if pattern.get("case_sensitive") else re.IGNORECASE
        return bool(re.search(pattern["regex"], text, flags))

    def test_only_target_languages_change(self):
        self.assertEqual(self.v010["schema_version"], "0.10")
        self.assertEqual(self.v010["languages"]["da"], self.v09["languages"]["da"])
        for language in set(self.v09["languages"]) - {"en", "fr", "sv", "de", "it"}:
            self.assertEqual(self.v010["languages"][language], self.v09["languages"][language])

    def test_french_bounded_perfect_and_conditional(self):
        self.assertTrue(self.matches("fr", "fr_perfect", "Je vous ai assez aimée."))
        self.assertTrue(self.matches("fr", "fr_future_conditional", "Je vous aimerais à la folie."))
        self.assertFalse(self.matches("fr", "fr_perfect", "Je vous ai, malgré tout ce temps, aimée."))
        self.assertFalse(self.matches("fr", "fr_future_conditional", "Je vous le dis: j'aimerais Marie."))

    def test_swedish_exclusive_modal_perfect_is_bounded(self):
        pattern = "sv_exclusive_modal_perfect"
        self.assertTrue(self.matches("sv", pattern, "Jag har aldrig kunnat älska någon annan än dig."))
        self.assertFalse(self.matches("sv", pattern, "Jag har aldrig kunnat förstå någon bättre än dig."))

    def test_german_euch_target(self):
        self.assertTrue(self.matches("de", "de_subordinate", "daß ich euch liebe"))

    def test_italian_elided_existing_tense_families(self):
        cases = {
            "it_imperfect": ("T'amavo.", "T’amavo."),
            "it_future": ("T'amerò.", "T’amerò."),
            "it_conditional": ("T'amerei.", "T’amerei."),
            "it_remote_past": ("T'amai.", "T’amai."),
            "it_present_elided": ("T'amo.", "T’amo."),
        }
        for pattern_id, examples in cases.items():
            for example in examples:
                with self.subTest(pattern_id=pattern_id, example=example):
                    self.assertTrue(self.matches("it", pattern_id, example))
        self.assertFalse(self.matches("it", "it_imperfect", "Amavo te."))

    def test_english_emphasized_you_only(self):
        pattern = "en_emphasized_target"
        self.assertTrue(self.matches("en", pattern, "I loved _you_."))
        self.assertTrue(self.matches("en", pattern, "I should say I loved _you;_"))
        self.assertFalse(self.matches("en", pattern, "I loved _him_, but you knew that."))


if __name__ == "__main__":
    unittest.main()
