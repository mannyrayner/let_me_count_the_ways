# Step 0: set up and verify

Open a Cygwin terminal. Edit only the Windows path in the first command, then
copy and paste the whole block:

```bash
export LMCW_REPO="$(cygpath 'C:/path/to/let_me_count_the_ways')"
cd "$LMCW_REPO"
printf 'Repository: %s\n' "$PWD"
python --version
git status --short
git log -1 --oneline
python -m unittest discover -s scripts/extraction -p 'test_*.py' -v
python -m json.tool data/development/search_patterns_v0_1.json >/dev/null
python -m json.tool prompts/annotation/classification_schema_v0_1.json >/dev/null
printf '%s\n' 'Setup checks passed.'
```

Expected result: Python 3 is reported, three extraction tests pass, both JSON
checks are silent, and the final line says `Setup checks passed.`

## Review checkpoint

Stop here and share the complete terminal output. Do not proceed if `git status
--short` shows unexpected files or any command reports an error.
