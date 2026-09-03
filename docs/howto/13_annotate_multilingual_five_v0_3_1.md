# Step 13: annotate the multilingual five-text batch with v0.3.1

This runbook acquires, extracts, reviews, annotates, and audits the named
`multilingual_five_v1` corpus. It stops after this batch. Do not add these works
to `development_three`, change annotation v0.3.1 during the run, or proceed to a
larger corpus from this runbook.

The membership manifest contains only provenance paths. Annotation version,
model, prompt, patterns, and context radius remain run configuration. The five
current provenance records are deliberately marked `acquisition_blocked`; that
is a safe checkpoint, not approval. Replace that status only after exact files
and rights findings have been reviewed.

## 1. Preflight

```bash
cd "$LMCW"
git pull --ff-only
test -z "$(git status --short)" || {
  echo 'Working tree is not clean; stop and review it.' >&2
  exit 1
}
python -m pytest -q
python -m json.tool data/batches/multilingual_five_v1.json
python -m json.tool data/development/search_patterns_v0_3.json
test -f prompts/annotation/classify_passage_v0_3_1.md
test -f prompts/annotation/classification_schema_v0_3.json
```

The expected IDs are `runeberg-dukkhjem`, `gutenberg-1256`,
`runeberg-frkjulie`, `gutenberg-2407-2408`, and `gutenberg-18797`.

## 2. Acquire, document, and check in the exact editions

This section follows the earlier acquisition runbooks: define the source,
refuse accidental overwrite, download it, create a provenance draft, inspect
both, approve only after human review, and commit before extraction. Run each
block from the repository root. Direct URLs remain candidates until compared
with their catalogue pages in a browser.

### Download the Project Gutenberg texts

Keep *Werther* as one corpus text. Gutenberg #2407 and #2408 are two physical
volumes of the same work, so treating them as separate batch members would
silently change the five-work research design. The commands below preserve both
HTML downloads and concatenate their extracted literary bodies, in volume
order, into the single source `gutenberg-2407-2408`.

First download the two single-file Gutenberg sources as before. This helper
writes through `.part`, so an HTTP failure cannot leave a false completed file.

```bash
cd "$LMCW"
acquire_gutenberg () {
  SOURCE_ID="$1" WORK_ID="$2" SOURCE_URL="$3" TRIM_GUTENBERG="$4"
  SOURCE_DIR="data/raw/$WORK_ID"; DOWNLOAD="$SOURCE_DIR/source-download.txt"
  PARTIAL="$DOWNLOAD.part"; SOURCE_FILE="$SOURCE_DIR/$SOURCE_ID.txt"
  mkdir -p "$SOURCE_DIR"
  test ! -e "$DOWNLOAD" && test ! -e "$PARTIAL" && test ! -e "$SOURCE_FILE" || {
    echo "Refusing to overwrite $SOURCE_DIR" >&2; return 1;
  }
  curl --fail --location --retry 3 --output "$PARTIAL" "$SOURCE_URL" || {
    rm -f "$PARTIAL"; return 1;
  }
  mv "$PARTIAL" "$DOWNLOAD"
  python - "$DOWNLOAD" "$SOURCE_FILE" "$TRIM_GUTENBERG" <<'PY'
import re, sys
from pathlib import Path
raw, destination, trim=Path(sys.argv[1]),Path(sys.argv[2]),sys.argv[3]=="1"
data=raw.read_bytes()
for encoding in ("utf-8-sig","iso-8859-1"):
    try: text=data.decode(encoding); break
    except UnicodeDecodeError: pass
else: raise SystemExit(f"Cannot decode {raw}")
if trim:
    start=re.search(r"(?im)^\*\*\* START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.*?\*\*\*\s*$",text)
    end=re.search(r"(?im)^\*\*\* END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.*?\*\*\*\s*$",text)
    if not start or not end or start.end()>=end.start(): raise SystemExit("Ambiguous boundaries")
    text=text[start.end():end.start()].lstrip("\r\n")
destination.write_text(text,encoding="utf-8",newline="")
PY
}
acquire_gutenberg gutenberg-1256 rostand-cyrano-de-bergerac \
  'https://www.gutenberg.org/cache/epub/1256/pg1256.txt' 0
acquire_gutenberg gutenberg-18797 lafayette-la-princesse-de-cleves \
  'https://www.gutenberg.org/cache/epub/18797/pg18797.txt' 1
unset -f acquire_gutenberg
```

