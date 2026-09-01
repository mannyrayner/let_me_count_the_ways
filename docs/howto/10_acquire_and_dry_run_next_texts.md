# Step 10: acquire and dry-run the next English and French texts

This step prepares two independent tests of annotation v0.2 without changing
the annotation prompt or schema:

- Louisa May Alcott, *Little Women* (English);
- Gustave Flaubert, *Madame Bovary* (French original).

The Project Gutenberg identifiers and URLs below are **candidates until they
have been checked on the machine performing acquisition**. The Codex execution
environment that prepared this runbook received HTTP 403 responses and could
not inspect the live catalogue pages or downloads. Do not convert the candidate
records into approved provenance merely because the URLs are printed here.

## Pattern decision

Use `data/development/search_patterns_v0_2.json`; do not edit v0.1. The v0.2
English pattern matches both `I love you` and emphatic `I do love you`, including
ordinary whitespace or line breaks, while remaining first-person-to-second-
person. The French patterns retain `je t'aime`/`je t’aime` and `je vous aime`,
case-insensitively and across whitespace where linguistically appropriate. They
deliberately exclude `I love him/her`, `je l'aime`, and other third-person
objects.

Run the pattern regression tests before acquisition:

```bash
cd "$LMCW"
python -m pytest scripts/extraction/test_extract_passages.py -q
```

## Acquire *Little Women* as a provenance draft

```bash
cd "$LMCW"
WORK_ID='alcott-little-women'
SOURCE_ID='gutenberg-514'
SOURCE_URL='https://www.gutenberg.org/cache/epub/514/pg514.txt'
SOURCE_PAGE_URL='https://www.gutenberg.org/ebooks/514'
SOURCE_FILE="data/raw/$WORK_ID/$SOURCE_ID.txt"
PROVENANCE_FILE="provenance/sources/$SOURCE_ID.json"

mkdir -p "data/raw/$WORK_ID" provenance/sources
test ! -e "$SOURCE_FILE" || { echo "Refusing to overwrite $SOURCE_FILE"; exit 1; }
test ! -e "$PROVENANCE_FILE" || { echo "Refusing to overwrite $PROVENANCE_FILE"; exit 1; }
curl --fail --location --retry 3 --output "$SOURCE_FILE" "$SOURCE_URL"

RETRIEVED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
SHA256="$(sha256sum "$SOURCE_FILE" | cut -d' ' -f1)"
python - "$PROVENANCE_FILE" "$SOURCE_FILE" "$RETRIEVED_AT" "$SHA256" <<'PY'
import json
import sys
from pathlib import Path

path, source_file, retrieved_at, checksum = sys.argv[1:]
record = {
    "source_id": "gutenberg-514",
    "work_id": "alcott-little-women",
    "author": "Louisa May Alcott",
    "title": "Little Women",
    "language": "en",
    "repository": "Project Gutenberg",
    "repository_ebook_id": "514",
    "source_url": "https://www.gutenberg.org/cache/epub/514/pg514.txt",
    "source_page_url": "https://www.gutenberg.org/ebooks/514",
    "local_path": source_file,
    "retrieved_at": retrieved_at,
    "sha256": checksum,
    "rights_note": "PENDING: transcribe an edition-specific rights finding from the reviewed source page/header.",
    "review_status": "draft"
}
Path(path).write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
PY
```

## Acquire *Madame Bovary* as a provenance draft

