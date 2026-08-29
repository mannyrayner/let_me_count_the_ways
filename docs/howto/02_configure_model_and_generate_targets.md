# Step 2: configure a priced model and generate target candidates

Each top-level API call takes a model alias such as `5.6`. The alias maps to the
exact API model identifier and its current per-million-token prices. This keeps
commands short while allowing different models to be compared without merging
their identity or cost records.

## Verify and record pricing

Open the official pricing page in a browser and verify the exact API model name
and prices:

<https://openai.com/api/pricing/>

Then replace the four values below. Prices are USD per one million tokens. Do not
copy illustrative numbers from another model.

```bash
cd "$LMCW"
python scripts/api/update_model_pricing.py \
  --alias '5.6' \
  --api-model 'REPLACE_WITH_EXACT_API_MODEL_ID' \
  --input REPLACE_WITH_INPUT_PRICE \
  --cached-input REPLACE_WITH_CACHED_INPUT_PRICE \
  --output REPLACE_WITH_OUTPUT_PRICE
python -m json.tool config/api_models.json
```

Pricing is deliberately human-verified rather than scraped from presentation
HTML as though it were a stable price feed. The runner automatically warns when
an entry is older than `stale_after_days` in the catalogue. Re-run the command
whenever a price or API identifier changes; the run itself retains the pricing
snapshot it used. For now, enter standard synchronous Responses API rates;
batch, flex, long-context, or other tiered prices require separate catalogue
support before those modes are used.

## Generate candidates

Confirm the global credential without displaying it, then make one API request:

```bash
cd "$LMCW"
test -n "${OPENAI_API_KEY:-}" || { echo 'OPENAI_API_KEY is not set'; exit 1; }
python scripts/api/call_responses.py \
  --model '5.6' \
  --prompt prompts/ontology_development/target_discovery_v0_1.md \
  --output-root results/development_runs/target_discovery
```

The command prints the new run directory. Inspect the newest run and its cost:

```bash
RUN_DIR="$(find results/development_runs/target_discovery -mindepth 1 \
  -maxdepth 1 -type d | sort | tail -1)"
printf 'Run directory: %s\n' "$RUN_DIR"
python -m json.tool "$RUN_DIR/metadata.json"
python -m json.tool "$RUN_DIR/pricing_snapshot.json"
python -m json.tool "$RUN_DIR/cost.json"
python -m json.tool "$RUN_DIR/response.json" >/dev/null
sed -n '1,240p' "$RUN_DIR/output.txt"
```

If the call fails, inspect the retained error:

```bash
find results/development_runs/target_discovery -name error.txt -print -exec cat {} \;
```

## Review checkpoint

Stop and share `metadata.json`, `pricing_snapshot.json`, `cost.json`, and
`output.txt`. We should check model identity, pricing freshness, candidate
diversity, likely phrase coverage, factual uncertainty, and valid JSON before
approving any source.
