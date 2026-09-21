"""Source-parsing risks: page-boundary words, notes, encodings and source endings."""
import unittest
import xml.etree.ElementTree as ET
from scripts.corpus_acquisition.prepare_context_extension import literary_inline, tolstoy_volume, ROOT, prince_text

class SourceTests(unittest.TestCase):
    def test_page_words_survive_but_numbers_and_note_pointers_do_not(self):
        node=ET.fromstring('<p>Я люблю <span class="opnumber">123</span><span class="opdelimiter">тебя</span><a type="note">[4]</a>!</p>')
        self.assertEqual('Я люблю тебя!',literary_inline(node))
    def test_main_tolstoy_chapter_counts_and_french_are_preserved(self):
        expected={9:65,10:97,11:96,12:102}
        for volume,n in expected.items():
            raw=(ROOT/f'data/raw/tolstoy-war-and-peace/volume-{volume:02d}.html').read_bytes()
            parts=tolstoy_volume(raw,volume)
            import re
            # The edition sometimes uses visually similar Cyrillic Х and І.
            self.assertEqual(n,sum(bool(re.fullmatch(r'[IVXLCХІ]+\.',text.split('\n')[0])) for _,text in parts))
            self.assertTrue(all(identifier.startswith('h000009001' if volume==9 else 'h000007001') for identifier,_ in parts))
        self.assertIn('Je vous aime!',(ROOT/'corpus/works/tolstoy-war-and-peace/canonical.txt').read_text())
    def test_prince_has_all_chapters_and_final_paragraph(self):
        path=ROOT/'data/local_candidate_sources/saint-exupery-le-petit-prince/source.html'
        if not path.exists():self.skipTest('Local source has not been acquired')
        text=prince_text(path.read_bytes())
        self.assertIn('CHAPITRE XXVII',text);self.assertTrue(text.rstrip().endswith("écrivez-moi vite qu'il est revenu..."))
        self.assertNotIn('Project Gutenberg',text)

if __name__=='__main__':unittest.main()