```bash
cd "$LMCW"
WORK_ID='flaubert-madame-bovary'
SOURCE_ID='gutenberg-14155'
SOURCE_URL='https://www.gutenberg.org/cache/epub/14155/pg14155.txt'
SOURCE_PAGE_URL='https://www.gutenberg.org/ebooks/14155'
SOURCE_FILE="data/raw/$WORK_ID/$SOURCE_ID.txt"
PROVENANCE_FILE="provenance/sources/$SOURCE_ID.json"

mkdir -p "data/raw/$WORK_ID" provenance/sources
test ! -e "$SOURCE_FILE" || { echo "Refusing to overwrite $SOURCE_FILE"; exit 1; }
test ! -e "$PROVENANCE_FILE" || { echo "Refusing to overwrite $PROVENANCE_FILE"; exit 1; }
curl --fail --location --retry 3 --output "$SOURCE_FILE" "$SOURCE_URL"

RETRIEVED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
SHA256="$(sha256sum "$SOURCE_FILE" | cut -d' ' -f1)"
python - "$PROVENANCE_FILE" "$SOURCE_FILE" "$RETRIEVED_AT" "$SHA256" <<'PY'
import json
import sys
from pathlib import Path

path, source_file, retrieved_at, checksum = sys.argv[1:]
record = {
    "source_id": "gutenberg-14155",
    "work_id": "flaubert-madame-bovary",
    "author": "Gustave Flaubert",
    "title": "Madame Bovary",
    "language": "fr",
    "repository": "Project Gutenberg",
    "repository_ebook_id": "14155",
    "source_url": "https://www.gutenberg.org/cache/epub/14155/pg14155.txt",
    "source_page_url": "https://www.gutenberg.org/ebooks/14155",
    "local_path": source_file,
    "retrieved_at": retrieved_at,
    "sha256": checksum,
    "rights_note": "PENDING: transcribe an edition-specific rights finding from the reviewed source page/header.",
    "review_status": "draft"
}
Path(path).write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
PY
```

## Edition and rights review checkpoint

For each draft, inspect the live catalogue page in a browser and the downloaded
file. Confirm title, author, original language, ebook identifier, release/update
information, encoding, header/footer boundaries, and the source's rights
statement. Record what the selected edition actually says; do not infer rights
only from the age of the underlying novel.

```bash
for SOURCE_ID in gutenberg-514 gutenberg-14155; do
  PROVENANCE_FILE="provenance/sources/$SOURCE_ID.json"
  SOURCE_FILE="$(python -c 'import json,sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["local_path"])' "$PROVENANCE_FILE")"
  echo "===== $SOURCE_ID ====="
  python -m json.tool "$PROVENANCE_FILE"
  sha256sum "$SOURCE_FILE"
  file "$SOURCE_FILE"
  sed -n '1,45p' "$SOURCE_FILE"
  tail -45 "$SOURCE_FILE"
done
```

Edit each provenance JSON to replace the pending rights note with the reviewed,
edition-specific finding and add observed release/update/format details. Only
after human review, set:

```json
"review_status": "approved_for_development_processing"
```

Then run this approval preflight:

```bash
python - provenance/sources/gutenberg-514.json provenance/sources/gutenberg-14155.json <<'PY'
import hashlib
import json
import sys
from pathlib import Path

for name in sys.argv[1:]:
    path = Path(name)
    record = json.loads(path.read_text(encoding="utf-8"))
    source = Path(record["local_path"])
    assert record["review_status"] == "approved_for_development_processing", path
    assert "PENDING" not in record["rights_note"], path
    assert source.is_file(), source
    assert hashlib.sha256(source.read_bytes()).hexdigest() == record["sha256"], source
    print(f"Approved source passed: {record['title']} ({record['source_id']})")
PY
```

Commit each reviewed source and provenance record before deriving pipeline
artifacts. Separate commits make edition approval easy to audit.

## Dry-run *Little Women*

```bash
python scripts/pipeline/run_single_text_pipeline.py \
  provenance/sources/gutenberg-514.json \
  --patterns data/development/search_patterns_v0_2.json \
  --annotation-version 0.2 \
  --model 5.6 \
  --dry-run
```

## Dry-run *Madame Bovary*

```bash
python scripts/pipeline/run_single_text_pipeline.py \
  provenance/sources/gutenberg-14155.json \
  --patterns data/development/search_patterns_v0_2.json \
  --annotation-version 0.2 \
  --model 5.6 \
  --dry-run
```

For each printed run directory, inspect `manifest.json`, `summary.json`,
`report.md`, `extraction/passages.jsonl`, and every input. Check occurrence
count, exact matched forms, false positives, local context, relative positions,
and chapter/section labels. The pipeline now recognises both `CHAPTER` and
`CHAPITRE`; a null label is acceptable where the source does not expose a cheap,
reliable heading.

## Stop/go decision

Stop before paid annotation if either source cannot be verified, the download
is not the intended original-language edition, decoding is suspect, or matches
show an extraction problem. Preserve the draft and report the issue.

If both dry runs are clean, resume each printed run directory without
`--dry-run` or `--force`. Preserve and check in the complete run directories as
described in Step 9. Do not modify annotation v0.2 in response to an interesting
case; first complete the two independent pressure tests.
