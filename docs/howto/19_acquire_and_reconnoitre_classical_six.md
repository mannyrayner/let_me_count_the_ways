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

This runbook deliberately uses the standard Cygwin `grep` utility rather than
requiring an additional search binary. Verify that the Cygwin `grep` package is
available before continuing:

```bash
command -v grep >/dev/null || {
  echo 'grep is required; install the Cygwin grep package first.' >&2
  exit 1
}
grep --version | head -n 1
```

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

Record the catalogue page in `catalogue_url` and the exact plain-text link in
`download_url`; these are separate provenance fields and neither replaces the
other. Record the catalogue metadata and update dates before downloading. Use
the Australian Copyright Agency duration guidance
in addition to Gutenberg's US statement. The relevant author death years are
Wharton 1937, Lawrence 1930, Dumas fils 1895, and Constant 1830.

Open the Runeberg collection and copyright pages. Manny's manual review verified
the authoritative processed ranges as URL indices `0093`–`0166` in volume 3
(*Victoria*) and `0335`–`0414` in volume 2 (*Pan*). The catalogue's printed-page
metadata (89–162 and 331–423 respectively) is distinct and does not map one to
one to those HTML names at the boundaries. Preserve both fields and record the
discrepancy; acquisition is defined by the verified inclusive HTML URL range.

```bash
cygstart 'https://runeberg.org/'
cygstart 'https://runeberg.org/admin/copyright.html'
```

Do not assume printed page 89 means `0089.html`. In a browser inspect `0093.html`,
`0166.html`, `0335.html`, and `0414.html`, plus several internal and adjacent
pages: each first page begins the named work, each last page ends it, and its
neighbours belong to other material. The
literary files must exclude *Siesta*, *I æventyrland*, *Redaktør Lynge*, and *Ny
jord*. Record the National Library scan/Runeberg OCR basis, possible modernized
spelling, explicitly unproofread/uncorrected OCR, facsimile availability, and
Hamsun's 1952 death year. Do not claim first-edition orthography.

## 3. Acquire the four Gutenberg texts atomically

Use the four manually verified direct UTF-8 URLs, then use the shared helper. It
refuses overwrites, downloads via
`.part`, preserves the raw response, requires explicit Gutenberg START/END
markers, and prints hashes for the provenance records.

```bash
URL_541='https://www.gutenberg.org/ebooks/541.txt.utf-8'
URL_4240='https://www.gutenberg.org/ebooks/4240.txt.utf-8'
URL_2419='https://www.gutenberg.org/ebooks/2419.txt.utf-8'
URL_13861='https://www.gutenberg.org/ebooks/13861.txt.utf-8'
mkdir -p data/raw/{wharton-age-of-innocence,lawrence-women-in-love,dumas-fils-la-dame-aux-camelias,constant-adolphe}
for SPEC in \
  "541 wharton-age-of-innocence $URL_541" \
  "4240 lawrence-women-in-love $URL_4240" \
  "2419 dumas-fils-la-dame-aux-camelias $URL_2419" \
  "13861 constant-adolphe $URL_13861"
do
  set -- $SPEC; ID=$1; WORK=$2; URL=$3
  python scripts/corpus_acquisition/acquire_public_domain_text.py gutenberg \
    --url "$URL" --raw "data/raw/$WORK/source-download.txt" \
    --output "data/raw/$WORK/gutenberg-$ID.txt" \
    > "data/raw/$WORK/acquisition-metadata.json"
done
```

Copy the emitted exact URLs, paths, and SHA-256 values into provenance. Preserve
raw downloads and derived texts. Never trim by approximate line counts.

## 4. Acquire the two verified Runeberg ranges

Only after the reusable helper and its offline tests pass, use the exact verified
volume bases and URL indices below. The helper constructs four-digit URLs
deterministically (never by following next links), downloads with `curl --fail
--location --retry 3` via `.part`, reuses valid nonempty pages, preserves every
exact HTML response, and rejects gaps/extras/empty pages. Derivation extracts
only the raw-OCR HTML fragment after `<!-- mode=normal -->` and before the first
subsequent `<!-- NEWIMAGE2 -->` (with `<!-- #### -->` as a recorded fallback).
It does not use `<hr>` as a boundary and does not correct OCR. `--force`
explicitly redownloads pages; it is intentionally absent here. A marker-bounded
page may legitimately contain only a title such as `Victoria`, so minimum-size
validation applies to the assembled work rather than each page. Do not proceed
from a partial range.

