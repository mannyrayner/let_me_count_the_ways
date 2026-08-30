# Step 6: classify one passage

Run this only after reviewing the extracted records. The first call deliberately
classifies one occurrence, allowing us to inspect the prompt and response before
batching or estimating category proportions.

Select the first Jane Eyre record by its stable occurrence ID and validate the
temporary input. Selecting by ID avoids silently changing the trial if JSONL
ordering changes later:

```bash
cd "$LMCW"
SOURCE_ID='gutenberg-1260'
OCCURRENCE_ID='bronte-jane-eyre-d0cd60fde247'
PASSAGES_FILE="data/development/passages/$SOURCE_ID.jsonl"
CLASSIFICATION_INPUT='results/development_runs/classification_inputs/one_passage.json'
mkdir -p results/development_runs/classification_inputs
python scripts/annotation/prepare_classification_input.py \
  "$PASSAGES_FILE" "$CLASSIFICATION_INPUT" \
  --occurrence-id "$OCCURRENCE_ID"
python -m json.tool "$CLASSIFICATION_INPUT"
```

Make the API request, setting an explicit model available to your API project:

```bash
test -n "${OPENAI_API_KEY:-}" || { echo 'OPENAI_API_KEY is not set'; exit 1; }
python scripts/api/call_responses.py \
  --model '5.6' \
  --prompt prompts/annotation/classify_passage_v0_1.md \
  --input "$CLASSIFICATION_INPUT" \
  --schema prompts/annotation/classification_schema_v0_1.json \
  --output-root results/development_runs/classification
```

Inspect the newest output:

```bash
RUN_DIR="$(find results/development_runs/classification -mindepth 1 \
  -maxdepth 1 -type d | sort | tail -1)"
python -m json.tool "$RUN_DIR/metadata.json"
python -m json.tool "$RUN_DIR/pricing_snapshot.json"
python -m json.tool "$RUN_DIR/cost.json"
python -m json.tool "$RUN_DIR/output.txt" >/dev/null
python scripts/annotation/validate_classification.py "$RUN_DIR/output.txt" \
  --expected-occurrence-id "$OCCURRENCE_ID"
sed -n '1,240p' "$RUN_DIR/output.txt"
```

## Review checkpoint

Stop and share `metadata.json`, `pricing_snapshot.json`, `cost.json`, and
`output.txt`. We should check whether the response conforms to
`classification_schema_v0_1.json`, uses only supplied textual evidence, treats
the three readings independently, and identifies a need for more context or an
inadequate typology naturally. Batch classification should wait until this check
passes.

## Reviewed result

The 2026-08-30 pilot passed structural validation and classified the selected
occurrence primarily as truth-conditional (`4`), with weak performative (`1`)
and exclamatory/reflexive (`1`) support. It distinguished speaker, hearer,
textual, and reader construals; cited supplied evidence; requested no additional
context; judged T/P/E adequate; and reported confidence `0.95`.

The analysis is natural for this passage. Its secondary reassuring and
anti-flattery effects show why label strengths and construal notes are more
informative than a forced single label. One successful easy case does not yet
validate the prompt or ontology; quoted, imagined, and nonromantic occurrences
should be tested before any batch run.

Preserve the input and complete API run after review:

```bash
cd "$LMCW"
RUN_ROOT='results/development_runs/classification'
CLASSIFICATION_INPUT='results/development_runs/classification_inputs/one_passage.json'
find "$RUN_ROOT" -mindepth 2 -maxdepth 2 -type f -print | sort
git add "$CLASSIFICATION_INPUT" "$RUN_ROOT"
git diff --cached --check
git status --short
git commit -m 'Record first Jane Eyre classification trial'
git push origin main
```
