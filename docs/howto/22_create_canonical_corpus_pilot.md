# Create the canonical corpus pilot

This pilot creates a stable input layer for three approved works. **Acquisition is
source-specific; downstream research should operate on canonical text.** The
canonical layer copies approved UTF-8 literary text byte-for-byte, records its
SHA-256 and source references, and does not download, trim, modernize, correct
OCR, extract passages, annotate, or alter historical IDs and results.

Run every command from the repository root (under the established Cygwin setup):

```bash
cd "$LMCW"
python scripts/corpus/build_canonical_work.py data/raw/wharton-age-of-innocence/gutenberg-541.txt --work-id wharton-age-of-innocence --title "The Age of Innocence" --author "Edith Wharton" --language en --source-type gutenberg_single --source-reference provenance/sources/gutenberg-541.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved wrapper-free Gutenberg literary text."
python scripts/corpus/build_canonical_work.py data/raw/hamsun-victoria/runeberg-hamsun-victoria.txt --work-id hamsun-victoria --title "Victoria" --author "Knut Hamsun" --language no --source-type runeberg --source-reference provenance/sources/runeberg-hamsun-victoria.json --source-reference data/raw/hamsun-victoria/page-map.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved uncorrected Runeberg OCR; no acquisition or OCR correction was rerun."
python scripts/corpus/build_canonical_work.py data/derived/cofield-nikkis-touch/lulu-cofield-nikkis-touch-ebook.txt --work-id cofield-nikkis-touch --title "Nikki's Touch" --author "Ania Cofield" --language en --source-type local_permissioned --source-reference provenance/sources/lulu-cofield-nikkis-touch-ebook.json --public-render-policy PERMISSIONED_CONTEXT_OK --notes "Byte-for-byte copy of the approved deterministic EPUB-to-text derivation under the recorded CC BY basis."
```

These commands implement only `existing acquisition/derivation → canonical
work`. Later stages (`canonical work → extraction → review → contextualization
→ annotation`) remain out of scope.

Validate the manifests and texts, regenerate the human-readable index, and run
the focused checks:

```bash
python scripts/corpus/validate_canonical_corpus.py corpus/works --write-index corpus/index.md
python -m pytest -q scripts/corpus/test_canonical_corpus.py
python scripts/docs/validate_runbook_index.py
git diff --check
git status --short
```

Inspect `corpus/index.md` and the three `corpus/works/*/work.json` manifests.
Each source reference should lead back to the existing acquisition record; the
manifest intentionally does not duplicate that detailed provenance.

After review, stage only the pilot paths explicitly:

```bash
git add corpus/index.md corpus/work.schema.json corpus/works/cofield-nikkis-touch/canonical.txt corpus/works/cofield-nikkis-touch/work.json corpus/works/hamsun-victoria/canonical.txt corpus/works/hamsun-victoria/work.json corpus/works/wharton-age-of-innocence/canonical.txt corpus/works/wharton-age-of-innocence/work.json docs/howto/22_create_canonical_corpus_pilot.md docs/howto/README.md scripts/corpus/__init__.py scripts/corpus/build_canonical_work.py scripts/corpus/test_canonical_corpus.py scripts/corpus/validate_canonical_corpus.py scripts/docs/test_howto_inventory.py
git commit -m "Add canonical corpus pilot"
```

Stop here for review; do not migrate further works or run downstream research.