If either failed #19794 attempt left an empty file, remove only the confirmed
empty artifact before using the replacement source:

```bash
WERTHER_DIR='data/raw/goethe-die-leiden-des-jungen-werther'
for OLD in "$WERTHER_DIR/source-download.txt" "$WERTHER_DIR/source-download.txt.part"
do
  test ! -e "$OLD" || {
    test ! -s "$OLD" || { echo "Refusing to remove non-empty $OLD" >&2; exit 1; }
    rm "$OLD"
  }
done
```

Now download and assemble Gutenberg #2407 and #2408. The converter keeps the
exact HTML files, extracts visible text, removes each ordinary Gutenberg
wrapper at its explicit markers, and joins the two bodies without modernising
the German text.

```bash
cd "$LMCW"
WERTHER_DIR='data/raw/goethe-die-leiden-des-jungen-werther'
WERTHER_TEXT="$WERTHER_DIR/gutenberg-2407-2408.txt"
mkdir -p "$WERTHER_DIR"
for VOLUME in 2407 2408
do
  DOWNLOAD="$WERTHER_DIR/gutenberg-$VOLUME.html"
  PARTIAL="$DOWNLOAD.part"
  test ! -e "$DOWNLOAD" && test ! -e "$PARTIAL" || {
    echo "Refusing to overwrite $DOWNLOAD" >&2; exit 1;
  }
  curl --fail --location --retry 3 --output "$PARTIAL" \
    "https://www.gutenberg.org/cache/epub/$VOLUME/pg$VOLUME-images.html" || {
      rm -f "$PARTIAL"; exit 1;
    }
  mv "$PARTIAL" "$DOWNLOAD"
done
test ! -e "$WERTHER_TEXT" || { echo "Refusing to overwrite $WERTHER_TEXT" >&2; exit 1; }
python - "$WERTHER_DIR/gutenberg-2407.html" "$WERTHER_DIR/gutenberg-2408.html" "$WERTHER_TEXT" <<'PY'
import re, sys
from html.parser import HTMLParser
from pathlib import Path
class VisibleText(HTMLParser):
    blocks={"address","article","blockquote","br","div","h1","h2","h3","h4",
            "h5","h6","hr","li","p","pre","section","table","tr"}
    def __init__(self): super().__init__(convert_charrefs=True); self.parts=[]; self.hidden=0
    def handle_starttag(self,tag,attrs):
        if tag in {"script","style"}: self.hidden+=1
        if tag in self.blocks: self.parts.append("\n")
    def handle_endtag(self,tag):
        if tag in {"script","style"}: self.hidden=max(0,self.hidden-1)
        if tag in self.blocks: self.parts.append("\n")
    def handle_data(self,data):
        if not self.hidden: self.parts.append(data)
def body(path):
    data=path.read_bytes(); match=re.search(br'charset=["\']?([A-Za-z0-9._-]+)',data[:10000],re.I)
    encoding=match.group(1).decode("ascii") if match else "utf-8"
    parser=VisibleText(); parser.feed(data.decode(encoding))
    text="\n".join(line.strip() for line in "".join(parser.parts).splitlines())
    text=re.sub(r"\n{3,}","\n\n",text)
    start=re.search(r"(?im)^\*\*\* START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.*?\*\*\*\s*$",text)
    end=re.search(r"(?im)^\*\*\* END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.*?\*\*\*\s*$",text)
    if not start or not end or start.end()>=end.start(): raise SystemExit(f"Ambiguous boundaries: {path}")
    return text[start.end():end.start()].strip()
parts=[body(Path(name)) for name in sys.argv[1:3]]
Path(sys.argv[3]).write_text("\n\n".join(parts)+"\n",encoding="utf-8",newline="")
PY
sha256sum "$WERTHER_DIR/gutenberg-2407.html" \
  "$WERTHER_DIR/gutenberg-2408.html" "$WERTHER_TEXT"
```

