# Step 3: acquire one approved text

Run this only after we have approved a specific edition and direct download URL.
Replace every `REPLACE_...` value with the agreed metadata. This trial uses one
text so that provenance and file handling can be reviewed before scaling up.

```bash
WORK_ID='REPLACE_WITH_WORK_ID'
SOURCE_ID='REPLACE_WITH_SOURCE_ID'
LANGUAGE='REPLACE_WITH_ISO_639_1_CODE'
SOURCE_URL='REPLACE_WITH_VERIFIED_DIRECT_TEXT_URL'
RIGHTS_NOTE='REPLACE_WITH_VERIFIED_RIGHTS_STATEMENT_OR_URL'
mkdir -p "data/raw/$WORK_ID" "provenance/sources"
curl --fail --location --retry 3 --output \
  "data/raw/$WORK_ID/$SOURCE_ID.txt" "$SOURCE_URL"
sha256sum "data/raw/$WORK_ID/$SOURCE_ID.txt"
file "data/raw/$WORK_ID/$SOURCE_ID.txt"
```

Create a provenance draft without copying the source’s licence wording from
memory:

```bash
RETRIEVED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
SHA256="$(sha256sum "data/raw/$WORK_ID/$SOURCE_ID.txt" | cut -d' ' -f1)"
cat > "provenance/sources/$SOURCE_ID.json" <<EOF_JSON
{
  "source_id": "$SOURCE_ID",
  "work_id": "$WORK_ID",
  "language": "$LANGUAGE",
  "source_url": "$SOURCE_URL",
  "retrieved_at": "$RETRIEVED_AT",
  "sha256": "$SHA256",
  "rights_note": "$RIGHTS_NOTE",
  "review_status": "draft"
}
EOF_JSON
python -m json.tool "provenance/sources/$SOURCE_ID.json"
```

## Review checkpoint

Stop and share the provenance JSON, checksum output, and the first and last 20
lines of the file:

```bash
sed -n '1,20p' "data/raw/$WORK_ID/$SOURCE_ID.txt"
tail -20 "data/raw/$WORK_ID/$SOURCE_ID.txt"
```

Do not commit the raw text yet. We must confirm that it is the intended edition,
plain text decodes correctly, boilerplate boundaries are understood, and the
rights statement permits the intended storage and processing.
