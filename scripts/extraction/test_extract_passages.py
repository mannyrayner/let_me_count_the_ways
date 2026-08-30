import json
import unittest
from pathlib import Path

from extract_passages import extract, load_patterns


PATTERNS = Path("data/development/search_patterns_v0_1.json")


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


if __name__ == "__main__":
    unittest.main()
