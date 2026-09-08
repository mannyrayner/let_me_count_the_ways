import tempfile
import unittest
from pathlib import Path

from scripts.corpus_acquisition.acquire_public_domain_text import (
    acquire_gutenberg, acquire_runeberg, extract_runeberg_ocr, page_urls, runeberg_html_to_text,
    sha256, trim_gutenberg,
)


def runeberg_page(content):
    return f"""<!doctype html><html><body>
<form><table><tr><td>Project Runeberg</td><td>Previous Next Facsimile</td></tr></table></form>
<div>Full resolution (JPEG) — On this page / på denna sida — Victoria</div>
<hr noshade>
<p>Below is the raw OCR text. This page has never been proofread.</p>
<!-- mode=normal -->
{content}
<!-- NEWIMAGE2 --><!-- #### -->
<tt>Project Runeberg Previous Next footer</tt>
</body></html>"""


class AcquisitionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)

    def tearDown(self):
        self.temporary.cleanup()

    @staticmethod
    def downloader(contents, reused=False):
        def download(url, destination):
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(contents[url], encoding="utf-8")
            return not reused
        return download

    def test_gutenberg_preserves_download_and_trims_only_explicit_markers(self):
        url = "https://example.test/book.txt"
        raw, output = self.root / "raw.txt", self.root / "book.txt"
        result = acquire_gutenberg(
            url, raw, output, self.downloader({url: "front\n*** START OF THE PROJECT GUTENBERG EBOOK X ***\nBody é.\n*** END OF THE PROJECT GUTENBERG EBOOK X ***\nback"}),
        )
        self.assertEqual(output.read_text(encoding="utf-8"), "Body é.\n")
        self.assertIn("front", raw.read_text(encoding="utf-8"))
        self.assertEqual(result["download_url"], url)

    def test_gutenberg_rejects_missing_markers(self):
        with self.assertRaises(ValueError):
            trim_gutenberg("only literary-looking text")

    def test_runeberg_parser_retains_ocr_unicode_and_excludes_chrome(self):
        extracted = runeberg_html_to_text(
            runeberg_page("<h2>Victoria</h2><p>Jeg elsker Dem — blå øyne, og ordene "
                          "blir stående urørt i den elektroniske kilden.</p>")
        )
        self.assertIn("Jeg elsker Dem — blå øyne", extracted)
        self.assertNotIn("Previous", extracted)
        self.assertNotIn("Runeberg", extracted)

    def test_runeberg_parser_excludes_scanned_page_link_chrome(self):
        source = """<html><body><div>Project Runeberg</div>
<div>Full resolution (JPEG); On this page / på denna sida; Victoria (1898)</div>
<hr noshade><p>Below is the raw OCR text.</p>
<p>This page has never been proofread. Proofread the page now!</p>
<!-- mode=normal -->
Gi<br><br>Pause. Victoria ytrer hen for sig:<br><br>Hvordan ser hun ut mon?<br>
<br>Å Gud bevare dig, hun er vakrere end noget menneske på jorden.<br>
<!-- NEWIMAGE2 --><!-- #### --><div>next page; Project Runeberg</div></body></html>"""
        self.assertEqual(
            runeberg_html_to_text(source),
            "Gi\n\nPause. Victoria ytrer hen for sig:\n\nHvordan ser hun ut mon?\n\n"
            "Å Gud bevare dig, hun er vakrere end noget menneske på jorden.\n",
        )
        extracted = runeberg_html_to_text(source)
        self.assertIn("Pause. Victoria ytrer hen for sig:", extracted)
        self.assertNotIn("On this page / på denna sida", extracted)
        self.assertNotIn("Project Runeberg", extracted)

    def test_runeberg_parser_rejects_navigation_only_page(self):
        source = """<html><body><!-- mode=normal -->
<!-- NEWIMAGE2 --></body></html>"""
        with self.assertRaisesRegex(ValueError, "empty"):
            runeberg_html_to_text(source)

    def test_runeberg_parser_rejects_empty_or_malformed_pages(self):
        with self.assertRaisesRegex(ValueError, "empty"):
            runeberg_html_to_text(runeberg_page(""))
        with self.assertRaisesRegex(ValueError, "start marker"):
            runeberg_html_to_text("<html><body><p>orphan text</p></body></html>")

    def test_runeberg_parser_rejects_missing_reversed_and_ambiguous_markers(self):
        with self.assertRaisesRegex(ValueError, "end marker not found"):
            runeberg_html_to_text("<!-- mode=normal --><p>Literary OCR remains here.</p>")
        with self.assertRaisesRegex(ValueError, "before start"):
            runeberg_html_to_text("<!-- NEWIMAGE2 --><!-- mode=normal --><p>OCR</p>")
        with self.assertRaisesRegex(ValueError, "ambiguous.*start"):
            runeberg_html_to_text(
                "<!-- mode=normal --><p>OCR</p><!-- mode=normal --><!-- NEWIMAGE2 -->"
            )
        with self.assertRaisesRegex(ValueError, "ambiguous.*end"):
            runeberg_html_to_text(
                "<!-- mode=normal --><p>OCR text is deliberately long enough to pass "
                "the normal sanity validation here.</p><!-- NEWIMAGE2 --><!-- NEWIMAGE2 -->"
            )

    def test_runeberg_parser_supports_and_reports_fallback_marker(self):
        source = ("<!-- mode=normal --><p>This sufficiently substantial literary OCR "
                  "fragment remains exactly present for deterministic fallback testing.</p>"
                  "<!-- #### -->")
        text, marker = extract_runeberg_ocr(source)
        self.assertIn("substantial literary OCR", text)
        self.assertEqual(marker, "####")

    def test_runeberg_parser_rejects_short_and_forbidden_content(self):
        with self.assertRaisesRegex(ValueError, "too short"):
            runeberg_html_to_text("<!-- mode=normal -->Victoria I<!-- NEWIMAGE2 -->")
        with self.assertRaisesRegex(ValueError, "forbidden navigation"):
            runeberg_html_to_text(
                "<!-- mode=normal --><p>Project Runeberg navigation accidentally "
                "entered this otherwise sufficiently long OCR fragment.</p><!-- NEWIMAGE2 -->"
            )

    def test_runeberg_range_is_ordered_mapped_and_reproducible(self):
        base = "https://runeberg.test/ham/2"
        urls = page_urls(base, 401, 402)
        contents = {
            urls[0]: runeberg_page("<p>Første blå side inneholder nok litterære ord til "
                                    "å passere den konservative kvalitetskontrollen.</p>"),
            urls[1]: runeberg_page("<p>Andre øyeblikk følger i riktig orden og beholder "
                                    "hele den urettede norske OCR-teksten.</p>"),
        }
        raw = self.root / "pages"
        first_output, first_map = self.root / "pan.txt", self.root / "map.json"
        result = acquire_runeberg(base, 401, 402, raw, first_output, first_map,
                                  331, 332, downloader=self.downloader(contents))
        self.assertEqual(first_output.read_text(encoding="utf-8"),
                         "Første blå side inneholder nok litterære ord til å passere den "
                         "konservative kvalitetskontrollen.\n\nAndre øyeblikk følger i "
                         "riktig orden og beholder hele den urettede norske OCR-teksten.\n")
        records = __import__("json").loads(first_map.read_text(encoding="utf-8"))
        assembled = first_output.read_text(encoding="utf-8")
        self.assertEqual([r["url_index"] for r in records], [401, 402])
        self.assertEqual([r["ocr_end_marker"] for r in records], ["NEWIMAGE2", "NEWIMAGE2"])
        self.assertEqual(result["fallback_end_marker_url_indices"], [])
        self.assertEqual(result["allowed_short_url_indices"], [])
        self.assertEqual([assembled[r["output_start"]:r["output_end"]] for r in records],
                         ["Første blå side inneholder nok litterære ord til å passere den "
                          "konservative kvalitetskontrollen.",
                          "Andre øyeblikk følger i riktig orden og beholder hele den "
                          "urettede norske OCR-teksten."])
        self.assertEqual(result["printed_page_range"], [331, 332])
        self.assertEqual(result["runeberg_url_index_range"], [401, 402])

        second_output, second_map = self.root / "pan-2.txt", self.root / "map-2.json"
        rerun = acquire_runeberg(base, 401, 402, raw, second_output, second_map,
                                 331, 332, downloader=self.downloader(contents, reused=True))
        self.assertEqual(rerun["pages_downloaded"], 0)
        self.assertEqual(sha256(first_output), sha256(second_output))
        self.assertEqual(first_map.read_text(encoding="utf-8"),
                         second_map.read_text(encoding="utf-8"))

    def test_runeberg_rejects_unexpected_or_missing_page(self):
        base = "https://runeberg.test/work/"
        urls = page_urls(base, 1, 2)
        raw = self.root / "pages"
        raw.mkdir()
        (raw / "0003.html").write_text("unexpected", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "unexpected"):
            acquire_runeberg(base, 1, 2, raw, self.root / "out.txt",
                             self.root / "map.json",
                             downloader=self.downloader({u: runeberg_page(f"<p>{u}</p>") for u in urls}))

    def test_runeberg_refuses_output_overwrite(self):
        output = self.root / "existing.txt"
        output.write_text("keep", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            acquire_runeberg("https://example.test/v", 1, 1, self.root / "pages",
                             output, self.root / "map.json", downloader=self.downloader({}))


if __name__ == "__main__":
    unittest.main()
