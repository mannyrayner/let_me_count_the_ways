import json
import tempfile
import unittest
from pathlib import Path

from scripts.extraction.extract_canonical_corpus import ROOT, extract_candidates, run


PATTERNS = ROOT / "data/development/search_patterns_v0_7.json"
PATTERNS_V08 = ROOT / "data/development/search_patterns_v0_8.json"
PATTERNS_V09 = ROOT / "data/development/search_patterns_v0_9.json"
EXPANSION_MANIFEST = ROOT / "data/canonicalization/expansion_15_v1/manifest.json"


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
            expansion_ids = {work["work_id"] for work in
                             json.loads(EXPANSION_MANIFEST.read_text())["works"]}
            original_ids = sorted(path.parent.name for path in
                                  (ROOT / "corpus/works").glob("*/work.json")
                                  if path.parent.name not in expansion_ids)
            original_manifest = base / "original.json"
            original_manifest.write_text(json.dumps({"works": original_ids}))
            result = run(PATTERNS, base / "public", base / "private", 100, original_manifest)
            self.assertEqual(16, result["works_attempted"])
            private = next(w for w in result["works"] if w["work_id"] == "mcmillan-error-of-understanding")
            self.assertNotEqual("public", private["candidate_artifact"])
            self.assertFalse((base / "public/works/mcmillan-error-of-understanding/candidates.jsonl").exists())
            self.assertTrue(all(result["known_case_assertions"].values()))

    def test_filtered_run_uses_manifest_and_skips_irrelevant_known_cases(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            result = run(PATTERNS_V08, base / "public", base / "private", 100,
                         EXPANSION_MANIFEST)
            self.assertEqual(15, result["works_requested"])
            self.assertEqual(15, result["works_attempted"])
            self.assertEqual(15, result["works_extracted"])
            self.assertEqual({"not_applicable"}, set(result["known_case_assertions"].values()))


class Version08PatternTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old = json.loads(PATTERNS.read_text(encoding="utf-8"))
        cls.config = json.loads(PATTERNS_V08.read_text(encoding="utf-8"))

    def matches(self, language, text):
        manifest = {"work_id": "fixture", "language": language, "canonical_sha256": "0" * 64}
        return extract_candidates(text, manifest, "0.8",
                                  self.config["languages"][language]["patterns"], 100)

    def test_inherited_language_definitions_are_exactly_equal(self):
        for language in ("en", "fr", "de", "no", "sv"):
            self.assertEqual(self.old["languages"][language], self.config["languages"][language])

    def test_danish_positive_and_negative_fixtures(self):
        positives = ["Jeg elsker dig.", "Jeg elskede Dem.", "Jeg har altid elsket dig.",
                     "Jeg har aldrig elsket dig.", "Jeg elsker dig ikke mere.",
                     "Elsker jeg dig?"]
        negatives = ["Du elsker mig.", "Jeg holder af dig.", "Han elsker dig."]
        for text in positives:
            with self.subTest(text=text):
                self.assertTrue(self.matches("da", text))
        for text in negatives:
            with self.subTest(text=text):
                self.assertEqual([], self.matches("da", text))

    def test_italian_positive_and_negative_fixtures(self):
        positives = ["Ti amo.", "Io ti amo.", "T'amo.", "T’amo.", "Vi amo.",
                     "Ti amavo.", "Ti amai.", "Ti ho amato.", "Ti ho amata.",
                     "Ti ho sempre amata.", "Non ti amo.", "Non t'amo più.",
                     "Ti amerò.", "Ti amerei.", "Voglio amarti.", "Vorrei amarvi."]
        negatives = ["Mi ami.", "Mi ama.", "Amami.", "Lei ama lui.", "Lui ti ama.",
                     "Amarti è impossibile.", "Vorrei che lui ti amasse.",
                     "Ti voglio bene.", "Sono innamorato di te."]
        for text in positives:
            with self.subTest(text=text):
                self.assertTrue(self.matches("it", text))
        for text in negatives:
            with self.subTest(text=text):
                self.assertEqual([], self.matches("it", text))

    def test_italian_cessative_wins_overlap(self):
        records = self.matches("it", "Non ti amo più.")
        self.assertEqual(["it_cessative"], [record["pattern_id"] for record in records])


class Version09ExclusiveTargetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads(PATTERNS_V09.read_text(encoding="utf-8"))

    def matches(self, language, text):
        manifest = {"work_id": "fixture", "language": language, "canonical_sha256": "0" * 64}
        return extract_candidates(text, manifest, "0.9",
                                  self.config["languages"][language]["patterns"], 100)

    def test_evidence_backed_english_positives(self):
        examples = ["I have loved none but you.", "I love only you.",
                    "I loved no one but you.", "I have loved nobody but you."]
        for example in examples:
            with self.subTest(example=example):
                records = self.matches("en", example)
                self.assertEqual(1, len(records))
                self.assertEqual("exclusive_target", records[0]["form_family"])
                self.assertEqual("affirmative", records[0]["polarity"])

    def test_english_misleading_material_is_not_matched(self):
        for text in ["I have loved none of you.", "I loved nobody, but you knew that.",
                     "I loved him, but you did not.",
                     "I have loved none better than this book."]:
            with self.subTest(text=text):
                self.assertEqual([], self.matches("en", text))

    def test_languages_without_corpus_evidence_remain_unchanged(self):
        old = json.loads(PATTERNS_V08.read_text(encoding="utf-8"))
        for language in ("fr", "de", "no", "sv", "da", "it"):
            self.assertEqual(old["languages"][language], self.config["languages"][language])


if __name__ == "__main__":
    unittest.main()
