import json
import os
import tempfile
import unittest
from pathlib import Path

from scripts.corpus_acquisition.finalize_acquisition_provenance import (
    file_sha256,
    finalize_batch,
)


class FinalizeAcquisitionProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.previous = Path.cwd()
        os.chdir(self.root)

    def tearDown(self):
        os.chdir(self.previous)
        self.temporary.cleanup()

    def write_json(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def test_finalizes_single_download_and_page_range(self):
        raw = Path("data/raw/book/source.txt")
        literary = Path("data/raw/book/book.txt")
        raw.parent.mkdir(parents=True)
        raw.write_text("raw wrapper", encoding="utf-8")
        literary.write_text("literary text", encoding="utf-8")
        os.utime(raw, (1_700_000_000, 1_700_000_000))
        gutenberg = Path("provenance/gutenberg.json")
        self.write_json(gutenberg, {
            "source_id": "gutenberg-test", "local_path": str(literary),
            "download_path": str(raw), "rights_note": "Reviewed public domain",
            "review_status": "acquisition_pending",
        })

        page_dir = Path("data/raw/pages/source-pages")
        page_dir.mkdir(parents=True)
        pages = []
        for index in (1, 2):
            path = page_dir / f"{index:04d}.html"
            path.write_text(f"raw page {index}", encoding="utf-8")
            pages.append({"url_index": index, "raw_path": str(path)})
        runeberg_text = Path("data/raw/pages/runeberg.txt")
        runeberg_text.write_text("assembled OCR", encoding="utf-8")
        page_map = Path("data/raw/pages/page-map.json")
        self.write_json(page_map, pages)
        self.write_json(Path("data/raw/pages/acquisition-metadata.json"), {
            "pages_requested": 2, "pages_downloaded": 2, "pages_nonempty": 2,
            "assembled_character_count": 13, "assembled_word_count": 2,
            "sha256": file_sha256(runeberg_text),
        })
        runeberg = Path("provenance/runeberg.json")
        self.write_json(runeberg, {
            "source_id": "runeberg-test", "local_path": str(runeberg_text),
            "page_map_path": str(page_map), "rights_note": "Reviewed public domain",
            "review_status": "acquisition_pending",
        })
        batch = Path("batch.json")
        self.write_json(batch, {"sources": [
            {"provenance": str(gutenberg)}, {"provenance": str(runeberg)},
        ]})

        finalize_batch(batch, "2026-09-08", approve=True)

        first = json.loads(gutenberg.read_text(encoding="utf-8"))
        self.assertEqual(first["sha256"], file_sha256(literary))
        self.assertEqual(first["download_sha256"], file_sha256(raw))
        self.assertEqual(first["retrieved_at"], "2023-11-14T22:13:20Z")
        self.assertEqual(first["reviewed_on"], "2026-09-08")
        self.assertEqual(first["review_status"], "approved_for_development_processing")
        second = json.loads(runeberg.read_text(encoding="utf-8"))
        self.assertEqual(second["download_paths"], [str(page_dir / "0001.html"),
                                                     str(page_dir / "0002.html")])
        self.assertEqual(set(second["download_sha256"]), {"0001.html", "0002.html"})
        self.assertEqual(second["acquisition_summary"]["pages_requested"], 2)

    def test_rejects_pending_rights_before_writing_any_record(self):
        source = Path("source.txt")
        source.write_text("text", encoding="utf-8")
        raw = Path("raw.txt")
        raw.write_text("raw", encoding="utf-8")
        provenance = Path("provenance.json")
        original = {"source_id": "pending", "local_path": str(source),
                    "download_path": str(raw), "rights_note": "PENDING REVIEW"}
        self.write_json(provenance, original)
        batch = Path("batch.json")
        self.write_json(batch, {"sources": [{"provenance": str(provenance)}]})

        with self.assertRaisesRegex(ValueError, "pending rights_note"):
            finalize_batch(batch, "2026-09-08", approve=True)
        self.assertEqual(json.loads(provenance.read_text()), original)


if __name__ == "__main__":
    unittest.main()
