#!/usr/bin/env python3
"""Focused unit tests for reusable case-study selection and context helpers."""
import tempfile
import unittest
from pathlib import Path

from scripts.case_studies.common import matches_criterion, natural_window, page_ids

class CaseStudyHelpersTest(unittest.TestCase):
    def test_configurable_score_confidence_and_fit_criteria(self):
        case={"scores":{"P":2,"T":4,"E":0,"O":0},"confidence":.7,"ontology_fit":"strained"}
        self.assertTrue(matches_criterion(case,"P>=2"))
        self.assertTrue(matches_criterion(case,"confidence < 0.75"))
        self.assertTrue(matches_criterion(case,"ontology_fit != natural"))
        self.assertFalse(matches_criterion(case,"O>0"))

    def test_natural_window_preserves_verbatim_paragraphs(self):
        text="first paragraph\n\nbefore target after\n\nlast paragraph"
        target=text.index("target")
        start,end,context=natural_window(text,target,target+6,3,3)
        self.assertEqual(context,text[start:end])
        self.assertIn("target",context)
        self.assertNotIn("first paragraph",context)

    def test_page_map_overlap(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/"map.json"
            path.write_text('[{"url_index": 1, "url": "u1", "output_start": 0, "output_end": 10}, {"url_index": 2, "url": "u2", "output_start": 10, "output_end": 20}]')
            self.assertEqual([p["url_index"] for p in page_ids(path,9,11)],[1,2])

if __name__=="__main__": unittest.main()
