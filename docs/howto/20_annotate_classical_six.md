# Step 20: annotate the reviewed classical six

This runbook consumes the frozen `classical_six_v1` extraction made with
patterns v0.6 and the definitive reviewed occurrence decisions from Step 19. It
annotates only the 37 effective KEEP occurrences. The Dumas lexical false
positive remains in the raw 38-hit inventory and is visibly filtered before any
model call; occurrence IDs never change.

Reuse the established annotation machinery used for `development_three`,
`multilingual_five_v1`, and `indie_romance_pilot_v1`: annotation v0.3.1, model
alias `5.6` (GPT-5.6 Sol), and the existing prompt and schema unchanged. Context
comes from the validated 1000-character Step 19 dry runs.

## 1. Materialize and inspect the reviewed KEEP set

The review helper acts as a reusable allowlist boundary. It rejects missing,
unknown, and duplicate review IDs; checks source, pattern, and offsets against
the extraction inventory; applies a valid optional human occurrence-validity
override; and explicitly reports every filtered EXCLUDE. It does not alter the
raw inventory.

```bash
cd "$LMCW"
RECON=results/reconnaissance/classical_six_v1
KEEP_ROOT="$RECON/reviewed_extractions"

python scripts/review/classical_six_review.py validate \
  --inventory "$RECON/occurrence_inventory.tsv" \
  --review "$RECON/reviewed_occurrences.json"
python scripts/review/classical_six_review.py filter \
  --inventory "$RECON/occurrence_inventory.tsv" \
  --review "$RECON/reviewed_occurrences.json" \
  --selected-runs "$RECON/selected-runs.json" \
  --output "$KEEP_ROOT"
```

If `review_overrides.json` exists, add
`--overrides "$RECON/review_overrides.json"` to both commands. Expected current
output is 37 prepared KEEP occurrences and one visibly filtered ID,
`dumas-fils-la-dame-aux-camelias-dec42bc1687b`. Inspect every prepared JSONL and
confirm the four structurally marked KEEP cases documented in Step 19 remain.

## 2. Dry run and then annotate resumably

```bash
python scripts/pipeline/run_batch.py \
  --manifest data/batches/classical_six_v1.json \
  --annotation-version 0.3.1 --model 5.6 \
  --patterns data/development/search_patterns_v0_6.json \
  --context-chars 1000 --extraction-root "$KEEP_ROOT" \
  --output-root results/batch_runs --dry-run

# Inspect all 37 inputs and the dry-run summary before authorizing model calls.
python scripts/pipeline/run_batch.py \
  --manifest data/batches/classical_six_v1.json \
  --annotation-version 0.3.1 --model 5.6 \
  --patterns data/development/search_patterns_v0_6.json \
  --context-chars 1000 --extraction-root "$KEEP_ROOT" \
  --output-root results/batch_runs
```

Rerun the second command unchanged to resume. A valid existing annotation is
skipped; a missing or failed occurrence is retried; a completed occurrence is
never silently overwritten. Do not use `--force` merely to resume. Existing
per-attempt infrastructure records model, annotation version, prompt hash,
schema hash, source/extraction hash, occurrence ID, usage/cost, and status.

## 3. Aggregate and inspect descriptive results

Inspect
`results/batch_runs/classical_six_v1/v0.3.1-5.6/{summary.json,report.md,unusual_cases.json}`
and retained request/response/status files. Report the classical-six batch
separately with:

- P, T, E, and O score distributions and ontology-fit distribution;
- counts for P >= 2, E >= 2, and two or more of P/T/E >= 2;
- 37 reviewed target occurrences and approximately 24 scene clusters.

Occurrences, not scenes, are annotation units. Scene clusters are descriptive
dependence information and are not independent sample counts. A descriptive
comparison with the previous canonical eight may be prepared if existing report
tooling makes it straightforward, but do not perform significance testing.

```bash
python -m pytest -q
python scripts/docs/validate_runbook_index.py
python scripts/security/scan_credentials.py results/batch_runs/classical_six_v1
python -m json.tool results/batch_runs/classical_six_v1/v0.3.1-5.6/summary.json >/dev/null
git diff --check
git status --short
```

After descriptive reporting, proceed only to the read-only checkpoint below.
Do not make another model call or acquire more works.

## 4. Validate the completed annotation checkpoint

The batch has already completed. **Do not run `run_batch.py` again merely to
check it in, and do not use `--force`.** Validate the stored artifacts without
making any model call:

```bash
cd "$LMCW"
RESULT=results/batch_runs/classical_six_v1/v0.3.1-5.6
RECON=results/reconnaissance/classical_six_v1

python scripts/reporting/validate_classical_six_batch.py \
  --batch-root "$RESULT" \
  --reconnaissance-root "$RECON"
```