Open the beginning/end and the join between volumes. Confirm that #2407 is Band
1, #2408 is Band 2, both are original German, and the assembled output contains
one complete *Werther*. The source ID changes to `gutenberg-2407-2408`; update
the batch manifest and provenance filename before extraction as described below.

### Download and combine the Project Runeberg parts

Keep each play as one corpus text. Runeberg divides *Et dukkehjem* into three
act pages and *Fröken Julie* into five pages; those are source parts, not
separate works. This helper downloads every part atomically, preserves all HTML
responses, extracts visible text with one standard-library converter, and
concatenates the parts in supplied order without modernising the wording.

If a failed continuous-page attempt left empty artifacts, remove only those
confirmed-empty files first:

```bash
for DIRECTORY in data/raw/ibsen-et-dukkehjem data/raw/strindberg-froken-julie
do
  for OLD in "$DIRECTORY/source-download.html" "$DIRECTORY/source-download.html.part"
  do
    test ! -e "$OLD" || {
      test ! -s "$OLD" || { echo "Refusing to remove non-empty $OLD" >&2; exit 1; }
      rm "$OLD"
    }
  done
done
```

Download and combine both plays:

```bash
cd "$LMCW"
acquire_runeberg_parts () {
  SOURCE_ID="$1" WORK_ID="$2"; shift 2
  SOURCE_DIR="data/raw/$WORK_ID"; SOURCE_FILE="$SOURCE_DIR/$SOURCE_ID.txt"
  mkdir -p "$SOURCE_DIR"
  test ! -e "$SOURCE_FILE" || { echo "Refusing to overwrite $SOURCE_FILE" >&2; return 1; }
  DOWNLOADS=(); PART_NUMBER=0
  for SOURCE_URL in "$@"
  do
    PART_NUMBER=$((PART_NUMBER + 1))
    DOWNLOAD="$SOURCE_DIR/source-part-$(printf '%02d' "$PART_NUMBER").html"
    PARTIAL="$DOWNLOAD.part"
    test ! -e "$PARTIAL" || {
      echo "Remove or inspect incomplete $PARTIAL before resuming" >&2; return 1;
    }
    if test -e "$DOWNLOAD"; then
      test -s "$DOWNLOAD" || { echo "Existing $DOWNLOAD is empty" >&2; return 1; }
      echo "Reusing completed part $DOWNLOAD"
    else
      curl --fail --location --retry 3 --output "$PARTIAL" "$SOURCE_URL" || {
        rm -f "$PARTIAL"; return 1;
      }
      mv "$PARTIAL" "$DOWNLOAD"
    fi
    DOWNLOADS+=("$DOWNLOAD")
  done
  python - "$SOURCE_FILE" "${DOWNLOADS[@]}" <<'PY'
import re, sys
from html.parser import HTMLParser
from pathlib import Path
class VisibleText(HTMLParser):
    blocks={"address","article","blockquote","br","div","h1","h2","h3","h4",
            "h5","h6","hr","li","p","pre","section","table","tr"}
    def __init__(self): super().__init__(convert_charrefs=True); self.parts=[]; self.hidden=0
    def handle_starttag(self,tag,attrs):
        if tag in {"script","style"}: self.hidden+=1
        if tag in self.blocks: self.parts.append("\n")
    def handle_endtag(self,tag):
        if tag in {"script","style"}: self.hidden=max(0,self.hidden-1)
        if tag in self.blocks: self.parts.append("\n")
    def handle_data(self,data):
        if not self.hidden: self.parts.append(data)
def visible_text(path):
    data=path.read_bytes(); match=re.search(br'charset=["\']?([A-Za-z0-9._-]+)',data[:10000],re.I)
    encoding=match.group(1).decode("ascii") if match else "iso-8859-1"
    parser=VisibleText(); parser.feed(data.decode(encoding))
    text="\n".join(line.strip() for line in "".join(parser.parts).splitlines())
    return re.sub(r"\n{3,}","\n\n",text).strip()
destination=Path(sys.argv[1]); parts=[visible_text(Path(name)) for name in sys.argv[2:]]
destination.write_text("\n\n".join(parts)+"\n",encoding="utf-8",newline="")
PY
}
acquire_runeberg_parts runeberg-dukkhjem ibsen-et-dukkehjem \
  'https://runeberg.org/dukkhjem/1.html' \
  'https://runeberg.org/dukkhjem/2.html' \
  'https://runeberg.org/dukkhjem/3.html'
acquire_runeberg_parts runeberg-frkjulie strindberg-froken-julie \
  'https://runeberg.org/frkjulie/01.html' \
  'https://runeberg.org/frkjulie/02.html' \
  'https://runeberg.org/frkjulie/03.html' \
  'https://runeberg.org/frkjulie/04.html' \
  'https://runeberg.org/frkjulie/05.html'
unset -f acquire_runeberg_parts
sha256sum data/raw/ibsen-et-dukkehjem/* data/raw/strindberg-froken-julie/*
```

