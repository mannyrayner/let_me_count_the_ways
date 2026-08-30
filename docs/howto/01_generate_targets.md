# Step 1: generate target candidates

This step makes one API request using the versioned target-discovery prompt. It
stores request metadata, the exact request, the raw API response, and extracted
output text in a timestamped directory.

Start from the repository root. Set the model explicitly to a model available to
your API project; do not rely on a changing default.

```bash
read -rsp 'OpenAI API key: ' OPENAI_API_KEY && echo
export OPENAI_API_KEY
export OPENAI_MODEL='REPLACE_WITH_MODEL_ID'
python scripts/api/call_responses.py \
  --prompt prompts/ontology_development/target_discovery_v0_1.md \
  --output-root results/development_runs/target_discovery
unset OPENAI_API_KEY
```

The command prints the new run directory. Capture and inspect the newest run:

```bash
RUN_DIR="$(find results/development_runs/target_discovery -mindepth 1 \
  -maxdepth 1 -type d | sort | tail -1)"
printf 'Run directory: %s\n' "$RUN_DIR"
python -m json.tool "$RUN_DIR/metadata.json"
python -m json.tool "$RUN_DIR/response.json" >/dev/null
sed -n '1,240p' "$RUN_DIR/output.txt"
```

If the API call fails, inspect the retained error without exposing the API key:

```bash
find results/development_runs/target_discovery -name error.txt -print -exec cat {} \;
```

## Review checkpoint

Stop here and share `metadata.json` and `output.txt`. Do not approve sources or
start downloads yet. We should first check candidate diversity, likely phrase
coverage, factual uncertainty, and whether the returned text is valid JSON.
