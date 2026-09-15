# Migrate three multilingual works to the canonical corpus

This migration adds only *Et dukkehjem*, *Cyrano de Bergerac*, and *Fröken
Julie* to the canonical corpus. It copies the approved repository literary
texts byte-for-byte with the existing builder. It does not download or derive
sources, rerun OCR, or run extraction, annotation, review, case-study, or batch
workflows.

The approved sources and their provenance records are:

- `data/raw/ibsen-et-dukkehjem/runeberg-dukkhjem.txt` and
  `provenance/sources/runeberg-dukkhjem.json`;
- `data/raw/rostand-cyrano-de-bergerac/gutenberg-1256.txt` and
  `provenance/sources/gutenberg-1256.json`;
- `data/raw/strindberg-froken-julie/runeberg-frkjulie.txt` and
  `provenance/sources/runeberg-frkjulie.json`.

The Runeberg texts are already derived, page-assembled literary texts. Their
provenance records identify the preserved source pages and derivation. No
separate page maps exist for these historical representations. The approved
*Cyrano* text comes from one Gutenberg file and retains its Gutenberg wrapper,
so its source type is `gutenberg_single`.

Run each command block from the established Cygwin setup. Stop if any command
fails or an identity check reports a difference.

## Build Ibsen

```bash
cd "$LMCW"
python scripts/corpus/build_canonical_work.py data/raw/ibsen-et-dukkehjem/runeberg-dukkhjem.txt --work-id ibsen-et-dukkehjem --title "Et dukkehjem" --author "Henrik Ibsen" --language no --source-type runeberg --source-reference provenance/sources/runeberg-dukkhjem.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved Runeberg-derived literary text assembled from the preserved HTML pages; no acquisition, derivation, or correction was rerun."
```

## Build Rostand

```bash
cd "$LMCW"
python scripts/corpus/build_canonical_work.py data/raw/rostand-cyrano-de-bergerac/gutenberg-1256.txt --work-id rostand-cyrano-de-bergerac --title "Cyrano de Bergerac" --author "Edmond Rostand" --language fr --source-type gutenberg_single --source-reference provenance/sources/gutenberg-1256.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved single-file Gutenberg-derived literary text with its wrapper retained."
```

## Build Strindberg

```bash
cd "$LMCW"
python scripts/corpus/build_canonical_work.py data/raw/strindberg-froken-julie/runeberg-frkjulie.txt --work-id strindberg-froken-julie --title "Fröken Julie" --author "August Strindberg" --language sv --source-type runeberg --source-reference provenance/sources/runeberg-frkjulie.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved Runeberg-derived literary text assembled from the preserved HTML pages; no acquisition, derivation, or correction was rerun."
```

## Confirm byte identity

Each successful `cmp` is silent. Stop immediately if any comparison fails.

```bash
cd "$LMCW"
cmp data/raw/ibsen-et-dukkehjem/runeberg-dukkhjem.txt corpus/works/ibsen-et-dukkehjem/canonical.txt
cmp data/raw/rostand-cyrano-de-bergerac/gutenberg-1256.txt corpus/works/rostand-cyrano-de-bergerac/canonical.txt
cmp data/raw/strindberg-froken-julie/runeberg-frkjulie.txt corpus/works/strindberg-froken-julie/canonical.txt
```

## Validate and regenerate the index

The validator must report `Canonical corpus valid: 9 work(s).`; it also checks
every manifest's recorded SHA-256 against its `canonical.txt`.

```bash
cd "$LMCW"
python scripts/corpus/validate_canonical_corpus.py corpus/works --write-index corpus/index.md
```

## Ask Manny to inspect the generated records

Manny should inspect the index and all three manifests. Confirm each author,
title, language, source type, source references, rights policy, and canonical
SHA-256 before staging.

```bash
cd "$LMCW"
cat corpus/index.md
cat corpus/works/ibsen-et-dukkehjem/work.json
cat corpus/works/rostand-cyrano-de-bergerac/work.json
cat corpus/works/strindberg-froken-julie/work.json
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
git add corpus/index.md corpus/works/ibsen-et-dukkehjem/ corpus/works/rostand-cyrano-de-bergerac/ corpus/works/strindberg-froken-julie/ docs/howto/24_migrate_multilingual_three_to_canonical_corpus.md docs/howto/README.md
git diff --cached --check
git diff --cached --stat
git commit -m "Migrate three multilingual works to canonical corpus"
```

## Verify the commit

`git status --short` must print nothing.

```bash
cd "$LMCW"
git status --short
git log -1 --oneline
git show --stat --oneline HEAD
```

Stop here for Manny/ChatGPT review. The corpus now has exactly nine works. Do
not migrate more works or begin new extraction design.
