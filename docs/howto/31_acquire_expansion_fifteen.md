# Step 31: acquire the fifteen-work corpus expansion

This is an acquisition-only checkpoint. It must not create canonical work
manifests, extract expressions, call a model, translate, annotate, or correct
OCR. The checked-in inventory currently records a network-blocked attempt; run
this procedure only where Project Gutenberg and Project Runeberg are reachable.

## 1. Preflight and source identity review

```bash
cd "$LMCW"
test -z "$(git status --short)" || { echo 'Working tree is not clean.' >&2; exit 1; }
python -m pytest -q scripts/corpus_acquisition
python scripts/docs/validate_runbook_index.py
for ID in 798 54723 59926 23582 60810 5323 34346 69294 13175 41786 969 105 145; do
  cygstart "https://www.gutenberg.org/ebooks/$ID"
done
cygstart 'https://runeberg.org/berling/'
cygstart 'https://runeberg.org/kristin/'
```

For every Gutenberg catalogue page, compare ebook number, author, title, and
language with `data/acquisition/expansion_15_v1/manifest.json`, inspect the
public-domain statement, and copy the current official UTF-8 plain-text link.
Stop an individual acquisition on any mismatch or rights warning. For 54723,
also verify that the containing volume includes *Les deux poètes*, *Un grand
homme de province à Paris*, and *Ève et David*. Do not manually cut that volume.

## 2. Gutenberg

The commands below use the exact official UTF-8 text links from the reviewed
catalogue pages. They run in a fail-fast subshell so a missing variable or failed
download stops the entire group rather than allowing later commands to receive
an empty URL. Do not replace these links with mirror URLs.

```bash
(
set -euo pipefail
URL_798='https://www.gutenberg.org/ebooks/798.txt.utf-8'
URL_54723='https://www.gutenberg.org/ebooks/54723.txt.utf-8'
URL_59926='https://www.gutenberg.org/ebooks/59926.txt.utf-8'
URL_23582='https://www.gutenberg.org/ebooks/23582.txt.utf-8'
URL_60810='https://www.gutenberg.org/ebooks/60810.txt.utf-8'
URL_5323='https://www.gutenberg.org/ebooks/5323.txt.utf-8'
URL_34346='https://www.gutenberg.org/ebooks/34346.txt.utf-8'
URL_69294='https://www.gutenberg.org/ebooks/69294.txt.utf-8'
URL_13175='https://www.gutenberg.org/ebooks/13175.txt.utf-8'
URL_41786='https://www.gutenberg.org/ebooks/41786.txt.utf-8'
URL_969='https://www.gutenberg.org/ebooks/969.txt.utf-8'
URL_105='https://www.gutenberg.org/ebooks/105.txt.utf-8'
URL_145='https://www.gutenberg.org/ebooks/145.txt.utf-8'
for SPEC in \
 "798 stendhal-le-rouge-et-le-noir $URL_798" \
 "54723 balzac-illusions-perdues $URL_54723" \
 "59926 colette-le-ble-en-herbe $URL_59926" \
 "23582 sand-la-mare-au-diable $URL_23582" \
 "60810 stael-corinne $URL_60810" \
 "5323 fontane-effi-briest $URL_5323" \
 "34346 zuccoli-lamore-di-loredana $URL_34346" \
 "69294 verona-colei-che-non-si-deve-amare $URL_69294" \
 "13175 bang-ved-vejen $URL_13175" \
 "41786 nansen-maria $URL_41786" \
 "969 bronte-tenant-of-wildfell-hall $URL_969" \
 "105 austen-persuasion $URL_105" \
 "145 eliot-middlemarch $URL_145"
do
  set -- $SPEC; ID=$1; WORK=$2; URL=$3
  mkdir -p "data/raw/$WORK"
  python scripts/corpus_acquisition/acquire_public_domain_text.py gutenberg \
    --url "$URL" --raw "data/raw/$WORK/source-download.txt" \
    --output "data/raw/$WORK/gutenberg-$ID.txt" \
    > "data/raw/$WORK/acquisition-metadata.json.part" && \
  mv "data/raw/$WORK/acquisition-metadata.json"{.part,}
done
)
```

## 3. Runeberg Swedish

The reviewed Swedish electronic edition consists of the introduction page
`i01.html`, followed by the 36 chapter pages `k01.html` through `k36.html`.
The first page begins “Äntligen stod prästen i predikstolen.” The last ends with
the little Ruster beehive exchange and the narrator's comparison between the
imagination's giant bees and reality's hive. These nonnumeric Runeberg names
are why the command uses the reviewed named-page form of `runeberg-range`.
Never use `/gberlingen/`, which is an English translation.