```bash
(
set -e
VICTORIA_VOLUME='https://runeberg.org/hamsun/6-3/'
VICTORIA_FIRST_URL_INDEX=93; VICTORIA_LAST_URL_INDEX=166
PAN_VOLUME='https://runeberg.org/hamsun/6-2/'
PAN_FIRST_URL_INDEX=335; PAN_LAST_URL_INDEX=414
mkdir -p data/raw/{hamsun-victoria,hamsun-pan}
rm -f data/raw/hamsun-victoria/acquisition-metadata.json.part
python scripts/corpus_acquisition/acquire_public_domain_text.py runeberg-range \
  --volume-url "$VICTORIA_VOLUME" --first-url-index "$VICTORIA_FIRST_URL_INDEX" \
  --last-url-index "$VICTORIA_LAST_URL_INDEX" --printed-first 89 --printed-last 162 \
  --raw-dir data/raw/hamsun-victoria/source-pages \
  --output data/raw/hamsun-victoria/runeberg-hamsun-victoria.txt \
  --page-map data/raw/hamsun-victoria/page-map.json \
  > data/raw/hamsun-victoria/acquisition-metadata.json.part && \
mv data/raw/hamsun-victoria/acquisition-metadata.json{.part,}
rm -f data/raw/hamsun-pan/acquisition-metadata.json.part
python scripts/corpus_acquisition/acquire_public_domain_text.py runeberg-range \
  --volume-url "$PAN_VOLUME" --first-url-index "$PAN_FIRST_URL_INDEX" \
  --last-url-index "$PAN_LAST_URL_INDEX" --printed-first 331 --printed-last 423 \
  --raw-dir data/raw/hamsun-pan/source-pages \
  --output data/raw/hamsun-pan/runeberg-hamsun-pan.txt \
  --page-map data/raw/hamsun-pan/page-map.json \
  > data/raw/hamsun-pan/acquisition-metadata.json.part && \
mv data/raw/hamsun-pan/acquisition-metadata.json{.part,}
test "$(find data/raw/hamsun-victoria/source-pages -name '*.html' | wc -l)" -eq 74
test "$(find data/raw/hamsun-pan/source-pages -name '*.html' | wc -l)" -eq 80
python - <<'PY'
import json
for path, first, last in (
    ('data/raw/hamsun-victoria/acquisition-metadata.json', 93, 166),
    ('data/raw/hamsun-pan/acquisition-metadata.json', 335, 414),
):
    metadata=json.load(open(path, encoding='utf-8'))
    expected=list(range(first,last+1))
    assert metadata['ordered_url_indices'] == expected
    assert metadata['pages_requested'] == metadata['pages_nonempty'] == len(expected)
    print(path, {key: metadata[key] for key in ('pages_requested','pages_downloaded',
          'pages_nonempty','assembled_character_count','assembled_word_count','sha256')})
PY
)
```

Reject catastrophic chrome extraction, require plausible literary size, and
reconcile every page-map slice before inspecting individual pages:

```bash
for FILE in \
 data/raw/hamsun-victoria/runeberg-hamsun-victoria.txt \
 data/raw/hamsun-pan/runeberg-hamsun-pan.txt
do
  ! grep -En 'Project Runeberg|On this page / på denna sida|Proofread the page now|Korrekturläs sidan nu|Table of Contents / Innehåll|Full resolution \(JPEG\)' "$FILE"
  test "$(wc -c < "$FILE")" -gt 50000
  test "$(wc -w < "$FILE")" -gt 8000
done
python - <<'PY'
import json
from pathlib import Path
from scripts.corpus_acquisition.acquire_public_domain_text import runeberg_html_to_text
for work in ('victoria','pan'):
    root=Path(f'data/raw/hamsun-{work}')
    assembled=(root/f'runeberg-hamsun-{work}.txt').read_text(encoding='utf-8')
    records=json.loads((root/'page-map.json').read_text(encoding='utf-8'))
    for record in records:
        start,end=record['output_start'],record['output_end']
        assert start < end
        expected=runeberg_html_to_text(
            Path(record['raw_path']).read_text(encoding='utf-8-sig')).rstrip()
        assert assembled[start:end] == expected, record['url_index']
PY
```

If an assembled file was produced by the earlier extractor and begins with repeated
`Full resolution (JPEG)` / page-navigation blocks, **stop**: that output and its
map/metadata are invalid. The rejected hashes are retained in provenance only as
an audit record and must not be approved as corpus hashes. Preserve the downloaded
HTML, remove only the derived artifacts, and rerun the two acquisition commands;
the valid nonempty source pages will be reused rather than downloaded again:

