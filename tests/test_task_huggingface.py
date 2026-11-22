import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from export_huggingface import build
from publish_huggingface import publish
from task_hf_common import MANAGED,SOURCE,TARGET
from huggingface_hub.errors import EntryNotFoundError

class FakeHub:
    def __init__(self,root):self.files={'.gitattributes':b'preserve me','unrelated.md':b'preserve me too'};self.parent='destination-parent';self.commits=[];self.root=root;self.reject_concurrent=False
    def repo_info(self,**kwargs):return SimpleNamespace(sha=self.parent)
    def download(self,filename,**kwargs):
        if filename not in self.files:raise EntryNotFoundError('Missing test file')
        path=self.root/'old'/filename;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(self.files[filename]);return str(path)
    def create_commit(self,**kwargs):
        if self.reject_concurrent or kwargs['parent_commit']!=self.parent:raise RuntimeError('Concurrent destination change')
        self.commits.append(kwargs)
        for op in kwargs['operations']:self.files[op.path_in_repo]=op.path_or_fileobj
        self.parent='next-destination-parent'

class TaskExport(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.work=Path(self.tmp.name);self.root=self.work/'source';self.output=self.work/'export'
        subprocess.run(['git','clone','--quiet','--no-hardlinks',str(ROOT),str(self.root)],check=True)
    def tearDown(self):self.tmp.cleanup()
    def rows(self,name):return [json.loads(l) for l in (self.output/name).read_text().splitlines()]
    def preview(self):return build(self.root,self.output)
    def publish(self,hub,**kw):return publish(self.output,'hf_synthetic_not_a_real_credential',source_root=self.root,api=hub,download=hub.download,check_public=lambda:None,**kw)
    def commit(self):
        subprocess.run(['git','-C',str(self.root),'-c','user.name=Test','-c','user.email=test@example.invalid','add','-A'],check=True)
        subprocess.run(['git','-C',str(self.root),'-c','user.name=Test','-c','user.email=test@example.invalid','commit','-qm','Fixture change'],check=True)
    def test_documents_preserve_full_source_and_draft_authority(self):
        report=self.preview();self.assertEqual(8,report['documents'])
        for r in self.rows('documents.jsonl'):
            self.assertEqual((self.root/r['source_path']).read_text(),r['text']);self.assertIn('draft',json.loads(r['authority_context_json'])['qualification'].lower())
    def test_learning_sections_reconstruct_complete_guide_with_scope(self):
        report=self.preview();self.assertEqual(14,report['learning_sections']);rows=self.rows('learning_sections.jsonl')
        self.assertEqual(list(range(1,15)),[r['section_number'] for r in rows]);self.assertEqual((self.root/'TA Methodology.md').read_text(),rows[0]['shared_guide_prefix']+''.join(r['text'] for r in rows)+rows[0]['shared_guide_suffix'])
        for r in rows:self.assertIn('not to rank employees',r['shared_guide_prefix']);self.assertEqual('source_guidance_not_executed_test',r['evaluation_status'])
    def test_activities_reconstruct_source_and_preserve_20_prompts(self):
        report=self.preview();self.assertEqual(10,report['activities']);self.assertEqual(20,report['illustrative_prompts']);rows=self.rows('activities.jsonl')
        source=self.root/'Task-Analysis-for-Comparative-Accessibility-RAG-and-Prompts/QA_Testing_and_Evaluation_Activities_and_Prompts.md'
        self.assertEqual(source.read_text(),rows[0]['shared_activity_prefix']+''.join(r['text'] for r in rows)+rows[0]['shared_activity_suffix'])
        for r in rows:self.assertTrue(r['prompt_1']);self.assertTrue(r['prompt_2']);self.assertFalse(r['observed_participant_evidence']);self.assertEqual('not_executed_example',r['execution_status'])
    def test_only_managed_files_and_no_report_are_published(self):
        self.preview();self.assertEqual(set(MANAGED),{p.name for p in self.output.iterdir()});self.assertFalse(any('report' in name for name in MANAGED))
    def test_missing_learning_section_is_rejected_after_commit(self):
        p=self.root/'TA Methodology.md';p.write_text(p.read_text().replace('## 14. ','## 98. '));self.commit()
        with self.assertRaisesRegex(ValueError,'14 ordered|Missing source fragment'):self.preview()
    def test_method_version_drift_is_rejected(self):
        p=self.root/'AGENTS.md';p.write_text(p.read_text().replace('methodology_version: "1.2.0"','methodology_version: "99"'));self.commit()
        with self.assertRaisesRegex(ValueError,'metadata version mismatch'):self.preview()
    def test_source_context_preserves_employment_and_rights_limits(self):
        self.preview()
        for r in self.rows('learning_sections.jsonl'):
            context=json.loads(r['authority_context_json'])
            self.assertIn('not calibrated acceptance rules',context['qualification'])
            self.assertIn('MIT',context['rights_and_status'])
            self.assertIn('not runtime authority',context['qualification'])
    def test_invented_policy_adoption_stops_export(self):
        p=self.root/'AGENTS.md';p.write_text(p.read_text().replace('policy_adopted_by: null','policy_adopted_by: invented'));self.commit()
        with self.assertRaisesRegex(ValueError,'Local adoption metadata changed'):self.preview()
    def test_committed_guidance_update_reaches_next_publication(self):
        self.preview();hub=FakeHub(self.work);self.publish(hub)
        p=self.root/'TA Methodology.md';p.write_text(p.read_text()+'\nAdditional scoped editorial clarification.\n');self.commit();self.preview();self.publish(hub)
        self.assertEqual(2,len(hub.commits));rows=[json.loads(x) for x in hub.files['documents.jsonl'].decode().splitlines()]
        self.assertEqual(p.read_text(),next(x['text'] for x in rows if x['source_path']=='TA Methodology.md'))
    def test_dataset_name_in_token_field_stops_before_network(self):
        with self.assertRaisesRegex(ValueError,'generated hf_ token'):publish(self.output,TARGET,source_root=self.root,check_public=lambda:self.fail('Network check must not run'))
    def test_same_revision_is_deterministic(self):
        self.preview();other=self.work/'second';build(self.root,other)
        for n in MANAGED:self.assertEqual((self.output/n).read_bytes(),(other/n).read_bytes())
    def test_dirty_canonical_source_stops_export(self):
        p=self.root/'TA Methodology.md';p.write_text(p.read_text()+'\n')
        with self.assertRaisesRegex(ValueError,'Working source differs'):self.preview()
    def test_missing_committed_required_source_stops_export(self):
        (self.root/'TA Methodology.md').unlink();self.commit()
        with self.assertRaisesRegex(ValueError,'committed regular file'):self.preview()
    def test_changed_licence_stops_export(self):
        p=self.root/'LICENSE';p.write_text(p.read_text()+'\nChanged licence.\n');self.commit()
        with self.assertRaisesRegex(ValueError,'Licence bytes changed'):self.preview()
    def test_wrong_destination_stops_before_publish(self):
        self.preview();hub=FakeHub(self.work)
        with self.assertRaisesRegex(ValueError,'HF_DATASET_ID'):self.publish(hub,dataset_id='GarethFW/wrong')
        self.assertEqual([],hub.commits)
    def test_modified_export_cannot_publish(self):
        self.preview();p=self.output/'documents.jsonl';p.write_text(p.read_text()+'\n');hub=FakeHub(self.work)
        with self.assertRaisesRegex(ValueError,'Export bytes differ'):self.publish(hub)
        self.assertEqual([],hub.commits)
    def test_first_publish_is_atomic_and_preserves_other_files(self):
        self.preview();hub=FakeHub(self.work);self.publish(hub)
        self.assertEqual(1,len(hub.commits));self.assertEqual('destination-parent',hub.commits[0]['parent_commit'])
        self.assertEqual(set(MANAGED),{o.path_in_repo for o in hub.commits[0]['operations']});self.assertEqual(b'preserve me',hub.files['.gitattributes'])
    def test_repeat_publish_creates_no_extra_commit(self):
        self.preview();hub=FakeHub(self.work);self.publish(hub);result=self.publish(hub)
        self.assertIn('No changes',result);self.assertEqual(1,len(hub.commits))
    def test_foreign_destination_provenance_is_not_overwritten(self):
        self.preview();hub=FakeHub(self.work);hub.files['provenance.json']=b'{"source_repository":"another/source"}'
        with self.assertRaisesRegex(ValueError,'different source'):self.publish(hub)
        self.assertEqual([],hub.commits)
    def test_concurrent_destination_change_is_not_blindly_retried(self):
        self.preview();hub=FakeHub(self.work);hub.reject_concurrent=True
        with self.assertRaisesRegex(RuntimeError,'Concurrent'):self.publish(hub)
        self.assertEqual([],hub.commits)
    def test_private_source_failure_prevents_destination_write(self):
        self.preview();hub=FakeHub(self.work)
        def private():raise ValueError('Source is private')
        with self.assertRaisesRegex(ValueError,'private'):publish(self.output,'hf_synthetic',source_root=self.root,api=hub,download=hub.download,check_public=private)
        self.assertEqual([],hub.commits)
    def test_whitespace_token_is_rejected_without_echoing_it(self):
        self.preview();token=' accidental-sensitive-token\n'
        with self.assertRaises(ValueError) as raised:publish(self.output,token,source_root=self.root,check_public=lambda:None)
        self.assertNotIn(token.strip(),str(raised.exception))

    def test_new_nested_content_stops_before_destination_write(self):
        p=self.root/'new-guidance/deeper/extra.md';p.parent.mkdir(parents=True);p.write_text('# New substantive content\n');self.commit()
        with self.assertRaisesRegex(ValueError,'New committed content'):self.preview()
    def test_allowlist_addition_without_export_role_is_rejected(self):
        p=self.root/'extra.md';p.write_text('# New content\n')
        cfg=self.root/'huggingface/export-config.json';data=json.loads(cfg.read_text());data['source_files'].append('extra.md');cfg.write_text(json.dumps(data));self.commit()
        with self.assertRaisesRegex(ValueError,'needs an export or navigation role'):self.preview()
    def test_reviewed_nested_document_is_included_in_full(self):
        name='new-guidance/deeper/extra.md';p=self.root/name;p.parent.mkdir(parents=True);p.write_text('# Reviewed content\n\nA complete new guidance document.\n')
        cfg=self.root/'huggingface/export-config.json';data=json.loads(cfg.read_text());data['source_files'].append(name);data['document_files'].append(name);cfg.write_text(json.dumps(data));self.commit();self.preview()
        self.assertEqual(p.read_text(),next(r['text'] for r in self.rows('documents.jsonl') if r['source_path']==name))
    def test_all_source_github_links_survive(self):
        import re
        self.preview();cfg=json.loads((self.root/'huggingface/export-config.json').read_text())
        links=lambda text:set(re.findall(r'https://github\.com/[^\s<>\x22\x27`\\)\]]+',text))
        source=links('\n'.join((self.root/p).read_text() for p in cfg['source_files']))
        exported=links(''.join((self.output/n).read_text() for n in ['documents.jsonl','learning_sections.jsonl','activities.jsonl']))
        self.assertTrue(source<=exported)
    def test_source_url_encodes_spaces(self):
        self.preview();r=next(r for r in self.rows('documents.jsonl') if r['source_path']=='TA Methodology.md')
        self.assertIn('TA%20Methodology.md',r['source_url']);self.assertNotIn(' ',r['source_url'])
    def test_navigation_is_explicitly_excluded_as_records(self):
        self.preview();cfg=json.loads((self.root/'huggingface/export-config.json').read_text())
        exported={r['source_path'] for r in self.rows('documents.jsonl')}
        self.assertTrue(set(cfg['navigation_files']).isdisjoint(exported))
        self.assertEqual(cfg['navigation_files'],json.loads((self.output/'provenance.json').read_text())['coverage']['navigation_files_checked_not_exported_as_records'])

class PublicSourceCheck(unittest.TestCase):
    def test_uses_workflow_github_token_for_github_request(self):
        from unittest.mock import patch
        from io import BytesIO
        from task_hf_common import public_source
        info={'full_name':SOURCE,'private':False,'visibility':'public'}
        with patch.dict('os.environ',{'GITHUB_TOKEN':'synthetic-github-token'}),patch('urllib.request.urlopen',return_value=BytesIO(json.dumps(info).encode())) as call:
            public_source()
            request=call.call_args.args[0]
            self.assertEqual('https://api.github.com/repos/'+SOURCE,request.full_url)
            self.assertEqual('Bearer synthetic-github-token',request.get_header('Authorization'))
    def test_http_error_identifies_source_check_without_sensitive_body(self):
        from unittest.mock import patch
        from io import BytesIO
        from urllib.error import HTTPError
        from task_hf_common import public_source
        failure=HTTPError('https://api.github.com/repos/'+SOURCE,403,'sensitive response detail',{},BytesIO(b'private response body'))
        with patch('urllib.request.urlopen',side_effect=failure):
            with self.assertRaisesRegex(ValueError,r'Public GitHub source verification failed \(HTTP 403\)') as raised:public_source()
        self.assertNotIn('sensitive',str(raised.exception));self.assertNotIn('private response body',str(raised.exception))
    def test_authenticated_private_source_is_still_blocked(self):
        from unittest.mock import patch
        from io import BytesIO
        from task_hf_common import public_source
        info={'full_name':SOURCE,'private':True,'visibility':'private'}
        with patch.dict('os.environ',{'GITHUB_TOKEN':'synthetic-github-token'}),patch('urllib.request.urlopen',return_value=BytesIO(json.dumps(info).encode())):
            with self.assertRaisesRegex(ValueError,'approved public'):public_source()

if __name__=='__main__':unittest.main()