Inspect every preserved part and both assembled texts. Confirm the Ibsen pages
are Acts 1–3 in order, the Strindberg pages are parts 01–05 in order, and neither
assembled result contains an error page or omits literary content. Navigation
text may remain documented in the derived source, but it must not interrupt or
alter target utterances.

### Create uniform provenance drafts

This updates the checked-in placeholders rather than discarding their
source-specific notes. It records paths, retrieval time, and calculated hashes,
while intentionally leaving rights approval pending.

```bash
cd "$LMCW"
RETRIEVED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
python - "$RETRIEVED_AT" <<'PY'
import hashlib, json, sys
from pathlib import Path
retrieved_at=sys.argv[1]
sources={
 "gutenberg-1256": ("rostand-cyrano-de-bergerac","https://www.gutenberg.org/cache/epub/1256/pg1256.txt","source-download.txt","Gutenberg wrapper retained in literary text."),
 "gutenberg-18797": ("lafayette-la-princesse-de-cleves","https://www.gutenberg.org/cache/epub/18797/pg18797.txt","source-download.txt","Gutenberg wrapper removed at explicit START/END markers."),
}
sha=lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
for source_id,(work_id,url,download_name,processing) in sources.items():
    directory=Path("data/raw")/work_id; local=directory/f"{source_id}.txt"
    download=directory/download_name; provenance=Path("provenance/sources")/f"{source_id}.json"
    record=json.loads(provenance.read_text(encoding="utf-8"))
    record.update({"source_url":url,"local_path":str(local),"retrieved_at":retrieved_at,
      "sha256":sha(local),"download_path":str(download),"download_sha256":sha(download),
      "processing_note":processing,"observed_format":"UTF-8 plain text (derived literary text)",
      "rights_note":"PENDING: record source statement and independent Australian review.",
      "review_status":"draft"})
    record.pop("acquisition_note",None)
    provenance.write_text(json.dumps(record,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"Drafted {provenance}")

# Werther is one derived source with two preserved downloads.
source_id="gutenberg-2407-2408"; directory=Path("data/raw/goethe-die-leiden-des-jungen-werther")
local=directory/f"{source_id}.txt"
downloads=[directory/"gutenberg-2407.html",directory/"gutenberg-2408.html"]
provenance=Path("provenance/sources/gutenberg-2407-2408.json")
record=json.loads(provenance.read_text(encoding="utf-8"))
record.update({
  "source_urls":["https://www.gutenberg.org/cache/epub/2407/pg2407-images.html",
                 "https://www.gutenberg.org/cache/epub/2408/pg2408-images.html"],
  "local_path":str(local),"retrieved_at":retrieved_at,"sha256":sha(local),
  "download_paths":[str(path) for path in downloads],
  "download_sha256":{path.name:sha(path) for path in downloads},
  "processing_note":"Visible text extracted from #2407 and #2408 HTML, each Gutenberg wrapper removed at explicit markers, then Band 1 and Band 2 concatenated in order.",
  "observed_format":"UTF-8 plain text assembled from two preserved HTML downloads",
  "rights_note":"PENDING: record both source statements and independent Australian review.",
  "review_status":"draft"})
record.pop("acquisition_note",None)
provenance.write_text(json.dumps(record,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(f"Drafted {provenance}")

# Each Runeberg play is one derived source backed by several preserved pages.
runeberg_sources={
 "runeberg-dukkhjem": ("ibsen-et-dukkehjem",
   ["https://runeberg.org/dukkhjem/1.html","https://runeberg.org/dukkhjem/2.html","https://runeberg.org/dukkhjem/3.html"]),
 "runeberg-frkjulie": ("strindberg-froken-julie",
   [f"https://runeberg.org/frkjulie/{part}.html" for part in ("01","02","03","04","05")]),
}
for source_id,(work_id,urls) in runeberg_sources.items():
    directory=Path("data/raw")/work_id; local=directory/f"{source_id}.txt"
    downloads=sorted(directory.glob("source-part-*.html"))
    assert len(downloads)==len(urls),(source_id,downloads)
    provenance=Path("provenance/sources")/f"{source_id}.json"
    record=json.loads(provenance.read_text(encoding="utf-8"))
    record.update({"source_urls":urls,"local_path":str(local),"retrieved_at":retrieved_at,
      "sha256":sha(local),"download_paths":[str(path) for path in downloads],
      "download_sha256":{path.name:sha(path) for path in downloads},
      "processing_note":"Visible text extracted from each preserved Runeberg HTML page and concatenated in listed order; entities decoded and block boundaries converted to newlines.",
      "observed_format":"UTF-8 plain text assembled from preserved HTML pages",
      "rights_note":"PENDING: record Runeberg source statement and independent Australian review.",
      "review_status":"draft"})
    record.pop("acquisition_note",None)
    provenance.write_text(json.dumps(record,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"Drafted {provenance}")
PY
```