```bash
rm -f data/raw/hamsun-victoria/{runeberg-hamsun-victoria.txt,page-map.json,acquisition-metadata.json,acquisition-metadata.json.part}
rm -f data/raw/hamsun-pan/{runeberg-hamsun-pan.txt,page-map.json,acquisition-metadata.json,acquisition-metadata.json.part}
# Rerun the two runeberg-range commands and the mechanical checks above.
```

The dictionaries printed by the checks are summaries. The complete records are
already saved by the `>` redirections as `acquisition-metadata.json`; per-page
hashes and offsets are in `page-map.json`, and exact responses remain in
`source-pages/`. Do not move those files merely to preserve terminal output.
Only after the boundary/content inspection below succeeds should the new
assembled hashes be copied to the provenance `sha256` fields.

The page map records each ordered URL index, exact OCR URL, output offsets, raw
path/hash, and facsimile availability. The earlier bad summaries are marked as
rejected audit records in provenance; replace neither `sha256` field until the
corrected extraction passes inspection. Retain the complete newly generated
metadata locally for the later approval checkpoint. State that this is Project
Runeberg OCR of Knut Hamsun, *Samlede
verker*, 6th ed.; it is marked not proofread, while page facsimiles are available
for checking suspicious readings. Leave spelling, punctuation, `De`/`Dem`, names,
broken words, dialogue, and OCR untouched. Record both OCR and scan readings if a
target-relevant error is found; use a versioned correction layer rather than
casually hand-editing this source.

Inspect boundary and internal page extracts through their page-map offsets:

```bash
python - <<'PY'
import json
from pathlib import Path
for root, wanted in (('hamsun-victoria',(93,101,129,166)),
                     ('hamsun-pan',(335,350,375,414))):
    base=Path('data/raw')/root
    text=next(base.glob('runeberg-*.txt')).read_text(encoding='utf-8')
    pages={p['url_index']:p for p in json.loads((base/'page-map.json').read_text())}
    for index in wanted:
        p=pages[index]
        print(f"===== {p['url']} =====\n{text[p['output_start']:p['output_end']]}"[:2500])
PY
```

Confirm the first/last pages belong to the intended work, no neighbouring work
is included, internal pages are literary OCR, and assembled order is correct.
Compare each excerpt with the raw OCR fragment in its HTML. Preserve OCR errors,
including `Gi` where the facsimile reads `97`; the facsimile is verification, not
the extraction source.

Finally, make a lexical plausibility check before resuming reconnaissance:

```bash
grep -En 'Victoria|Johannes|elsker|Dem' data/raw/hamsun-victoria/runeberg-hamsun-victoria.txt || test $? -eq 1
grep -En 'Pan|Glahn|Edvarda|elsker|Dem' data/raw/hamsun-pan/runeberg-hamsun-pan.txt || test $? -eq 1
```

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
`approved_for_development_processing`. Changing `review_status` alone is not
enough: `sha256`, the raw download hash(es), `retrieved_at`, and `reviewed_on`
must not still be `null` or empty.

All six works in this acquisition were reviewed on 8 September 2026. Populate
their machine-derived fields from the files themselves, use the latest raw-file
modification time as the UTC completion time for each download, and mark the
already-reviewed records approved. The helper validates every member before it
writes any record, refuses pending rights notes, hashes the literary and raw
files, obtains Runeberg raw paths from the page maps, and reconciles each
available acquisition-metadata hash:

```bash
python scripts/corpus_acquisition/finalize_acquisition_provenance.py \
  --batch "$BATCH" --reviewed-on 2026-09-08 --approve
git diff -- provenance/sources
```

Review that diff before continuing. If manual diagnosis is needed, print the
current literary and raw hashes directly:

```bash
python - "$BATCH" <<'PY'
import hashlib,json,sys
from pathlib import Path
for member in json.load(open(sys.argv[1],encoding='utf-8'))['sources']:
    provenance=Path(member['provenance'])
    record=json.loads(provenance.read_text(encoding='utf-8'))
    source=Path(record['local_path'])
    print(f"\n{provenance}\n  sha256: {hashlib.sha256(source.read_bytes()).hexdigest()}")
    raw_paths=([record['download_path']] if record.get('download_path')
               else [entry['raw_path'] for entry in json.loads(
                   Path(record['page_map_path']).read_text(encoding='utf-8'))])
    for raw in map(Path,raw_paths):
        print(f"  raw {raw.name}: {hashlib.sha256(raw.read_bytes()).hexdigest()}")
PY
```

