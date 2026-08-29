# Step 3: review and approve targets

Run this only after we have reviewed the Step 2 response together. The AI output
is a proposal, not an acquisition manifest: every edition, URL, rights claim,
and likely phrase occurrence still needs verification.

Set the reviewed file path to the corrected JSON file agreed during review:

```bash
cd "$LMCW"
REVIEWED_JSON='REPLACE_WITH_REVIEWED_JSON_PATH'
python -m json.tool "$REVIEWED_JSON" >/dev/null
cp "$REVIEWED_JSON" data/development/target_candidates_v0_1.json
sha256sum data/development/target_candidates_v0_1.json
python -m json.tool data/development/target_candidates_v0_1.json | sed -n '1,240p'
git diff --no-index /dev/null data/development/target_candidates_v0_1.json || true
```

Do not copy `response.json`; it is the API envelope. The reviewed file should be
the candidate JSON itself, based on `output.txt`, with uncertain claims retained
as verification tasks rather than silently converted into facts.

## Review checkpoint

Stop and share the checksum, formatted JSON, and diff. We should select one
specific, clearly reusable edition for the acquisition trial before Step 4.