This Python validator reports labelled expected/actual failures and checks all
of the following together:

- batch identity, annotation/model version, non-dry-run complete status, 6/6
  completed texts, 37/37 valid annotations, zero failures, zero historical
  failures, and zero model calls still needed;
- the 38-item raw inventory, 37 reviewed KEEP decisions, sole Dumas EXCLUDE,
  and absence of an annotation directory or output for
  `dumas-fils-la-dame-aux-camelias-dec42bc1687b`;
- complete per-text counts of 1, 9, 8, 4, 14, and 1 in manifest order;
- all 37 unique valid `output.json` files and their `status.json` files;
- the exact P/T/E/O and ontology-fit distributions and derived unusual-case
  totals observed in this run;
- exact regeneration of `report.md` from `summary.json`;
- every `unusual_cases.json` entry against its reviewed KEEP ID, valid output,
  scores, ontology fit, confidence, and documented selection reason; and
- the preserved noteworthy results
  `lawrence-women-in-love-5ab672887915` (P=0, T=0, E=0, O=4) and
  `hamsun-victoria-be00bbdbf853` (P=0, T=4, E=3, O=0).

Presence in `unusual_cases.json` is not an error. Do not reinterpret or edit a
stored annotation because it is theoretically surprising; these are research
results, and interpretation belongs in later analysis.

## 5. Concise human sanity check

Before staging, inspect—not regenerate—the aggregate artifacts:

```bash
sed -n '1,220p' "$RESULT/report.md"
python -m json.tool "$RESULT/summary.json" | sed -n '1,240p'
python -m json.tool "$RESULT/unusual_cases.json" | sed -n '1,260p'
```

Optionally spot-check the stored output for the O=4 Lawrence case, the E=3
Hamsun case, and at least one P=2 case. This is a final aggregate-to-output
sanity check, not a second full annotation review. Preserve all per-attempt
input, request, response, parsing, validation, status, output, metadata, and
cost artifacts so every result remains reconstructible.

## 6. Repository checks and safe staging

Run the normal checks before staging:

```bash
python -m json.tool \
  results/batch_runs/classical_six_v1/v0.3.1-5.6/summary.json >/dev/null
python -m json.tool \
  results/batch_runs/classical_six_v1/v0.3.1-5.6/unusual_cases.json >/dev/null
python -m pytest -q
python scripts/docs/validate_runbook_index.py
python scripts/security/scan_credentials.py \
  results/batch_runs/classical_six_v1 \
  docs/howto/20_annotate_classical_six.md \
  scripts/reporting/validate_classical_six_batch.py \
  scripts/reporting/test_validate_classical_six_batch.py
git diff --check
git status --short
```

Classify every changed or untracked path printed by `git status --short`.
Exclude unrelated work. For this checkpoint, the intended paths are the full
auditable result tree, this runbook, its validator, and its tests. Stage exactly
those paths; never use `git add .`:

```bash
git add \
  results/batch_runs/classical_six_v1/v0.3.1-5.6 \
  docs/howto/20_annotate_classical_six.md \
  scripts/reporting/validate_classical_six_batch.py \
  scripts/reporting/test_validate_classical_six_batch.py

git diff --cached --stat
git diff --cached --check
git status --short
```

The staged tree must contain `summary.json`, `report.md`,
`unusual_cases.json`, all six text result directories, and all 37 valid
annotation outputs with their complete attempt provenance. It must contain no
credential, unrelated file, or annotation directory for the excluded Dumas ID.
Rerun the read-only validator after staging to machine-count the current 37
unique outputs once more:

```bash
python scripts/reporting/validate_classical_six_batch.py \
  --batch-root "$RESULT" \
  --reconnaissance-root "$RECON"
```

## 7. Commit and verify

```bash
git commit -m "Complete classical six v0.3.1 annotations"
git status --short
test -z "$(git status --short)" || {
  echo 'Working tree is not clean; classify the remaining paths.' >&2
  exit 1
}
git log -1 --oneline
git show --stat --oneline HEAD
```

Observed completed run (not generic constants for future batches):

```text
6/6 texts complete
37/37 annotations valid
0 failures
estimated recorded cost USD 1.432100
```

The checkpoint is complete only when the summary is complete; all six text
counts and 37 reviewed KEEP outputs reconcile; the excluded Dumas hit has no
annotation; report and unusual cases agree with valid outputs; tests, runbook
index, credential scan, and diff checks pass; only intended artifacts are
committed; and the post-commit working tree is clean. Then stop. Do not acquire
or annotate the next corpus from this runbook.