If filling a record manually, copy rather than retype those values and use
explicit ISO 8601 timestamps. Then validate paths, completion, and hashes. This
validator reports the field and expected/actual values instead of stopping at an
unlabelled assertion:

```bash
python - "$BATCH" <<'PY'
import hashlib,json,sys
from pathlib import Path
errors=[]
def problem(path, message): errors.append(f'{path}: {message}')
for member in json.load(open(sys.argv[1],encoding='utf-8'))['sources']:
 p=Path(member['provenance']); r=json.loads(p.read_text(encoding='utf-8'))
 if r.get('review_status') != 'approved_for_development_processing':
  problem(p, f"review_status is {r.get('review_status')!r}")
 if not r.get('rights_note') or 'PENDING' in r['rights_note'].upper():
  problem(p, 'rights_note is missing or still pending')
 for field in ('retrieved_at','reviewed_on'):
  if not r.get(field): problem(p, f'{field} is null or empty')
 source=Path(r['local_path'])
 if not source.is_file() or not source.stat().st_size:
  problem(p, f'literary source is missing or empty: {source}')
 else:
  actual=hashlib.sha256(source.read_bytes()).hexdigest()
  if not r.get('sha256'):
   problem(p, f'sha256 is null or empty; actual is {actual}')
  elif actual != r['sha256']:
   problem(p, f"sha256 mismatch: recorded {r['sha256']}, actual {actual}")
 raw_paths=([r['download_path']] if r.get('download_path') else r.get('download_paths',[]))
 if not raw_paths: problem(p, 'no raw download path(s) recorded')
 raw_hashes=r.get('download_sha256')
 for raw_name in raw_paths:
  raw=Path(raw_name)
  if not raw.is_file() or not raw.stat().st_size:
   problem(p, f'raw download is missing or empty: {raw}')
   continue
  actual=hashlib.sha256(raw.read_bytes()).hexdigest()
  recorded=(raw_hashes if isinstance(raw_hashes,str) else
            raw_hashes.get(raw.name,raw_hashes.get(str(raw))) if isinstance(raw_hashes,dict)
            else None)
  if not recorded:
   problem(p, f'raw hash is not recorded for {raw}; actual is {actual}')
  elif recorded != actual:
   problem(p, f'raw hash mismatch for {raw}: recorded {recorded}, actual {actual}')
 if not raw_hashes:
  problem(p, 'download_sha256 is null or empty')
 if not any(message.startswith(f'{p}:') for message in errors):
  print(f"approved {r['source_id']}: {r['sha256']}")
if errors:
 print('\nProvenance validation failed:',file=sys.stderr)
 print('\n'.join(f'- {message}' for message in errors),file=sys.stderr)
 raise SystemExit(1)
PY
```

Commit this acquisition/rights checkpoint before extraction with an explicit,
auditable path list. Do not use `git add .`:

```bash
git status --short
git add \
  data/batches/classical_six_v1.json \
  data/raw/wharton-age-of-innocence \
  data/raw/lawrence-women-in-love \
  data/raw/hamsun-victoria \
  data/raw/hamsun-pan \
  data/raw/dumas-fils-la-dame-aux-camelias \
  data/raw/constant-adolphe \
  provenance/sources/gutenberg-541.json \
  provenance/sources/gutenberg-4240.json \
  provenance/sources/runeberg-hamsun-victoria.json \
  provenance/sources/runeberg-hamsun-pan.json \
  provenance/sources/gutenberg-2419.json \
  provenance/sources/gutenberg-13861.json \
  docs/howto/19_acquire_and_reconnoitre_classical_six.md \
  scripts/corpus_acquisition/acquire_public_domain_text.py \
  scripts/corpus_acquisition/finalize_acquisition_provenance.py \
  scripts/corpus_acquisition/test_acquire_public_domain_text.py \
  scripts/corpus_acquisition/test_finalize_acquisition_provenance.py \
  scripts/extraction/test_search_patterns_v0_6.py
git diff --cached --check
git status --short
git commit -m "Acquire classical six corpus sources"
git status --short
test -z "$(git status --short)" || {
  echo 'Working tree is not clean after the acquisition checkpoint.' >&2
  exit 1
}
```

## 6. Narrow diagnostics and the common pattern decision

Extraction for French and Norwegian reuses the validated multilingual pattern
framework from the earlier corpus. This is not a new manual extraction method.
Reconnaissance is limited to detecting source-edition variants not covered by
v0.5; for Hamsun, particular attention goes to formal `De/Dem` in older
Riksmål. Do not review every occurrence of `aime` or `elsker`.

