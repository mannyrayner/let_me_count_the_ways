"""Regression checks for publication decisions and byte-preserving import using synthetic fixtures."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from scripts.reader.records import ROOT, read, load_collection, publication_approved
from scripts.reader.include_petit_prince import WORK, RUN, EXPORT, CONFIG, DECISION, include, plan


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False)+'\n', encoding='utf-8')

class PublicationTests(unittest.TestCase):
    def test_public_extension_is_in_combined_reader(self):
        config = read(ROOT/CONFIG)
        config["annotation_runs"] = [run for run in config["annotation_runs"] if run != RUN]
        config["additional_works"] = [wid for wid in config["additional_works"] if wid != WORK]
        records, inventory, _ = load_collection(config=config)
        self.assertEqual(292, len(records))
        self.assertEqual(37, len(inventory))
        self.assertEqual(36, sum(r['work']['work_id']=='tolstoy-war-and-peace' for r in records))

    def fixture(self, root):
        # Reuse a historical French input solely as a synthetic test fixture; no new model output.
        config = read(ROOT/'data/reader/collection_v1.json')
        records, _, _ = load_collection(config=config)
        record = next(r for r in records if r['work']['language']=='fr')
        work = copy.deepcopy(record['work'])
        original_wid = work['work_id']
        work.update(work_id=WORK, canonical_storage='local_private', canonical_text=None,
                    canonical_local_path=f'data/local_candidate_derived/{WORK}/canonical.txt')
        work['rights']['public_render_policy']='LIMITED_QUOTATION_ONLY'
        write(root/'corpus/works'/WORK/'work.json',work)
        canonical = root/work['canonical_local_path']
        canonical.parent.mkdir(parents=True)
        shutil.copyfile(ROOT/'corpus/works'/original_wid/'canonical.txt', canonical)
        write(root/DECISION, {'decision':'PROJECT_PUBLICATION_APPROVED', 'work_id':WORK,
                              'canonical_sha256':work['canonical_sha256'], 'qualification':'Synthetic fixture.'})
        config.update(annotation_runs=[], additional_works=[], work_inventory='inventory.json')
        write(root/CONFIG, config)
        write(root/'inventory.json', {'works':{}})
        for name in ('reader.css','reader.js'):
            target=root/'scripts/reader'/name
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(ROOT/'scripts/reader'/name,target)
        ann=root/'results/annotation_private/context_extension_3_v0_13_v0_3_1'
        output_path=ROOT/record['output_path']
        dest=ann/'annotations'/record['occurrence_id']/output_path.parent.name
        shutil.copytree(output_path.parent,dest)
        request=read(dest/'request.json')
        prefix, raw=request['input'].split('## Input\n\n',1)
        prepared=json.loads(raw)
        prepared['METADATA']['work']=work
        request['input']=prefix+'## Input\n\n'+json.dumps(prepared,ensure_ascii=False)
        write(dest/'request.json', request)
        summary=read(ROOT/'results/annotation'/record['run']/'summary.json')
        case=next(c for c in summary['cases'] if c['occurrence_id']==record['occurrence_id'])
        case['work_id']=WORK
        summary.update(cases=[case],valid=1,requested=1,failed=0,status='complete')
        write(ann/'summary.json',summary)
        write(root/'results/annotation_private/context_extension_3_v0_13_translations_v1/summary.json',
              {'status':'complete','failed':0})
        write(root/'results/review_private/context_extension_3_v0_13_ai_review_v1/summary.json',{'fixture':True})
        write(root/'results/extraction_private/context_extension_3_v0_13/works'/WORK/'fixture.json',{'work_id':WORK})
        return canonical, dest

    def test_import_is_resumable_and_preserves_original_request(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            canonical,dest=self.fixture(root)
            before=(dest/'request.json').read_bytes()
            include(root)
            records,inventory,_=load_collection(root,read(root/CONFIG))
            self.assertEqual(1,len(records));self.assertEqual(1,len(inventory))
            self.assertEqual(before,(dest/'request.json').read_bytes())
            copied=next((root/EXPORT/'annotation/annotations').glob('*/*/request.json'))
            self.assertEqual(before,copied.read_bytes())
            self.assertEqual(canonical.read_bytes(),(root/EXPORT/'canonical.txt').read_bytes())
            include(root)
            (root/EXPORT/'canonical.txt').write_text('divergent',encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'divergent'):
                plan(root)

    def test_approval_cannot_cover_different_hash_or_no_public_render(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);self.fixture(root)
            config,copies=plan(root)
            work=read(root/'corpus/works'/WORK/'work.json')
            changed=copy.deepcopy(work);changed['canonical_sha256']='0'*64
            with self.assertRaisesRegex(ValueError,'source hash'):
                publication_approved(root,config,changed,{})
            work['rights']['public_render_policy']='NO_PUBLIC_RENDER'
            write(root/'corpus/works'/WORK/'work.json',work)
            with self.assertRaisesRegex(ValueError,'Public rendering not allowed'):
                plan(root)

if __name__=='__main__':unittest.main()
