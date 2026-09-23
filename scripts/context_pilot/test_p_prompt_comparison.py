"""Checks for a prompt-only comparison, not tests of expected literary scores."""
from copy import deepcopy
import unittest
from unittest.mock import patch
from scripts.context_pilot import compare_p_prompts as c
from scripts.context_pilot import run_pilot as p


class PComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Deterministic preparation only; no credentials or model calls.
        for scope,cases in [('dossier',None),('full_text',['C05','C06'])]:
            p.prepare(scope,'5.6',cases,'v3')

    def test_request_difference_is_only_prompt(self):
        for scope in ('dossier','full_text'):
            _,old=c.load_run(scope,'v2')
            _,new=c.load_run(scope,'v3')
            self.assertEqual(set(old),set(new))
            for key in old:
                self.assertEqual(old[key]['prepared'],new[key]['prepared'])
                self.assertEqual({k:v for k,v in old[key]['body'].items() if k!='input'},
                                 {k:v for k,v in new[key]['body'].items() if k!='input'})
                self.assertNotEqual(old[key]['body']['input'],new[key]['body']['input'])
                self.assertNotEqual(old[key]['artifact'],new[key]['artifact'])

    def test_T_E_O_definitions_and_schema_are_unchanged(self):
        a=(p.ROOT/'prompts/context_pilot/classify_v2.md').read_text()
        b=(p.ROOT/'prompts/context_pilot/classify_v3.md').read_text()
        self.assertEqual(a[a.index('E: expressive'):],b[b.index('E: expressive'):])
        self.assertEqual(a[a.index('Give independent support scores'):a.index('P: undertaking')],
                         b[b.index('Give independent support scores'):b.index('P: undertaking')])
        self.assertEqual(a[a.index('Use only TARGET'):a.index('Give independent support scores')],
                         b[b.index('Use only TARGET'):b.index('Give independent support scores')])

    def test_partial_and_insufficient_scores_do_not_become_zero(self):
        def fixture(score):
            return {'dimensions':{k:{'score':score} for k in 'TPEO'}}
        self.assertIsNone(c.describe([fixture(2),None,fixture(4)],3)['dimensions']['P']['median'])
        self.assertIsNone(c.describe([fixture(2),fixture(None),fixture(4)],3)['dimensions']['P']['median'])
        self.assertEqual(2,c.describe([fixture(0),fixture(2),fixture(4)],3)['dimensions']['P']['median'])

    def test_comparison_rejects_changed_evidence(self):
        old=c.load_run('dossier','v2');new=c.load_run('dossier','v3')
        modified=deepcopy(new)
        first=next(iter(modified[1]))
        modified[1][first]['prepared']['TARGET']='different target'
        with patch.object(c,'load_run',side_effect=[old,modified]):
            with self.assertRaisesRegex(ValueError,'Source evidence or target metadata changed'):
                c.compare('dossier')

if __name__=='__main__':unittest.main()
