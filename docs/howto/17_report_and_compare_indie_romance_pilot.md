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
PILOT_RUN='results/batch_runs/indie_romance_pilot_v1/v0.3.1-5.6'
test -f "$PILOT_RUN/summary.json" || {
  echo "Missing pilot batch summary: $PILOT_RUN/summary.json" >&2
  exit 1
}
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

## 3. Run the deterministic descriptive comparison

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

The command is local and deterministic: it reads the two completed JSON
reports, makes no model calls, and refuses inputs other than the canonical eight
and the one-work *Nikki's Touch* pilot. This block is self-contained and can be
pasted into a fresh Cygwin shell. `test -f` is a silent file predicate: no output
means success, while `echo $?` immediately afterward would print `0`. The loop
uses it to produce a clearer missing-input error before running Python, and now
prints an explicit confirmation for each successful check:

```bash
CANONICAL_REPORT='results/corpus_reports/canonical_eight_v0_3_1.json'
PILOT_REPORT='results/corpus_reports/indie_romance_pilot_v1_v0_3_1.json'
COMPARISON_JSON='results/corpus_reports/canonical_vs_indie_romance_pilot_v1.json'
COMPARISON_MARKDOWN='results/corpus_reports/canonical_vs_indie_romance_pilot_v1.md'

for REPORT in "$CANONICAL_REPORT" "$PILOT_REPORT"; do
  if ! test -f "$REPORT"; then
    echo "Missing report: $REPORT" >&2
    exit 1
  fi
  if ! python -m json.tool "$REPORT" >/dev/null; then
    echo "Report is not valid JSON: $REPORT" >&2
    exit 1
  fi
  printf 'Found and validated report: %s\n' "$REPORT"
done

python scripts/reporting/compare_corpus_reports.py \
  --canonical-report "$CANONICAL_REPORT" \
  --pilot-report "$PILOT_REPORT" \
  --output-json "$COMPARISON_JSON" \
  --output-markdown "$COMPARISON_MARKDOWN"

python -m json.tool "$COMPARISON_JSON" >/dev/null
test -s "$COMPARISON_MARKDOWN"
less "$COMPARISON_MARKDOWN"
```

Do not run significance tests. One work cannot support broad genre inference;
describe this as an exploratory contrast using raw counts and proportions.

## 4. Test and review symmetrically

The comparison tests cover zero denominators, unknown statuses, score
boundaries, mixed-case definition, deterministic ordering, and total
reconciliation. Interpret all live outcomes without preference: more P, more E,
continuing T dominance, more mixed cases, or credible O cases. Reinspect
surprising cases before ontology changes and avoid taste-coded comparisons.

Run this self-contained audit block. The audit reconciles every distribution,
threshold denominator, group total, and per-work total; verifies the input
hashes and fixed 8/41-versus-1/10 scope; and prints the cache/cost summary,
missing-data inventory, cautions, and every pilot P, E, O, mixed,
non-natural-fit, or low-confidence case that needs human review:

```bash
CANONICAL_REPORT='results/corpus_reports/canonical_eight_v0_3_1.json'
PILOT_REPORT='results/corpus_reports/indie_romance_pilot_v1_v0_3_1.json'
PILOT_MARKDOWN='results/corpus_reports/indie_romance_pilot_v1_v0_3_1.md'
PILOT_RUN='results/batch_runs/indie_romance_pilot_v1/v0.3.1-5.6'
COMPARISON_JSON='results/corpus_reports/canonical_vs_indie_romance_pilot_v1.json'
COMPARISON_MARKDOWN='results/corpus_reports/canonical_vs_indie_romance_pilot_v1.md'

python scripts/reporting/build_corpus_report.py \
  --name indie_romance_pilot_v1_v0_3_1 \
  --batch-run "$PILOT_RUN" \
  --enrichment-model 5.6 | tee /tmp/step17-cache-check.txt
grep -Fx 'Cache hits: 10' /tmp/step17-cache-check.txt
grep -Fx 'Cache misses: 0' /tmp/step17-cache-check.txt
grep -Fx 'Model calls required: 0' /tmp/step17-cache-check.txt

python scripts/reporting/validate_corpus_report.py \
  --report "$PILOT_REPORT" \
  --batch-run "$PILOT_RUN"
python scripts/reporting/audit_indie_comparison.py \
  --canonical-report "$CANONICAL_REPORT" \
  --pilot-report "$PILOT_REPORT" \
  --comparison "$COMPARISON_JSON" | tee /tmp/step17-audit.txt
python -m pytest -q
python scripts/security/scan_credentials.py \
  "$PILOT_REPORT" "$PILOT_MARKDOWN" \
  "$COMPARISON_JSON" "$COMPARISON_MARKDOWN"
wc -l -w -c "$PILOT_REPORT" "$PILOT_MARKDOWN" \
  "$COMPARISON_JSON" "$COMPARISON_MARKDOWN"
git status --short
```

Open both Markdown files and inspect every case listed under
`pilot_cases_requiring_review` in `/tmp/step17-audit.txt`. In particular, treat
the two P=3 occurrences in the short final exchange as two corpus occurrences
but one scene-level signal. The untracked cache directories are expected from
the ten pilot enrichments; the second no-force report build must report ten
cache hits, zero cache misses, and zero model calls before they are retained.
Do not stage or commit until this human review is complete.

Stop and share both pilot report files, both comparison files, tests, cache/cost
summary, missing-data inventory, and unexpected P, E, O, mixed, non-natural-fit,
and low-confidence cases. The next stage is to extend the indie-romance corpus
with locally triaged works whose public excerpts are supported by explicit
author permission or separately reviewed fair-dealing grounds.