```bash
(
set -euo pipefail
BERLING_PAGES=(i01)
for NUMBER in {01..36}; do BERLING_PAGES+=("k$NUMBER"); done
PAGE_ARGS=()
for PAGE in "${BERLING_PAGES[@]}"; do PAGE_ARGS+=(--page-name "$PAGE"); done
mkdir -p data/raw/lagerlof-gosta-berlings-saga
python scripts/corpus_acquisition/acquire_public_domain_text.py runeberg-range \
  --volume-url 'https://runeberg.org/berling/' \
  "${PAGE_ARGS[@]}" \
  --raw-dir data/raw/lagerlof-gosta-berlings-saga/source-pages \
  --output data/raw/lagerlof-gosta-berlings-saga/runeberg-berling.txt \
  --page-map data/raw/lagerlof-gosta-berlings-saga/page-map.json \
  > data/raw/lagerlof-gosta-berlings-saga/acquisition-metadata.json.part && \
mv data/raw/lagerlof-gosta-berlings-saga/acquisition-metadata.json{.part,}
)
```

## 4. Runeberg Norwegian trilogy

The three independently reviewed numeric ranges are `0005`–`0370` for
*Kransen*, `0009`–`0505` for *Husfrue*, and `0007`–`0527` for *Korset*. The
first pages respectively begin “I / JØRUNDGAARD”, “SYNDENS FRUGT / f / I”, and
“FRÆNDSØMD”; the isolated `f` and the other defects are source OCR and must not
be corrected. The last pages respectively end with Kristin and Erlend sitting
silent together, Simon walking toward the sleeping house with Jon and Ulf, and
Sira Eiliv leading the man toward the cookhouse across new snow. Keep the parts
as separate acquisition artifacts with their own maps and provenance.

```bash
(
set -euo pipefail
for SPEC in \
 "1 kransen 5 370" \
 "2 husfrue 9 505" \
 "3 korset 7 527"
do
  set -- $SPEC; VOLUME=$1; PART=$2; FIRST=$3; LAST=$4
  ROOT="data/raw/undset-kristin-lavransdatter/$PART"
  mkdir -p "$ROOT"
  python scripts/corpus_acquisition/acquire_public_domain_text.py runeberg-range \
    --volume-url "https://runeberg.org/kristin/$VOLUME/" \
    --first-url-index "$FIRST" --last-url-index "$LAST" \
    --raw-dir "$ROOT/source-pages" --output "$ROOT/runeberg-kristin-$PART.txt" \
    --page-map "$ROOT/page-map.json" > "$ROOT/acquisition-metadata.json.part" && \
  mv "$ROOT/acquisition-metadata.json"{.part,}
done
)
```

## 5. Provenance, inventory, and validation

Create one reviewed provenance record per Gutenberg work, one for Gösta
Berlings saga, and one per Undset constituent part, following the existing
records in `provenance/sources/`. Create a batch whose `sources` entries point
to those records, then let the finalizer compute hashes; never type hashes by
hand.

```bash
python scripts/corpus_acquisition/finalize_acquisition_provenance.py \
  --batch data/batches/expansion_15_acquisition_v1.json \
  --reviewed-on "$(date +%F)" --approve
python -m pytest -q scripts/corpus_acquisition
python scripts/docs/validate_runbook_index.py
python -m json.tool data/acquisition/expansion_15_v1/manifest.json >/dev/null
python - <<'PY'
import json
from pathlib import Path
m=json.loads(Path('data/acquisition/expansion_15_v1/manifest.json').read_text(encoding='utf-8'))
assert len(m['works']) == 15
assert sum(w['language']=='fr' for w in m['works']) == 5
assert sum(w['language']=='de' for w in m['works']) == 1
assert sum(w['language']=='it' for w in m['works']) == 2
assert sum(w['language']=='da' for w in m['works']) == 2
assert sum(w['language']=='en' for w in m['works']) == 3
assert sum(w['language']=='sv' for w in m['works']) == 1
assert sum(w['language']=='no' for w in m['works']) == 1
for w in m['works']:
    if w['acquisition_status'] == 'acquired':
        p=Path(w['derived_text_path']); assert p.is_file() and p.stat().st_size
        p.read_text(encoding='utf-8')
PY
git diff --check
```

Update the acquisition inventory and summary from finalized provenance only.
It is not complete unless it truthfully says `15/15 acquired`, includes all
three Undset parts, and every acquired entry has a resolving path and hash.

## 6. Explicit staging and commit

```bash
git add data/raw/stendhal-le-rouge-et-le-noir \
 data/raw/balzac-illusions-perdues data/raw/colette-le-ble-en-herbe \
 data/raw/sand-la-mare-au-diable data/raw/stael-corinne \
 data/raw/fontane-effi-briest data/raw/zuccoli-lamore-di-loredana \
 data/raw/verona-colei-che-non-si-deve-amare data/raw/bang-ved-vejen \
 data/raw/nansen-maria data/raw/bronte-tenant-of-wildfell-hall \
 data/raw/austen-persuasion data/raw/eliot-middlemarch \
 data/raw/lagerlof-gosta-berlings-saga \
 data/raw/undset-kristin-lavransdatter \
 provenance/sources data/batches/expansion_15_acquisition_v1.json \
 data/acquisition/expansion_15_v1 docs/howto/31_acquire_expansion_fifteen.md \
 docs/howto/README.md
git status --short
git diff --cached --name-only
git diff --cached --check
git commit -m "Acquire fifteen corpus expansion works"
git status --short
git log -1 --oneline
git show --stat --oneline HEAD
```

Stop for review. Do not begin canonicalization or extraction.
