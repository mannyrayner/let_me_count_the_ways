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

## 3. Aggregate and audit descriptive results

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

Stop after annotation and descriptive reporting. Do not acquire more works.
Manny and ChatGPT will next inspect corpus size, language/genre/period balance,
P/T/E distributions, scene dependence, and rare high-P/high-E cases before
making another corpus-design decision.
