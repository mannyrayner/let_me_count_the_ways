# Step 16: extract and annotate the indie-romance pilot with v0.3.1

Run this only after Step 15's source, conversion, provenance, and rights review
is approved. The batch is exactly the three supplied works in
`indie_romance_three_v1`; do not acquire more titles or merge it into a
canonical manifest.

## 1. Preflight and immutable configuration

```bash
cd "$LMCW"
git pull --ff-only
test -z "$(git status --short)" || {
  echo 'Working tree is not clean; stop and review it.' >&2
  exit 1
}
python -m pytest -q
python -m json.tool data/batches/indie_romance_three_v1.json >/dev/null
test -f prompts/annotation/classify_passage_v0_3_1.md
test -f prompts/annotation/classification_schema_v0_3.json
```

Confirm all three provenance records are approved for processing and every
derived-text hash matches its reviewed record. Select and record the exact
model alias/pricing snapshot. Annotation version is exactly `0.3.1`; do not
recalibrate it for genre, emotional intensity, sexual content, or expected
results.

## 2. Define a conservative English search family

Reuse the established English first-person-to-second-person target family.
Verify that its tested regular expression permits ordinary intervening
adverbs/auxiliaries needed for examples such as “I do/really/still love you”
and contractions in negated forms such as “I don't love you anymore,” while
remaining linguistically constrained. Inspect edition punctuation and Unicode
apostrophes. Do not expand to every occurrence of `love`.

Extraction is candidate discovery, not exclusion. Retain direct affirmative,
negated, embedded/reported, quoted/revoiced, hypothetical, deceptive, sexual,
and explicit-context matches. Preserve exact offsets and source text.

## 3. Dry-run all three works

Use the batch runner's actual CLI and a reviewed English patterns file:

```bash
cd "$LMCW"
python scripts/pipeline/run_batch.py \
  --manifest data/batches/indie_romance_three_v1.json \
  --annotation-version 0.3.1 \
  --model 5.6 \
  --patterns data/development/search_patterns_v0_3.json \
  --dry-run
```

If the reviewed model alias or patterns path differs, substitute it and record
the exact command; do not edit an established pattern version in place. The
dry-run must make no API calls.

For every work, reconcile extraction counts and inspect all hits when feasible;
otherwise inspect a documented representative sample plus every negated,
embedded/reported, quoted/revoiced, unusual, and boundary-sensitive hit. Also
search diagnostic nearby forms to determine whether obvious orthographic
variants were missed. Revise a new versioned pattern file only when supported by
examples, tests, and a repeated dry run.

Stop here if text quality, offsets, chapter order, punctuation, scope, or rights
are questionable.

## 4. Annotate without changing calibration

After approving the extraction inventory and exact cost estimate, rerun the
same command without `--dry-run`. Preserve the generated run directory and
resume it rather than forcing successful calls again.

Apply v0.3.1 literally: passion, sex, exclamation, repetition, bodily arousal,
and intensity do not alone establish E; relationship consequences do not alone
establish P; deception is orthogonal to P/T/E; O has a high burden. Do not omit
explicit material relevant to the target.

## 5. Audit and review

Use `scripts/pipeline/audit_pipeline_run.py --help` to select the correct audit
invocation for every text run, then audit the batch summary against its member
runs. Confirm each extracted occurrence has exactly one valid terminal
annotation, version/model/prompt/schema hashes are uniform, costs reconcile,
and no source passage was silently dropped.

Create a compact review inventory of P >= 2, E >= 2, O > 0, mixed P/T/E,
non-natural ontology fit, low confidence, and all structurally marked cases.
This is an index for review, not a filter.

```bash
cd "$LMCW"
python -m pytest -q
python scripts/security/scan_credentials.py
git status --short
```

Stop and share the extraction inventory, representative/all-hit inspection
notes, exact run command, pricing estimate and actual cost, batch report,
audits, and unusual-case inventory. Do not generate the genre comparison until
the batch is accepted.
