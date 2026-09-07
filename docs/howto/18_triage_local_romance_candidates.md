# Step 18: triage three local romance candidates

This procedure supersedes step 15's instruction to exclude these works **only
for private empirical triage**. It does not approve rights, redistribution,
public excerpts, or annotation. Never stage the ebooks, converted texts, local
provenance, occurrence JSONL, review sheets, or passages produced here.

The candidates are Khulasande Dumisa's *The Corners of My Heart*, Stella
McMillan's *Error of Understanding*, and Marie Cardno's *How to Get a
Girlfriend (When You're a Terrifying Monster)*. Prefer title and author metadata
actually embedded in each supplied file, and record any discrepancy.

## 1. Preflight the local-only boundary

From the repository root, confirm the three workspace roots are ignored before
copying anything:

```bash
cd "$LMCW"
for PATH_TO_CHECK in \
  data/local_candidate_sources/probe \
  data/local_candidate_derived/probe \
  results/local_candidate_triage/probe
do
  git check-ignore -v "$PATH_TO_CHECK" || {
    echo "Not ignored: $PATH_TO_CHECK" >&2
    exit 1
  }
done
git status --short
```

Set the only machine-specific paths and verify the supplied files. Do not
redownload them:

```bash
CORNERS_SOURCE='/replace/with/local/path/to/CornersOfMyHeart.pdf'
ERROR_SOURCE='/replace/with/local/path/to/ErrorOfUnderstanding.epub'
CARDNO_SOURCE='/replace/with/local/path/to/MonsterGirlfriend.epub'

for SOURCE in "$CORNERS_SOURCE" "$ERROR_SOURCE" "$CARDNO_SOURCE"; do
  test -f "$SOURCE" || { echo "Missing source: $SOURCE" >&2; exit 1; }
done
file "$CORNERS_SOURCE"
file "$ERROR_SOURCE"
file "$CARDNO_SOURCE"
```

Record the actual formats. A filename extension is not sufficient evidence of
format.

## 2. Copy without overwriting and record source facts

```bash
mkdir -p \
  data/local_candidate_sources/dumisa-corners-of-my-heart \
  data/local_candidate_sources/mcmillan-error-of-understanding \
  data/local_candidate_sources/cardno-how-to-get-a-girlfriend \
  data/local_candidate_derived/dumisa-corners-of-my-heart \
  data/local_candidate_derived/mcmillan-error-of-understanding \
  data/local_candidate_derived/cardno-how-to-get-a-girlfriend \
  results/local_candidate_triage

CORNERS_COPY='data/local_candidate_sources/dumisa-corners-of-my-heart/CornersOfMyHeart.pdf'
ERROR_COPY='data/local_candidate_sources/mcmillan-error-of-understanding/ErrorOfUnderstanding.epub'
CARDNO_COPY='data/local_candidate_sources/cardno-how-to-get-a-girlfriend/MonsterGirlfriend.epub'
for DESTINATION in "$CORNERS_COPY" "$ERROR_COPY" "$CARDNO_COPY"; do
  test ! -e "$DESTINATION" || { echo "Refusing overwrite: $DESTINATION" >&2; exit 1; }
done
cp --no-clobber -- "$CORNERS_SOURCE" "$CORNERS_COPY"
cp --no-clobber -- "$ERROR_SOURCE" "$ERROR_COPY"
cp --no-clobber -- "$CARDNO_SOURCE" "$CARDNO_COPY"
chmod a-w "$CORNERS_COPY" "$ERROR_COPY" "$CARDNO_COPY"
sha256sum "$CORNERS_COPY" "$ERROR_COPY" "$CARDNO_COPY"
wc -c "$CORNERS_COPY" "$ERROR_COPY" "$CARDNO_COPY"
file "$CORNERS_COPY" "$ERROR_COPY" "$CARDNO_COPY"
git status --short
```

In an ignored local note, record filename, bytes, detected format, SHA-256,
acquisition source/date when known, and `unknown` rather than guesses when not.

## 3. Convert both EPUBs twice with Calibre

```bash
if command -v ebook-convert >/dev/null 2>&1; then
  EBOOK_CONVERT="$(command -v ebook-convert)"
elif test -x '/cygdrive/c/Program Files/Calibre2/ebook-convert.exe'; then
  EBOOK_CONVERT='/cygdrive/c/Program Files/Calibre2/ebook-convert.exe'
else
  echo 'Calibre ebook-convert not found.' >&2
  exit 1
fi
"$EBOOK_CONVERT" --version

convert_epub_twice () {
  SOURCE=$1 OUTPUT=$2 RECHECK="${2%.txt}.recheck.txt"
  test ! -e "$OUTPUT" && test ! -e "$RECHECK" || return 1
  "$EBOOK_CONVERT" "$SOURCE" "$OUTPUT" \
    --txt-output-encoding=utf-8 --txt-output-formatting=plain \
    --max-line-length=0 --newline=unix
  "$EBOOK_CONVERT" "$SOURCE" "$RECHECK" \
    --txt-output-encoding=utf-8 --txt-output-formatting=plain \
    --max-line-length=0 --newline=unix
  sha256sum "$OUTPUT" "$RECHECK"
  cmp "$OUTPUT" "$RECHECK" && rm "$RECHECK"
}

ERROR_TEXT='data/local_candidate_derived/mcmillan-error-of-understanding/text.txt'
CARDNO_TEXT='data/local_candidate_derived/cardno-how-to-get-a-girlfriend/text.txt'
convert_epub_twice "$ERROR_COPY" "$ERROR_TEXT"
convert_epub_twice "$CARDNO_COPY" "$CARDNO_TEXT"
git status --short
```

Do not add smart punctuation or editorial transformations. Stop and diagnose if
either hash pair or `cmp` differs.

## 4. Inspect and convert the PDF text layer

Record `pdftotext -v`. First create both ordinary and layout-preserving
candidates; neither is yet the accepted conversion:

```bash
command -v pdftotext >/dev/null || { echo 'pdftotext not found.' >&2; exit 1; }
pdftotext -v
CORNERS_TEXT='data/local_candidate_derived/dumisa-corners-of-my-heart/text.txt'
CORNERS_LAYOUT='data/local_candidate_derived/dumisa-corners-of-my-heart/text-layout.txt'
pdftotext "$CORNERS_COPY" "$CORNERS_TEXT"
pdftotext -layout "$CORNERS_COPY" "$CORNERS_LAYOUT"
sed -n '1,120p' "$CORNERS_TEXT"
sed -n '1,120p' "$CORNERS_LAYOUT"
```

Compare early, middle, and late output with rendered pages and select the one
with correct literary reading order. If neither text layer is materially
complete and ordered, stop with `drop — extraction/format problem`; do not OCR
or improvise. Delete the rejected version. Re-run the exact selected command to
`text.recheck.txt`, then use `sha256sum` and `cmp` as above. Record the exact
accepted command. Do not manually clean the text.

## 5. Inspect all three conversions

For each accepted text, run:

```bash
for TEXT in "$CORNERS_TEXT" "$ERROR_TEXT" "$CARDNO_TEXT"; do
  sed -n '1,120p' "$TEXT"
  tail -120 "$TEXT"
  wc -l -w -c "$TEXT"
  grep -n $'\uFFFD' "$TEXT" && echo "Replacement character in $TEXT" >&2
done
```

Also inspect internal positions. Check embedded title/author, chapter order,
dialogue punctuation, apostrophes and quotes, missing or duplicated chapters,
navigation/footer pollution, replacement characters, and suspiciously short
output. Compare several EPUB passages in Thorium and early/middle/late PDF
passages against rendered pages. Record discrepancies locally.

## 6. Run diagnostics, then create local provenance

The following searches are diagnostic only:

```bash
for TEXT in "$CORNERS_TEXT" "$ERROR_TEXT" "$CARDNO_TEXT"; do
  grep -Ein '\bI[[:space:]]+(do[[:space:]]+)?love[[:space:]]+you\b' "$TEXT" || true
  grep -Ein '\bI[[:space:]]+(really|still|truly|always|just)[[:space:]]+love[[:space:]]+you\b' "$TEXT" || true
done
```

The block below calculates the six hashes and writes all three ignored records.
It refuses to overwrite an existing record. The title and author values reflect
the expected metadata; if the metadata you inspected in section 5 differs, edit
those literal values in this block before running it.

```bash
CORNERS_PROVENANCE='data/local_candidate_derived/dumisa-corners-of-my-heart/provenance.json'
ERROR_PROVENANCE='data/local_candidate_derived/mcmillan-error-of-understanding/provenance.json'
CARDNO_PROVENANCE='data/local_candidate_derived/cardno-how-to-get-a-girlfriend/provenance.json'

for REQUIRED_FILE in \
  "$CORNERS_COPY" "$ERROR_COPY" "$CARDNO_COPY" \
  "$CORNERS_TEXT" "$ERROR_TEXT" "$CARDNO_TEXT"
do
  test -f "$REQUIRED_FILE" || {
    echo "Missing input: $REQUIRED_FILE" >&2
    exit 1
  }
done
for PROVENANCE in \
  "$CORNERS_PROVENANCE" "$ERROR_PROVENANCE" "$CARDNO_PROVENANCE"
do
  test ! -e "$PROVENANCE" || {
    echo "Refusing overwrite: $PROVENANCE" >&2
    exit 1
  }
done

CORNERS_SOURCE_SHA256="$(sha256sum "$CORNERS_COPY" | cut -d ' ' -f 1)"
ERROR_SOURCE_SHA256="$(sha256sum "$ERROR_COPY" | cut -d ' ' -f 1)"
CARDNO_SOURCE_SHA256="$(sha256sum "$CARDNO_COPY" | cut -d ' ' -f 1)"
CORNERS_TEXT_SHA256="$(sha256sum "$CORNERS_TEXT" | cut -d ' ' -f 1)"
ERROR_TEXT_SHA256="$(sha256sum "$ERROR_TEXT" | cut -d ' ' -f 1)"
CARDNO_TEXT_SHA256="$(sha256sum "$CARDNO_TEXT" | cut -d ' ' -f 1)"

cat > "$CORNERS_PROVENANCE" <<EOF
{
  "review_status": "local_triage_only",
  "source_id": "local-dumisa-corners-of-my-heart-text",
  "work_id": "dumisa-corners-of-my-heart",
  "title": "The Corners of My Heart",
  "author": "Khulasande Dumisa",
  "language": "en",
  "local_path": "$CORNERS_TEXT",
  "sha256": "$CORNERS_TEXT_SHA256",
  "original_source_path": "$CORNERS_COPY",
  "original_source_sha256": "$CORNERS_SOURCE_SHA256",
  "acquisition_note": "Purchased from Lulu; local triage only."
}
EOF

cat > "$ERROR_PROVENANCE" <<EOF
{
  "review_status": "local_triage_only",
  "source_id": "local-mcmillan-error-of-understanding-text",
  "work_id": "mcmillan-error-of-understanding",
  "title": "Error of Understanding",
  "author": "Stella McMillan",
  "language": "en",
  "local_path": "$ERROR_TEXT",
  "sha256": "$ERROR_TEXT_SHA256",
  "original_source_path": "$ERROR_COPY",
  "original_source_sha256": "$ERROR_SOURCE_SHA256",
  "acquisition_note": "Purchased from Lulu; local triage only."
}
EOF

cat > "$CARDNO_PROVENANCE" <<EOF
{
  "review_status": "local_triage_only",
  "source_id": "local-cardno-how-to-get-a-girlfriend-text",
  "work_id": "cardno-how-to-get-a-girlfriend",
  "title": "How to Get a Girlfriend (When You're a Terrifying Monster)",
  "author": "Marie Cardno",
  "language": "en",
  "local_path": "$CARDNO_TEXT",
  "sha256": "$CARDNO_TEXT_SHA256",
  "original_source_path": "$CARDNO_COPY",
  "original_source_sha256": "$CARDNO_SOURCE_SHA256",
  "acquisition_note": "Purchased from Kobo as Monster Girlfriend; local triage only."
}
EOF

for PROVENANCE in \
  "$CORNERS_PROVENANCE" "$ERROR_PROVENANCE" "$CARDNO_PROVENANCE"
do
  python -m json.tool "$PROVENANCE" >/dev/null || exit 1
  git check-ignore -v "$PROVENANCE" || {
    echo "Provenance is not ignored: $PROVENANCE" >&2
    exit 1
  }
done
sha256sum "$CORNERS_COPY" "$CORNERS_TEXT"
sha256sum "$ERROR_COPY" "$ERROR_TEXT"
sha256sum "$CARDNO_COPY" "$CARDNO_TEXT"
git status --short
```

The printed pairs let you compare the source and derived hashes with those
recorded earlier. These are temporary triage records, not permanent rights
provenance.

## 7. Extract locally without model calls

Do **not** change a status to bypass
`run_single_text_pipeline.py`'s production rights gate. The dedicated helper
accepts only `local_triage_only`, verifies the derived hash and Git-ignore
boundary, reuses the production extractor, and has no API/annotation path:

```bash
for LOCAL_PROVENANCE in \
  data/local_candidate_derived/dumisa-corners-of-my-heart/provenance.json \
  data/local_candidate_derived/mcmillan-error-of-understanding/provenance.json \
  data/local_candidate_derived/cardno-how-to-get-a-girlfriend/provenance.json
do
  python scripts/extraction/run_local_candidate_triage.py "$LOCAL_PROVENANCE" \
    --patterns data/development/search_patterns_v0_5.json \
    --output-root results/local_candidate_triage
done
git status --short
```

Each ignored work directory contains bounded-context `occurrences.jsonl`, a
passage-free `manual_review.tsv`, and a manifest recording pattern/hash/count
facts and zero model calls.

## 8. Review every occurrence and summarize

Read every local occurrence context. Fill every review-sheet row with exactly
one of `potentially interesting`, `ordinary avowal`, `embedded`,
`repeated/clustered`, or `unclear`; assign the same scene-cluster identifier to
obvious adjacent repetitions; and note negation, reporting/quotation,
extraction artifacts, and context adequacy. Occurrences remain separate even
when clustered. Do not add P/T/E/O labels.

Create an ignored summary with columns `Work`, `Format`, `Words`, `Candidate
occurrences`, `Distinct scene clusters`, `Potentially interesting`, and
`Recommendation`. The recommendation must be one of:

* `retain for legal/permission review`
* `probably retain`
* `drop — too few occurrences`
* `drop — text too short`
* `drop — extraction/format problem`

Base it on useful data rather than literary quality. Finally run `git status
--short` and `git check-ignore -v` on every source, text, provenance, occurrence,
review, and summary path. Stop before fair-dealing analysis, permission contact,
public excerpt decisions, or annotation.
