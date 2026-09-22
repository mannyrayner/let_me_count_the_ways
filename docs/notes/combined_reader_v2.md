# Combined reader v2 and Le petit prince publication

The default reader now combines the 252 earlier annotations with the 40 completed
public annotations from the context extension: 36 War and Peace and four King Lear.
It contains 292 records from 37 searched works in eight languages. The historical
paper statistics and collection_v1 configuration remain frozen.

Manny Rayner authorized inclusion of Le petit prince on 2026-09-22, citing its
widespread availability and the project's earlier openly published LARA editions.
The exact source hash, scope and basis are recorded in
`provenance/publication/saint-exupery-le-petit-prince-2026-09-22.json`.
This is a project publication decision, not a claim of worldwide public-domain
status or a grant from a rights holder.

## Complete the combined reader locally

After installing this patch, from the repository root run:

```bash
python scripts/reader/include_petit_prince.py &&
python scripts/reader/build_reader.py --check
cygstart docs/reader/index.html
```

The import requires the completed local Prince review, translations and annotations
from run_context_extension.py, plus its original canonical source and extraction.
It checks completion, work identity, source hash, exact source offsets, saved scores,
and the recorded publication decision before export. It makes no API calls.
With one retained Prince annotation, the resulting reader has 293 records from
38 searched works in eight languages.

The importer copies only the Prince stages to
`results/publication/petit_prince_v1/` and adds that run to
`data/reader/collection_v2.json`. It preserves source and saved request bytes,
including the earlier publication metadata, and displays the later publication
decision separately. Original local files remain intact. Existing acquisition and
annotation commands continue to use their original paths; no reannotation is needed.
Other private works and context-pilot outputs are not exported.

Source-record links for the copied Prince run use main until a later revision pins
its publication commit. Earlier runs use the already published data commit.
The export records file hashes with newline normalization for cross-platform JSON;
the canonical text's byte hash is separately preserved by .gitattributes.

## Check in after import

```bash
git add -- .gitattributes scripts/reader data/reader docs/reader \
  docs/notes/combined_reader_v2.md provenance/publication \
  results/publication/petit_prince_v1
git diff --cached --stat
git commit -m "Combine all saved annotations and include Le petit prince"
git push origin HEAD
```

No force-add or broad change to ignore rules is required. Keep the downloaded patch
and archive out of the commit. After pushing, all three new works' saved annotation
records will be accessible through the same reader.

Validation performed when preparing the patch: 292-record build and exact rebuild
check; historical reader regression tests; synthetic-fixture tests of the import,
repeat import, original-request preservation, hash-scoped decision, and refusal to
overwrite divergent exports. The real Prince annotation remains on Manny's machine,
so its actual import must be completed there.
