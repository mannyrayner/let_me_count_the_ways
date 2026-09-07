# Step 19: acquire and reconnoitre the classical six

This runbook acquires and rights-reviews six original-language classical works,
then makes reviewed extraction-only inventories. It stops before annotation.
The balanced membership is two English, two Norwegian, and two French works.
Its research motivations are social constraint and renunciation (*The Age of
Innocence*), embodiment and volatility (*Women in Love*), frustrated courtship,
class, and jealousy (*Victoria*), passionate instability (*Pan*), sacrifice and
social constraint (*La Dame aux camélias*), and avowal divided from sustained
commitment (*Adolphe*). These motivations are never annotation labels or prompt
inputs. Annotation v0.3.1 remains frozen and is not called by this procedure.

## 1. Preflight and immutable membership

```bash
cd "$LMCW"
git pull --ff-only
test -z "$(git status --short)" || { echo 'Working tree is not clean.' >&2; exit 1; }
BATCH=data/batches/classical_six_v1.json
PATTERNS=data/development/search_patterns_v0_5.json
python -m json.tool "$BATCH" >/dev/null
python -m json.tool "$PATTERNS" >/dev/null
python scripts/docs/validate_runbook_index.py
python -m pytest -q
```

The batch manifest contains only identity, description, and provenance paths.
Confirm that no model, annotation, prompt, or pattern version leaked into it:

```bash
python - "$BATCH" <<'PY'
import json,sys
m=json.load(open(sys.argv[1],encoding='utf-8'))
assert set(m)=={'schema_version','batch_id','description','sources'}
assert m['batch_id']=='classical_six_v1' and len(m['sources'])==6
assert len({x['provenance'] for x in m['sources']})==6
print('\n'.join(x['provenance'] for x in m['sources']))
PY
```

## 2. Resolve and record the live catalogue editions

Open the four catalogue pages and verify title, author, language, public-domain
statement, and the current UTF-8 plain-text link. The French records must be
French, and `gutenberg-2419.json` must identify Alexandre Dumas **fils** and
preserve *La Dame aux camélias* with its accent.

```bash
for ID in 541 4240 2419 13861; do
  cygstart "https://www.gutenberg.org/ebooks/$ID"
done
```

Record each exact link in the matching provenance `source_url`; do not infer a
URL without checking the catalogue. Record the catalogue metadata and update
dates before downloading. Use the Australian Copyright Agency duration guidance
in addition to Gutenberg's US statement. The relevant author death years are
Wharton 1937, Lawrence 1930, Dumas fils 1895, and Constant 1830.

Open the Runeberg collection and copyright pages. From the live contents of
*Samlede verker*, sixth edition (1963–1964), obtain the volume URL and actual URL
indices linked for printed pages 89–162 in volume 3 (*Victoria*) and 331–423 in
volume 2 (*Pan*). Record both printed and URL-index ranges in provenance.

```bash
cygstart 'https://runeberg.org/'
cygstart 'https://runeberg.org/admin/copyright.html'
```

Do not assume printed page 89 means `0089.html`. In a browser verify the linked
first and last pages and both adjacent pages: each first page begins the named
work, each last page ends it, and its neighbours belong to other material. The
literary files must exclude *Siesta*, *I æventyrland*, *Redaktør Lynge*, and *Ny
jord*. Record the National Library scan/Runeberg OCR basis, possible modernized
spelling, possibly unproofread OCR, and Hamsun's 1952 death year. Do not claim
first-edition orthography.

## 3. Acquire the four Gutenberg texts atomically

Set the four verified catalogue download URLs (examples must not replace live
verification), then use the shared helper. It refuses overwrites, downloads via
`.part`, preserves the raw response, requires explicit Gutenberg START/END
markers, and prints hashes for the provenance records.

```bash
URL_541='PASTE_VERIFIED_UTF8_URL'
URL_4240='PASTE_VERIFIED_UTF8_URL'
URL_2419='PASTE_VERIFIED_UTF8_URL'
URL_13861='PASTE_VERIFIED_UTF8_URL'
for SPEC in \
  "541 wharton-age-of-innocence $URL_541" \
  "4240 lawrence-women-in-love $URL_4240" \
  "2419 dumas-fils-la-dame-aux-camelias $URL_2419" \
  "13861 constant-adolphe $URL_13861"
do
  set -- $SPEC; ID=$1; WORK=$2; URL=$3
  test "$URL" != PASTE_VERIFIED_UTF8_URL || { echo "Set URL_$ID" >&2; exit 1; }
  python scripts/corpus_acquisition/acquire_public_domain_text.py gutenberg \
    --url "$URL" --raw "data/raw/$WORK/source-download.txt" \
    --output "data/raw/$WORK/gutenberg-$ID.txt" \
    > "data/raw/$WORK/acquisition-metadata.json"
done
```

Copy the emitted exact URLs, paths, and SHA-256 values into provenance. Preserve
raw downloads and derived texts. Never trim by approximate line counts.

## 4. Acquire the two verified Runeberg ranges

