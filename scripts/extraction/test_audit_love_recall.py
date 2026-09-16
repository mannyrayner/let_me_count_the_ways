import unittest

from scripts.extraction.audit_love_recall import cue_matches


class RecallAuditRuleTests(unittest.TestCase):
    def assert_audited(self, language, text):
        _, matches = cue_matches(language, text)
        self.assertTrue(matches, text)

    def test_required_exclusive_examples_are_audited(self):
        self.assert_audited("en", "I have loved none but you.")
        self.assert_audited("fr", "Je n'aime que toi.")
        self.assert_audited("sv", "Jag älskar ingen annan än dig.")

    def test_every_corpus_language_has_an_exclusive_fixture(self):
        fixtures = {"de": "Ich liebe nur dich.", "no": "Jeg elsker bare deg.",
                    "da": "Jeg elsker kun dig.", "it": "Non amo nessuno tranne te."}
        for language, text in fixtures.items():
            with self.subTest(language=language):
                self.assert_audited(language, text)


if __name__ == "__main__":
    unittest.main()
