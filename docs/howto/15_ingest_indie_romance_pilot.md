# Step 15: ingest the one-work indie-romance pilot

This runbook preserves, converts, reviews, and—only after a final rights
approval—commits *Nikki's Touch* by Ania Cofield. The other two purchased
candidates failed in-book rights inspection and are excluded in
`docs/notes/rights/indie-romance-pilot-exclusions-2026-09-05.md`. Do not copy,
convert, create active provenance for, or commit *The Corners Of My Heart* or
*Error of Understanding*.

The sole active candidate is:

| Work | Work ID | Source ID | Original filename |
| --- | --- | --- | --- |
| *Nikki's Touch* — Ania Cofield | `cofield-nikkis-touch` | `lulu-cofield-nikkis-touch-ebook` | `NikkisTouch.epub` |

Purchase is not permission to redistribute, and the absence of an internal
copyright statement is not evidence that a work is uncopyrighted. The proposed
positive basis is the explicit CC BY designation on the current Lulu listing.
If that evidence is missing, changed, or ambiguous, keep the ebook and derived
text local and stop.

## 1. Preflight and confirm the exclusions

```bash
cd "$LMCW"
git pull --ff-only
test -z "$(git status --short)" || {
  echo 'Working tree is not clean; stop and review it.' >&2
  exit 1
}
python -m pytest -q
sed -n '1,160p' \
  docs/notes/rights/indie-romance-pilot-exclusions-2026-09-05.md
test ! -e data/raw/dumisa-the-corners-of-my-heart
test ! -e data/raw/mcmillan-error-of-understanding
test ! -e data/derived/dumisa-the-corners-of-my-heart
test ! -e data/derived/mcmillan-error-of-understanding
```

If either rejected ebook is already under `data/raw` or `data/derived`, do not
stage it. Move it to secure storage outside the public checkout, confirm the
move, and rerun these gates.

## 2. Recheck the current Lulu licence in a browser

Open the primary product page, not a search snippet or cached third-party page:

```text
https://www.lulu.com/shop/ania-cofield/nikkis-touch/ebook/product-q6d8gkz.html
```

Record the access date and exactly what the live page displays for title,
author, EPUB format, publication year, licence name, and licence link. Follow
the link to the official Creative Commons deed and record its URL/version and
attribution requirements. The expected metadata from the prior review is Ania
Cofield, EPUB, 2025, and Creative Commons Attribution (CC BY); these are facts
to verify, not values to copy mechanically.

Also inspect the purchased EPUB in Thorium Reader. Record whether anything in
the book contradicts the storefront licence and whether the named uploader is
plausibly the author/rightsholder. Do not quote unnecessary copyright text.

If the page is unavailable, no longer says CC BY, does not clearly apply to this
edition, points to an unclear licence, or authorship/rightsholder authority is
implausible, stop. Do not copy the file into the public checkout.

## 3. Copy the purchased EPUB without overwriting it

Replace only the machine-specific source path:

```bash
cd "$LMCW"
NIKKI_EPUB='/replace/with/path/to/NikkisTouch.epub'
NIKKI_SOURCE='data/raw/cofield-nikkis-touch/NikkisTouch.epub'
NIKKI_TEXT='data/derived/cofield-nikkis-touch/lulu-cofield-nikkis-touch-ebook.txt'

test -f "$NIKKI_EPUB" || {
  echo 'NikkisTouch.epub not found; stop.' >&2
  exit 1
}
mkdir -p data/raw/cofield-nikkis-touch
test ! -e "$NIKKI_SOURCE" || {
  echo 'Destination already exists; stop before overwriting.' >&2
  exit 1
}
cp --no-clobber -- "$NIKKI_EPUB" "$NIKKI_SOURCE"
test -f "$NIKKI_SOURCE"
sha256sum "$NIKKI_SOURCE"
chmod a-w "$NIKKI_SOURCE"
```

The copied EPUB is an exact, read-only provenance artifact. Do not redownload,
edit, unzip in place, or replace it after recording its hash.

## 4. Install or locate Calibre on Windows/Cygwin

First check both `PATH` and Calibre's normal Windows location:

```bash
command -v ebook-convert || true
test -x '/cygdrive/c/Program Files/Calibre2/ebook-convert.exe' && \
  echo 'Found Calibre ebook-convert'
```

If neither succeeds, open one of these official Calibre pages in a browser:

```text
https://calibre-ebook.com/download
https://calibre-ebook.com/download_windows64
```

Download the Windows 64-bit installer only from the official Calibre site, run
it normally, accept the default location unless there is a reason not to, and
close and reopen Cygwin. Do not use a third-party download site. The current
Calibre Windows page should be checked for its current operating-system
requirements rather than relying on a copied version claim.

