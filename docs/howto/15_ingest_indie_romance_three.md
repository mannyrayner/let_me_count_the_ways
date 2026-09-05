# Step 15: ingest and verify the three purchased indie-romance sources

This runbook preserves Manny's three exact files, verifies current licensing,
derives UTF-8 literary text reproducibly, and creates provenance records. It
does not download books from Lulu, annotate text, or authorize public
redistribution merely because a file was purchased.

The intended IDs are:

| Work | Work ID | Source ID | Original filename |
| --- | --- | --- | --- |
| *The Corners Of My Heart* — Khulasande Dumisa | `dumisa-the-corners-of-my-heart` | `lulu-dumisa-corners-of-my-heart-ebook` | `CornersOfMyHeart.pdf` |
| *Error of Understanding* — Stella McMillan | `mcmillan-error-of-understanding` | `lulu-mcmillan-error-of-understanding-ebook` | `ErrorOfUnderstanding.epub` |
| *Nikki's Touch* — Ania Cofield | `cofield-nikkis-touch` | `lulu-cofield-nikkis-touch-ebook` | `NikkisTouch.epub` |

## 1. Preflight

```bash
cd "$LMCW"
git pull --ff-only
test -z "$(git status --short)" || {
  echo 'Working tree is not clean; stop and review it.' >&2
  exit 1
}
python -m pytest -q
```

Complete Step 14 first. Work on a local branch. Until the rights review below
is approved, keep all ebook binaries and derived full text untracked; check
`.gitignore` before copying and use `git status --short` after every stage.

## 2. Copy the user-supplied originals without overwriting

Set each variable to Manny's existing local file. `cp --no-clobber` copies; it
does not move or alter the supplied original.

```bash
cd "$LMCW"
CORNERS_PDF='/replace/with/path/to/CornersOfMyHeart.pdf'
ERROR_EPUB='/replace/with/path/to/ErrorOfUnderstanding.epub'
NIKKI_EPUB='/replace/with/path/to/NikkisTouch.epub'

test -f "$CORNERS_PDF" && test -f "$ERROR_EPUB" && test -f "$NIKKI_EPUB" || {
  echo 'One or more supplied paths are not regular files; stop.' >&2
  exit 1
}
mkdir -p data/raw/dumisa-the-corners-of-my-heart \
  data/raw/mcmillan-error-of-understanding \
  data/raw/cofield-nikkis-touch
for DESTINATION in \
  data/raw/dumisa-the-corners-of-my-heart/CornersOfMyHeart.pdf \
  data/raw/mcmillan-error-of-understanding/ErrorOfUnderstanding.epub \
  data/raw/cofield-nikkis-touch/NikkisTouch.epub
do
  test ! -e "$DESTINATION" || {
    echo "Refusing to overwrite $DESTINATION" >&2
    exit 1
  }
done
cp --no-clobber -- "$CORNERS_PDF" \
  data/raw/dumisa-the-corners-of-my-heart/CornersOfMyHeart.pdf
cp --no-clobber -- "$ERROR_EPUB" \
  data/raw/mcmillan-error-of-understanding/ErrorOfUnderstanding.epub
cp --no-clobber -- "$NIKKI_EPUB" \
  data/raw/cofield-nikkis-touch/NikkisTouch.epub

sha256sum \
  data/raw/dumisa-the-corners-of-my-heart/CornersOfMyHeart.pdf \
  data/raw/mcmillan-error-of-understanding/ErrorOfUnderstanding.epub \
  data/raw/cofield-nikkis-touch/NikkisTouch.epub \
  | tee indie-romance-original-sha256.local.txt
chmod a-w \
  data/raw/dumisa-the-corners-of-my-heart/CornersOfMyHeart.pdf \
  data/raw/mcmillan-error-of-understanding/ErrorOfUnderstanding.epub \
  data/raw/cofield-nikkis-touch/NikkisTouch.epub
```

Keep `indie-romance-original-sha256.local.txt` local until its eventual
provenance fields and repository policy have been reviewed. Compare file sizes
and hashes with any purchase/download records Manny retains.

## 3. Verify licensing from current primary pages

Open and save a dated review note for each current Lulu listing:

- `https://www.lulu.com/shop/khulasande-dumisa/the-corners-of-my-heart/ebook/product-j2vrjn.html`
- `https://www.lulu.com/shop/stella-mcmillan/error-of-understanding/ebook/product-14nwnw5e.html`
- `https://www.lulu.com/shop/ania-cofield/nikkis-touch/ebook/product-q6d8gkz.html`

