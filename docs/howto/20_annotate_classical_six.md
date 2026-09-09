# Step 20: annotate the adjudicated classical six

This consumes Step 19's frozen occurrence set and annotates only explicit KEEP
occurrences. EXCLUDE is never sent to the model. Structurally unusual KEEP cases
(negative/interrogative, hypothetical, written, embedded, or deceptive) remain.
Stable IDs join annotations to corrected-context AI v2, human audit, and adjudication. Step 20 remains blocked until those Step 19 artifacts have no unresolved cases.

## 1. Materialize the KEEP-only extraction

Use annotation v0.3.1, model alias `5.6` (GPT-5.6 Sol), patterns v0.6, and the
validated 1000-character context radius. Do not change the frozen ontology,
prompt, or schema used by the canonical and indie batches.

```bash
cd "$LMCW"
test -z "$(git status --short)" || { echo 'Working tree is not clean.' >&2; exit 1; }
RECON=results/reconnaissance/classical_six_v1
KEEP_ROOT="$RECON/adjudicated_extractions"
python scripts/review/classical_six_review.py validate \
  --inventory "$RECON/occurrence_inventory.tsv" \
  --review "$RECON/review_adjudicated.json"
python scripts/review/classical_six_review.py filter \
  --inventory "$RECON/occurrence_inventory.tsv" \
  --review "$RECON/review_adjudicated.json" \
  --selected-runs "$RECON/selected-runs.json" --output "$KEEP_ROOT"
```

The helper preserves IDs, filters only by decision (never structural status),
records review provenance/counts, and updates the inventory hash. Inspect every
prepared JSONL before an API call.

## 2. Dry run, then resume the existing batch machinery

```bash
python scripts/pipeline/run_batch.py \
  --manifest data/batches/classical_six_v1.json \
  --annotation-version 0.3.1 --model 5.6 \
  --patterns data/development/search_patterns_v0_6.json \
  --context-chars 1000 --extraction-root "$KEEP_ROOT" \
  --output-root results/batch_runs --dry-run
# Inspect inputs and prove every ID is an adjudicated KEEP.
python scripts/pipeline/run_batch.py \
  --manifest data/batches/classical_six_v1.json \
  --annotation-version 0.3.1 --model 5.6 \
  --patterns data/development/search_patterns_v0_6.json \
  --context-chars 1000 --extraction-root "$KEEP_ROOT" \
  --output-root results/batch_runs
```

Rerun the second command unchanged to resume; do not use `--force` just to
resume. Existing machinery skips valid outputs and records model/pricing,
prompt/schema/extraction hashes, per-occurrence validity/failure, and cost.

## 3. Audit descriptive results

Inspect `summary.json`, `report.md`, `unusual_cases.json`, statuses, and preserved
requests/responses. Report P/T/E/O and ontology-fit distributions, P >= 2, E >=
2, mixed dimensions (two or more P/T/E >= 2), retained occurrence count, and
approximate distinct non-NA scene clusters. Occurrences are annotation units;
clusters are descriptive dependence units. Do not merge them or perform
significance testing. Confirm unchanged IDs join every output to all three Step
19 review stages.

```bash
python -m pytest -q
python scripts/docs/validate_runbook_index.py
git diff --check
git status --short
```
