# Step 1: check out and verify the repository

The first block creates the sister checkout if it does not exist:

```bash
mkdir -p /home/github
if test -d "$LMCW/.git"; then
  echo "Checkout already exists at $LMCW"
else
  git clone https://github.com/mannyrayner/let_me_count_the_ways.git "$LMCW"
fi
cd "$LMCW"
printf 'Repository: %s\n' "$PWD"
git remote -v
git status --short
git log -1 --oneline
```

Then run the self-contained verification commands:

```bash
python --version
python -m unittest discover -s scripts/api -p 'test_*.py' -v
python -m unittest discover -s scripts/extraction -p 'test_*.py' -v
python -m json.tool config/api_models.json >/dev/null
python -m json.tool data/development/search_patterns_v0_1.json >/dev/null
python -m json.tool prompts/annotation/classification_schema_v0_1.json >/dev/null
printf '%s\n' 'Checkout and setup checks passed.'
```

## Review checkpoint

Stop and share the terminal output. Do not proceed if `git status --short` shows
unexpected files, the remote is wrong, or any check reports an error.
