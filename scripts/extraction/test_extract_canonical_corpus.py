import json
import tempfile
import unittest
from pathlib import Path

from scripts.extraction.extract_canonical_corpus import ROOT, extract_candidates, run


PATTERNS = ROOT / "data/development/search_patterns_v0_7.json"


class BroadenedPatternTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads(PATTERNS.read_text(encoding="utf-8"))

    def matches(self, language, text):
        manifest = {"work_id": "fixture", "language": language, "canonical_sha256": "0" * 64}
        return extract_candidates(text, manifest, "0.7",
                                  self.config["languages"][language]["patterns"], 100)

    def assert_matches_all(self, language, examples):
        for example in examples:
            with self.subTest(language=language, example=example):
                self.assertTrue(self.matches(language, example))

    def test_english_families(self):
        self.assert_matches_all("en", [
            "I love you", "I do love you", "I loved you once", "I did love you",
            "That I have loved you is true", "I've always loved you", "I still love you",
            "I do not love you", "I don't love you anymore", "I no longer love you",
            "I never loved you", "I have never loved you", "I haven't loved you",
            "I will love you", "I'll love you", "I would love you", "I'd love you",
            "I could love you", "I can love you", "I loved you not",
            "Why don't I love you?", "He wrote, ‘I love you,’ as a formula.",
        ])

    def test_other_languages_and_formal_pronouns(self):
        examples = {
            "fr": ["je t’aime", "je vous aimais toujours", "je vous ai aimé",
                   "je ne t’aime pas", "je ne vous aime plus", "je ne vous ai jamais aimé"],
            "de": ["ich liebe dich", "ich liebte Sie", "ich habe dich geliebt",
                   "ich liebe Sie nicht", "ich habe Sie nie geliebt", "dass ich dich liebe"],
            "no": ["jeg elsker deg", "jeg elsket Dem", "jeg har elsket Dem",
                   "jeg elsker deg ikke", "jeg elsker deg ikke mer", "jeg har aldri elsket Dem"],
            "sv": ["jag älskar dig", "jag älskade er", "jag har älskat er",
                   "jag älskar dig inte", "jag har aldrig älskat er", "jag älskar eder"],
        }
        for language, forms in examples.items():
            self.assert_matches_all(language, forms)

    def test_semantic_equivalents_are_not_targeted(self):
        for text in ["I'd die for you.", "You mean everything to me.",
                     "I cannot live without you.", "You are my whole life."]:
            self.assertEqual([], self.matches("en", text))

    def test_offsets_are_into_unmodified_text_and_identity_is_stable(self):
        text = "e\u0301 — I love you"
        first = self.matches("en", text)
        second = self.matches("en", text)
        self.assertEqual(5, first[0]["start"])
        self.assertEqual("I love you", text[first[0]["start"]:first[0]["end"]])
        self.assertEqual(first[0]["occurrence_id"], second[0]["occurrence_id"])

    def test_corpus_run_attempts_every_manifest_and_keeps_private_output_separate(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            result = run(PATTERNS, base / "public", base / "private", 100)
            manifest_count = len(list((ROOT / "corpus/works").glob("*/work.json")))
            self.assertEqual(manifest_count, result["works_attempted"])
            self.assertEqual(16, result["works_attempted"])
            private = next(w for w in result["works"] if w["work_id"] == "mcmillan-error-of-understanding")
            self.assertNotEqual("public", private["candidate_artifact"])
            self.assertFalse((base / "public/works/mcmillan-error-of-understanding/candidates.jsonl").exists())
            self.assertTrue(all(result["known_case_assertions"].values()))


if __name__ == "__main__":
    unittest.main()
