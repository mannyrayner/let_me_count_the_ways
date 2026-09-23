from copy import deepcopy
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import tempfile
import unittest
from scripts.context_pilot.quotation_matching import match
from scripts.context_pilot import run_pilot as p
from scripts.context_pilot import test_pilot as fixtures

SOURCE='«Что-то такое особенное говорят в этих случаях», думал он, но никак не мог вспомнить, чтò такое именно говорят в этих случаях.'
QUOTE=SOURCE.replace('чтò','чтó')

class QuotationTests(unittest.TestCase):
    def test_long_unique_passage_is_audited_with_exact_source(self):
        block='Перед этим.\n'+SOURCE+'\nПосле этого.'
        self.assertIsNone(match(QUOTE,block))
        audit=match(QUOTE,block,True)
        self.assertEqual('accent_alignment',audit['kind'])
        self.assertEqual(SOURCE,block[audit['source_start']:audit['source_end']])
        self.assertEqual(SOURCE,audit['source_quotation'])
        self.assertEqual(1,len(audit['differences']))

    def test_short_ambiguous_or_lexically_changed_quotes_fail(self):
        self.assertIsNone(match('чтó','чтò',True))
        self.assertIsNone(match(QUOTE,SOURCE+' '+SOURCE,True))
        self.assertIsNone(match(QUOTE.replace('особенное','необычное'),SOURCE,True))
        self.assertIsNone(match(QUOTE.replace('думал','Думал'),SOURCE,True))
        self.assertIsNone(match(QUOTE.replace('»,','»;'),SOURCE,True))

    def test_decomposed_accents_and_whitespace_keep_raw_offsets(self):
        block=SOURCE.replace('ò','o\u0300').replace(' думал','\nдумал')
        audit=match(QUOTE,block,True)
        self.assertEqual(block,audit['source_quotation'])
        self.assertEqual(len(block),audit['source_end'])
        self.assertEqual('whitespace',match('a b','a\nb')['kind'])
        self.assertEqual('verbatim',match('a b','x a b y')['kind'])

    def test_recovery_keeps_response_and_scores_and_does_not_replace_accepted(self):
        prepared={'TARGET':'Je vous aime','SOURCE_BLOCKS':[{'block_id':'scene','text':SOURCE}],
                  'TARGET_REFERENCE':None}
        # Use expression-only identity validation; the synthetic scene is solely for quote recovery.
        answer=fixtures.PilotTests.answer(self,prepared)
        answer['target_identification']={'speaker':None,'addressee':None,'anchor_quote':prepared['TARGET']}
        answer['dimensions']['E']['evidence']=[{'block_id':'scene','quotation':QUOTE}]
        schema=p.read(p.ROOT/'prompts/context_pilot/schema_v2.json')
        with tempfile.TemporaryDirectory() as td:
            directory=Path(td);attempt=directory/'attempt-001'
            body={'model':'fixture','input':'fixture','max_output_tokens':8000}
            response={'status':'completed','output':[{'content':[{'type':'output_text','text':json.dumps(answer)}]}]}
            p.write(attempt/'request.json',body);p.write(attempt/'response.json',response)
            before=(attempt/'response.json').read_bytes()
            call={'directory':directory,'prepared':prepared,'body':body,'fingerprint':'fixture',
                  'case_id':'test','condition':'B','repeat':1}
            with redirect_stdout(io.StringIO()):
                self.assertEqual(1,p.recover_saved([call],schema))
                self.assertEqual(0,p.recover_saved([call],schema))
            self.assertEqual(answer,p.result_for(call,schema))
            self.assertEqual(before,(attempt/'response.json').read_bytes())
            self.assertTrue(any(x['kind']=='accent_alignment' for x in p.read(directory/'quotation_audit.json')))

if __name__=='__main__':unittest.main()
