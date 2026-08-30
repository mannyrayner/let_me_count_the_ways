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
python - "$PASSAGES_FILE" "$CLASSIFICATION_INPUT" "$OCCURRENCE_ID" <<'PY'
import json
import sys
from pathlib import Path

source = Path(sys.argv[1])
destination = Path(sys.argv[2])
occurrence_id = sys.argv[3]
records = [json.loads(line) for line in source.read_text(encoding="utf-8").splitlines()]
selected = [record for record in records if record["occurrence_id"] == occurrence_id]
assert len(selected) == 1, f"expected one {occurrence_id} record, found {len(selected)}"
destination.write_text(json.dumps(selected[0], ensure_ascii=False) + "\n",
                       encoding="utf-8")
PY
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
sed -n '1,240p' "$RUN_DIR/output.txt"
```

## Review checkpoint

Stop and share `metadata.json`, `pricing_snapshot.json`, `cost.json`, and
`output.txt`. We should check whether the response conforms to
`classification_schema_v0_1.json`, uses only supplied textual evidence, treats
the three readings independently, and identifies a need for more context or an
inadequate typology naturally. Batch classification should wait until this check
passes.
