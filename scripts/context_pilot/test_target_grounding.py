"""Regression checks for identity drift, source preservation and v2 isolation."""
from copy import deepcopy
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
from scripts.context_pilot import run_pilot as p
from scripts.context_pilot.target_grounding import START, END, unmark_inputs
from scripts.context_pilot import test_pilot as fixtures


class TargetGroundingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = p.read(p.ROOT/'data/context_pilot/selection_v2.json')
        cls.schema = p.read(p.ROOT/'prompts/context_pilot/schema_v2.json')

    def inputs(self, case=4, scope='dossier'):
        return p.inputs(self.config['cases'][case], scope, self.config)[0]

    def answer(self, prepared):
        value = fixtures.PilotTests.answer(self, prepared)
        ref = prepared['TARGET_REFERENCE']
        value['target_identification'] = (
            {k: ref[k] for k in ('speaker','addressee','anchor_quote')} if ref else
            {'speaker':None, 'addressee':None, 'anchor_quote':prepared['TARGET']})
        return value

    def test_every_case_keeps_spans_and_source_bytes(self):
        for case in self.config['cases']:
            text, _ = p.source(case, self.config)
            original = next(c for c in p.read(p.SELECTION)['cases'] if c['case_id']==case['case_id'])
            for key in ('target','scene','prior','later','speech_unit_for_review','canonical_sha256'):
                self.assertEqual(original[key], case[key])
            for scope in ('dossier', 'full_text'):
                values, _ = p.inputs(case, scope, self.config)
                self.assertEqual({'TARGET':text[slice(*case['target'])], 'SOURCE_BLOCKS':[], 'TARGET_REFERENCE':None}, values['A'])
                for condition in 'BCD':
                    prepared = values[condition]
                    self.assertEqual(1, sum(b['text'].count(START) for b in prepared['SOURCE_BLOCKS']))
                    self.assertEqual(1, sum(b['text'].count(END) for b in prepared['SOURCE_BLOCKS']))
                    raw = unmark_inputs(prepared)
                    scene = next(b['text'] for b in raw['SOURCE_BLOCKS'] if b['block_id']=='scene')
                    self.assertEqual(text[slice(*case['scene'])], scene)
                    p.validate(self.answer(prepared), prepared, self.schema)
                if scope=='full_text':
                    self.assertEqual(text, ''.join(b['text'] for b in unmark_inputs(values['D'])['SOURCE_BLOCKS']))

    def test_wrong_speaker_and_wrong_recipient_are_rejected(self):
        prepared = self.inputs()['D']
        answer = self.answer(prepared)
        answer['target_identification']['speaker'] = 'Cordelia'
        with self.assertRaisesRegex(ValueError, 'Wrong target speaker'):
            p.validate(answer, prepared, self.schema)
        answer = self.answer(prepared)
        answer['target_identification']['addressee'] = 'Cordelia'
        with self.assertRaisesRegex(ValueError, 'Wrong target addressee'):
            p.validate(answer, prepared, self.schema)

    def test_actual_old_misattribution_cannot_pass_new_schema(self):
        path = p.ROOT/'results/context_pilot/v1_dossier/calls/C05/D/r2-626e7a294af73fcf/output.json'
        old = p.read(path)
        self.assertIn('Cordelia', old['original_speech_situation'])
        with self.assertRaises(ValueError):
            p.validate(old, self.inputs()['D'], self.schema)
        # Retaining the old answer's stated speaker also fails the identity gate.
        old['target_identification'] = {'speaker':'Cordelia','addressee':'Lear',
            'anchor_quote':self.inputs(case=5)['D']['TARGET_REFERENCE']['anchor_quote']}
        with self.assertRaisesRegex(ValueError,'Wrong target speaker'):
            p.validate(old, self.inputs()['D'], self.schema)

    def test_A_has_no_attribution_and_rejects_invented_names(self):
        prepared = self.inputs()['A']
        answer = self.answer(prepared)
        p.validate(answer, prepared, self.schema)
        answer['target_identification']['speaker'] = 'Goneril'
        with self.assertRaisesRegex(ValueError,'Wrong target speaker'):
            p.validate(answer, prepared, self.schema)
        encoded = json.dumps(prepared)
        for name in ('Goneril','Cordelia','Lear'):
            self.assertNotIn(name, encoded)

    def test_first_Goneril_occurrence_and_quotes_crossing_marker(self):
        prepared = self.inputs()['B']
        scene = prepared['SOURCE_BLOCKS'][0]['text']
        self.assertIn('Sir, '+START+'I love you'+END+' more than', scene)
        self.assertIn('so much I love you.', scene)
        answer = self.answer(prepared)
        answer['dimensions']['T']['evidence'] = [{'block_id':'scene','quotation':'Sir, I love you more than word can wield the matter;'}]
        p.validate(answer, prepared, self.schema)
        answer['target_identification']['anchor_quote'] = self.inputs(case=5)['B']['TARGET_REFERENCE']['anchor_quote']
        with self.assertRaisesRegex(ValueError,'Wrong target anchor'):
            p.validate(answer, prepared, self.schema)

    def test_A_and_B_identical_across_scopes(self):
        for index in (4,5):
            dossier, full = self.inputs(index), self.inputs(index,'full_text')
            for condition in 'AB':
                self.assertEqual(dossier[condition],full[condition])

    def test_protocol_resumes_after_CRLF_checkout_conversion(self):
        # No API calls; temporary protocol documents simulate Windows line endings.
        prepared = self.inputs()
        manifest = {'rights':{'public_render_policy':'PUBLIC_DOMAIN_FULL_CONTEXT_OK'}}
        pricing = {'pricing_verified_on':'fixture'}
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            documents = []
            for relative in ('data/context_pilot/selection_v2.json',
                             'prompts/context_pilot/classify_v2.md',
                             'prompts/context_pilot/schema_v2.json'):
                path = root/relative
                path.parent.mkdir(parents=True,exist_ok=True)
                path.write_bytes((p.ROOT/relative).read_bytes())
                documents.append(path)
            with patch.object(p,'ROOT',root),patch.object(p,'inputs',return_value=(prepared,manifest)),patch.object(p,'resolve_model',return_value=('fixture',pricing)):
                first = p.prepare('dossier','fixture',['C05'],'v2')
                for path in documents:
                    path.write_bytes(path.read_bytes().replace(b'\n',b'\r\n'))
                second = p.prepare('dossier','fixture',['C05'],'v2')
            self.assertEqual(first[4],second[4])
            self.assertEqual([c['fingerprint'] for c in first[0]], [c['fingerprint'] for c in second[0]])

    def test_v2_paid_calls_resume_and_do_not_recover_wrong_identity(self):
        prepared = self.inputs()['B']
        answer = self.answer(prepared)
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            body={'model':'fixture','input':json.dumps(prepared),'max_output_tokens':8000}
            call={'case_id':'C05','condition':'B','repeat':1,'public':False,'prepared':prepared,
                  'body':body,'fingerprint':'v2-fixture','directory':root/'call'}
            wrong=deepcopy(answer);wrong['target_identification']['speaker']='Cordelia'
            attempt=root/'call/attempt-001'
            p.write(attempt/'request.json',body)
            p.write(attempt/'response.json',{'status':'completed','output':[{'content':[{'type':'output_text','text':json.dumps(wrong)}]}]})
            self.assertEqual(0,p.recover_saved([call],self.schema))
            protocol={'protocol_version':'context_pilot_v2','scope':'dossier','api_model':'fixture',
                      'repetitions':1,'cases':[{'case_id':'C05','label':'fixture'}]}
            pricing={'pricing_verified_on':'2026-09-21','usd_per_million_tokens':{'input':4,'cached_input':0.4,'output':20}}
            args=SimpleNamespace(protocol='v2',scope='dossier',model='fixture',cases=None,run=True,
                max_input_chars=250000,max_estimate_usd=25,max_calls=None,timeout=1,retry_failed=True)
            sent=[]
            def caller(body,*unused):
                sent.append(body)
                return {'status':'completed','output':[{'content':[{'type':'output_text','text':json.dumps(answer)}]}]}
            with patch.object(p,'prepare',return_value=([call],root,pricing,self.schema,protocol)),patch.dict('os.environ',{'OPENAI_API_KEY':'fixture'}),redirect_stdout(io.StringIO()):
                p.run(args,caller);p.run(args,caller)
            self.assertEqual(1,len(sent));self.assertEqual(8000,sent[0]['max_output_tokens'])
            self.assertEqual('Goneril',p.read(root/'summary.json')['judgments'][0]['target_identification']['speaker'])
            self.assertTrue((root/'call/attempt-002/response.json').exists())
            self.assertTrue((attempt/'response.json').exists())
            # An old fingerprint can never resume as a new protocol result.
            call['fingerprint']='v1-fixture'
            with self.assertRaisesRegex(ValueError,'fingerprint mismatch'):
                p.result_for(call,self.schema)

if __name__=='__main__':unittest.main()