### Inspect, approve, and check in immediately

Compare catalogue page, exact download, derived text, and provenance. Confirm
identity, original language, release/update data, completeness, encoding,
transformations, and the source rights statement. Replace `PENDING` with that
finding and the separately researched Australian basis; add
`rights_guidance_url` and `reviewed_on`. Do not infer status from age alone.
Then set `review_status` to `approved_for_development_processing`.

```bash
for SOURCE_ID in runeberg-dukkhjem gutenberg-1256 runeberg-frkjulie gutenberg-2407-2408 gutenberg-18797
do
  echo "===== $SOURCE_ID ====="
  python -m json.tool "provenance/sources/$SOURCE_ID.json"
  python - "provenance/sources/$SOURCE_ID.json" <<'PY'
import hashlib,json,sys
from pathlib import Path
record=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
paths=[record["local_path"]]+record.get("download_paths",[record.get("download_path")])
for name in paths:
    path=Path(name); print(hashlib.sha256(path.read_bytes()).hexdigest(),path)
PY
  SOURCE_FILE="$(python -c 'import json,sys; print(json.load(open(sys.argv[1],encoding="utf-8"))["local_path"])' "provenance/sources/$SOURCE_ID.json")"
  sed -n '1,35p' "$SOURCE_FILE"; tail -20 "$SOURCE_FILE"
done
```

Run approval and credential checks before staging:

