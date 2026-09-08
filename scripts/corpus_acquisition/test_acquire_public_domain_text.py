import tempfile
import unittest
from pathlib import Path

from scripts.corpus_acquisition.acquire_public_domain_text import (
    acquire_gutenberg, acquire_runeberg, page_urls, runeberg_html_to_text,
    sha256, trim_gutenberg,
)


def runeberg_page(content):
    return f"""<!doctype html><html><body>
<form><table><tr><td>Project Runeberg</td><td>Previous Next Facsimile</td></tr></table></form>
{content}
<hr noshade><tt>Project Runeberg Previous Next footer</tt>
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
            runeberg_page("<h2>Victoria</h2><p>Jeg elsker Dem — blå øyne.</p>")
        )
        self.assertEqual(extracted, "Victoria\n\nJeg elsker Dem — blå øyne.\n")
        self.assertNotIn("Previous", extracted)
        self.assertNotIn("Runeberg", extracted)

    def test_runeberg_parser_rejects_empty_or_malformed_pages(self):
        with self.assertRaisesRegex(ValueError, "empty"):
            runeberg_html_to_text(runeberg_page(""))
        with self.assertRaisesRegex(ValueError, "structure"):
            runeberg_html_to_text("<html><body><p>orphan text</p></body></html>")

    def test_runeberg_range_is_ordered_mapped_and_reproducible(self):
        base = "https://runeberg.test/ham/2"
        urls = page_urls(base, 401, 402)
        contents = {urls[0]: runeberg_page("<p>Første blå</p>"),
                    urls[1]: runeberg_page("<p>Andre øyeblikk</p>")}
        raw = self.root / "pages"
        first_output, first_map = self.root / "pan.txt", self.root / "map.json"
        result = acquire_runeberg(base, 401, 402, raw, first_output, first_map,
                                  331, 332, downloader=self.downloader(contents))
        self.assertEqual(first_output.read_text(encoding="utf-8"),
                         "Første blå\n\nAndre øyeblikk\n")
        records = __import__("json").loads(first_map.read_text(encoding="utf-8"))
        assembled = first_output.read_text(encoding="utf-8")
        self.assertEqual([r["url_index"] for r in records], [401, 402])
        self.assertEqual([assembled[r["output_start"]:r["output_end"]] for r in records],
                         ["Første blå", "Andre øyeblikk"])
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
