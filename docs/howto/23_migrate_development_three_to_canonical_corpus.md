# Migrate the original development three to the canonical corpus

This migration adds only *Jane Eyre*, *Little Women*, and *Madame Bovary* to
the canonical corpus. It reuses the approved repository texts and the existing
canonical builder; it does not download sources or run extraction, annotation,
review, case-study, or batch workflows.

Run each command block from the repository root under the established Cygwin
setup. Stop if any command fails or an identity check reports a difference.

## Build Jane Eyre

```bash
cd "$LMCW"
python scripts/corpus/build_canonical_work.py data/raw/bronte-jane-eyre/gutenberg-1260.txt --work-id bronte-jane-eyre --title "Jane Eyre" --author "Charlotte Brontë" --language en --source-type gutenberg_single --source-reference provenance/sources/gutenberg-1260.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved wrapper-free Gutenberg literary text."
```

## Build Little Women

```bash
cd "$LMCW"
python scripts/corpus/build_canonical_work.py data/raw/alcott-little-women/gutenberg-514.txt --work-id alcott-little-women --title "Little Women" --author "Louisa May Alcott" --language en --source-type gutenberg_single --source-reference provenance/sources/gutenberg-514.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved wrapper-free Gutenberg literary text."
```

## Build Madame Bovary

```bash
cd "$LMCW"
python scripts/corpus/build_canonical_work.py data/raw/flaubert-madame-bovary/gutenberg-14155.txt --work-id flaubert-madame-bovary --title "Madame Bovary" --author "Gustave Flaubert" --language fr --source-type gutenberg_single --source-reference provenance/sources/gutenberg-14155.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved wrapper-free Gutenberg literary text."
```

## Confirm byte identity

Each successful `cmp` is silent.

```bash
cd "$LMCW"
cmp data/raw/bronte-jane-eyre/gutenberg-1260.txt corpus/works/bronte-jane-eyre/canonical.txt
cmp data/raw/alcott-little-women/gutenberg-514.txt corpus/works/alcott-little-women/canonical.txt
cmp data/raw/flaubert-madame-bovary/gutenberg-14155.txt corpus/works/flaubert-madame-bovary/canonical.txt
```

## Validate and regenerate the index

The validator must report `Canonical corpus valid: 6 work(s).`; it also checks
each manifest's recorded SHA-256 against its `canonical.txt`.

```bash
cd "$LMCW"
python scripts/corpus/validate_canonical_corpus.py corpus/works --write-index corpus/index.md
```

## Inspect the generated records

Inspect the index and all three manifests. Confirm the titles, authors,
languages, source references, rights policies, and SHA-256 values before
staging.

```bash
cd "$LMCW"
cat corpus/index.md
cat corpus/works/bronte-jane-eyre/work.json
cat corpus/works/alcott-little-women/work.json
cat corpus/works/flaubert-madame-bovary/work.json
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
git add .gitattributes corpus/index.md corpus/works/bronte-jane-eyre/ corpus/works/alcott-little-women/ corpus/works/flaubert-madame-bovary/ docs/howto/23_migrate_development_three_to_canonical_corpus.md docs/howto/README.md
git diff --cached --check
git diff --cached --stat
git commit -m "Migrate development three to canonical corpus"
```

## Verify the commit

`git status --short` must print nothing.

```bash
cd "$LMCW"
git status --short
git log -1 --oneline
git show --stat --oneline HEAD
```

Stop here for review. Do not migrate any further works or run downstream
research workflows.
