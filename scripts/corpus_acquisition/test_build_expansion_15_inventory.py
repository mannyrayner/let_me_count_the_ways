import json
import os
import tempfile
import unittest
from pathlib import Path

from scripts.corpus_acquisition.build_expansion_15_inventory import (
    build_inventory,
    summary_markdown,
)


class BuildExpansionInventoryTests(unittest.TestCase):
    def test_builds_single_and_multipart_work_inventory(self):
        with tempfile.TemporaryDirectory() as temporary:
            previous = Path.cwd()
            os.chdir(temporary)
            try:
                Path("texts").mkdir()
                Path("provenance").mkdir()
                sources = []
                records = [
                    ("single", "Single", "single.txt", "a" * 64, None),
                    ("multi", "Trilogy: One", "one.txt", "b" * 64, "https://runeberg/1/"),
                    ("multi", "Trilogy: Two", "two.txt", "c" * 64, "https://runeberg/2/"),
                ]
                for index, (work, title, name, digest, volume_url) in enumerate(records):
                    local = Path("texts") / name
                    local.write_text(f"text {index}", encoding="utf-8")
                    record = {
                        "source_id": f"source-{index}", "work_id": work,
                        "title": title, "local_path": str(local), "sha256": digest,
                        "review_status": "approved_for_development_processing",
                    }
                    if volume_url:
                        record["volume_url"] = volume_url
                    provenance = Path("provenance") / f"{index}.json"
                    provenance.write_text(json.dumps(record), encoding="utf-8")
                    sources.append({"provenance": str(provenance)})
                Path("batch.json").write_text(json.dumps({"sources": sources}), encoding="utf-8")
                manifest = {
                    "status": "blocked", "successful_work_count": 0,
                    "target_work_count": 2, "blocking_reason": "network",
                    "works": [
                        {"work_id": "single", "title": "Single", "language": "en",
                         "source_type": "gutenberg", "source_identity": {"ebook_number": 1}},
                        {"work_id": "multi", "title": "Trilogy", "language": "no",
                         "source_type": "runeberg-range",
                         "source_identity": {"volume_url": "https://runeberg/multi/"}},
                    ],
                }
                Path("manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
                result = build_inventory(Path("batch.json"), Path("manifest.json"))
                self.assertEqual(result["status"], "acquired")
                self.assertEqual(result["successful_work_count"], 2)
                self.assertEqual(result["works"][0]["derived_sha256"], "a" * 64)
                self.assertEqual(len(result["works"][1]["constituent_parts"]), 2)
                summary = summary_markdown(result)
                self.assertIn("2/2 acquired", summary)
                self.assertIn("| Trilogy | Runeberg", summary)
            finally:
                os.chdir(previous)


if __name__ == "__main__":
    unittest.main()