```bash
python - <<'PY'
import hashlib,json
from pathlib import Path
manifest=json.loads(Path("data/batches/multilingual_five_v1.json").read_text(encoding="utf-8"))
for member in manifest["sources"]:
    path=Path(member["provenance"]); record=json.loads(path.read_text(encoding="utf-8"))
    assert record["review_status"]=="approved_for_development_processing",path
    assert "PENDING" not in record["rights_note"].upper(),path
    for key in ("local_path","retrieved_at","sha256","download_sha256",
                "processing_note","rights_guidance_url","reviewed_on"):
        assert record.get(key),(path,key)
    assert record.get("source_url") or record.get("source_urls"),(path,"source URL")
    raw_paths=record.get("download_paths",[record.get("download_path")])
    assert all(raw_paths),(path,"download path")
    local=Path(record["local_path"])
    assert hashlib.sha256(local.read_bytes()).hexdigest()==record["sha256"]
    if isinstance(record["download_sha256"],dict):
        for name in raw_paths:
            raw=Path(name)
            assert hashlib.sha256(raw.read_bytes()).hexdigest()==record["download_sha256"][raw.name]
    else:
        raw=Path(raw_paths[0])
        assert hashlib.sha256(raw.read_bytes()).hexdigest()==record["download_sha256"]
    local.read_text(encoding="utf-8"); print(f"Approved: {record['source_id']}")
PY
python scripts/security/scan_credentials.py data/raw provenance/sources
```

Check in exactly these sources and records now, before pattern inspection:

```bash
test -z "$(git diff --cached --name-only)" || {
  echo 'The index already contains staged files; review it first.' >&2; exit 1;
}
git add data/raw/ibsen-et-dukkehjem data/raw/rostand-cyrano-de-bergerac \
  data/raw/strindberg-froken-julie data/raw/goethe-die-leiden-des-jungen-werther \
  data/raw/lafayette-la-princesse-de-cleves \
  provenance/sources/{runeberg-dukkhjem,gutenberg-1256,runeberg-frkjulie,gutenberg-2407-2408,gutenberg-18797}.json
git diff --cached --check
git diff --cached --stat
python scripts/security/scan_credentials.py $(git diff --cached --name-only)
git commit -m 'Acquire multilingual five-text source editions'
git push origin HEAD
git status --short
```

Stop if a review/check fails. Proceed to patterns only from this clean,
committed source/provenance checkpoint.

## 3. Inspect source spelling and patterns

Inspect actual bytes, including every eventual zero-hit work:

```bash
rg -n -i -C 2 'jeg|elsker|deg|dig' data/raw/ibsen-et-dukkehjem/runeberg-dukkhjem.txt
rg -n -i -C 2 "je|t[’']|vous|aime" data/raw/rostand-cyrano-de-bergerac/gutenberg-1256.txt
rg -n -i -C 2 'jag|älskar|dig|er' data/raw/strindberg-froken-julie/runeberg-frkjulie.txt
rg -n -i -C 2 'ich|liebe|dich|euch|sie' data/raw/goethe-die-leiden-des-jungen-werther/gutenberg-2407-2408.txt
rg -n -i -C 2 "je|t[’']|vous|aime" data/raw/lafayette-la-princesse-de-cleves/gutenberg-18797.txt
```

If this demonstrates a missing historical/typographic variant, revise the
shared versioned pattern file and tests before extraction. Do not broaden it to
general affection, third-person love, or book-specific heuristics.

## 4. Make and inspect extraction-only dry runs

```bash
for PROVENANCE in \
  provenance/sources/runeberg-dukkhjem.json \
  provenance/sources/gutenberg-1256.json \
  provenance/sources/runeberg-frkjulie.json \
  provenance/sources/gutenberg-2407-2408.json \
  provenance/sources/gutenberg-18797.json
do
  python scripts/pipeline/run_single_text_pipeline.py "$PROVENANCE" \
    --patterns data/development/search_patterns_v0_3.json \
    --annotation-version 0.3.1 --model 5.6 --dry-run || exit 1
done
```

For each printed run, inspect `extraction/passages.jsonl`, metadata/fingerprint,
manifest, prepared inputs, and report. Manually confirm every hit is a direct
first-person/second-person target in adequate context. For zero hits, recheck
orthography, apostrophes, spacing, inflection, encoding, and conventional forms.
Do not annotate until all five inventories are accepted. Preserve and commit the
reviewed extraction runs, not disposable batch summaries.

## 5. Prepare, execute, and resume the one-command batch

The batch runner reuses compatible reviewed extractions and refuses implicit
re-extraction. First make a call-free batch dry run:

