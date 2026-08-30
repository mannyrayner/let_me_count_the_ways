# Step 4: acquire one approved text

The first acquisition trial uses Charlotte Brontë’s *Jane Eyre*, Project
Gutenberg ebook 1260. This is a high-familiarity English candidate with a direct
plain-text download and an edition landing page that states the source’s US
rights status. The Australian basis recorded below is a provisional research
note, not legal advice; it must remain linked to its supporting guidance.

```bash
cd "$LMCW"
WORK_ID='bronte-jane-eyre'
SOURCE_ID='gutenberg-1260'
LANGUAGE='en'
SOURCE_URL='https://www.gutenberg.org/cache/epub/1260/pg1260.txt'
SOURCE_PAGE_URL='https://www.gutenberg.org/ebooks/1260'
RIGHTS_GUIDANCE_URL='https://www.copyright.com.au/about-copyright/duration/'
RIGHTS_NOTE='Project Gutenberg ebook #1260 is marked public domain in the USA: https://www.gutenberg.org/ebooks/1260 ; Australian Copyright Agency guidance says published text is out of copyright in Australia when published before 1955 and the creator died before 1955: https://www.copyright.com.au/about-copyright/duration/'

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
  "author": "Charlotte Brontë",
  "title": "Jane Eyre",
  "language": "$LANGUAGE",
  "repository": "Project Gutenberg",
  "repository_ebook_id": "1260",
  "source_url": "$SOURCE_URL",
  "source_page_url": "$SOURCE_PAGE_URL",
  "retrieved_at": "$RETRIEVED_AT",
  "sha256": "$SHA256",
  "rights_note": "$RIGHTS_NOTE",
  "rights_guidance_url": "$RIGHTS_GUIDANCE_URL",
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
