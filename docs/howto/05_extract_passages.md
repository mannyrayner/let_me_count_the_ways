# Step 5: extract passages from one text

Run this after the Step 4 source and its UTF-8 decoding have been approved. Reuse
the exact IDs and language code from the provenance record.

```bash
cd "$LMCW"
WORK_ID='REPLACE_WITH_WORK_ID'
SOURCE_ID='REPLACE_WITH_SOURCE_ID'
LANGUAGE='REPLACE_WITH_ISO_639_1_CODE'
mkdir -p data/development/passages
python scripts/extraction/extract_passages.py \
  "data/raw/$WORK_ID/$SOURCE_ID.txt" \
  "data/development/passages/$SOURCE_ID.jsonl" \
  --language "$LANGUAGE" \
  --work-id "$WORK_ID" \
  --source-id "$SOURCE_ID" \
  --context-chars 1000
wc -l "data/development/passages/$SOURCE_ID.jsonl"
python -m json.tool --json-lines \
  "data/development/passages/$SOURCE_ID.jsonl" | sed -n '1,240p'
```

Check that every stored offset recovers the exact match:

```bash
python - "data/raw/$WORK_ID/$SOURCE_ID.txt" \
  "data/development/passages/$SOURCE_ID.jsonl" <<'PY'
import json, sys, unicodedata
text = unicodedata.normalize('NFC', open(sys.argv[1], encoding='utf-8').read())
with open(sys.argv[2], encoding='utf-8') as stream:
    records = [json.loads(line) for line in stream]
assert all(text[r['start']:r['end']] == r['match'] for r in records)
print(f'Offset check passed for {len(records)} occurrence(s).')
PY
```

## Review checkpoint

Stop and share the occurrence count and JSON for the first few records. We should
inspect false positives, missed spelling variants, boilerplate matches, context
size, and the contribution of this work before sampling or classification.
