#!/usr/bin/env python3
"""Publish the authorized saved Prince records and rebuild the combined reader; no API calls."""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.reader.records import read, load_collection, publication_approved
from scripts.reader.build_reader import generate

WORK = 'saint-exupery-le-petit-prince'
RUN = 'context_extension_prince_v0_13_v0_3_1'
EXPORT = Path('results/publication/petit_prince_v1')
DECISION = f'provenance/publication/{WORK}-2026-09-22.json'
CONFIG = Path('data/reader/collection_v2.json')


def plan(root):
    work = read(root / 'corpus/works' / WORK / 'work.json')
    config = read(root / CONFIG)
    config.setdefault('publication_decisions', {})[WORK] = DECISION
    if not publication_approved(root, config, work, {}):
        raise ValueError('Missing matching publication decision')
    canonical = Path(work['canonical_local_path'])
    annotation = Path('results/annotation_private/context_extension_3_v0_13_v0_3_1')
    translations = Path('results/annotation_private/context_extension_3_v0_13_translations_v1')
    review = Path('results/review_private/context_extension_3_v0_13_ai_review_v1')
    summary = read(root / annotation / 'summary.json')
    if (summary['status'] != 'complete' or summary['failed'] or not summary['valid']
            or any(c['work_id'] != WORK for c in summary['cases'])):
        raise ValueError('Expected a completed Prince-only annotation run')
    tr = read(root / translations / 'summary.json')
    if tr['status'] != 'complete' or tr['failed']:
        raise ValueError('Prince translations are incomplete')
    for directory in (review, translations, annotation):
        if not (root / directory).is_dir():
            raise ValueError('Missing saved stage: ' + directory.as_posix())
    if RUN not in config['annotation_runs']:
        config['annotation_runs'].append(RUN)
    if WORK not in config.setdefault('additional_works', []):
        config['additional_works'].append(WORK)
    config.setdefault('run_data_commits', {})[RUN] = 'main'
    config.setdefault('run_paths', {})[RUN] = (EXPORT / 'annotation').as_posix()
    config.setdefault('canonical_paths', {})[WORK] = (EXPORT / 'canonical.txt').as_posix()
    # Validate the real saved inputs, translations, outputs and source offsets before copying.
    local_config = copy.deepcopy(config)
    local_config['run_paths'][RUN] = annotation.as_posix()
    local_config['canonical_paths'][WORK] = canonical.as_posix()
    load_collection(root, local_config)
    copies = {EXPORT / 'canonical.txt': (root / canonical).read_bytes()}
    for source, destination in [(review, 'review'), (translations, 'translations'), (annotation, 'annotation')]:
        for path in sorted((root / source).rglob('*')):
            if path.is_symlink():
                raise ValueError('Unexpected symlink in saved outputs: ' + str(path))
            if path.is_file():
                copies[EXPORT / destination / path.relative_to(root / source)] = path.read_bytes()
    # Include only this work's extraction, never the whole private-output tree.
    extraction = root / 'results/extraction_private/context_extension_3_v0_13/works' / WORK
    if not extraction.is_dir():
        raise ValueError('Missing Prince extraction: ' + str(extraction))
    for path in sorted(extraction.rglob('*')):
        if path.is_symlink():
            raise ValueError('Unexpected extraction symlink')
        if path.is_file():
            copies[EXPORT / 'extraction' / path.relative_to(extraction)] = path.read_bytes()
    # Reruns tolerate checkout newline normalization for textual records; canonical bytes stay exact.
    for relative, data in copies.items():
        target = root / relative
        if target.exists() and target.read_bytes() != data:
            if relative.name == 'canonical.txt' or target.read_text(encoding='utf-8') != data.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n'):
                raise ValueError('Refusing to overwrite a divergent published artifact: ' + str(relative))
    return config, copies


def include(root=ROOT):
    config, copies = plan(root)
    for relative, data in copies.items():
        target = root / relative
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    # The originals, including historical rights metadata, remain untouched.
    export_manifest = {
        'work_id': WORK, 'publication_decision': DECISION,
        'canonical_sha256': hashlib.sha256(copies[EXPORT / 'canonical.txt']).hexdigest(),
        'note': 'Copies of saved local records; no rescoring or altered requests. Original paths in provenance refer to the original run.',
        'files': {p.relative_to(EXPORT).as_posix(): hashlib.sha256((root/p).read_text(encoding='utf-8').encode()).hexdigest()
                  for p in sorted(copies)},
        'hash_normalization': 'UTF-8 text after universal-newline decoding; canonical_sha256 separately hashes original bytes.'}
    manifest = root / EXPORT / 'publication.json'
    manifest.write_text(json.dumps(export_manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')
    outputs = generate(root, config)
    for relative, content in outputs.items():
        path = root / 'docs/reader' / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8', newline='\n')
    (root / CONFIG).write_text(json.dumps(config, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')
    result = json.loads(outputs['manifest.json'])
    print(json.dumps({'status':'included', 'occurrences':result['occurrences'],
                      'works_searched':result['works_searched'], 'export':EXPORT.as_posix(), 'api_calls':0}))

if __name__ == '__main__':
    try:
        include()
    except (ValueError, FileNotFoundError) as exc:
        raise SystemExit(str(exc))