Resolve the executable robustly and record its exact version:

```bash
if command -v ebook-convert >/dev/null 2>&1; then
  EBOOK_CONVERT="$(command -v ebook-convert)"
elif test -x '/cygdrive/c/Program Files/Calibre2/ebook-convert.exe'; then
  EBOOK_CONVERT='/cygdrive/c/Program Files/Calibre2/ebook-convert.exe'
else
  echo 'Calibre ebook-convert not found; install Calibre and reopen Cygwin.' >&2
  exit 1
fi
CALIBRE_VERSION="$("$EBOOK_CONVERT" --version)"
test -n "$CALIBRE_VERSION"
printf '%s\n' "$CALIBRE_VERSION"
```

If a space-containing executable path behaves unexpectedly, retain the quotes
shown around every `$EBOOK_CONVERT` invocation below.

## 5. Convert EPUB to plain UTF-8 text

Create the separate derived directory and refuse overwrite:

```bash
cd "$LMCW"
mkdir -p data/derived/cofield-nikkis-touch
test -f "$NIKKI_SOURCE"
test ! -e "$NIKKI_TEXT" || {
  echo "$NIKKI_TEXT already exists; stop before overwriting." >&2
  exit 1
}
```

Run Calibre's command-line converter:

```bash
"$EBOOK_CONVERT" \
  "$NIKKI_SOURCE" \
  "$NIKKI_TEXT" \
  --txt-output-encoding=utf-8 \
  --txt-output-formatting=plain \
  --max-line-length=0 \
  --newline=unix
```

These options request UTF-8, plain text, no forced maximum line wrapping, and
Unix newlines. Do not add `--smarten-punctuation` or any other punctuation,
semantic, or stylistic transformation. Thorium is for inspection; this Calibre
command is the definitive reproducible conversion.

Record both hashes and the tool version:

```bash
sha256sum "$NIKKI_SOURCE" "$NIKKI_TEXT"
printf '%s\n' "$CALIBRE_VERSION"
```

## 6. Reconvert and prove deterministic output

```bash
TMP_TEXT='data/derived/cofield-nikkis-touch/lulu-cofield-nikkis-touch-ebook.recheck.txt'
test ! -e "$TMP_TEXT" || {
  echo "$TMP_TEXT already exists; inspect and remove it before retrying." >&2
  exit 1
}
"$EBOOK_CONVERT" \
  "$NIKKI_SOURCE" \
  "$TMP_TEXT" \
  --txt-output-encoding=utf-8 \
  --txt-output-formatting=plain \
  --max-line-length=0 \
  --newline=unix
sha256sum "$NIKKI_TEXT" "$TMP_TEXT"
cmp "$NIKKI_TEXT" "$TMP_TEXT"
rm "$TMP_TEXT"
```

If `cmp` fails, retain the recheck file outside Git, document the difference,
and stop. Do not choose one output arbitrarily.

## 7. Inspect conversion quality

```bash
sed -n '1,120p' "$NIKKI_TEXT"
tail -120 "$NIKKI_TEXT"
wc -l -w -c "$NIKKI_TEXT"
grep -nEi '^(chapter|prologue|epilogue)\b' "$NIKKI_TEXT" | head -50 || true
if grep -n $'\uFFFD' "$NIKKI_TEXT"; then
  echo 'Unicode replacement character found; stop and inspect conversion.' >&2
  exit 1
else
  echo 'No Unicode replacement characters found.'
fi
```

Open the EPUB in Thorium and compare the derived text near the beginning,
middle, end, and a dialogue-heavy scene. Confirm chapter order, punctuation,
apostrophes/quotes, complete blocks, no duplicated chapters, and no obvious
navigation content in the prose. Record this review in the rights note below.
Do not manually edit the derived file to fix a problem; stop and document it.

## 8. Explore the target family before production extraction

These diagnostics check conversion integrity and likely counts; they are not the
production extraction:

```bash
grep -Ein -C 2 '\bI[[:space:]]+(do[[:space:]]+)?love[[:space:]]+you\b' \
  "$NIKKI_TEXT" || true
grep -Ein -C 2 \
  '\bI[[:space:]]+(really|still|truly|always|just)[[:space:]]+love[[:space:]]+you\b' \
  "$NIKKI_TEXT" || true
```

Do not widen to arbitrary `love` occurrences. If both searches yield zero,
inspect apostrophes, whitespace, nearby variants, and representative text before
proposing any new versioned production pattern.

## 9. Create the dated rights note

Set the values from the live-page and in-book review, then create the note. Use
the actual official Creative Commons deed URL followed from Lulu.