For each, record the access date, exact title/author/format/year, displayed
licence name and link, and evidence that the licence applies to the supplied
ebook edition. Follow the licence link to the official Creative Commons deed
and record its version and attribution/ShareAlike requirements. Assess whether
the named uploader appears plausibly to be the author/rightsholder; a storefront
label alone does not prove authority.

The handoff reports CC BY-SA for *Corners* and CC BY for the other two. Treat
those as claims to verify, not established provenance. Purchase alone is not a
redistribution licence. If the page is unavailable, metadata differs, scope is
unclear, or authorship/rightsholder authority is doubtful, mark the work
`rights_review_blocked`, keep full files local, and stop public ingestion for
that work. Do not commit page captures whose own terms do not permit it.

## 4. Convert deterministically, never in place

First record tool names and exact versions. Implement conversion as a tested
local script rather than retaining an unrepeatable chain of shell filters.

For the PDF, first use a PDF-inspection tool to confirm an embedded selectable
text layer. If present, extract that layer to a separate UTF-8 file. Do not OCR.
If it is absent, reordered, or materially incomplete, document the fault and
stop before proposing a fallback.

For each EPUB, validate the ZIP/container, locate the package document, parse
its manifest and spine, and extract XHTML in spine reading order. Do not sort
archive filenames. Exclude navigation/container metadata, retain literary
headings and paragraph boundaries, decode declared encodings, and emit
normalized UTF-8 text with documented newline/whitespace-only cleaning.

Use these derived paths:

```text
data/derived/dumisa-the-corners-of-my-heart/lulu-dumisa-corners-of-my-heart-ebook.txt
data/derived/mcmillan-error-of-understanding/lulu-mcmillan-error-of-understanding-ebook.txt
data/derived/cofield-nikkis-touch/lulu-cofield-nikkis-touch-ebook.txt
```

The converter must refuse overwrite unless an explicit reviewed force option is
given, write atomically, and emit conversion provenance including input/output
hashes, tool versions, spine order (EPUB), PDF page/text-layer findings, and all
transformations. Re-run into a temporary directory and verify identical hashes.

## 5. Inspect conversion quality

For every derived work, inspect the beginning, ending, several internal
chapters/scenes, and chapter transitions. Confirm title/author, complete chapter
order, adequate dialogue punctuation, and absence of missing sections. For the
PDF, compare samples from early/middle/late pages with the rendered source and
look for column/order errors. For EPUBs, compare the recorded spine with the
table of contents and inspect nonlinear/nav exclusions. Search for repeated
headers/footers, replacement characters, page numbers inside sentences, and
suspiciously short output.

Record observations; do not “clean” content manually. Any new transformation
belongs in the converter, its tests, and conversion record.

## 6. Create and review provenance

Create one JSON record under `provenance/sources/` per source ID. Include source
and work IDs, exact bibliographic metadata, language `en`, Lulu platform and
listing URL, `purchased ebook`, original format/path/hash, derived path/hash,
known purchase/retrieval date, displayed licence and official licence URL,
attribution requirements, authorship/licensing evidence and caveats, conversion
method/version/transformations, and review status.

Explicitly state that these sources rely on an asserted explicit licence, not
public-domain expiry. Create `data/batches/indie_romance_three_v1.json` with
only the three provenance references; model and annotation version do not
belong in the membership manifest.

```bash
cd "$LMCW"
python -m json.tool provenance/sources/lulu-dumisa-corners-of-my-heart-ebook.json >/dev/null
python -m json.tool provenance/sources/lulu-mcmillan-error-of-understanding-ebook.json >/dev/null
python -m json.tool provenance/sources/lulu-cofield-nikkis-touch-ebook.json >/dev/null
python -m json.tool data/batches/indie_romance_three_v1.json >/dev/null
python -m pytest -q
python scripts/security/scan_credentials.py
git status --short
```

## 7. Redistribution gate and review checkpoint

Do not `git add` any original or full derived ebook until a human has approved,
for each edition: licence identity/scope, rightsholder plausibility, required
attribution, and (for CC BY-SA) the treatment and licensing of redistributed
adapted material. If approval is ambiguous, retain local-only paths/hashes,
ensure ignore rules prevent accidental commits, and decide separately whether
limited passages and annotations are permissible.

Stop and share the three rights notes, hashes, conversion records, inspection
notes, provenance JSON, proposed batch manifest, and `git status --short`.
Proceed only with the works explicitly approved for processing and the precise
repository artifacts explicitly approved for redistribution.
