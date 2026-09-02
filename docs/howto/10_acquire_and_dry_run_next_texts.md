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

### Required provenance fields before check-in

An approved record must preserve more than the checksum and a prose rights
conclusion. Before committing, add the following edition-level fields from the
downloaded header, live catalogue page, and local review:

- `gutenberg_release_date`;
- `gutenberg_last_updated`;
- `observed_format` (the output of `file`, including line-ending observations
  where relevant);
- `rights_guidance_url` (the exact Australian guidance page actually reviewed);
- `reviewed_on` (UTC calendar date).

The `rights_note` should identify its sources rather than merely naming an
institution. It should record the publication and author-death facts used in
the Australian assessment and where those facts were checked, rather than only
saying that an independent determination occurred. Keep the Project Gutenberg
warning and the independently reviewed Australian basis distinct. This is a
provenance record, not legal advice.

For the downloads retrieved on 2026-09-01, the collaborator reported these
checksums:

```text
gutenberg-514    677d034b4a3d1cea92d075939878f852a7a3ec757dc9ed05ef0c40cab5c1e6de
gutenberg-14155  93f0a2259dbaf5fde6e7b96adc22346d52f80eb1e9319336c8381a045efe40cd
```

These hashes identify those downloads; they do not independently establish
edition identity or rights. After adding the fields above, run the following
pre-commit audit. It checks the exact reported files, hashes, source identities,
required metadata, Project Gutenberg boundary text, and absence of credentials:

```bash
cd "$LMCW"
test -z "$(git diff --cached --name-only)" || {
  echo 'The index already contains staged files; review or unstage them first.' >&2
  exit 1
}

python - <<'PY'
import hashlib
import json
from pathlib import Path

expected = {
    "gutenberg-514": {
        "work_id": "alcott-little-women",
        "author": "Louisa May Alcott",
        "title": "Little Women",
        "language": "en",
        "local_path": "data/raw/alcott-little-women/gutenberg-514.txt",
        "sha256": "677d034b4a3d1cea92d075939878f852a7a3ec757dc9ed05ef0c40cab5c1e6de",
    },
    "gutenberg-14155": {
        "work_id": "flaubert-madame-bovary",
        "author": "Gustave Flaubert",
        "title": "Madame Bovary",
        "language": "fr",
        "local_path": "data/raw/flaubert-madame-bovary/gutenberg-14155.txt",
        "sha256": "93f0a2259dbaf5fde6e7b96adc22346d52f80eb1e9319336c8381a045efe40cd",
    },
}
required_review_fields = {
    "gutenberg_release_date", "gutenberg_last_updated", "observed_format",
    "rights_guidance_url", "reviewed_on",
}

for source_id, wanted in expected.items():
    provenance_path = Path("provenance/sources") / f"{source_id}.json"
    record = json.loads(provenance_path.read_text(encoding="utf-8"))
    assert record["source_id"] == source_id
    assert record["repository"] == "Project Gutenberg"
    assert record["repository_ebook_id"] == source_id.removeprefix("gutenberg-")
    for key, value in wanted.items():
        assert record[key] == value, (source_id, key, record[key], value)
    missing = required_review_fields - record.keys()
    assert not missing, f"{source_id} lacks review fields: {sorted(missing)}"
    assert record["review_status"] == "approved_for_development_processing"
    assert "PENDING" not in record["rights_note"]
    assert record["rights_guidance_url"].startswith("https://")

    source_path = Path(record["local_path"])
    raw = source_path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == record["sha256"]
    text = raw.decode("utf-8")
    upper = text.upper()
    assert "PROJECT GUTENBERG EBOOK" in upper
    assert "START OF" in upper and "END OF" in upper
    print(f"Source audit passed: {record['title']} ({source_id})")
PY

python scripts/security/scan_credentials.py \
  provenance/sources/gutenberg-514.json \
  provenance/sources/gutenberg-14155.json \
  data/raw/alcott-little-women/gutenberg-514.txt \
  data/raw/flaubert-madame-bovary/gutenberg-14155.txt
```

This repository-native scanner has no `ripgrep` dependency. It fails nonzero
when a likely credential is found, a path is missing, or a file cannot be read;
it cannot silently turn a missing scanner command into a successful result.
Do not wrap an optional external scanner as `if scanner ...; then ...; else
passed; fi`: Bash treats “command not found” as a false condition and therefore
runs that misleading success branch.

Inspect the headers and provenance one final time:

```bash
for SOURCE_ID in gutenberg-514 gutenberg-14155; do
  PROVENANCE_FILE="provenance/sources/$SOURCE_ID.json"
  SOURCE_FILE="$(python -c 'import json,sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["local_path"])' "$PROVENANCE_FILE")"
  echo "===== $SOURCE_ID ====="
  python -m json.tool "$PROVENANCE_FILE"
  sed -n '1,45p' "$SOURCE_FILE"
  tail -45 "$SOURCE_FILE"
done
```

Commit the two editions separately, then update the living source inventory:

```bash
git add \
  data/raw/alcott-little-women/gutenberg-514.txt \
  provenance/sources/gutenberg-514.json
git diff --cached --check -- . ':(exclude)data/raw/**'
git diff --cached --stat
git status --short
git commit -m 'Add Project Gutenberg Little Women source'

git add \
  data/raw/flaubert-madame-bovary/gutenberg-14155.txt \
  provenance/sources/gutenberg-14155.json
git diff --cached --check -- . ':(exclude)data/raw/**'
git diff --cached --stat
git status --short
git commit -m 'Add Project Gutenberg Madame Bovary source'

python - <<'PY'
from pathlib import Path

path = Path("provenance/required_sources.md")
text = path.read_text(encoding="utf-8")
replacements = {
    "### Louisa May Alcott, *Little Women* — `locating`":
        "### Louisa May Alcott, *Little Women* — `cleared`",
    "### Gustave Flaubert, *Madame Bovary* — `locating`":
        "### Gustave Flaubert, *Madame Bovary* — `cleared`",
}
for old, new in replacements.items():
    assert old in text, old
    text = text.replace(old, new, 1)
path.write_text(text, encoding="utf-8")
PY
git add provenance/required_sources.md
git diff --cached --check
git diff --cached --stat
git commit -m 'Mark next development sources cleared'

git push origin HEAD
git status --short
```

Do not continue to the dry runs until all three commits succeed and the working
tree contains no unexpected source or provenance changes.

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