The v0.5 production patterns remain the baseline:

```text
French:    \bje\s+t\s*[’']\s*aime\b
           \bje\s+vous\s+aime\b
Norwegian: \bjeg\s+elsker\s+(?:deg|dig|dere)\b
```

Run only bounded safety checks for plausible missed structural variants. These
files are diagnostic evidence, not occurrence inventories:

```bash
mkdir -p results/reconnaissance/classical_six_v1/diagnostics
python - <<'PY' > results/reconnaissance/classical_six_v1/diagnostics/french-bounded.txt
import re
from pathlib import Path
for path in (Path('data/raw/dumas-fils-la-dame-aux-camelias/gutenberg-2419.txt'),
             Path('data/raw/constant-adolphe/gutenberg-13861.txt')):
    for number,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if re.search(r'\bje\b.{0,20}\baime\b',line,re.IGNORECASE):
            print(f'{path}:{number}:{line}')
PY
python - <<'PY' > results/reconnaissance/classical_six_v1/diagnostics/norwegian-formal.txt
import re
from pathlib import Path
exact=re.compile(r'\b[Jj]eg\s+elsker\s+Dem\b')
bounded=re.compile(r'\b[Jj]eg\b.{0,40}\belsk(?:er|et)\b.{0,40}\bDem\b')
for path in (Path('data/raw/hamsun-victoria/runeberg-hamsun-victoria.txt'),
             Path('data/raw/hamsun-pan/runeberg-hamsun-pan.txt')):
    for number,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if exact.search(line) or bounded.search(line):
            print(f'{path}:{number}:{line}')
PY
```

Inspect these short reports only to answer whether a concrete source-edition
variant escapes v0.5. The French production extraction continues to use the two
established patterns unless this bounded evidence shows a missed direct
first-person-to-second-person construction. Other uses of *aimer* do not justify
a pattern change. Likewise, the ordinary Norwegian pattern remains unchanged.
Check target-relevant or suspicious Hamsun OCR against the page facsimile.

If and only if the inspected Hamsun evidence attests formal second-person `Dem`,
create v0.6 as a minimal successor; never modify v0.5:

```bash
cp data/development/search_patterns_v0_5.json \
   data/development/search_patterns_v0_6.json
python - <<'PY'
import json
from pathlib import Path
path=Path('data/development/search_patterns_v0_6.json')
config=json.loads(path.read_text(encoding='utf-8'))
assert config['schema_version']=='0.5'
config['schema_version']='0.6'
patterns=config['languages']['no']['patterns']
assert [p['id'] for p in patterns]==['no_jeg_elsker_deg_dig_dere']
patterns.append({
    'id':'no_jeg_elsker_dem_formal',
    'regex':r'\b[Jj]eg\s+elsker\s+Dem\b',
    'case_sensitive':True,
})
path.write_text(json.dumps(config,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
PY
PATTERNS=data/development/search_patterns_v0_6.json
```

If no relevant formal construction or other missed variant is attested, do not
create v0.6 and retain:

```bash
PATTERNS=data/development/search_patterns_v0_5.json
```

Use exactly one selected manifest for all six works. Run the complete regression
suite after the decision; the conditional v0.6 tests activate automatically when
the file exists and check formal-case behavior, ordinary Norwegian forms, and
that English, French, Swedish, and German remain identical to v0.5:

```bash
python -m json.tool "$PATTERNS" >/dev/null
python -m pytest -q scripts/extraction/test_extract_passages.py \
  scripts/extraction/test_search_patterns_v0_6.py
python -m pytest -q
```

## 7. Standard extraction-only single-text dry runs

Use the same `run_single_text_pipeline.py --dry-run` machinery validated for the
multilingual-five corpus. New source texts, Runeberg OCR acquisition, and a
possible formal-pronoun pattern are the only differences; there is no parallel
manual extraction workflow. The selected `PATTERNS` manifest applies to all six
works. These commands prepare extraction and classification inputs but make no
annotation API calls. `--dry-run` performs extraction and prepares annotation
inputs but stops before any annotation-model call.

If the first source needs isolated debugging, this optional block preserves the
pipeline's stdout and stderr and reports failure without closing the interactive
shell:

