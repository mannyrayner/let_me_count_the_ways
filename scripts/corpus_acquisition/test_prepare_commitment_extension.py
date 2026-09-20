import tempfile
import unittest
from pathlib import Path

from scripts.corpus_acquisition.prepare_commitment_extension import alto_text, assemble, correct_page, digest, stable_write
from scripts.corpus_acquisition.acquire_public_domain_text import extract_runeberg_page


class CommitmentAcquisitionTests(unittest.TestCase):
    def test_runeberg_single_rule_requires_terminal_attribution(self):
        prose = "Selma talade med sin farbror. " * 10
        good = f'<html><body><form>Project Runeberg navigation</form><h1>1</h1><p>{prose}<hr><tt>Project Runeberg, 2012</tt></body></html>'
        text, _ = extract_runeberg_page(good)
        self.assertIn(prose.strip(), text)
        self.assertNotIn("Project Runeberg", text)
        with self.assertRaises(ValueError):
            extract_runeberg_page(good.replace('<tt>Project Runeberg, 2012</tt>', '<p>Unrelated text</p>'))

    def test_alto_preserves_word_line_order_and_numeric_dialogue(self):
        raw = b'''<alto xmlns="http://www.loc.gov/standards/alto/ns-v3#"><Layout><Page>
        <PrintSpace><TextBlock><TextLine><String CONTENT="176"/></TextLine></TextBlock>
        <TextBlock><TextLine><String CONTENT="jeg"/><String CONTENT="elsker"/></TextLine>
        <TextLine><String CONTENT="Dig."/></TextLine></TextBlock>
        <TextBlock><TextLine><String CONTENT="176"/></TextLine></TextBlock>
        </PrintSpace></Page></Layout></alto>'''
        self.assertEqual(alto_text(raw, "176"), "jeg elsker\nDig.\n\n176")

    def test_alto_does_not_remove_first_literary_line_without_number(self):
        raw = b'<alto><TextBlock><TextLine><String CONTENT="Love"/></TextLine></TextBlock></alto>'
        self.assertEqual(alto_text(raw, "1"), "Love")

    def test_alto_rejects_error_document_and_preserves_empty_page(self):
        with self.assertRaises(ValueError):
            alto_text(b"<html>Unavailable</html>", "1")
        self.assertEqual(alto_text(b"<alto><Layout/></alto>", "1"), "")

    def test_unicode_page_offsets_reconstruct_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            parts = [("1", b"first", "\u00e4lskar", root / "one.xml"),
                     ("2", b"second", "dig", root / "two.xml")]
            data, mapping = assemble(parts, root)
            text = data.decode("utf-8")
            for part, entry in zip(parts, mapping):
                self.assertEqual(text[entry["output_start"]:entry["output_end"]], part[2])
            self.assertEqual(text, "\u00e4lskar\n\ndig\n")

    def test_correction_requires_expected_source_and_unique_anchor(self):
        correction = {"correction_id": "test", "source_sha256": digest(b"raw"),
                      "before": "pJeg", "after": "\u201eJeg"}
        self.assertEqual(correct_page("pJeg elsker dig", b"raw", [correction]), "\u201eJeg elsker dig")
        for text, raw in [("pJeg elsker dig", b"changed"), ("Jeg", b"raw"), ("pJeg pJeg", b"raw")]:
            with self.assertRaises(ValueError):
                correct_page(text, raw, [correction])

    def test_idempotence_and_divergence_guard(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "derived.txt"
            stable_write(path, b"original")
            stable_write(path, b"original")
            with self.assertRaises(ValueError):
                stable_write(path, b"different")
            self.assertEqual(path.read_bytes(), b"original")


if __name__ == "__main__":
    unittest.main()
