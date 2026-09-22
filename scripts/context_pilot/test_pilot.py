"""Check context boundaries, source-only evidence, isolation and paid-call resumption."""
from copy import deepcopy
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import patch
from scripts.context_pilot import run_pilot as p

class PilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config=p.read(p.SELECTION);cls.schema=p.read(p.SCHEMA)
    def test_nested_evidence_has_fixed_target_and_no_later_text_in_C(self):
        for case in self.config['cases']:
            values,_=p.inputs(case,'dossier')
            self.assertEqual(1,len({x['TARGET'] for x in values.values()}))
            self.assertEqual([],values['A']['SOURCE_BLOCKS'])
            self.assertEqual(values['B']['SOURCE_BLOCKS'][0],values['C']['SOURCE_BLOCKS'][-1])
            self.assertEqual(values['C']['SOURCE_BLOCKS'],values['D']['SOURCE_BLOCKS'][:len(values['C']['SOURCE_BLOCKS'])])
            self.assertTrue(all(not b['block_id'].startswith('later') for b in values['C']['SOURCE_BLOCKS']))
            self.assertNotIn('scores',values['A']);self.assertNotIn('work_id',values['A'])
    def test_full_text_D_reconstructs_entire_canonical_source(self):
        for case in self.config['cases']:
            values,_=p.inputs(case,'full_text');text,_=p.source(case)
            self.assertEqual(text,''.join(x['text'] for x in values['D']['SOURCE_BLOCKS']))
    def test_future_in_prior_is_rejected(self):
        case=deepcopy(self.config['cases'][0]);case['prior']=[[case['scene'][1],case['scene'][1]+10]]
        with self.assertRaises(ValueError):p.inputs(case,'dossier')
    def answer(self,prepared):
        return {'target_translation':prepared['TARGET'],'dimensions':{k:{'score':4 if k=='T' else 0,'evidence_status':'assessable','confidence':0.8,'reason':'Synthetic fixture only.','evidence':[{'block_id':'target','quotation':prepared['TARGET']}]} for k in 'TPEO'},'original_speech_situation':'Synthetic test.','affection_evidence':'unknown','undertaking_and_uptake':'Unspecified.','recognised_work':False,'recognition_note':'','limitations':'Fixture, not research data.'}
    def test_unknown_is_not_zero_and_quotes_cannot_come_from_memory(self):
        values,_=p.inputs(self.config['cases'][0],'dossier');prepared=values['A'];answer=self.answer(prepared)
        p.validate(answer,prepared,self.schema)
        answer['dimensions']['P']['evidence_status']='insufficient'
        with self.assertRaises(ValueError):p.validate(answer,prepared,self.schema)
        answer['dimensions']['P']['score']=None;p.validate(answer,prepared,self.schema)
        answer['dimensions']['T']['evidence'][0]['quotation']='Invented plot fact'
        with self.assertRaises(ValueError):p.validate(answer,prepared,self.schema)
    def test_quote_matching_ignores_only_whitespace(self):
        self.assertTrue(p.quote_matches('for lidt end for meget', 'for lidt\nend for meget'))
        self.assertFalse(p.quote_matches('for lidt, end for meget', 'for lidt\nend for meget'))
        self.assertFalse(p.quote_matches('for meget end for lidt', 'for lidt\nend for meget'))
        self.assertFalse(p.quote_matches('For lidt end for meget', 'for lidt\nend for meget'))
        self.assertFalse(p.quote_matches('   ', 'anything'))
        prepared={'TARGET':'A', 'SOURCE_BLOCKS':[{'block_id':'scene','text':'for lidt\nend for meget'}, {'block_id':'prior_1','text':'different'}]}
        answer=self.answer(prepared)
        answer['dimensions']['T']['evidence']=[{'block_id':'scene','quotation':'for lidt end for meget'}]
        p.validate(answer,prepared,self.schema)
        answer['dimensions']['T']['evidence'][0]['block_id']='prior_1'
        with self.assertRaises(ValueError):p.validate(answer,prepared,self.schema)

    def test_recovery_keeps_original_attempt_and_is_resumable(self):
        prepared={'TARGET':'for lidt\nend for meget', 'SOURCE_BLOCKS':[]}
        answer=self.answer(prepared)
        for dim in answer['dimensions'].values():
            dim['evidence'][0]['quotation']='for lidt end for meget'
        body={'model':'fixture','input':'synthetic fixture','max_output_tokens':2400}
        with tempfile.TemporaryDirectory() as td:
            directory=Path(td)/'call';attempt=directory/'attempt-001'
            p.write(attempt/'request.json',body)
            p.write(attempt/'response.json',{'status':'completed','output':[{'content':[{'type':'output_text','text':json.dumps(answer)}]}]})
            p.write(attempt/'failure.json',{'message':'Old exact-quote validation failure'})
            before={f.name:f.read_bytes() for f in attempt.iterdir()}
            call={'directory':directory,'prepared':prepared,'body':body,'fingerprint':'test', 'case_id':'fixture','condition':'C','repeat':2}
            with redirect_stdout(io.StringIO()):
                self.assertEqual(1,p.recover_saved([call],self.schema))
                self.assertEqual(0,p.recover_saved([call],self.schema))
            self.assertEqual(before,{f.name:f.read_bytes() for f in attempt.iterdir()})
            self.assertEqual(answer,p.result_for(call,self.schema))
            self.assertTrue(p.read(directory/'provenance.json')['recovered_from_saved_response'])
            self.assertFalse((directory/'attempt-002').exists())

    def test_only_output_ceiling_increase_is_compatible(self):
        planned={'model':'fixture','input':'same evidence','max_output_tokens':2400}
        self.assertTrue(p.compatible_attempt_request(dict(planned,max_output_tokens=8000),planned))
        self.assertFalse(p.compatible_attempt_request(dict(planned,max_output_tokens=1000),planned))
        self.assertFalse(p.compatible_attempt_request(dict(planned,input='changed evidence',max_output_tokens=8000),planned))
        self.assertFalse(p.compatible_attempt_request(dict(planned,model='other',max_output_tokens=8000),planned))

    def test_truncated_response_has_actionable_error(self):
        with self.assertRaisesRegex(ValueError,'Response truncated at max_output_tokens'):
            p.require_complete_response({'status':'incomplete','incomplete_details':{'reason':'max_output_tokens'}})
        with self.assertRaisesRegex(ValueError,'not complete'):
            p.require_complete_response({'status':'failed'})
        p.require_complete_response({'status':'completed'})

    def test_resume_sends_each_independent_request_once(self):
        prepared,_=p.inputs(self.config['cases'][0],'dossier')
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);calls=[]
            for letter in 'AB':
                body={'model':'fixture','input':json.dumps(prepared[letter]),'max_output_tokens':2400}
                calls.append({'case_id':'C01','condition':letter,'repeat':1,'public':False,'prepared':prepared[letter],'body':body,'fingerprint':letter*64,'directory':root/letter})
            pricing={'pricing_verified_on':'2026-09-21','usd_per_million_tokens':{'input':4,'cached_input':0.4,'output':20}}
            protocol={'scope':'dossier','api_model':'fixture','repetitions':1,'cases':[{'case_id':'C01','label':'fixture'}]}
            args=SimpleNamespace(scope='dossier',model='fixture',cases=None,run=True,max_input_chars=250000,max_estimate_usd=25,max_calls=1,timeout=1,retry_failed=False)
            sent=[]
            def caller(body,*ignored):
                sent.append(body);self.assertNotIn('previous_response_id',body)
                result=self.answer(json.loads(body['input']))
                return {'output':[{'content':[{'type':'output_text','text':json.dumps(result)}]}],'usage':{'input_tokens':10,'output_tokens':10}}
            with patch.object(p,'prepare',return_value=(calls,root,pricing,self.schema,protocol)),patch.dict('os.environ',{'OPENAI_API_KEY':'test-placeholder'}),redirect_stdout(io.StringIO()):
                p.run(args,caller)
                args.max_output_tokens=8000
                p.run(args,caller);p.run(args,caller)
            self.assertEqual([2400,8000],[body['max_output_tokens'] for body in sent])
            self.assertEqual(2,len(sent));self.assertEqual('complete',p.read(root/'summary.json')['status'])
            self.assertTrue((root/'A/attempt-001/cost.json').exists())
            self.assertFalse((root/'A/attempt-002').exists())

if __name__=='__main__':unittest.main()
