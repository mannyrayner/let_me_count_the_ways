# Canonicalize the expansion fifteen locally

Codex prepared and tested the lightweight machinery in this repository. **Manny
performs the actual bulk canonicalization locally.** This separation is
intentional: the local Git client, not Codex's generated-diff mechanism, must
handle the large literary-text commit. Stop on any unexpected error; do not run
extraction, scholarly AI review, or annotation in this runbook.

## 1. Pull/check repository state

Start from the laptop checkout containing the committed lightweight driver:

```bash
cd "$LMCW"
git pull --ff-only
git status --short
git log -1 --oneline
```

The status must be clean. The acquisition inventory at
`data/acquisition/expansion_15_v1/manifest.json` is authoritative.

## 2. Run lightweight tests

```bash
python -m pytest -q scripts/corpus
python -m pytest -q scripts/corpus_acquisition
python scripts/docs/validate_runbook_index.py
git diff --check
```

All tests must pass before generation.

## 3. Preflight/dry-run canonicalization

```bash
python scripts/corpus/canonicalize_expansion_15.py --check
git status --short
```

This verifies exactly 15 inventory IDs, every input's existence, SHA-256, and
UTF-8 validity, both deterministic derivations, all Undset repair regressions,
and every prospective output. It writes nothing. Each absent work reports
`CREATE`; an identical prior output reports `VALID/UNCHANGED`. A mismatch stops
the operation rather than overwriting it. The status must remain clean.

## 4. Run full 15-work canonicalization locally

```bash
python scripts/corpus/canonicalize_expansion_15.py
```

The driver prepares Balzac and Undset derived sources, calls the established
canonical work builder, verifies ordinary copies byte-for-byte, and writes the
checkpoint inventory. It only addresses the named expansion works and never
rewrites any of the original 16 canonical works. Safe identical reruns are
allowed; divergent existing output causes a hard stop.

## 5. Validate 31-work corpus

```bash
python scripts/corpus/validate_canonical_corpus.py \
  corpus/works \
  --write-index corpus/index.md
```

Expect `Canonical corpus valid: 31 work(s).` The normal warning that the private
McMillan source is unavailable is acceptable. The final corpus has 31 research
works (30 repository-backed and one local/private) across `en`, `fr`, `de`,
`no`, `sv`, `da`, and `it`.

## 6. Inspect Balzac

Inspect metadata and targeted boundaries rather than the whole novel:

```bash
cat data/derived/balzac-illusions-perdues/derivation.json
head -30 data/derived/balzac-illusions-perdues/canonical-source.txt
tail -30 data/derived/balzac-illusions-perdues/canonical-source.txt
cmp data/derived/balzac-illusions-perdues/canonical-source.txt \
  corpus/works/balzac-illusions-perdues/canonical.txt
rg -n 'LES DEUX POÈTES|UN GRAND HOMME DE PROVINCE A PARIS|ÈVE ET DAVID' \
  corpus/works/balzac-illusions-perdues/canonical.txt
```

Confirm the three parts occur in order and unrelated material before the work,
the volume footer, table of contents, and corrections after it are excluded.

## 7. Inspect Undset

```bash
cat data/derived/undset-kristin-lavransdatter/derivation.json
cmp data/derived/undset-kristin-lavransdatter/canonical-source.txt \
  corpus/works/undset-kristin-lavransdatter/canonical.txt
rg -n -F \
  -e 'Ved skiftet efter Ivar unge Gjesling paa Sundbu i' \
  -e 'ti Ragnfrid var noget sær og tungsindig' \
  -e 'Hun blir saa rusende, hun kan ikke gaa ned til' \
  -e 'sæteren,» sa Halvdan' \
  corpus/works/undset-kristin-lavransdatter/canonical.txt
```

Confirm the recorded input order is Kransen, Husfrue, Korset and the separator
rule preserves each volume while inserting no editorial prose.

## 8. Inspect canonicalization inventory

```bash
cat data/canonicalization/expansion_15_v1/README.md
python -m json.tool data/canonicalization/expansion_15_v1/manifest.json
```

Confirm `15/15 canonicalized`, 15 entries, canonical hashes, source or derived
paths, source relationships, and `VALID` statuses.

## 9. Run rights-review scan

```bash
python scripts/corpus/validate_canonical_corpus.py \
  corpus/works \
  --report-rights-review
```

The unresolved report should still contain
`mcmillan-error-of-understanding` and
`AUTHOR_APPROVAL_FOR_PUBLICATION_EXCERPTS`. The 15 public-domain additions must
introduce no unresolved rights issue, and the existing McMillan rights state
must be unchanged.

## 10. Run final tests

```bash
python -m pytest -q scripts/corpus
python -m pytest -q scripts/corpus_acquisition
python scripts/docs/validate_runbook_index.py
git diff --check
```

## 11. Inspect git diff/stat

```bash
git status --short
git diff --stat
git diff --name-only
```

The stat will be large because it adds full literary texts; that is expected.
Do not attempt to inspect the entire textual diff interactively. Review the
status, stat, name list, manifests and hashes, plus the targeted `cmp` and
content assertions above. Stop if paths outside the expected generated set or
`corpus/index.md` changed.

## 12. Explicitly stage generated outputs

Never use `git add .`. Stage exactly the generated paths:

```bash
git add \
  corpus/works/stendhal-le-rouge-et-le-noir \
  corpus/works/balzac-illusions-perdues \
  corpus/works/colette-le-ble-en-herbe \
  corpus/works/sand-la-mare-au-diable \
  corpus/works/stael-corinne \
  corpus/works/fontane-effi-briest \
  corpus/works/zuccoli-lamore-di-loredana \
  corpus/works/verona-colei-che-non-si-deve-amare \
  corpus/works/bang-ved-vejen \
  corpus/works/nansen-maria \
  corpus/works/bronte-tenant-of-wildfell-hall \
  corpus/works/austen-persuasion \
  corpus/works/eliot-middlemarch \
  corpus/works/lagerlof-gosta-berlings-saga \
  corpus/works/undset-kristin-lavransdatter \
  corpus/index.md \
  data/derived/balzac-illusions-perdues \
  data/derived/undset-kristin-lavransdatter \
  data/canonicalization/expansion_15_v1
git status --short
git diff --cached --stat
git diff --cached --name-only
```

The driver, tests, and this runbook should already be present in the pulled
Codex commit and therefore are not restaged here.

## 13. Commit locally

```bash
git commit -m "Canonicalize fifteen corpus expansion works"
```

This deliberately uses the local Git client to handle the large textual commit,
rather than Codex's generated-diff mechanism.

## 14. Push locally

```bash
git push
```

## 15. Post-push verification

```bash
git status --short
git log -1 --oneline
git ls-tree -r --name-only HEAD corpus/works
python scripts/corpus/validate_canonical_corpus.py corpus/works
```

Confirm a clean status and 31 canonical work directories (or equivalently the
validator's 31-work result). This canonicalization checkpoint is the endpoint;
do not proceed to extraction in this run.
