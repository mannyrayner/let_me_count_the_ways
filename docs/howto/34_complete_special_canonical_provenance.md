# Complete special canonical provenance

Complete the provenance chain for the Balzac and Undset canonical texts by
linking each work manifest to both its source-material records and its
deterministic derivation record. This is a metadata-only repair: do not modify
canonical text, regenerate hashes, or begin extraction.

## 1. Inspect current manifests and record hashes

```bash
cd "$LMCW"
git status --short
cat corpus/works/balzac-illusions-perdues/work.json
cat corpus/works/undset-kristin-lavransdatter/work.json
sha256sum \
  corpus/works/balzac-illusions-perdues/canonical.txt \
  corpus/works/undset-kristin-lavransdatter/canonical.txt
```

Start from a clean tree. Record the hashes before editing; they must be
`419f47435e440d4d44539f423bef3fbe9286f3bbbb359d4985ccb8436f6c0bcf`
for Balzac and
`6400013e56dd14a00ebad42e137d7b7cc42cd7092299112be07f1a361ac8b0b8`
for Undset.

## 2. Apply and verify provenance links

In the Balzac manifest, retain the Gutenberg source record and append:

```text
data/derived/balzac-illusions-perdues/derivation.json
```

In the Undset manifest, retain the three Runeberg source records in Kransen,
Husfrue, Korset order and append:

```text
data/derived/undset-kristin-lavransdatter/derivation.json
```

Verify both transformation records exist:

```bash
test -f data/derived/balzac-illusions-perdues/derivation.json
test -f data/derived/undset-kristin-lavransdatter/derivation.json
```

## 3. Validate the 31-work corpus

```bash
python scripts/corpus/validate_canonical_corpus.py corpus/works
```

Expect `Canonical corpus valid: 31 work(s).` The normal warning that the local,
private McMillan source is unavailable is acceptable.

## 4. Verify hashes and content are unchanged

```bash
sha256sum \
  corpus/works/balzac-illusions-perdues/canonical.txt \
  corpus/works/undset-kristin-lavransdatter/canonical.txt
git diff --exit-code -- \
  corpus/works/balzac-illusions-perdues/canonical.txt \
  corpus/works/undset-kristin-lavransdatter/canonical.txt \
  corpus/index.md
```

Confirm the hashes match those recorded in step 1 and the content/index diff is
empty.

## 5. Run focused and repository tests

```bash
python -m pytest -q scripts/corpus
python scripts/docs/validate_runbook_index.py
python scripts/corpus/validate_canonical_corpus.py corpus/works
git diff --check
```

The corpus validator checks that every listed source reference resolves, so
these checks cover both newly linked derivation records.

## 6. Explicitly stage and inspect

Never use `git add .`. Stage only the four intended files:

```bash
git add \
  corpus/works/balzac-illusions-perdues/work.json \
  corpus/works/undset-kristin-lavransdatter/work.json \
  docs/howto/34_complete_special_canonical_provenance.md \
  docs/howto/README.md
git diff --cached --name-only
git diff --cached --check
```

Confirm no canonical text, corpus index, extraction code, or review artifact is
staged.

## 7. Commit

```bash
git commit -m "Complete canonical derivation provenance"
```

## 8. Post-commit verification

```bash
git status --short
git log -1 --oneline
git show --stat --oneline HEAD
```

Require a clean working tree. Stop here for review; do not begin extraction in
this handoff.
