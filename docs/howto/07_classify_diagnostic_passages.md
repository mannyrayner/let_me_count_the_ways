# Step 7: classify diagnostic Jane Eyre passages

The first pilot was a comparatively straightforward truth-conditional avowal.
Before any batch run, test three cases that stress distinctions already present
in the annotation design. Run **one case at a time** and stop for review after
each API call.

| Substep | Status | Case | Occurrence ID | Primary diagnostic question |
| --- | --- | --- | --- | --- |
| 7A | Completed | Quoted repetition | `bronte-jane-eyre-14913cd0a6a4` | Does the model distinguish Jane’s earlier avowal from Rochester’s present quotation and uptake? |
| 7B | Run next | Imagined utterance | `bronte-jane-eyre-f221719b1af4` | Does the model recognize that “he seemed to say” attributes words that were not spoken aloud? |
| 7C | Blocked pending 7B review | Sisterly love | `bronte-jane-eyre-b57472f62694` | Does the model avoid treating a direct avowal as romantic merely because it says “I love you”? |

## Completed substep 7A

The commands below record the completed 7A setup and are retained for
reproducibility; do not rerun them.

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

The 7A result and preservation review appear below.

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

## Reviewed result and preservation

The 7A result passed validation and is reviewed in
[`docs/notes/diagnostic_classification_review_7a.md`](../notes/diagnostic_classification_review_7a.md).
Preserve the exact input and complete case-specific run before inviting further
commentary or proceeding to 7B:

```bash
cd "$LMCW"
CASE_NAME='quoted_repetition'
OCCURRENCE_ID='bronte-jane-eyre-14913cd0a6a4'
CLASSIFICATION_INPUT="results/development_runs/classification_inputs/$OCCURRENCE_ID.json"
RUN_ROOT="results/development_runs/classification_diagnostics/$CASE_NAME"
find "$RUN_ROOT" -mindepth 2 -maxdepth 2 -type f -print | sort
git add "$CLASSIFICATION_INPUT" "$RUN_ROOT"
git diff --cached --check
git status --short
git commit -m 'Record quoted-repetition diagnostic classification'
git push origin main
git status --short
```

## Working hypothesis after 7A

The current working hypothesis is to keep T/P/E for the core “I love you”
construction while annotating embedding context orthogonally, together with the
effect of that context on interpretation. This is a provisional design direction,
not a schema revision. Continue using the unchanged v0.1 prompt and schema for
7B and 7C so their results remain directly comparable.

## Substep 7B: imagined utterance

Copy and paste this setup block unchanged:

```bash
cd "$LMCW"
SOURCE_ID='gutenberg-1260'
CASE_NAME='imagined_utterance'
OCCURRENCE_ID='bronte-jane-eyre-f221719b1af4'
PASSAGES_FILE="data/development/passages/$SOURCE_ID.jsonl"
CLASSIFICATION_INPUT="results/development_runs/classification_inputs/$OCCURRENCE_ID.json"
RUN_ROOT="results/development_runs/classification_diagnostics/$CASE_NAME"

python scripts/annotation/prepare_classification_input.py \
  "$PASSAGES_FILE" "$CLASSIFICATION_INPUT" \
  --occurrence-id "$OCCURRENCE_ID"
python -m json.tool "$CLASSIFICATION_INPUT"
```

Make one API call with the unchanged v0.1 artifacts:

```bash
test -n "${OPENAI_API_KEY:-}" || { echo 'OPENAI_API_KEY is not set'; exit 1; }
python scripts/api/call_responses.py \
  --model '5.6' \
  --prompt prompts/annotation/classify_passage_v0_1.md \
  --input "$CLASSIFICATION_INPUT" \
  --schema prompts/annotation/classification_schema_v0_1.json \
  --output-root "$RUN_ROOT"
```

Inspect and validate the result:

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

## Review checkpoint for 7B

Stop and share `metadata.json`, `cost.json`, and the complete `output.txt`.
Review whether the result:

- recognizes that the words are attributed through “he seemed to say” and were
  explicitly not spoken “with his lips”;
- separates the interpretation of the represented “I love you” construction
  from the narrator’s embedding of an inferred, unspoken message;
- avoids assigning an actual speaker commitment without textual evidence;
- identifies quotation, attribution, or another missing embedding dimension
  without forcing the case into T/P/E alone;
- requests additional context only for claims the passage cannot settle;
- remains comparable with 7A because the prompt and schema are unchanged.

Do not run 7C or commit the 7B artifacts until this review is complete.
