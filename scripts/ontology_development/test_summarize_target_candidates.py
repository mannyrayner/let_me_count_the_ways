import unittest

from summarize_target_candidates import validate


class ValidateTests(unittest.TestCase):
    def candidate(self, candidate_id="one"):
        return {
            "candidate_id": candidate_id,
            "author": "Author",
            "title": "Title",
            "original_language": "en",
            "original_publication_year": 1900,
            "genre": "novel",
            "why_contextually_useful": "Reason",
            "likely_phrase_forms": ["I love you"],
            "possible_repositories": [],
            "rights_notes": "Verify",
            "familiarity": "high",
            "selection_dimensions": [],
            "verification_needed": ["Verify source"],
        }

    def test_accepts_valid_document(self):
        candidates = validate({"prompt_version": "0.1", "candidates": [self.candidate()]})
        self.assertEqual(len(candidates), 1)

    def test_rejects_duplicate_ids(self):
        document = {
            "prompt_version": "0.1",
            "candidates": [self.candidate(), self.candidate()],
        }
        with self.assertRaisesRegex(ValueError, "duplicate candidate_id"):
            validate(document)

    def test_rejects_missing_fields(self):
        candidate = self.candidate()
        del candidate["rights_notes"]
        with self.assertRaisesRegex(ValueError, "rights_notes"):
            validate({"prompt_version": "0.1", "candidates": [candidate]})


if __name__ == "__main__":
    unittest.main()