Only after the boundary review, set the exact volume bases and URL indices. The
helper constructs zero-padded URLs deterministically, preserves every HTML page,
rejects failed/empty responses, extracts visible OCR text without correcting it,
concatenates in numeric order, and emits page lists and hashes.

```bash
VICTORIA_VOLUME='PASTE_VERIFIED_VOLUME_URL'
VICTORIA_FIRST_URL_INDEX='PASTE_INTEGER'; VICTORIA_LAST_URL_INDEX='PASTE_INTEGER'
PAN_VOLUME='PASTE_VERIFIED_VOLUME_URL'
PAN_FIRST_URL_INDEX='PASTE_INTEGER'; PAN_LAST_URL_INDEX='PASTE_INTEGER'
case "$VICTORIA_FIRST_URL_INDEX$VICTORIA_LAST_URL_INDEX$PAN_FIRST_URL_INDEX$PAN_LAST_URL_INDEX" in
  *[!0-9]*) echo 'Replace all Runeberg URL-index placeholders.' >&2; exit 1;;
esac
python scripts/corpus_acquisition/acquire_public_domain_text.py runeberg-range \
  --volume-url "$VICTORIA_VOLUME" --first-url-index "$VICTORIA_FIRST_URL_INDEX" \
  --last-url-index "$VICTORIA_LAST_URL_INDEX" --printed-first 89 --printed-last 162 \
  --raw-dir data/raw/hamsun-victoria/source-pages \
  --output data/raw/hamsun-victoria/runeberg-hamsun-victoria.txt \
  > data/raw/hamsun-victoria/acquisition-metadata.json
python scripts/corpus_acquisition/acquire_public_domain_text.py runeberg-range \
  --volume-url "$PAN_VOLUME" --first-url-index "$PAN_FIRST_URL_INDEX" \
  --last-url-index "$PAN_LAST_URL_INDEX" --printed-first 331 --printed-last 423 \
  --raw-dir data/raw/hamsun-pan/source-pages \
  --output data/raw/hamsun-pan/runeberg-hamsun-pan.txt \
  > data/raw/hamsun-pan/acquisition-metadata.json
```

Copy all emitted page URLs, paths, ranges, raw hashes, and assembled hash into
provenance. Leave spelling, punctuation, pronouns, dialogue, and OCR untouched.
Document suspected OCR in the review notes and compare it with the linked scan.

## 5. Inspect sources and approve provenance

Inspect beginning, middle, and end of every text. Confirm author/title, original
language, completeness, work boundaries, and absence of obvious corruption.

```bash
for FILE in \
 data/raw/wharton-age-of-innocence/gutenberg-541.txt \
 data/raw/lawrence-women-in-love/gutenberg-4240.txt \
 data/raw/hamsun-victoria/runeberg-hamsun-victoria.txt \
 data/raw/hamsun-pan/runeberg-hamsun-pan.txt \
 data/raw/dumas-fils-la-dame-aux-camelias/gutenberg-2419.txt \
 data/raw/constant-adolphe/gutenberg-13861.txt
do
  echo "===== $FILE ====="; sed -n '1,80p' "$FILE"
  LINES=$(wc -l < "$FILE"); MID=$((LINES/2)); sed -n "${MID},$((MID+80))p" "$FILE"
  tail -n 80 "$FILE"
done
```

Complete every provenance field, including retrieval time, exact edition facts,
transformations, raw and literary hashes, independent Australian reasoning, and
review date. Only after genuine human source and rights review change each
`review_status` from `acquisition_pending` to
`approved_for_development_processing`. Validate paths and hashes:

```bash
python - "$BATCH" <<'PY'
import hashlib,json,sys
from pathlib import Path
for member in json.load(open(sys.argv[1],encoding='utf-8'))['sources']:
 p=Path(member['provenance']); r=json.loads(p.read_text(encoding='utf-8'))
 assert r['review_status']=='approved_for_development_processing', p
 assert r.get('rights_note') and 'PENDING' not in r['rights_note'].upper(), p
 source=Path(r['local_path']); assert source.is_file() and source.stat().st_size, source
 assert hashlib.sha256(source.read_bytes()).hexdigest()==r['sha256'], p
 for raw in ([r['download_path']] if r.get('download_path') else r['download_paths']):
  assert Path(raw).is_file() and Path(raw).stat().st_size, raw
 print(f"approved {r['source_id']}: {r['sha256']}")
PY
```

Commit this acquisition/rights checkpoint before extraction.

## 6. Diagnostic reconnaissance and the common pattern decision

Start with v0.5 and write all diagnostic output to a review directory:

