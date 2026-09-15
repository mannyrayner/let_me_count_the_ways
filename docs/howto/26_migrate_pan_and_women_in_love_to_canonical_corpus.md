# Migrate Pan and Women in Love to the canonical corpus

This migration adds only Knut Hamsun's *Pan* and D. H. Lawrence's *Women in
Love* to the canonical corpus. It copies the approved repository literary
texts byte-for-byte with the existing builder. It does not download or derive
sources or run extraction, annotation, review, case-study, or batch workflows.

The approved *Pan* source is the corrected Runeberg derivation at
`data/raw/hamsun-pan/runeberg-hamsun-pan.txt`, produced after the line-break
repair and recorded by `provenance/sources/runeberg-hamsun-pan.json` and
`data/raw/hamsun-pan/page-map.json`. Its OCR remains uncorrected. The approved
*Women in Love* source is the wrapper-free Gutenberg literary text at
`data/raw/lawrence-women-in-love/gutenberg-4240.txt`, recorded by
`provenance/sources/gutenberg-4240.json` and used by the classical-six
workflow. Run each block from the established Cygwin setup and stop if any
command fails.

## Build Pan

```bash
cd "$LMCW"
python scripts/corpus/build_canonical_work.py data/raw/hamsun-pan/runeberg-hamsun-pan.txt --work-id hamsun-pan --title "Pan" --author "Knut Hamsun" --language no --source-type runeberg --source-reference provenance/sources/runeberg-hamsun-pan.json --source-reference data/raw/hamsun-pan/page-map.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved post-line-break-repair Runeberg-derived literary text, preserving the uncorrected OCR; no acquisition, derivation, OCR correction, or lineation normalization was rerun."
```

## Build Women in Love

```bash
cd "$LMCW"
python scripts/corpus/build_canonical_work.py data/raw/lawrence-women-in-love/gutenberg-4240.txt --work-id lawrence-women-in-love --title "Women in Love" --author "D. H. Lawrence" --language en --source-type gutenberg_single --source-reference provenance/sources/gutenberg-4240.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved wrapper-free Gutenberg-derived literary text used by the classical-six workflow; no acquisition, wrapper stripping, derivation, or correction was rerun."
```

## Confirm byte identity

Both successful comparisons are silent. Stop immediately if either reports a
difference.

```bash
cd "$LMCW"
cmp data/raw/hamsun-pan/runeberg-hamsun-pan.txt corpus/works/hamsun-pan/canonical.txt
cmp data/raw/lawrence-women-in-love/gutenberg-4240.txt corpus/works/lawrence-women-in-love/canonical.txt
```

## Validate and regenerate the index

The validator must report `Canonical corpus valid: 13 work(s).`; it also checks
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
cat corpus/works/hamsun-pan/work.json
cat corpus/works/lawrence-women-in-love/work.json
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
git add corpus/index.md corpus/works/hamsun-pan/ corpus/works/lawrence-women-in-love/ docs/howto/26_migrate_pan_and_women_in_love_to_canonical_corpus.md docs/howto/README.md
git diff --cached --check
git diff --cached --stat
git commit -m "Migrate Pan and Women in Love to canonical corpus"
```

## Verify the commit

`git status --short` must print nothing.

```bash
cd "$LMCW"
git status --short
git log -1 --oneline
git show --stat --oneline HEAD
```

Stop here for Manny/ChatGPT review. The corpus now has exactly thirteen works.
Do not migrate more works or begin the redesigned extraction pipeline.
