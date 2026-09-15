# Migrate the remaining multilingual-five works to the canonical corpus

This migration adds only *Die Leiden des jungen Werther* and *La Princesse de
Clèves* to the canonical corpus, completing the historical multilingual-five
batch. It copies the approved repository literary texts byte-for-byte with the
existing builder. It does not download or derive sources or run extraction,
annotation, review, case-study, or batch workflows.

The approved sources and their provenance records are:

- `data/raw/goethe-die-leiden-des-jungen-werther/gutenberg-2407-2408.txt`
  and `provenance/sources/gutenberg-2407-2408.json`;
- `data/raw/lafayette-la-princesse-de-cleves/gutenberg-18797.txt` and
  `provenance/sources/gutenberg-18797.json`.

The approved *Werther* text is assembled in order from Gutenberg ebooks 2407
and 2408, so its source type is `gutenberg_multi`. The approved *Princesse*
text is derived from one Gutenberg ebook, so its source type is
`gutenberg_single`. Run each block from the established Cygwin setup and stop
if any command fails.

## Build Werther

```bash
cd "$LMCW"
python scripts/corpus/build_canonical_work.py data/raw/goethe-die-leiden-des-jungen-werther/gutenberg-2407-2408.txt --work-id goethe-die-leiden-des-jungen-werther --title "Die Leiden des jungen Werther" --author "Johann Wolfgang von Goethe" --language de --source-type gutenberg_multi --source-reference provenance/sources/gutenberg-2407-2408.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved Gutenberg-derived literary text assembled in order from the two preserved HTML downloads; no acquisition, derivation, or correction was rerun."
```

## Build La Princesse de Clèves

```bash
cd "$LMCW"
python scripts/corpus/build_canonical_work.py data/raw/lafayette-la-princesse-de-cleves/gutenberg-18797.txt --work-id lafayette-la-princesse-de-cleves --title "La Princesse de Clèves" --author "Madame de La Fayette" --language fr --source-type gutenberg_single --source-reference provenance/sources/gutenberg-18797.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved single-file Gutenberg-derived literary text with its wrapper already removed; no acquisition, derivation, or correction was rerun."
```

## Confirm byte identity

Both successful comparisons are silent. Stop immediately if either reports a
difference.

```bash
cd "$LMCW"
cmp data/raw/goethe-die-leiden-des-jungen-werther/gutenberg-2407-2408.txt corpus/works/goethe-die-leiden-des-jungen-werther/canonical.txt
cmp data/raw/lafayette-la-princesse-de-cleves/gutenberg-18797.txt corpus/works/lafayette-la-princesse-de-cleves/canonical.txt
```

## Validate and regenerate the index

The validator must report `Canonical corpus valid: 11 work(s).`; it also checks
every manifest's recorded SHA-256 against its `canonical.txt`.

```bash
cd "$LMCW"
python scripts/corpus/validate_canonical_corpus.py corpus/works --write-index corpus/index.md
```

## Ask Manny to inspect the generated records

Manny should confirm each title, author, language, source type, source
reference, rights policy, and canonical SHA-256 before staging.

```bash
cd "$LMCW"
cat corpus/index.md
cat corpus/works/goethe-die-leiden-des-jungen-werther/work.json
cat corpus/works/lafayette-la-princesse-de-cleves/work.json
```

## Run focused checks

These checks make no model calls.

```bash
cd "$LMCW"
python -m pytest -q scripts/corpus/test_canonical_corpus.py
python scripts/docs/validate_runbook_index.py
git diff --check
git status --short
```

## Stage and commit

Stage only this migration's canonical outputs and documentation. Do not use
`git add .`.

```bash
cd "$LMCW"
git add corpus/index.md corpus/works/goethe-die-leiden-des-jungen-werther/ corpus/works/lafayette-la-princesse-de-cleves/ docs/howto/25_migrate_remaining_multilingual_five_to_canonical_corpus.md docs/howto/README.md
git diff --cached --check
git diff --cached --stat
git commit -m "Migrate remaining multilingual works to canonical corpus"
```

## Verify the commit

`git status --short` must print nothing.

```bash
cd "$LMCW"
git status --short
git log -1 --oneline
git show --stat --oneline HEAD
```

Stop here for Manny/ChatGPT review. The corpus now has exactly eleven works.
Do not migrate more works or begin the redesigned extraction pipeline.