```bash
if (
BATCH=data/batches/classical_six_v1.json
PATTERNS=data/development/search_patterns_v0_6.json
RECON=results/reconnaissance/classical_six_v1
mkdir -p "$RECON/pipeline_runs" || exit 1
if ! PROVENANCE=$(
  python - "$BATCH" <<'PY'
import json
import sys
with open(sys.argv[1], encoding='utf-8') as stream:
    print(json.load(stream)['sources'][0]['provenance'])
PY
); then
  echo 'Could not read the first provenance path.' >&2
  exit 1
fi
echo "PROVENANCE=$PROVENANCE"
if python scripts/pipeline/run_single_text_pipeline.py \
    --provenance "$PROVENANCE" --patterns "$PATTERNS" \
    --annotation-version 0.3.1 --model 5.6 --context-chars 1000 --dry-run \
    --output-root "$RECON/pipeline_runs"
then
  echo 'SUCCESS'
else
  STATUS=$?
  echo "FAILED with exit status $STATUS" >&2
fi
); then
  :
else
  STATUS=$?
  echo "Single-source debug setup failed with exit status $STATUS" >&2
fi
```

The normal six-source block restates every important path so that it can run in
a fresh shell independently of earlier steps:

```bash
if (
BATCH=data/batches/classical_six_v1.json
PATTERNS=data/development/search_patterns_v0_6.json
RECON=results/reconnaissance/classical_six_v1

test -f "$BATCH" || {
  echo "Missing batch manifest: $BATCH" >&2
  exit 1
}
test -f "$PATTERNS" || {
  echo "Missing search-pattern manifest: $PATTERNS" >&2
  exit 1
}
if ! python -m json.tool "$BATCH" >/dev/null; then exit 1; fi
if ! python -m json.tool "$PATTERNS" >/dev/null; then exit 1; fi

if ! python - "$BATCH" <<'PY'
import json
import sys
from pathlib import Path

with open(sys.argv[1], encoding='utf-8') as stream:
    batch=json.load(stream)

sources=batch['sources']
if len(sources) != 6:
    raise SystemExit(f'Expected 6 sources, found {len(sources)}')
for source in sources:
    provenance=source.get('provenance')
    if not provenance:
        raise SystemExit(f'Missing provenance path in batch member: {source}')
    path=Path(provenance)
    if not path.is_file():
        raise SystemExit(f'Missing provenance file: {path}')
print('Batch contains 6 provenance records.')
PY
then
  exit 1
fi

mkdir -p "$RECON/pipeline_runs" || exit 1
FAILURES=0
while read -r PROVENANCE; do
  test -n "$PROVENANCE" || continue
  echo
  echo '============================================================'
  echo "Running extraction dry-run for: $PROVENANCE"
  echo '============================================================'
  if python scripts/pipeline/run_single_text_pipeline.py \
      --provenance "$PROVENANCE" --patterns "$PATTERNS" \
      --annotation-version 0.3.1 --model 5.6 --context-chars 1000 --dry-run \
      --output-root "$RECON/pipeline_runs"
  then
    echo "SUCCESS: $PROVENANCE"
  else
    STATUS=$?
    echo "FAILED: $PROVENANCE" >&2
    echo "Exit status: $STATUS" >&2
    FAILURES=$((FAILURES + 1))
    break
  fi
done < <(
  python - "$BATCH" <<'PY'
import json
import sys

with open(sys.argv[1], encoding='utf-8') as stream:
    batch=json.load(stream)

for source in batch['sources']:
    print(source['provenance'])
PY
)

if test "$FAILURES" -ne 0; then
  echo 'Step 7 stopped after a pipeline failure. Review the traceback above.' >&2
else
  echo 'All extraction dry-runs completed successfully.'
  find "$RECON/pipeline_runs" \
    -name manifest.json \
    -print \
    -exec python -m json.tool {} \;
fi
); then
  :
else
  STATUS=$?
  echo "Step 7 setup failed with exit status $STATUS; review the error above." >&2
fi
```

Earlier steps use strict mode only inside subshells. Step 7 also runs in a
subshell and guards every pipeline invocation explicitly, so a failed dry run
prints its traceback, source, and status without terminating the interactive
shell—even if that shell already has `set -e`. Do not remove zero-hit works and
do not run the batch without `--dry-run`.

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
zero, document the bounded structural safety check and whether a conventional
equivalent was missed. Broaden only when the text supplies concrete evidence of
an uncovered variant; record zero if none was missed.

## 9. Final no-model gate, checks, and checkpoint

```bash
! find "$RECON" -path '*/annotations/*' -type f -print -quit | grep -q .
! grep -n 'review: PENDING' "$RECON/human_review.md"
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
