# Step 16: extract and annotate the one-work indie-romance pilot with v0.3.1

Run this only after Step 15's source, conversion, provenance, and rights review
is approved and committed. The batch is exactly *Nikki's Touch* in
`indie_romance_pilot_v1`; do not add replacement titles or merge it into a
canonical manifest. The two rejected candidates remain exclusions, not active
corpus members.

## 1. Preflight and immutable configuration

```bash
cd "$LMCW"
git pull --ff-only
test -z "$(git status --short)" || {
  echo 'Working tree is not clean; stop and review it.' >&2
  exit 1
}
PILOT_MANIFEST='data/batches/indie_romance_pilot_v1.json'
PILOT_SOURCE='provenance/sources/lulu-cofield-nikkis-touch-ebook.json'
python -m pytest -q
python -m json.tool "$PILOT_MANIFEST" >/dev/null
python -m json.tool "$PILOT_SOURCE" >/dev/null
test -f prompts/annotation/classify_passage_v0_3_1.md
test -f prompts/annotation/classification_schema_v0_3.json
```

Confirm the sole provenance record is approved, its derived-text hash still
matches, and its rights note remains accepted. Select and record the exact model
alias/pricing snapshot. Annotation version is exactly `0.3.1`; do not
recalibrate it for genre, emotional intensity, sexual content, or expectations.

## 2. Review a conservative English search family

Reuse the established English first-person-to-second-person family. Before the
production dry run, inspect its exact regular expression and compare it with the
exploratory Step 15 results:

```bash
python -m json.tool data/development/search_patterns_v0_3.json
```

If the inspected source supplies real intervening-adverb or auxiliary examples
that v0.3 does not cover, add a new versioned, tested English pattern manifest;
do not edit v0.3 in place. Permit only attested conservative structures such as
“I do/really/still love you” and retain negated forms where the first-person
subject, love predicate, and second-person object are structurally present. Do
not expand to every occurrence of `love`.

Extraction is candidate discovery, not exclusion. Retain direct affirmative,
negated, embedded/reported, quoted/revoiced, hypothetical, deceptive, sexual,
and explicit-context matches. Preserve exact offsets and source text.

## 3. Make and inspect the extraction-only run

Use the reviewed patterns path below. Replace it only if section 2 produced an
approved newer version:

```bash
cd "$LMCW"
PATTERNS='data/development/search_patterns_v0_3.json'
python scripts/pipeline/run_single_text_pipeline.py "$PILOT_SOURCE" \
  --patterns "$PATTERNS" \
  --annotation-version 0.3.1 \
  --model 5.6 \
  --dry-run
```

Record the exact printed run directory as `PILOT_DRY_RUN`; do not select it with
a newest-directory glob. Inspect its manifest, report, prepared inputs, and all
passages:

```bash
PILOT_DRY_RUN='REPLACE-WITH-PRINTED-RUN-DIRECTORY'
python -m json.tool "$PILOT_DRY_RUN/manifest.json"
sed -n '1,320p' "$PILOT_DRY_RUN/report.md"
python -m json.tool "$PILOT_DRY_RUN/extraction/metadata.json"
sed -n '1,240p' "$PILOT_DRY_RUN/extraction/passages.jsonl"
```

Reconcile the extraction with Step 15 diagnostics. Inspect every hit, including
all negated, embedded/reported, quoted/revoiced, unusual, explicit, and
boundary-sensitive cases. Stop if text quality, offsets, punctuation, scope, or
rights are questionable.

## 4. Dry-run and execute the one-work batch

The batch runner reuses the reviewed extraction and refuses implicit
re-extraction:

```bash
python scripts/pipeline/run_batch.py \
  --manifest "$PILOT_MANIFEST" \
  --annotation-version 0.3.1 \
  --model 5.6 \
  --patterns "$PATTERNS" \
  --dry-run
PILOT_BATCH='results/batch_runs/indie_romance_pilot_v1/v0.3.1-5.6'
python -m json.tool "$PILOT_BATCH/summary.json"
sed -n '1,320p' "$PILOT_BATCH/report.md"
```

Require one requested/prepared work, the manually approved occurrence count,
zero attempted calls, and no source error. After approving the exact call count
and cost estimate, execute the identical command without `--dry-run`:

```bash
test -n "${OPENAI_API_KEY:-}" || {
  echo 'OPENAI_API_KEY is not set; stop before annotation.' >&2
  exit 1
}
python scripts/pipeline/run_batch.py \
  --manifest "$PILOT_MANIFEST" \
  --annotation-version 0.3.1 \
  --model 5.6 \
  --patterns "$PATTERNS"
```

Do not use `--force`. A normal rerun resumes missing work and preserves attempts.
Apply v0.3.1 literally: passion, sex, exclamation, repetition, bodily arousal,
and intensity do not alone establish E; relationship consequences do not alone
establish P; deception is orthogonal to P/T/E; O has a high burden.

## 5. Audit, preserve, and stop

```bash
EXPECTED="$(python -c 'import json,sys; print(json.load(open(sys.argv[1],encoding="utf-8"))["occurrences"])' "$PILOT_BATCH/summary.json")"
PILOT_TEXT_RUN="$PILOT_BATCH/texts/lulu-cofield-nikkis-touch-ebook"
python scripts/pipeline/audit_pipeline_run.py \
  "$PILOT_TEXT_RUN" --expected-occurrences "$EXPECTED"
python scripts/security/scan_credentials.py "$PILOT_BATCH"
python -m json.tool "$PILOT_BATCH/summary.json"
sed -n '1,420p' "$PILOT_BATCH/report.md"
python -m pytest -q
```

Review P >= 2, E >= 2, O > 0, mixed P/T/E, non-natural fit, low confidence, and
all structurally marked cases. Then stage only the reviewed dry run and batch:

```bash
test -z "$(git diff --cached --name-only)" || {
  echo 'The index already contains files; stop and review it.' >&2
  exit 1
}
git add "$PILOT_DRY_RUN" "$PILOT_BATCH"
git diff --cached --check
git diff --cached --stat
python scripts/security/scan_credentials.py "$PILOT_DRY_RUN" "$PILOT_BATCH"
git commit -m 'Record Nikki’s Touch v0.3.1 pilot run'
git push origin HEAD
git status --short
```

Stop and share the extraction inventory, exact commands, pricing estimate and
actual cost, batch report, audit, and unusual-case inventory. Do not generate
the comparison until the one-work batch is accepted.
