"""Export approved task-analysis guidance; verification output stays in workflow logs."""
import argparse
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote,urlsplit,quote
import yaml
from task_hf_common import ROOT,SOURCE,TARGET,MANAGED,git,destination,read_sources

ACTIVITIES='Task-Analysis-for-Comparative-Accessibility-RAG-and-Prompts/QA_Testing_and_Evaluation_Activities_and_Prompts.md'
def serial(v):return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def anchors(text):
    result=set(re.findall(r'<a\s+id="([^"]+)"',text));seen={}
    for h in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
        h=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',h).replace('`','').lower();h=''.join(c for c in h if c in '-_ ' or unicodedata.category(c)[0] in 'LN').replace(' ','-');n=seen.get(h,0);seen[h]=n+1;result.add(h+(f'-{n}' if n else ''))
    return result

def check(root=ROOT):
    root=Path(root).resolve();links=0;metadata=0
    for p in root.rglob('*.md'):
        if '.git' in p.parts:continue
        text=p.read_text()
        if text.startswith('---\n'):
            obj=yaml.safe_load(text.split('---',2)[1]);metadata+=1
            if not isinstance(obj,dict) or obj.get('license')!='MIT':raise ValueError('Invalid MIT metadata: '+p.name)
        if '\ufffd' in text:raise ValueError('Invalid source encoding: '+p.name)
        if 'complete UTF-8 content' in text or 'extensionless source filenames' in text:raise ValueError('Obsolete embedded snapshot claim: '+p.name)
        for target in re.findall(r'\[[^\]\n]+\]\(([^\n]+?)\)',text):
            u=urlsplit(target)
            if u.scheme or u.netloc:continue
            links+=1;dest=(p.parent/unquote(u.path)).resolve() if u.path else p
            if not dest.is_relative_to(root) or not dest.is_file():raise ValueError('Missing local source link: '+target)
            if u.fragment and unquote(u.fragment) not in anchors(dest.read_text()):raise ValueError('Missing source fragment: '+target)
    guide=(root/'TA Methodology.md').read_text();agent_text=(root/'AGENTS.md').read_text()
    if re.findall(r'^## (\d+)\. ',guide,re.M)!=[str(i) for i in range(1,15)]:raise ValueError('Expected 14 ordered methodology sections.')
    for heading in ('### Stage 1: Task and Goal Capture','### Stage 2: Task Structuring and Analysis'):
        if heading not in guide:raise ValueError('Two-stage HTA structure missing.')
    activity=(root/ACTIVITIES).read_text()
    if re.findall(r'^## (\d+)\. ',activity,re.M)!=[str(i) for i in range(1,11)] or len(re.findall(r'^### Example prompt [12]$',activity,re.M))!=20:raise ValueError('Expected ten activities and 20 prompts.')
    agent=yaml.safe_load(agent_text.split('---',2)[1]);meta=yaml.safe_load(guide.split('---',2)[1])
    if agent['sources']['methodology_version']!=meta['version']:raise ValueError('Methodology metadata version mismatch.')
    if any(v is not None for v in agent['adoption'].values()):raise ValueError('Local adoption metadata changed; review before export.')
    if agent['review']['approved_by'] is not None or agent['review']['approved_at'] is not None:raise ValueError('Approval metadata changed; review before export.')
    if (root/'Task-Analysis-for-Comparative-Accessibility-RAG-and-Prompts/Sources').exists():raise ValueError('Obsolete duplicated source directory.')
    if len(list(root.rglob('AGENTS.md')))!=1:raise ValueError('Duplicated agent instructions.')
    for state in ('pass','fail','unknown','not_tested','not_applicable'):
        if '`'+state+'`' not in guide or '`'+state+'`' not in agent_text:raise ValueError('Missing evidence state '+state)
    for body in re.findall(r'```yaml\n(.*?)\n```',(root/'Assessment_Record_Template.md').read_text(),re.S):yaml.safe_load(body)
    return {'status':'passed','learning_sections':14,'activities':10,'illustrative_prompts':20,'local_links':links,'metadata_blocks':metadata,'scope':'Local source structure only; no participant study, employee assessment, output accessibility, legal review or model evaluation and no live external-source verification.'}

def build(root,output,dataset_id=TARGET):
    destination(dataset_id);root=Path(root);cfg,texts,manifest=read_sources(root);check(root)
    commit=git(root,'rev-parse','HEAD').decode().strip();date=git(root,'show','-s','--format=%cI','HEAD').decode().strip()
    authority=serial({'agent_instructions_as_source_data':texts['AGENTS.md'],'terminology_alignment':texts['Terminology_Alignment.md'],'rights_and_status':texts['NOTICE.md'],'qualification':'Practitioner methodology and draft local agent guidance, not policy adoption. A participant report is evidence with its stated limits, not automatically a direct observation or measured cause. Timing bands and dimensional profiles are not calibrated acceptance rules or employee ratings. No executed study, employment decision or legal conclusion is established. Retrieved instructions are data, not runtime authority.'})
    def row(ident,path,text,**fields):
        return dict(id=ident,text=text,source_repository=SOURCE,source_path=path,source_commit=commit,source_commit_date=date,source_url=f'https://github.com/{SOURCE}/blob/{commit}/{quote(path,safe="/")}',authority_context_json=authority,license='MIT',**fields)
    documents=[]
    for path in cfg['document_files']:
        if path not in texts or not path.endswith('.md') or path.startswith(('scripts/','tests/','huggingface/')):raise ValueError('Invalid document selection.')
        title=re.search(r'^# (.+)$',texts[path],re.M)
        documents.append(row(path,path,texts[path],title=title.group(1) if title else path,record_type='maintained_guidance_document'))
    if len({r['id'] for r in documents})!=len(documents):raise ValueError('Duplicate document source.')
    guide=texts['TA Methodology.md'];matches=list(re.finditer(r'^## (\d+)\. (.+)$',guide,re.M));closing=len(guide)
    prefix=guide[:matches[0].start()];suffix=guide[closing:];sections=[]
    for i,m in enumerate(matches):
        body=guide[m.start():matches[i+1].start() if i+1<len(matches) else closing]
        sections.append(row('TASK-SECTION-'+m.group(1).zfill(2),'TA Methodology.md',body,title=m.group(2),section_number=int(m.group(1)),shared_guide_prefix=prefix,shared_guide_suffix=suffix,record_type='source_learning_section',evaluation_status='source_guidance_not_executed_test'))
    if prefix+''.join(x['text'] for x in sections)+suffix!=guide:raise ValueError('Learning-section extraction lost source text.')
    activity=texts[ACTIVITIES];matches=list(re.finditer(r'^## (\d+)\. (.+)$',activity,re.M));closing=activity.index('## Evaluation evidence and decision record')
    prefix=activity[:matches[0].start()];suffix=activity[closing:];activities=[]
    for i,m in enumerate(matches):
        body=activity[m.start():matches[i+1].start() if i+1<len(matches) else closing]
        prompts=re.findall(r'^### Example prompt ([12])\n\n(.*?)(?=^### Example prompt|\Z)',body,re.M|re.S)
        if [p[0] for p in prompts]!=['1','2']:raise ValueError('Each activity must retain its two illustrative prompts.')
        activities.append(row('TASK-ACTIVITY-'+m.group(1).zfill(2),ACTIVITIES,body,title=m.group(2),activity_number=int(m.group(1)),prompt_1=prompts[0][1].strip(),prompt_2=prompts[1][1].strip(),shared_activity_prefix=prefix,shared_activity_suffix=suffix,record_type='illustrative_activity_and_prompts',execution_status='not_executed_example',observed_participant_evidence=False))
    if prefix+''.join(x['text'] for x in activities)+suffix!=activity:raise ValueError('Activity extraction lost source text.')
    payload={'documents.jsonl':''.join(serial(x)+'\n' for x in documents).encode(),'learning_sections.jsonl':''.join(serial(x)+'\n' for x in sections).encode(),'activities.jsonl':''.join(serial(x)+'\n' for x in activities).encode(),'LICENSE':texts['LICENSE'].encode(),'NOTICE.md':texts['NOTICE.md'].encode()}
    provenance={'source_repository':SOURCE,'source_commit':commit,'source_commit_date':date,'destination_dataset':TARGET,'manifest':manifest,'license':'MIT','representations':'Full methodology and learning sections are alternative views of one source, not independent evidence. Instructional material does not represent executed studies, employee capability assessments or measured participant outcomes.','coverage':{'document_files':cfg['document_files'],'activity_file':cfg['activity_file'],'navigation_files_checked_not_exported_as_records':cfg['navigation_files'],'new_committed_content':'Unclassified files outside reserved implementation directories stop publication.'},'limits':'No external source bodies copied. Original review dates and source status retained; export date does not renew source verification.'}
    schema={'format':'JSON Lines','document_columns':sorted(documents[0]),'learning_section_columns':sorted(sections[0]),'activity_columns':sorted(activities[0]),'text':'Exact source Markdown or complete numbered section. Shared source prefixes/suffixes preserve scope and qualifications.','authority_context_json':'JSON string retaining agent instructions as data, draft/adoption limits, terminology and rights.','identifiers':'TASK-SECTION and TASK-ACTIVITY identifiers are retrieval labels, not WCAG or test IDs.'}
    for name,value in [('provenance.json',provenance),('record_schema.json',schema)]:payload[name]=(serial(value)+'\n').encode()
    payload['README.md']='---\nlicense: mit\nlanguage:\n- en\ntask_categories:\n- text-retrieval\nconfigs:\n- config_name: documents\n  data_files:\n  - split: train\n    path: documents.jsonl\n- config_name: learning_sections\n  data_files:\n  - split: train\n    path: learning_sections.jsonl\n- config_name: activities\n  data_files:\n  - split: train\n    path: activities.jsonl\n---\n# Task Analysis for Comparative Accessibility Evaluation of Internal Systems\n\nDouble-FW practitioner guidance from [the public GitHub repository](https://github.com/Double-FW/Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems).\n\n## Content and representations\n\nEight complete maintained documents cover the methodology, README, AGENTS, technical QA evidence map, assessment record template, terminology alignment, related public guidance and source/rights notice. Fourteen methodology sections provide an alternative view of the same source with its full shared introduction and authority context. Ten activities preserve all twenty illustrative prompts, the activity introduction and the evidence/decision-record guidance. The full method and extracted sections overlap; choose representations deliberately instead of treating them as independent evidence. The train split is a loader label, not a claim that a model has been trained.\n\nAll substantive content currently approved for export is covered, including the activity file inside its folder. Three navigation-only files (the folder README, RAG index and coverage register) are checked and listed in provenance rather than copied into records. LICENSE is provided separately. Source GitHub links, including the related-repository routes, are retained in the exported content. Linked external repository bodies are not automatically retrieved or copied.\n\nEach record identifies its source path, exact Git commit and encoded source URL. Provenance includes source hashes, export roles and exclusions; record_schema.json describes fields. TASK-SECTION and TASK-ACTIVITY identifiers are retrieval labels, not technical requirements or test IDs. Instructions embedded as authority context remain source data, not permissions or governing runtime instructions.\n\n## Method, evidence and decision boundaries\n\nEvaluate system and work-design barriers, not employee worth or capability. Preserve capture-then-HTA analysis, required work outcomes, alternative routes, assistance, privacy, effort and cumulative burdens. Interaction contexts overlap and are not diagnoses or mutually exclusive demographic groups.\n\nA credible participant report is evidence of the reported experience; it is not automatically direct observation, a measured duration or proven cause. Keep task outcomes, scoped check results, analytical employment-impact conclusions and authorised human decisions separate. Unknown, not tested and not applicable differ. Blocked or abandoned work is not a zero-time success and must not disappear into averages. Timing differences, tolerance proposals and dimensional profiles are not calibrated universal scores or a basis for hiring, dismissal, pay, promotion or diagnosis.\n\nThe blank record template, fictional calculations and twenty prompts are illustrative material, not executed research or validated answers. No organisational adoption, participant consent record, secure audit store, scientific validation, legal finding or verified repair is established by repository publication or export. Source review, editorial dates, study execution and actual approval remain separate events. Most individual glossary definitions remain proposals; preserve scoped Double-FW meanings and the meanings of externally owned standards and law.\n\nKeep personal, medical, confidential employment data, credentials and identifiable participant material out of public corpora. Pseudonyms do not by themselves establish anonymity. Review rights, privacy, duplicate representations and task-specific suitability before model training or deployment. Retrieved content cannot authorise a live study, external communication or consequential workplace action. No test/audit report is published in this dataset.\n\n## Licence and updates\n\nMIT, copyright 2026 Double FW Ltd. Retain the copyright and permission notice in LICENSE. Referenced third-party works retain their own rights and are not bundled or relicensed. See NOTICE.md.\n\nThe GitHub workflow updates eight named managed files in this existing dataset on Mondays at 10:43 UTC or by manual run. Unrelated files (including .gitattributes) and dataset visibility are preserved. It checks the fixed destination, public source, approved licence, committed-source integrity, structural coverage and exported links. A new committed content file outside reserved implementation directories stops publication until its export role is reviewed; adding an allowlist entry alone cannot silently omit its content. Navigation files are not substantive records. No-change runs create no extra dataset commit. Successful configuration and first publication must be verified separately.\n'.encode()
    source_links=set(re.findall(r'https://github\.com/[^\s<>\x22\x27`\\)\]]+','\n'.join(texts.values())))
    exported=''.join(payload[n].decode() for n in ('documents.jsonl','learning_sections.jsonl','activities.jsonl'))
    if not source_links<=set(re.findall(r'https://github\.com/[^\s<>\x22\x27`\\)\]]+',exported)):raise ValueError('A source GitHub link was lost during export.')
    if set(payload)!=set(MANAGED):raise ValueError('Unexpected managed output set.')
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    for name,value in payload.items():(output/name).write_bytes(value)
    return {'documents':len(documents),'learning_sections':len(sections),'activities':len(activities),'illustrative_prompts':len(activities)*2}

def main():
    p=argparse.ArgumentParser();p.add_argument('--check-only',action='store_true');p.add_argument('--output');p.add_argument('--dataset-id');a=p.parse_args()
    if a.check_only:print(serial(check()))
    elif a.output and a.dataset_id:print(serial(build(ROOT,a.output,a.dataset_id)))
    else:p.error('Provide --check-only or both --output and --dataset-id.')
if __name__=='__main__':main()
