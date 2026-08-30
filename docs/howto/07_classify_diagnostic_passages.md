# Step 7: classify diagnostic Jane Eyre passages

The first pilot was a comparatively straightforward truth-conditional avowal.
Before any batch run, test three cases that stress distinctions already present
in the annotation design. Run **one case at a time** and stop for review after
each API call.

| Substep | Case | Occurrence ID | Primary diagnostic question |
| --- | --- | --- | --- |
| 7A | Quoted repetition | `bronte-jane-eyre-14913cd0a6a4` | Does the model distinguish Jane’s earlier avowal from Rochester’s present quotation and uptake? |
| 7B | Imagined utterance | `bronte-jane-eyre-f221719b1af4` | Does the model recognize that “he seemed to say” attributes words that were not spoken aloud? |
| 7C | Sisterly love | `bronte-jane-eyre-b57472f62694` | Does the model avoid treating a direct avowal as romantic merely because it says “I love you”? |

## Select one case

For substep 7A, copy and paste this block unchanged:

```bash
cd "$LMCW"
SOURCE_ID='gutenberg-1260'
CASE_NAME='quoted_repetition'
OCCURRENCE_ID='bronte-jane-eyre-14913cd0a6a4'
PASSAGES_FILE="data/development/passages/$SOURCE_ID.jsonl"
CLASSIFICATION_INPUT="results/development_runs/classification_inputs/$OCCURRENCE_ID.json"
RUN_ROOT="results/development_runs/classification_diagnostics/$CASE_NAME"

python scripts/annotation/prepare_classification_input.py \
  "$PASSAGES_FILE" "$CLASSIFICATION_INPUT" \
  --occurrence-id "$OCCURRENCE_ID"
python -m json.tool "$CLASSIFICATION_INPUT"
```

Do not substitute the 7B or 7C values until the preceding result has been
reviewed.

## Make one API call

```bash
test -n "${OPENAI_API_KEY:-}" || { echo 'OPENAI_API_KEY is not set'; exit 1; }
python scripts/api/call_responses.py \
  --model '5.6' \
  --prompt prompts/annotation/classify_passage_v0_1.md \
  --input "$CLASSIFICATION_INPUT" \
  --schema prompts/annotation/classification_schema_v0_1.json \
  --output-root "$RUN_ROOT"
```

## Inspect and validate the result

```bash
RUN_DIR="$(find "$RUN_ROOT" -mindepth 1 -maxdepth 1 -type d | sort | tail -1)"
printf 'Run directory: %s\n' "$RUN_DIR"
python -m json.tool "$RUN_DIR/metadata.json"
python -m json.tool "$RUN_DIR/pricing_snapshot.json"
python -m json.tool "$RUN_DIR/cost.json"
python -m json.tool "$RUN_DIR/output.txt" >/dev/null
python scripts/annotation/validate_classification.py "$RUN_DIR/output.txt" \
  --expected-occurrence-id "$OCCURRENCE_ID"
sed -n '1,260p' "$RUN_DIR/output.txt"
```

## Review checkpoint for 7A

Stop and share `metadata.json`, `cost.json`, and the complete `output.txt`. Review
whether the result:

- separates the earlier speaker’s utterance from the present quoting speaker;
- marks quotation or metalinguistic use when supported;
- represents Rochester’s hearer uptake without replacing Jane’s original
  construal with his;
- distinguishes occurrence function from attributed function;
- requests more context if the supplied passage cannot settle a claim;
- uses `mixed_reading` only for genuinely supported simultaneous readings.

Do not run 7B yet. After 7A is reviewed, this runbook will be instantiated with
the 7B values from the table; the same will happen for 7C only after 7B review.
Preservation and any prompt revision will likewise be specified from the actual
result. This prevents the diagnostic calls from becoming an unreviewed batch.