```bash
RIGHTS_DATE="$(date -u +%Y-%m-%d)"
RIGHTS_NOTE="docs/notes/rights/lulu-cofield-nikkis-touch-$RIGHTS_DATE.md"
LICENSE_WORDING='REPLACE WITH EXACT LULU WORDING'
LICENSE_URL='REPLACE WITH OFFICIAL CREATIVE COMMONS DEED URL'

case "$LICENSE_WORDING" in
  *REPLACE*) echo 'Set LICENSE_WORDING from the live Lulu page; stop.' >&2; exit 1;;
esac
case "$LICENSE_URL" in
  https://creativecommons.org/*) ;;
  *) echo 'Set LICENSE_URL to the official Creative Commons URL; stop.' >&2; exit 1;;
esac
test ! -e "$RIGHTS_NOTE" || {
  echo "$RIGHTS_NOTE already exists; stop before overwriting." >&2
  exit 1
}
mkdir -p docs/notes/rights
cat > "$RIGHTS_NOTE" <<EOF_NOTE
# Rights review: *Nikki's Touch*

- **Reviewed on:** $RIGHTS_DATE
- **Lulu page:** https://www.lulu.com/shop/ania-cofield/nikkis-touch/ebook/product-q6d8gkz.html
- **Displayed title:** *Nikki's Touch*
- **Displayed author:** Ania Cofield
- **Displayed format:** EPUB
- **Displayed publication year:** 2025
- **Displayed licence:** $LICENSE_WORDING
- **Official licence/deed:** $LICENSE_URL
- **Attribution:** Ania Cofield, *Nikki's Touch*, Lulu product page and licence URL above.
- **In-book check:** No statement contradicting the displayed CC BY licence was apparent in the purchased EPUB during review.
- **Rights basis:** Explicit Lulu-displayed CC BY licence, not public-domain expiry and not purchase alone.
- **Conclusion:** Approved for development processing and public repository redistribution, subject to the attribution and licence terms recorded above.
EOF_NOTE
sed -n '1,160p' "$RIGHTS_NOTE"
```

If the evidence does not justify that conclusion, do not run the `cat` block as
written. Create a `rights_review_blocked` note instead, keep full text local, and
stop before provenance or batch membership.

## 10. Create the source provenance record

Capture exact hashes and the previously resolved Calibre version, then generate
the JSON without hand-copying checksums:

```bash
PURCHASED_DATE='REPLACE-IF-KNOWN-OR-USE-UNKNOWN'
ORIGINAL_SHA256="$(sha256sum "$NIKKI_SOURCE" | awk '{print $1}')"
DERIVED_SHA256="$(sha256sum "$NIKKI_TEXT" | awk '{print $1}')"
PROVENANCE='provenance/sources/lulu-cofield-nikkis-touch-ebook.json'
test ! -e "$PROVENANCE" || {
  echo "$PROVENANCE already exists; stop before overwriting." >&2
  exit 1
}
python - "$PROVENANCE" "$ORIGINAL_SHA256" "$DERIVED_SHA256" \
  "$CALIBRE_VERSION" "$PURCHASED_DATE" "$RIGHTS_DATE" \
  "$LICENSE_WORDING" "$LICENSE_URL" "$RIGHTS_NOTE" <<'PY'
import json, sys
from pathlib import Path
(destination, original_hash, derived_hash, calibre_version, purchased_date,
 reviewed_on, licence_name, licence_url, rights_note) = sys.argv[1:]
record = {
    "source_id": "lulu-cofield-nikkis-touch-ebook",
    "work_id": "cofield-nikkis-touch",
    "author": "Ania Cofield",
    "title": "Nikki's Touch",
    "language": "en",
    "publication_year": 2025,
    "repository": "Lulu",
    "source_url": "https://www.lulu.com/shop/ania-cofield/nikkis-touch/ebook/product-q6d8gkz.html",
    "source_page_url": "https://www.lulu.com/shop/ania-cofield/nikkis-touch/ebook/product-q6d8gkz.html",
    "source_type": "purchased ebook",
    "original_format": "EPUB",
    "original_local_path": "data/raw/cofield-nikkis-touch/NikkisTouch.epub",
    "original_sha256": original_hash,
    "local_path": "data/derived/cofield-nikkis-touch/lulu-cofield-nikkis-touch-ebook.txt",
    "sha256": derived_hash,
    "derived_text_path": "data/derived/cofield-nikkis-touch/lulu-cofield-nikkis-touch-ebook.txt",
    "derived_text_sha256": derived_hash,
    "purchased_or_retrieved_date": purchased_date,
    "license_name": licence_name,
    "license_url": licence_url,
    "license_evidence": rights_note,
    "attribution_requirements": "Credit Ania Cofield, identify the work, link the licence, and indicate changes as required by CC BY.",
    "authorship_rightsholder_plausibility_note": "Lulu identifies Ania Cofield as author; reviewed against the purchased EPUB. See rights note.",
    "conversion_tool": "Calibre ebook-convert",
    "conversion_tool_version": calibre_version,
    "conversion_options": ["--txt-output-encoding=utf-8", "--txt-output-formatting=plain", "--max-line-length=0", "--newline=unix"],
    "processing_note": "Calibre EPUB-to-TXT conversion; no punctuation smartening or editorial modernization; deterministic second conversion compared byte-for-byte.",
    "rights_basis": "Explicit Lulu-displayed CC BY licence, not public-domain expiry or purchase alone.",
    "rights_note": "Included on the basis of the explicit Lulu-displayed CC BY licence recorded in the dated rights-review note; not public-domain expiry or purchase alone.",
    "review_status": "approved_for_development_processing",
    "reviewed_on": reviewed_on,
}
Path(destination).write_text(json.dumps(record, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
PY
python -m json.tool "$PROVENANCE"
```

