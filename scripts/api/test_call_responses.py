import unittest

from call_responses import output_text


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


if __name__ == "__main__":
    unittest.main()
