import unittest

from scripts.corpus_acquisition.audit_runeberg_prefixes import page_prefix


class RunebergPrefixAuditTests(unittest.TestCase):
    def test_classifies_supported_prefixes(self):
        marker = "<!-- mode=normal -->"
        end = "<!-- NEWIMAGE2 -->"
        self.assertEqual(page_prefix(marker + "92<br>text" + end)[0], "NUMERIC_PAGE_FIELD")
        self.assertEqual(page_prefix(marker + " <br>text" + end)[0], "EMPTY")
        self.assertEqual(page_prefix(marker + "I<br>text" + end)[0], "PRESERVED_TEXT")
        self.assertEqual(page_prefix(marker + "literary text<br>more" + end)[0], "PRESERVED_TEXT")

    def test_reports_proofread_and_malformed_pages(self):
        self.assertEqual(page_prefix("<html>proofread</html>")[0], "NOT_RAW_OCR")
        self.assertEqual(page_prefix("<!-- mode=normal -->unbounded")[0], "AMBIGUOUS")