```bash
python scripts/pipeline/run_batch.py \
  --manifest data/batches/multilingual_five_v1.json \
  --patterns data/development/search_patterns_v0_3.json \
  --annotation-version 0.3.1 --model 5.6 --dry-run
BATCH_DIR='results/batch_runs/multilingual_five_v1/v0.3.1-5.6'
python -m json.tool "$BATCH_DIR/summary.json"
sed -n '1,360p' "$BATCH_DIR/report.md"
```

Require five requested/prepared texts, the manually approved total occurrence
count, zero attempted calls, and no source error. Then execute identically:

```bash
test -n "${OPENAI_API_KEY:-}" || {
  echo 'OPENAI_API_KEY is not set; stop before annotation.' >&2
  exit 1
}
python scripts/pipeline/run_batch.py \
  --manifest data/batches/multilingual_five_v1.json \
  --patterns data/development/search_patterns_v0_3.json \
  --annotation-version 0.3.1 --model 5.6
```

Do not use `--force`, modify v0.3.1, or redesign P/T/E/O. A normal rerun resumes,
skips compatible valid outputs, preserves failures, and lets other texts finish.

## 6. Audit completeness, costs, and unusual cases

```bash
python - "$BATCH_DIR" <<'PY'
import json, sys
from pathlib import Path
root = Path(sys.argv[1])
summary = json.loads((root / "summary.json").read_text(encoding="utf-8"))
assert summary["batch_id"] == "multilingual_five_v1", summary
assert summary["annotation_version"] == "0.3.1" and summary["model_alias"] == "5.6", summary
assert summary["status"] == "complete", summary
assert summary["texts_completed"] == summary["texts_requested"] == 5, summary
assert summary["valid_annotations"] == summary["occurrences"], summary
assert summary["failures"] == summary["model_calls_needed"] == 0, summary
assert sum(summary["ontology_statistics"]["score_distributions"]["T"].values()) == summary["valid_annotations"]
print(f"Complete: 5 texts, {summary['valid_annotations']} valid, USD {summary['estimated_total_cost_usd']:.6f}")
PY

for SOURCE_ID in runeberg-dukkhjem gutenberg-1256 runeberg-frkjulie gutenberg-2407-2408 gutenberg-18797
do
  RUN="$BATCH_DIR/texts/$SOURCE_ID"
  EXPECTED="$(python -c 'import json,sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["extracted_occurrences"])' "$RUN/manifest.json")"
  python scripts/pipeline/audit_pipeline_run.py "$RUN" --expected-occurrences "$EXPECTED" || exit 1
done
python scripts/security/scan_credentials.py "$BATCH_DIR"
python -m json.tool "$BATCH_DIR/unusual_cases.json"
sed -n '1,520p' "$BATCH_DIR/report.md"
```

The report covers requested/completed texts, valid outputs, unresolved and
historical failures, total/per-text cost, cost per valid annotation, locations,
P/T/E/O distributions, ontology fit, and thresholds. Review every unusual case
in full context; flags are informative, not errors. Closely inspect distributed
authorship in *Cyrano*, duty in *Et dukkehjem*, manipulation without false E in
*Fröken Julie*, intense but potentially T introspection in *Werther*, and
restrained confession in *La Princesse de Clèves*. Keep qualitative complexity
in `contextual_interpretation`, do not force O, and audit any background
knowledge declaration.

## 7. Preserve results and stop

```bash
test -z "$(git diff --cached --name-only)" || {
  echo 'The index already contains staged files; review it first.' >&2
  exit 1
}
git add "$BATCH_DIR"
git diff --cached --check
git diff --cached --stat
python scripts/security/scan_credentials.py "$BATCH_DIR"
git commit -m 'Record multilingual-five v0.3.1 batch run'
git push origin HEAD
git status --short
```

Then create a separate descriptive eight-text report combining this completed
batch with `development_three` v0.3.1: languages, occurrences, P/T/E/O
distributions, ontology fit, O cases, high-E cases, and high-P cases. Do not
modify either membership manifest or infer language effects. Answer the eight
handoff questions and stop for review; do not begin the next corpus expansion.
