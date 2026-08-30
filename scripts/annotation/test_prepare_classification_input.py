import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from prepare_classification_input import select_occurrence


class PrepareClassificationInputTests(unittest.TestCase):
    def test_selects_one_occurrence(self):
        with TemporaryDirectory() as directory:
            source = Path(directory) / "passages.jsonl"
            source.write_text(
                json.dumps({"occurrence_id": "one", "context": "first"}) + "\n" +
                json.dumps({"occurrence_id": "two", "context": "second"}) + "\n",
                encoding="utf-8",
            )
            self.assertEqual(select_occurrence(source, "two")["context"], "second")

    def test_rejects_missing_occurrence(self):
        with TemporaryDirectory() as directory:
            source = Path(directory) / "passages.jsonl"
            source.write_text("", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "found 0"):
                select_occurrence(source, "missing")


if __name__ == "__main__":
    unittest.main()
