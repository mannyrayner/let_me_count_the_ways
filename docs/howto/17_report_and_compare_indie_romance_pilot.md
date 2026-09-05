# Step 17: report and compare the one-work indie-romance pilot

This runbook uses the accepted Step 14 reporting machinery and accepted Step 16
v0.3.1 annotations for *Nikki's Touch*. It produces the pilot inspection report
and a descriptive comparison. It does not perform significance testing, add
texts, revise annotations, or encode claims about literary quality.

## 1. Preflight

```bash
cd "$LMCW"
git pull --ff-only
test -z "$(git status --short)" || {
  echo 'Working tree is not clean; stop and review it.' >&2
  exit 1
}
python -m pytest -q
CANONICAL_REPORT='results/corpus_reports/canonical_eight_v0_3_1.json'
PILOT_RUN='results/batch_runs/indie_romance_pilot_v1/v0.3.1-5.6'
test -f "$CANONICAL_REPORT"
test -f "$PILOT_RUN/summary.json"
python -m json.tool "$CANONICAL_REPORT" >/dev/null
python -m json.tool "$PILOT_RUN/summary.json" >/dev/null
```

Confirm the selected batch has exactly one completed work, *Nikki's Touch*, and
annotation version `0.3.1`. Do not use a mutable “latest” selection.

## 2. Generate the pilot report

Run the corpus-report command offline first, inspect the request/call estimate,
then generate using the same explicit batch path. Since the work is English,
translation must be `null`.

```bash
set +e
python scripts/reporting/build_corpus_report.py \
  --name indie_romance_pilot_v1_v0_3_1 \
  --batch-run "$PILOT_RUN" \
  --enrichment-model 5.6 \
  --offline
STATUS=$?
set -e
test "$STATUS" -eq 0 -o "$STATUS" -eq 2

python scripts/reporting/build_corpus_report.py \
  --name indie_romance_pilot_v1_v0_3_1 \
  --batch-run "$PILOT_RUN" \
  --enrichment-model 5.6
```

Validate and review:

```bash
PILOT_REPORT='results/corpus_reports/indie_romance_pilot_v1_v0_3_1.json'
PILOT_MARKDOWN='results/corpus_reports/indie_romance_pilot_v1_v0_3_1.md'
python -m json.tool "$PILOT_REPORT" >/dev/null
test -s "$PILOT_MARKDOWN"
python scripts/reporting/validate_corpus_report.py \
  --report "$PILOT_REPORT" \
  --batch-run "$PILOT_RUN"
less "$PILOT_MARKDOWN"
```

Rerun without force and require zero cache misses/model calls. Read every
occurrence and verify source passage, context, immutable scores, confidence,
commentary, utterance status, explicit/sexual-context retention, and provenance.

## 3. Implement and run the deterministic descriptive comparison

The comparison command must consume saved structured report/run data and make
no model calls. Define the groups explicitly:

- canonical literary fiction/drama: eight works from `development_three` and
  `multilingual_five_v1`;
- contemporary indie romance pilot: the one work *Nikki's Touch* from
  `indie_romance_pilot_v1`.

For each group and work, report works/occurrences; full P/T/E/O distributions;
P >= 2 and E >= 2 counts/proportions with denominators; mixed P/T/E using an
explicit definition; ontology-fit distribution; and direct-affirmative versus
embedded/reported, negated, quoted/revoiced, and hypothetical/other-marked
counts/proportions. Categories may overlap. Never force unknown status into
“direct”; surface missing fields.

Write:

```text
results/corpus_reports/canonical_vs_indie_romance_pilot_v1.md
results/corpus_reports/canonical_vs_indie_romance_pilot_v1.json
```

Do not run significance tests. One work cannot support broad genre inference;
describe this as an exploratory contrast using raw counts and proportions.

## 4. Test and review symmetrically

Add fixture tests for zero denominators, unknown/overlapping statuses, score
boundaries, mixed-case definition, deterministic ordering, and total
reconciliation. Interpret all live outcomes without preference: more P, more E,
continuing T dominance, more mixed cases, or credible O cases. Reinspect
surprising cases before ontology changes and avoid taste-coded comparisons.

```bash
python -m json.tool \
  results/corpus_reports/canonical_vs_indie_romance_pilot_v1.json >/dev/null
python -m pytest -q
python scripts/security/scan_credentials.py \
  results/corpus_reports/indie_romance_pilot_v1_v0_3_1.json \
  results/corpus_reports/indie_romance_pilot_v1_v0_3_1.md \
  results/corpus_reports/canonical_vs_indie_romance_pilot_v1.json \
  results/corpus_reports/canonical_vs_indie_romance_pilot_v1.md
git status --short
```

Stop and share both pilot report files, both comparison files, tests, cache/cost
summary, missing-data inventory, and unexpected P, E, O, mixed, non-natural-fit,
and low-confidence cases. The next decision is whether this one-work signal
justifies seeking further clearly licensed examples; do not acquire them here.
