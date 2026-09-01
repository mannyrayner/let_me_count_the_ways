import json
import unittest
from pathlib import Path

from extract_passages import extract, load_patterns


PATTERNS = Path("data/development/search_patterns_v0_1.json")
PATTERNS_V0_2 = Path("data/development/search_patterns_v0_2.json")


class PatternTests(unittest.TestCase):
    examples = {
        "en": "I love you.",
        "sv": "Jag älskar dig.",
        "fr": "Je t’aime. Je vous aime.",
        "no": "Jeg elsker deg.",
        "da": "Jeg elsker dig.",
        "de": "Ich liebe dich.",
        "it": "Ti amo.",
    }

    def test_each_language_has_a_working_example(self):
        for language, text in self.examples.items():
            with self.subTest(language=language):
                version, patterns = load_patterns(PATTERNS, language)
                records = extract(
                    text, language, "work", "source", version, patterns, 1000
                )
                self.assertGreaterEqual(len(records), 1)

    def test_offsets_recover_exact_match(self):
        text = "Before. I love you! After."
        version, patterns = load_patterns(PATTERNS, "en")
        record = extract(text, "en", "work", "source", version, patterns, 1000)[0]
        self.assertEqual(text[record["start"]:record["end"]], record["match"])

    def test_config_is_json(self):
        self.assertEqual(json.loads(PATTERNS.read_text())["schema_version"], "0.1")


class PatternV02Tests(unittest.TestCase):
    def matches(self, language, text):
        version, patterns = load_patterns(PATTERNS_V0_2, language)
        return extract(text, language, "work", "source", version, patterns, 1000)

    def test_english_matches_plain_and_emphatic_do_forms(self):
        records = self.matches("en", "I love you. I do love you. I\ndo love\nyou.")
        self.assertEqual([record["match"] for record in records], [
            "I love you", "I do love you", "I\ndo love\nyou",
        ])

    def test_english_remains_second_person_only(self):
        self.assertEqual(self.matches("en", "I love him. I do love her."), [])

    def test_french_handles_case_apostrophes_and_line_breaks(self):
        records = self.matches("fr", "Je t'aime. JE T’AIME. Je\nvous\naime.")
        self.assertEqual(len(records), 3)

    def test_french_remains_addressee_oriented(self):
        self.assertEqual(self.matches("fr", "Je l'aime. J’aime Emma."), [])

    def test_v0_1_remains_unchanged(self):
        self.assertEqual(json.loads(PATTERNS.read_text())["schema_version"], "0.1")
        self.assertEqual(json.loads(PATTERNS_V0_2.read_text())["schema_version"], "0.2")


if __name__ == "__main__":
    unittest.main()
