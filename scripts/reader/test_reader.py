"""Evidence fidelity, safe rendering, local navigation and filter behavior."""
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import shutil
import subprocess
import unittest
from scripts.reader.records import ROOT, load_collection
from scripts.reader.build_reader import generate, read, target_text

class Elements(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.rows=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        for key in ['href','src']:
            if key in a:self.links.append(a[key])
        if tag=='tr' and 'data-work' in a:self.rows.append({k[5:]:v for k,v in a.items() if k.startswith('data-')})

class ReaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records,cls.inventory,_=load_collection()
        cls.generated=generate(ROOT,read(ROOT/'data/reader/collection_v1.json'))
    def test_all_saved_records_and_zero_yield_work(self):
        self.assertEqual(252,len(self.records));self.assertEqual(35,len(self.inventory))
        self.assertIn('benedictsson-pengar',self.inventory)
        self.assertEqual(23,sum(r['scores']['P']>=3 for r in self.records))
    def test_all_html_links_resolve(self):
        for name,text in self.generated.items():
            if not name.endswith('.html'):continue
            parser=Elements();parser.feed(text)
            for link in parser.links:
                if link.startswith(('http:','https:','#','mailto:')):continue
                path=os.path.normpath(str(Path(name).parent/link.split('#')[0]))
                self.assertIn(path,self.generated,(name,link))
    def test_only_exact_target_highlighted_and_markup_escaped(self):
        r={'location':{'source_start':2,'source_end':5}}
        value=target_text(r,{'context_start':0,'text':'< ILY ILY >'})
        self.assertEqual(1,value.count('<mark>'));self.assertIn('<mark>ILY</mark>',value)
        self.assertIn('&lt;',value);self.assertIn('&gt;',value)
    def test_filter_javascript_on_actual_rendered_rows(self):
        node=shutil.which('node') or os.environ.get('CODEX_PRIMARY_RUNTIME_NODE')
        if not node or not Path(node).exists():self.skipTest('Node unavailable; static reader checks still run')
        parser=Elements();parser.feed(self.generated['index.html'])
        subprocess.run([node,str(ROOT/'scripts/reader/test_filters.js')],input=json.dumps(parser.rows),text=True,check=True,cwd=ROOT)

if __name__=='__main__':unittest.main()
