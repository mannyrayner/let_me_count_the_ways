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

## Expected review findings for this trial

The reviewed 2026-08-30 download had SHA-256
`13414dee2951c3ee731d76d2ffd822016b2479c892162760c5d0eb2aa5fa7631` and was
reported by `file` as UTF-8 Unicode text with CRLF line endings. Its header
identified *Jane Eyre: An Autobiography*, Charlotte Brontë, ebook 1260, a
1998-03-01 release date, and a 2025-09-27 update date. Its footer contained the
Project Gutenberg licence text.

CRLF line endings are not an error. Preserve them in the raw download; Python’s
text reader will normalize line endings when the later extraction stage creates
derived records. Likewise, rerunning `curl --output` replaced the interrupted
partial download rather than appending to it, so the final checksum pins the
complete file that was reviewed.

## Approve and preserve the source

After the review findings match, enrich the provenance record without changing
the raw text, mark it approved for development processing, and commit both files:

```bash
cd "$LMCW"
WORK_ID='bronte-jane-eyre'
SOURCE_ID='gutenberg-1260'
SOURCE_FILE="data/raw/$WORK_ID/$SOURCE_ID.txt"
PROVENANCE_FILE="provenance/sources/$SOURCE_ID.json"

python - "$PROVENANCE_FILE" <<'PY'
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
record = json.loads(path.read_text(encoding="utf-8"))
record.update({
    "gutenberg_release_date": "1998-03-01",
    "gutenberg_last_updated": "2025-09-27",
    "observed_format": "UTF-8 Unicode text with CRLF line endings",
    "review_status": "approved_for_development_processing",
    "reviewed_on": "2026-08-30"
})
path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8")
PY

test "$(sha256sum "$SOURCE_FILE" | cut -d' ' -f1)" = \
  '13414dee2951c3ee731d76d2ffd822016b2479c892162760c5d0eb2aa5fa7631'
python -m json.tool "$PROVENANCE_FILE"
git add "$SOURCE_FILE" "$PROVENANCE_FILE"
git diff --cached --check -- . ':(exclude)data/raw/**'
git status --short
git commit -m 'Add Project Gutenberg Jane Eyre source'
git push origin main
```

This approval is limited to the initial development pipeline. It does not turn
Project Gutenberg’s US determination or the recorded Australian guidance into a
general legal conclusion for other editions, jurisdictions, or uses.
