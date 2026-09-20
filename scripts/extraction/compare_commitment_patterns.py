#!/usr/bin/env python3
"""Compare v0.11/v0.12 spans across all available public canonical works."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.extraction.extract_canonical_corpus import PUBLIC_POLICIES, extract_candidates, resolve_canonical


def main() -> None:
    specs = [json.loads((ROOT / f"data/development/search_patterns_v0_{v}.json").read_text(encoding="utf-8"))
             for v in (11, 12)]
    selection = json.loads((ROOT / "data/acquisition/commitment_extension_5_v1/selection.json").read_text(encoding="utf-8"))
    extension = {work["work_id"] for work in selection["works"]}
    rows = []
    for path in sorted((ROOT / "corpus/works").glob("*/work.json")):
        manifest = json.loads(path.read_text(encoding="utf-8"))
        row = {"work_id": manifest["work_id"],
               "group": "extension" if manifest["work_id"] in extension else "baseline",
               "canonical_sha256": manifest["canonical_sha256"]}
        source, _ = resolve_canonical(path, manifest)
        rights = manifest["rights"]
        if rights["public_render_policy"] not in PUBLIC_POLICIES or not rights["analysis_allowed"]:
            row["status"] = "not_public_context_comparison"
        elif not source.is_file():
            row["status"] = "source_unavailable"
        else:
            if hashlib.sha256(source.read_bytes()).hexdigest() != manifest["canonical_sha256"]:
                raise ValueError(f"canonical hash mismatch: {manifest['work_id']}")
            text = source.read_text(encoding="utf-8")
            inventories = [extract_candidates(text, manifest, spec["schema_version"],
                           spec["languages"][manifest["language"]]["patterns"], 150) for spec in specs]
            old, new = [{(r["start"], r["end"], r["match"]): r for r in records}
                        for records in inventories]
            removed = [old[key] for key in sorted(old.keys() - new.keys())]
            if removed:
                raise ValueError(f"additive extension unexpectedly removed or changed spans in {manifest['work_id']}")
            row.update(status="compared", v0_11_count=len(old), v0_12_count=len(new),
                       unchanged_span_count=len(old.keys() & new.keys()), removed=removed,
                       added=[new[key] for key in sorted(new.keys() - old.keys())])
        rows.append(row)
    totals = {}
    for group in ("baseline", "extension"):
        subset = [r for r in rows if r["group"] == group and r["status"] == "compared"]
        totals[group] = {"works_compared": len(subset),
                         "v0_11_count": sum(r["v0_11_count"] for r in subset),
                         "v0_12_count": sum(r["v0_12_count"] for r in subset),
                         "added": sum(len(r["added"]) for r in subset), "removed": 0}
    report = {"comparison": "v0.11 versus v0.12 on identical canonical texts",
              "identity": "canonical SHA-256, Unicode start/end offsets, and exact matched text; occurrence IDs include the pattern version and therefore differ",
              "scope": "All available canonical works whose repository policy permits public context. Candidate comparison only; frozen annotations are not altered.",
              "totals": totals, "works": rows}
    output = ROOT / "results/extraction_audit/commitment_extension_5_v0_12"
    output.mkdir(parents=True, exist_ok=True)
    (output / "pattern_comparison.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Pattern v0.12 coverage comparison", "", report["scope"], "", report["identity"], "",
             "| Group | Works compared | v0.11 candidates | v0.12 candidates | Added | Removed |",
             "| --- | ---: | ---: | ---: | ---: | ---: |"]
    for group, total in totals.items():
        lines.append(f"| {group} | {total['works_compared']} | {total['v0_11_count']} | {total['v0_12_count']} | {total['added']} | 0 |")
    lines += ["", "## Added matches", "", "These are extraction candidates, not KEEP decisions or P scores.", ""]
    for row in rows:
        for record in row.get("added", []):
            lines.append(f"- `{record['occurrence_id']}` ({row['group']}): {record['match']!r}, `{record['pattern_id']}`, offsets {record['start']}–{record['end']}.")
    (output / "pattern_comparison.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(totals, indent=2))


if __name__ == "__main__":
    main()
