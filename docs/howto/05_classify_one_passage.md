# Step 5: classify one passage

Run this only after reviewing the extracted records. The first call deliberately
classifies one occurrence, allowing us to inspect the prompt and response before
batching or estimating category proportions.

Select the first record as a temporary input and validate it:

```bash
SOURCE_ID='REPLACE_WITH_SOURCE_ID'
mkdir -p results/development_runs/classification_inputs
head -n 1 "data/development/passages/$SOURCE_ID.jsonl" > \
  results/development_runs/classification_inputs/one_passage.json
python -m json.tool \
  results/development_runs/classification_inputs/one_passage.json
```

Make the API request, setting an explicit model available to your API project:

```bash
read -rsp 'OpenAI API key: ' OPENAI_API_KEY && echo
export OPENAI_API_KEY
export OPENAI_MODEL='REPLACE_WITH_MODEL_ID'
python scripts/api/call_responses.py \
  --prompt prompts/annotation/classify_passage_v0_1.md \
  --input results/development_runs/classification_inputs/one_passage.json \
  --schema prompts/annotation/classification_schema_v0_1.json \
  --output-root results/development_runs/classification
unset OPENAI_API_KEY
```

Inspect the newest output:

```bash
RUN_DIR="$(find results/development_runs/classification -mindepth 1 \
  -maxdepth 1 -type d | sort | tail -1)"
python -m json.tool "$RUN_DIR/metadata.json"
sed -n '1,240p' "$RUN_DIR/output.txt"
```

## Review checkpoint

Stop and share `metadata.json` and `output.txt`. We should check whether the
response conforms to `classification_schema_v0_1.json`, uses only supplied
textual evidence, treats the three readings independently, and identifies a
need for more context or an inadequate typology naturally. Batch classification
should wait until this check passes.
