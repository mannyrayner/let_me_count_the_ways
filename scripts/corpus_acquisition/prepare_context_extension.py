#!/usr/bin/env python3
"""Reproduce the three original-language context-study sources; no API calls."""
from __future__ import annotations
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.corpus_acquisition.prepare_commitment_extension import download, stable_write, json_bytes, digest
from scripts.corpus_acquisition.acquire_public_domain_text import trim_gutenberg
from scripts.corpus.validate_canonical_corpus import validate_work

SELECTION = Path('data/acquisition/context_extension_3_v1/selection.json')

def tag(node):
    return node.tag.rsplit('}', 1)[-1]

def literary_inline(node):
    # Delimiter spans contain actual words at page boundaries. Keep them.
    if (node.get('class') in {'npnumber', 'opnumber'}
            or (tag(node) == 'a' and node.get('type') == 'note')):
        return ''
    value = node.text or ''
    for child in node:
        value += literary_inline(child) + (child.tail or '')
    return value

def blocks(node):
    for child in node:
        if tag(child) in {'p', 'h2', 'h3', 'h4', 'h5'}:
            value = re.sub(r'\s+', ' ', literary_inline(child)).strip()
            if value:
                yield value
        elif tag(child) not in {'script', 'style', 'img'}:
            yield from blocks(child)

def tolstoy_volume(raw, volume):
    tree = ET.fromstring(raw)
    prefix = 'h000009001' if volume == 9 else 'h000007001'
    parts = []
    for node in tree.iter():
        identifier = node.get('id', '')
        if tag(node) != 'div' or node.get('class') != 'section' or not identifier.startswith(prefix):
            continue
        if identifier == prefix:
            # Volume heading only; portraits and captions are not narrative.
            values = [re.sub(r'\s+', ' ', literary_inline(n)).strip() for n in node if tag(n) == 'h2']
        else:
            values = list(blocks(node))
        if values:
            parts.append((identifier, '\n\n'.join(values)))
    if not parts:
        raise ValueError('Tolstoy main-text sections missing')
    return parts

class PrinceParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.current = None
        self.buffer = []
        self.values = []
    def handle_starttag(self, name, attrs):
        if name in {'p', 'h2'}:
            self.current, self.buffer = name, []
        elif name == 'br' and self.current:
            self.buffer.append(' ')
    def handle_data(self, data):
        if self.current:
            self.buffer.append(data)
    def handle_endtag(self, name):
        if name == self.current:
            value = re.sub(r'\s+', ' ', ''.join(self.buffer)).strip()
            if value:
                self.values.append((name, value))
            self.current = None

def prince_text(raw):
    parser = PrinceParser()
    parser.feed(raw.decode('iso-8859-1'))
    active, paragraphs = False, []
    for kind, value in parser.values:
        if kind == 'h2' and value == 'DEDICACE':
            active = True
        if kind == 'h2' and value == 'THE END':
            break
        if active:
            paragraphs.append(value)
    text = '\n\n'.join(paragraphs) + '\n'
    if len(re.findall(r'(?m)^(?:PREMIER CHAPITRE|CHAPITRE [IVX]+)$', text)) != 27:
        raise ValueError('Expected 27 Petit Prince chapters')
    if "écrivez-moi vite qu'il est revenu" not in text:
        raise ValueError('Petit Prince ending missing')
    return text

def section_map(text, pattern):
    matches = list(re.finditer(pattern, text, re.M))
    return [{'heading': m.group(), 'start': m.start(),
             'end': matches[i+1].start() if i+1 < len(matches) else len(text)}
            for i, m in enumerate(matches)]

def prepare(root=ROOT):
    selection = json.loads((root / SELECTION).read_text(encoding='utf-8'))
    for work in selection['works']:
        wid = work['work_id']
        private = work.get('private', False)
        raw_dir = root / ('data/local_candidate_sources' if private else 'data/raw') / wid
        downloads, sections = [], []
        if work['source_type'] == 'tolstoy_online':
            chunks, offset = [], 0
            for volume in range(9, 13):
                url = f'https://tolstoy.ru/online/90/{volume:02d}/'
                path = raw_dir / f'volume-{volume:02d}.html'
                raw = download(url, path)
                downloads.append({'url': url, 'path': str(path.relative_to(root)), 'sha256': digest(raw)})
                for identifier, part in tolstoy_volume(raw, volume):
                    if chunks:
                        chunks.append('\n\n'); offset += 2
                    start = offset
                    chunks.append(part); offset += len(part)
                    sections.append({'volume': volume, 'source_id': identifier,
                                     'source_url': url + '#' + identifier,
                                     'start': start, 'end': offset, 'heading': part.split('\n', 1)[0]})
            text = ''.join(chunks) + '\n'
        else:
            path = raw_dir / ('source.html' if private else 'source-download.txt')
            raw = download(work['download_url'], path)
            downloads.append({'url': work['download_url'], 'path': str(path.relative_to(root)), 'sha256': digest(raw)})
            if private:
                text = prince_text(raw)
                sections = section_map(text, r'^(?:PREMIER CHAPITRE|CHAPITRE [IVX]+)$')
            else:
                text = trim_gutenberg(raw.decode('utf-8-sig')).replace('\r\n', '\n').replace('\r', '\n')
                sections = section_map(text, r'^SCENE [IVX]+\.[^\n]*')
                if len(sections) != 26:
                    raise ValueError('Expected 26 King Lear scenes')
        data = text.encode('utf-8')
        canonical = (root / 'data/local_candidate_derived' / wid / 'canonical.txt' if private
                     else root / 'corpus/works' / wid / 'canonical.txt')
        stable_write(canonical, data)
        map_path = root / 'data/acquisition/context_extension_3_v1' / f'{wid}-sections.json'
        stable_write(map_path, json_bytes({'canonical_sha256': digest(data), 'sections': sections}))
        provenance_path = Path('provenance/sources') / (wid + '-context-v1.json')
        provenance = {k: v for k, v in work.items() if k != 'private'}
        provenance.update(downloads=downloads, canonical_sha256=digest(data),
                          derivation_version='context_sources_v1', retrieved_on=selection['selected_on'],
                          section_map=str(map_path.relative_to(root)))
        stable_write(root / provenance_path, json_bytes(provenance))
        manifest = {'schema_version': '1.0', **{k: work[k] for k in ('work_id','title','author','language','source_type')},
                    'canonical_text': None if private else 'canonical.txt', 'canonical_sha256': digest(data),
                    'source_references': [str(provenance_path), str(SELECTION)],
                    'rights': {'analysis_allowed': True, 'public_render_policy':
                               'LIMITED_QUOTATION_ONLY' if private else 'PUBLIC_DOMAIN_FULL_CONTEXT_OK'},
                    'notes': work['source_note']}
        if private:
            manifest.update(canonical_storage='local_private', canonical_local_path=str(canonical.relative_to(root)))
            manifest['rights']['rights_review'] = {'status': 'REVIEW_REQUIRED', 'issue': 'territorial_copyright',
                'note': 'Source designates public domain in Australia. Full-text redistribution elsewhere is not cleared; keep source and contexts in ignored local directories.'}
        work_dir = root / 'corpus/works' / wid
        stable_write(work_dir / 'work.json', json_bytes(manifest))
        errors, _ = validate_work(work_dir, root)
        if errors:
            raise ValueError(errors)
        print(json.dumps({'work_id': wid, 'characters': len(text), 'sections': len(sections), 'storage': manifest.get('canonical_storage','repository')}))

if __name__ == '__main__':
    prepare()
