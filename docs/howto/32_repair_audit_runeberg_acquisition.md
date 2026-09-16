# Step 32: repair and audit Runeberg acquisition

This procedure repairs deterministic page-prefix extraction only. It does not
redownload source HTML, correct source OCR, alter frozen canonical texts,
canonicalize expansion works, or run extraction, annotation, translation, or AI
review. Stop for review when the committed acquisition state is clean.

## 1. Test and audit

```bash
cd "$LMCW"
python -m pytest -q scripts/corpus_acquisition
python scripts/corpus_acquisition/audit_runeberg_prefixes.py \
  --output data/acquisition/runeberg_prefix_audit_v1.json
python -m json.tool data/acquisition/runeberg_prefix_audit_v1.json >/dev/null
```

Inspect every `PRESERVED_TEXT` count. The audit deliberately reports Hamsun
pages for human review; do not silently rebuild existing canonical texts.
Named-page *Gösta Berlings saga* pages use the proofread-page parser and appear
as `NOT_RAW_OCR`. Ibsen and Strindberg predate retained page directories, so the
report records that their prefixes cannot be reconstructed locally.

## 2. Rederive Undset from retained pages

The rebuild stages each text, map, and metadata file in a temporary directory,
checks stored raw hashes and the aggregate raw-page digest, and only then
replaces derived artifacts atomically:

```bash
python scripts/corpus_acquisition/rederive_undset_from_stored_pages.py
```

Confirm the known boundaries and formerly broken join:

```bash
python - <<'PY'
from pathlib import Path
p = Path('data/raw/undset-kristin-lavransdatter/kransen/runeberg-kristin-kransen.txt')
t = p.read_text(encoding='utf-8')
assert t.startswith('I\nJØRUNDGAARD\nVed skiftet efter Ivar unge Gjesling')
assert 'Ved skiftet efter Ivar unge Gjesling paa Sundbu i\naaret 1306' in t
assert 'ti Ragnfrid var noget sær og tungsindig' in t
assert ('Hun blir saa rusende, hun kan ikke gaa ned til\nsæteren,» sa Halvdan '
        'og lo, men Lavrans strøk om\nhendes runde kinder') in t
PY
```

## 3. Verify local Gutenberg provenance

```bash
grep -En 'LES DEUX POÈTES|UN GRAND HOMME DE PROVINCE A PARIS|ÈVE ET DAVID' \
  data/raw/balzac-illusions-perdues/gutenberg-54723.txt
grep -En 'Title: Colei che non si deve amare: romanzo|EBOOK COLEI CHE NON SI DEVE AMARE: ROMANZO' \
  data/raw/verona-colei-che-non-si-deve-amare/source-download.txt
```

These checks establish containment and publication heading from acquired local
sources. `romanzo` is bibliographic description, not a work-title rename.

## 4. Regenerate and validate inventory

After updating the three finalized provenance hashes, regenerate the inventory:

```bash
python scripts/corpus_acquisition/build_expansion_15_inventory.py \
  --batch data/batches/expansion_15_acquisition_v1.json \
  --manifest data/acquisition/expansion_15_v1/manifest.json \
  --summary data/acquisition/expansion_15_v1/README.md
python -m pytest -q scripts/corpus_acquisition
python scripts/docs/validate_runbook_index.py
git diff --check
git diff --stat
git status --short
```

## 5. Explicit staging and commit

Never use `git add .`. Stage only reviewed repair artifacts:

```bash
git add \
  scripts/corpus_acquisition/acquire_public_domain_text.py \
  scripts/corpus_acquisition/audit_runeberg_prefixes.py \
  scripts/corpus_acquisition/rederive_undset_from_stored_pages.py \
  scripts/corpus_acquisition/build_expansion_15_inventory.py \
  scripts/corpus_acquisition/test_acquire_public_domain_text.py \
  scripts/corpus_acquisition/test_audit_runeberg_prefixes.py \
  data/raw/undset-kristin-lavransdatter \
  provenance/sources/runeberg-kristin-kransen.json \
  provenance/sources/runeberg-kristin-husfrue.json \
  provenance/sources/runeberg-kristin-korset.json \
  provenance/sources/gutenberg-54723.json \
  provenance/sources/gutenberg-69294.json \
  data/acquisition/expansion_15_v1 \
  data/acquisition/runeberg_prefix_audit_v1.json \
  docs/howto/32_repair_audit_runeberg_acquisition.md \
  docs/howto/README.md \
  docs/notes/methodology/runeberg-cross-domain-debugging-example.md
git diff --cached --check
git diff --cached --stat
git commit -m "Repair Runeberg first-line extraction and rederive Undset"
```

## 6. Post-commit checkpoint

```bash
git status --short
git log -1 --oneline
git show --stat --oneline HEAD
```

Require an empty status, then stop before canonicalization for Manny/ChatGPT
review.
