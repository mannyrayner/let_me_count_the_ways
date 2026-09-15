# Complete the existing canonical corpus with private-text support

This migration completes the 16-work research corpus without publishing Stella
McMillan's contemporary novel. Canonical storage now has two modes:
`repository` means `canonical.txt` is versioned beside its manifest;
`local_private` means the public manifest identifies a locally held UTF-8 file
and its hash. A missing private file is an availability warning, not structural
failure; when present it is decoded as UTF-8 and hash-checked.

No command below downloads, reconverts, extracts, or annotates text.

## Build the two public-domain works

```bash
cd "$LMCW"
python scripts/corpus/build_canonical_work.py data/raw/dumas-fils-la-dame-aux-camelias/gutenberg-2419.txt --work-id dumas-fils-la-dame-aux-camelias --title "La Dame aux camélias" --author "Alexandre Dumas fils" --language fr --source-type gutenberg_single --source-reference provenance/sources/gutenberg-2419.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved wrapper-free Gutenberg-derived literary text; no acquisition, wrapper stripping, derivation, or correction was rerun."
python scripts/corpus/build_canonical_work.py data/raw/constant-adolphe/gutenberg-13861.txt --work-id constant-adolphe --title "Adolphe" --author "Benjamin Constant" --language fr --source-type gutenberg_single --source-reference provenance/sources/gutenberg-13861.json --public-render-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK --notes "Byte-for-byte copy of the approved wrapper-free Gutenberg-derived literary text; no acquisition, wrapper stripping, derivation, or correction was rerun."
cmp data/raw/dumas-fils-la-dame-aux-camelias/gutenberg-2419.txt corpus/works/dumas-fils-la-dame-aux-camelias/canonical.txt
cmp data/raw/constant-adolphe/gutenberg-13861.txt corpus/works/constant-adolphe/canonical.txt
```

The successful `cmp` commands are silent.

## Create and validate the private manifest

Create `corpus/works/mcmillan-error-of-understanding/work.json` from the reviewed
values in this migration (do not copy the novel). Confirm the established local
derivation directly:

```bash
cd "$LMCW"
sha256sum data/local_candidate_derived/mcmillan-error-of-understanding/text.txt
python scripts/corpus/validate_canonical_corpus.py corpus/works --write-index corpus/index.md
```

The hash must be
`b941746d22087c6cfc9e9634880d0f950db8017de786077c37fdfc643f880839`.
A clone without that file instead prints a clear warning and still reports 16
structurally valid works.

## Report outstanding rights review

```bash
cd "$LMCW"
python scripts/corpus/validate_canonical_corpus.py corpus/works --report-rights-review
```

Expected output includes:

```text
REVIEW_REQUIRED mcmillan-error-of-understanding AUTHOR_APPROVAL_FOR_PUBLICATION_EXCERPTS
```

(The command uses tabs.) This is intentional, not an error: before publication,
Manny must send the author the proposed quoted passages and obtain explicit
approval.

## Inspect and test

```bash
cd "$LMCW"
cat corpus/works/dumas-fils-la-dame-aux-camelias/work.json
cat corpus/works/constant-adolphe/work.json
cat corpus/works/mcmillan-error-of-understanding/work.json
cat corpus/index.md
python -m pytest -q scripts/corpus/test_canonical_corpus.py
python scripts/docs/validate_runbook_index.py
git diff --check
git status --short
```

## Stage only public-safe artifacts and commit

Never use `git add .`. The private text and purchased EPUB must not appear in
the staged-name list.

```bash
cd "$LMCW"
git add corpus/index.md corpus/work.schema.json \
  corpus/works/dumas-fils-la-dame-aux-camelias/ \
  corpus/works/constant-adolphe/ \
  corpus/works/mcmillan-error-of-understanding/work.json \
  provenance/sources/local-mcmillan-error-of-understanding-text.json \
  docs/notes/rights/mcmillan-error-of-understanding-author-permission-2026-09-07.md \
  scripts/corpus/validate_canonical_corpus.py scripts/corpus/test_canonical_corpus.py \
  docs/howto/27_complete_existing_canonical_corpus.md docs/howto/README.md
git diff --cached --name-only
git diff --cached --check
git commit -m "Complete canonical migration with private text support"
```

Inspect any suspicious staged path before committing. In particular, neither a
McMillan `canonical.txt` nor an EPUB may be listed.

## Post-commit verification

```bash
cd "$LMCW"
git status --short
git log -1 --oneline
git show --stat --oneline HEAD
```

The status should be empty; ignored local/private source material is expected
not to appear.