Review every value. The canonical `local_path` and `sha256` fields intentionally
point to the reviewed derived UTF-8 text consumed by the extraction pipeline;
the separate original fields preserve the purchased EPUB provenance.

## 11. Create the one-work batch manifest

```bash
BATCH_MANIFEST='data/batches/indie_romance_pilot_v1.json'
test ! -e "$BATCH_MANIFEST" || {
  echo "$BATCH_MANIFEST already exists; stop before overwriting." >&2
  exit 1
}
cat > "$BATCH_MANIFEST" <<'EOF_BATCH'
{
  "schema_version": "0.1",
  "batch_id": "indie_romance_pilot_v1",
  "description": "One-work exploratory contemporary indie-romance pilot: Nikki's Touch by Ania Cofield.",
  "sources": [
    {
      "provenance": "provenance/sources/lulu-cofield-nikkis-touch-ebook.json"
    }
  ]
}
EOF_BATCH
python -m json.tool "$BATCH_MANIFEST"
```

The manifest contains membership/provenance only. Annotation remains exactly
v0.3.1 later: emotional or sexual context alone does not imply E, relationship
stakes alone do not imply P, deception does not mechanically change core force,
and O retains its high burden.

## 12. Final rights, integrity, and repository gate

```bash
python -m json.tool "$PROVENANCE" >/dev/null
python -m json.tool "$BATCH_MANIFEST" >/dev/null
test "$(sha256sum "$NIKKI_SOURCE" | awk '{print $1}')" = "$ORIGINAL_SHA256"
test "$(sha256sum "$NIKKI_TEXT" | awk '{print $1}')" = "$DERIVED_SHA256"
test -f "$RIGHTS_NOTE"
python -m pytest -q
python scripts/security/scan_credentials.py \
  "$NIKKI_SOURCE" "$NIKKI_TEXT" "$PROVENANCE" "$RIGHTS_NOTE" "$BATCH_MANIFEST"
git status --short
```

Read the rights note once more. A human must explicitly approve that the live
Lulu CC BY evidence applies to this exact EPUB and supports public
redistribution. If it is not clear, add the raw/derived paths to local ignore
configuration (`.git/info/exclude`, not the shared `.gitignore`), commit only an
appropriate blocked review note, and stop.

## 13. Commit only after explicit redistribution approval

Check that the index is initially empty, then stage only the approved active
source, derived text, provenance, rights notes, and one-work manifest:

```bash
test -z "$(git diff --cached --name-only)" || {
  echo 'The index already contains files; stop and review it.' >&2
  exit 1
}
git add \
  data/raw/cofield-nikkis-touch/NikkisTouch.epub \
  data/derived/cofield-nikkis-touch/lulu-cofield-nikkis-touch-ebook.txt \
  provenance/sources/lulu-cofield-nikkis-touch-ebook.json \
  docs/notes/rights/indie-romance-pilot-exclusions-2026-09-05.md \
  "$RIGHTS_NOTE" \
  "$BATCH_MANIFEST"
git diff --cached --check
git diff --cached --stat
python scripts/security/scan_credentials.py $(git diff --cached --name-only)
git commit -m 'Ingest licensed Nikki’s Touch pilot source'
git push origin HEAD
git status --short
```

Confirm neither rejected title appears in the staged paths or commit. Preserve
required attribution and licence links with any later redistributed derivative.

## 14. Stop before extraction and annotation

Share the Lulu rights note, exclusion note, original/derived hashes, Calibre
version/options, deterministic `cmp` result, conversion-quality observations,
exploratory target counts, provenance JSON, manifest, security scan, and clean
Git status. Stop for review before Step 16; do not annotate or acquire a
replacement title in this runbook.
