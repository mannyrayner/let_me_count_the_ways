"""Deterministic target location and reviewed attribution for pilot v2.

Source bytes and offsets remain unchanged. Markers exist only in model inputs.
Reference labels are supplied in B/C/D; condition A contains no such labels.
"""
from copy import deepcopy

START = '[[[FOCAL_TARGET_START]]]'
END = '[[[FOCAL_TARGET_END]]]'


def normalized(text):
    return ' '.join(text.split())


def ground_inputs(prepared, case, text):
    values = {condition: deepcopy(value) for condition, value in prepared.items()}
    a, b = case['scene']
    start, end = case['target']
    left, right = case['speech_unit_for_review']
    if not a <= left <= start < end <= right <= b:
        raise ValueError('Reference anchor must contain target and lie within scene')
    identity = case['reviewed_identity']
    if any(not isinstance(identity.get(k), str) or not identity[k].strip()
           for k in ('speaker', 'addressee', 'basis')):
        raise ValueError('Missing reviewed target attribution')
    for condition, value in values.items():
        value['TARGET_REFERENCE'] = None
        if condition == 'A':
            if value['SOURCE_BLOCKS']:
                raise ValueError('Expression-only condition must not contain context')
            continue
        reference = {k: identity[k] for k in ('speaker', 'addressee')}
        reference.update(block_id='scene', anchor_quote=text[left:right],
                         target_start_in_unmarked_scene=start-a,
                         target_end_in_unmarked_scene=end-a)
        value['TARGET_REFERENCE'] = reference
        scenes = [block for block in value['SOURCE_BLOCKS'] if block['block_id'] == 'scene']
        if len(scenes) != 1:
            raise ValueError('Expected exactly one scene')
        for block in value['SOURCE_BLOCKS']:
            if START in block['text'] or END in block['text']:
                raise ValueError('Editorial marker collides with source')
        scene = scenes[0]
        if scene['text'] != text[a:b] or scene['text'][start-a:end-a] != value['TARGET']:
            raise ValueError('Target offsets do not match scene')
        scene['text'] = text[a:start] + START + text[start:end] + END + text[end:b]
    return values


def unmark_inputs(prepared):
    value = deepcopy(prepared)
    for block in value['SOURCE_BLOCKS']:
        block['text'] = block['text'].replace(START, '').replace(END, '')
    return value


def validate_identification(result, prepared):
    identity = result['target_identification']
    ref = prepared['TARGET_REFERENCE']
    if ref is None:
        expected = {'speaker': None, 'addressee': None, 'anchor_quote': prepared['TARGET']}
    else:
        expected = {k: ref[k] for k in ('speaker', 'addressee', 'anchor_quote')}
        scene = next(b['text'] for b in prepared['SOURCE_BLOCKS'] if b['block_id'] == 'scene')
        if scene.count(START) != 1 or scene.count(END) != 1:
            raise ValueError('Expected one marked target in scene')
        if scene.split(START, 1)[1].split(END, 1)[0] != prepared['TARGET']:
            raise ValueError('Marked target differs from TARGET')
        unmarked = scene.replace(START, '').replace(END, '')
        a, b = ref['target_start_in_unmarked_scene'], ref['target_end_in_unmarked_scene']
        if scene.index(START) != a or unmarked[a:b] != prepared['TARGET']:
            raise ValueError('Marker does not identify frozen target offsets')
        if ref['anchor_quote'] not in unmarked:
            raise ValueError('Reference anchor is not source text')
    for key in ('speaker', 'addressee'):
        if identity[key] != expected[key]:
            raise ValueError('Wrong target ' + key + ': expected ' + repr(expected[key]) + ', got ' + repr(identity[key]))
    if normalized(identity['anchor_quote']) != normalized(expected['anchor_quote']):
        raise ValueError('Wrong target anchor: copy the supplied source anchor without substitution')
