"""Committed-source and fixed-destination rules for task-analysis publication."""
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import urllib.request
import urllib.error

ROOT=Path(__file__).resolve().parents[1]
SOURCE='Double-FW/Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems'
TARGET='GarethFW/Task_Analysis_for_Comparative_Accessibility_Evaluation_of_Internal_Systems'
MANAGED=('README.md','LICENSE','NOTICE.md','documents.jsonl','learning_sections.jsonl','activities.jsonl','provenance.json','record_schema.json')
CONFIG='huggingface/export-config.json'

def digest(data):return hashlib.sha256(data).hexdigest()
def git(root,*args):return subprocess.check_output(['git','-C',str(root),*args])
def destination(value):
    if value!=TARGET:raise ValueError('HF_DATASET_ID must be '+TARGET+'.')
    return value

def committed(root,path):
    p=PurePosixPath(path)
    if p.is_absolute() or '..' in p.parts or any(x.startswith('.') for x in p.parts):raise ValueError('Invalid approved source path: '+path)
    info=git(root,'ls-tree','HEAD','--',path).decode().strip()
    if not info.startswith('100644 blob '):raise ValueError('Required source must be a committed regular file: '+path)
    sha=info.split()[2];data=git(root,'cat-file','blob',sha)
    if hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()!=sha:raise ValueError('Git source integrity failed: '+path)
    return data,{'path':path,'git_blob_sha':sha,'sha256':digest(data),'size_bytes':len(data)}

def read_sources(root=ROOT):
    raw,entry=committed(root,CONFIG);cfg=json.loads(raw)
    if (Path(root)/CONFIG).read_bytes()!=raw:raise ValueError('Working export configuration differs from committed snapshot.')
    if cfg['source_repository']!=SOURCE:raise ValueError('Wrong source repository in export configuration.')
    destination(cfg['destination_dataset'])
    paths=cfg['source_files']
    if not isinstance(paths,list) or len(paths)!=len(set(paths)) or not all(isinstance(p,str) for p in paths):raise ValueError('Source allowlist must contain unique paths.')
    required={'README.md','AGENTS.md','LICENSE','NOTICE.md','TA Methodology.md','Terminology_Alignment.md','Related_Double_FW_Guidance.md','QA_and_Comparative_Evaluation_Evidence_Map.md','Assessment_Record_Template.md','Task-Analysis-for-Comparative-Accessibility-RAG-and-Prompts/QA_Testing_and_Evaluation_Activities_and_Prompts.md'}
    if not required<=set(paths):raise ValueError('Required guidance, authority and activity sources must remain included.')
    documents=cfg['document_files'];navigation=cfg['navigation_files'];activities=cfg['activity_file']
    if len(documents)!=len(set(documents)) or len(navigation)!=len(set(navigation)):raise ValueError('Duplicate document or navigation classification.')
    roles=[set(documents),set(navigation),{activities},{'LICENSE'}]
    if any(a & b for i,a in enumerate(roles) for b in roles[i+1:]):raise ValueError('Source roles must not overlap.')
    if set(paths)!=set().union(*roles):raise ValueError('Every approved source needs an export or navigation role.')
    tracked=git(root,'ls-tree','-r','--name-only','-z','HEAD').decode().split('\0')
    unclassified=[p for p in tracked if p and p not in paths and not p.startswith(('.github/','scripts/','tests/','huggingface/'))]
    if unclassified:raise ValueError('New committed content is not classified for export: '+', '.join(unclassified))
    texts={};manifest=[entry]
    for path in paths:
        data,e=committed(root,path);text=data.decode('utf-8')
        if any(x in text for x in ['chatgpt.com/library?','account_id=personal','file_id=libfile_']):raise ValueError('Personal source-access locator in public export: '+path)
        texts[path]=text;manifest.append(e)
        working=Path(root)/path
        if not working.is_file() or working.is_symlink() or working.read_bytes()!=data:raise ValueError('Working source differs from the committed snapshot: '+path)
    if digest(texts['LICENSE'].encode())!=cfg['approved_license_sha256']:raise ValueError('Licence bytes changed; review before publication.')
    return cfg,texts,manifest

def public_source():
    headers={'User-Agent':'Double-FW-task-analysis-dataset-sync','Accept':'application/vnd.github+json'}
    token=os.environ.get('GITHUB_TOKEN')
    if token:headers['Authorization']='Bearer '+token
    request=urllib.request.Request('https://api.github.com/repos/'+SOURCE,headers=headers)
    try:
        with urllib.request.urlopen(request,timeout=30) as response:info=json.load(response)
    except urllib.error.HTTPError as e:
        raise ValueError('Public GitHub source verification failed (HTTP '+str(e.code)+'). Check the workflow GitHub token and API availability; no Hugging Face write was attempted.') from None
    except urllib.error.URLError:
        raise ValueError('Public GitHub source verification could not reach the API; no Hugging Face write was attempted.') from None
    if info.get('full_name')!=SOURCE or info.get('private') is not False or info.get('visibility')!='public':raise ValueError('Publishing requires the approved public GitHub source.')