```bash
mkdir -p results/reconnaissance/classical_six_v1/diagnostics
rg -n -i -C 3 "I (really |still |truly )?love you|I love you still|I (don.?t|never) love[d]? you" \
 data/raw/{wharton-age-of-innocence,lawrence-women-in-love}/*.txt \
 > results/reconnaissance/classical_six_v1/diagnostics/english.txt || test $? -eq 1
rg -n -i -C 3 "aime|t[’']?aime|vous aime" \
 data/raw/{dumas-fils-la-dame-aux-camelias,constant-adolphe}/*.txt \
 > results/reconnaissance/classical_six_v1/diagnostics/french.txt || test $? -eq 1
rg -n -i -C 3 "elsker|jeg.{0,60}elsker|elsker (Dem|dig|deg)" \
 data/raw/{hamsun-victoria,hamsun-pan}/*.txt \
 > results/reconnaissance/classical_six_v1/diagnostics/norwegian.txt || test $? -eq 1
```

Inspect every plausible direct first-person-to-second-person declaration. Do not
broaden for lexical density, use `I .* love .* you`, or force a nonzero result.
If and only if attested evidence requires a general refinement, copy v0.5 to
`search_patterns_v0_6.json`, change its schema version, and add the minimal
pattern. For formal Norwegian `Dem`, keep the ordinary pattern and add exactly a
case-sensitive `\\b[Jj]eg\\s+elsker\\s+Dem\\b` family; test that `Jeg elsker
Dem` and `jeg elsker Dem` match while lowercase `jeg elsker dem` does not. Keep
all six works on one selected pattern file and preserve v0.5 unchanged.

## 7. Make extraction-only single-text dry runs

Set `PATTERNS` to v0.6 only when the reviewed diagnostics justify it. These
commands pass `--dry-run`; they prepare extraction and classification inputs but
make no annotation API calls.

```bash
RECON=results/reconnaissance/classical_six_v1
while read -r PROVENANCE; do
  python scripts/pipeline/run_single_text_pipeline.py \
    --provenance "$PROVENANCE" --patterns "$PATTERNS" \
    --annotation-version 0.3.1 --model 5.6 --context-chars 1000 --dry-run \
    --output-root "$RECON/pipeline_runs"
done < <(python -c "import json; print(*[x['provenance'] for x in json.load(open('$BATCH'))['sources']],sep='\n')")
find "$RECON/pipeline_runs" -name manifest.json -print -exec python -m json.tool {} \;
```

Do not remove zero-hit works and do not run the batch without `--dry-run`.

## 8. Inspect every occurrence and record scene clusters

Generate a passage-free index plus readable inspection file from the exact run
selected for each source. Replace each `RUN_DIR` with the printed dry-run path;
do not use a newest-directory glob when recording final evidence.

```bash
: > "$RECON/occurrence_inventory.tsv"
: > "$RECON/human_review.md"
for RUN_DIR in PASTE_SIX_EXACT_RUN_DIRECTORIES
do
  test -f "$RUN_DIR/extraction/passages.jsonl" || { echo "Bad run: $RUN_DIR" >&2; exit 1; }
  python - "$RUN_DIR" "$RECON" <<'PY'
import json,sys
from pathlib import Path
run=Path(sys.argv[1]); out=Path(sys.argv[2])
rows=[json.loads(x) for x in (run/'extraction/passages.jsonl').read_text(encoding='utf-8').splitlines() if x]
with (out/'occurrence_inventory.tsv').open('a',encoding='utf-8') as f:
 for r in rows: f.write(f"{r['source_id']}\t{r['occurrence_id']}\t{r['pattern_id']}\t{r['start']}\t{r['end']}\t{r['match']}\n")
with (out/'human_review.md').open('a',encoding='utf-8') as f:
 for r in rows:
  f.write(f"\n## {r['occurrence_id']}\n\n- source: `{r['source_id']}`\n- pattern: `{r['pattern_id']}`\n- offsets: {r['start']}–{r['end']}\n- review: PENDING\n\n```text\n{r['context']}\n```\n")
PY
done
```

For every hit verify direction, polarity, embedding/report/quotation/hypothesis,
context size, overlaps, OCR, and adjacent declarations. Check suspicious Hamsun
OCR against scan images. Retain structurally marked cases. Replace every
`review: PENDING` with a concise decision. Create `$RECON/summary.md` containing:

```text
| Work | Language | Occurrences | Approx. scene clusters | Extraction issues | Recommendation |
| --- | --- | ---: | ---: | --- | --- |
```

Scene clusters are descriptive and never change occurrence identities. For each
zero, document a broad lexical review and whether a conventional equivalent was
missed. Record zero if none was missed.

## 9. Final no-model gate, checks, and checkpoint

```bash
! find "$RECON" -path '*/annotations/*' -type f -print -quit | grep -q .
! rg -n 'review: PENDING' "$RECON/human_review.md"
python scripts/docs/validate_runbook_index.py
python -m pytest -q
python scripts/security/scan_credentials.py \
 data/batches/classical_six_v1.json provenance/sources \
 scripts/corpus_acquisition "$RECON"
git diff --check
git status --short
```

Commit only after the six sources and exact editions are verified, all rights
records are approved, one common pattern version is chosen, occurrence and scene
counts are recorded, every hit is reviewed, and extraction problems/zeros are
listed. Stop and share the inventory. Do **not** annotate until Manny and ChatGPT
review whether all six works should proceed.
