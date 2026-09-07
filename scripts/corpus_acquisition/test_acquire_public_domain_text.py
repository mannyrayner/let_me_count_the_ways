import tempfile
import unittest
from pathlib import Path

from scripts.corpus_acquisition.acquire_public_domain_text import (
    acquire_gutenberg, acquire_runeberg, page_urls, trim_gutenberg,
)


class AcquisitionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)

    def tearDown(self):
        self.temporary.cleanup()

    @staticmethod
    def downloader(contents):
        def download(url, destination):
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(contents[url], encoding="utf-8")
        return download

    def test_gutenberg_preserves_download_and_trims_only_explicit_markers(self):
        url = "https://example.test/book.txt"
        raw, output = self.root / "raw.txt", self.root / "book.txt"
        result = acquire_gutenberg(
            url, raw, output, self.downloader({url: "front\n*** START OF THE PROJECT GUTENBERG EBOOK X ***\nBody é.\n*** END OF THE PROJECT GUTENBERG EBOOK X ***\nback"}),
        )
        self.assertEqual(output.read_text(), "Body é.\n")
        self.assertIn("front", raw.read_text())
        self.assertEqual(len(result["sha256"]), 64)

    def test_gutenberg_rejects_missing_markers(self):
        with self.assertRaises(ValueError):
            trim_gutenberg("only literary-looking text")

    def test_runeberg_range_is_ordered_preserved_and_hashed(self):
        base = "https://runeberg.test/ham/2"
        urls = page_urls(base, 401, 402)
        result = acquire_runeberg(
            base, 401, 402, 331, 332, self.root / "pages", self.root / "pan.txt",
            self.downloader({urls[0]: "<p>First</p>", urls[1]: "<p>Second</p>"}),
        )
        self.assertEqual((self.root / "pan.txt").read_text(), "First\n\nSecond\n")
        self.assertEqual(result["printed_page_range"], [331, 332])
        self.assertEqual(result["url_index_range"], [401, 402])
        self.assertEqual(len(result["download_sha256"]), 2)

    def test_runeberg_refuses_overwrite(self):
        output = self.root / "existing.txt"
        output.write_text("keep")
        with self.assertRaises(FileExistsError):
            acquire_runeberg("https://example.test/v", 1, 1, 1, 1,
                              self.root / "pages", output, self.downloader({}))


if __name__ == "__main__":
    unittest.main()
