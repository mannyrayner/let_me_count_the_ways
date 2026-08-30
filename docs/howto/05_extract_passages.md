# Step 5: extract passages from one text

Run this after the Step 4 source and its UTF-8 decoding have been approved. Reuse
the exact IDs and language code from the provenance record. This instantiation
uses the reviewed Project Gutenberg *Jane Eyre* source from Step 4.

```bash
cd "$LMCW"
WORK_ID='bronte-jane-eyre'
SOURCE_ID='gutenberg-1260'
LANGUAGE='en'
SOURCE_FILE="data/raw/$WORK_ID/$SOURCE_ID.txt"
PROVENANCE_FILE="provenance/sources/$SOURCE_ID.json"
PASSAGES_FILE="data/development/passages/$SOURCE_ID.jsonl"

python - "$SOURCE_FILE" "$PROVENANCE_FILE" <<'PY'
import hashlib
import json
import sys
from pathlib import Path

source = Path(sys.argv[1])
provenance = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
actual_hash = hashlib.sha256(source.read_bytes()).hexdigest()
assert actual_hash == provenance["sha256"], "source checksum does not match provenance"
assert provenance["review_status"] == "approved_for_development_processing"
print(f"Source preflight passed: {actual_hash}")
PY

mkdir -p data/development/passages
python scripts/extraction/extract_passages.py \
  "$SOURCE_FILE" \
  "$PASSAGES_FILE" \
  --language "$LANGUAGE" \
  --work-id "$WORK_ID" \
  --source-id "$SOURCE_ID" \
  --context-chars 1000
wc -l "$PASSAGES_FILE"
python -m json.tool --json-lines "$PASSAGES_FILE" | sed -n '1,240p'
```

Check that every stored offset recovers the exact match:

```bash
python - "$SOURCE_FILE" "$PASSAGES_FILE" <<'PY'
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

## Reviewed result

The 2026-08-30 trial produced six records, and every normalized-text offset
recovered its exact match. The set is substantively useful: it includes romantic
avowals, Rochester’s repetition of Jane’s words, imagined rather than spoken
language, explicitly sisterly love, and a later comparative avowal. Newline-
separated `I\nlove you` was correctly found by the whitespace-aware pattern.

The third record is quoted repetition and the fourth is language Rochester only
“seemed to say”; these are not false positives. They are valuable tests of the
annotation features for quotation, attributed function, and construal. Some
contexts end before the surrounding paragraph does because the 1,000-character
radius was reached, so the classifier must remain able to request more context.

Before classification, preserve the reviewed derived data:

```bash
cd "$LMCW"
PASSAGES_FILE='data/development/passages/gutenberg-1260.jsonl'
python -m json.tool --json-lines "$PASSAGES_FILE" >/dev/null
sha256sum "$PASSAGES_FILE"
git add "$PASSAGES_FILE"
git diff --cached --check
git status --short
git commit -m 'Add initial Jane Eyre passage extraction'
git push origin main
```
