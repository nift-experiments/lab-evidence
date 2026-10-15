import sys,json,tempfile,subprocess,hashlib,collections
from pathlib import Path
sys.path.insert(0,'/opt/supplement/current/scripts')
from campaign import legacy,validate
from campaign_measure import isolated_env
R=Path('/opt/supplement/evidence/fixture-audit');R.mkdir(exist_ok=True)
def snapshot(root):
 a=[]
 for p in sorted(root.rglob('*')):
  if p.is_file():a.append({'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 return a
rows=[]
for engine in ('Nift','Hugo'):
 with tempfile.TemporaryDirectory(prefix='supp-work-accounting-') as td:
  root=Path(td);exe='/opt/nift/nift' if engine=='Nift' else '/opt/supplement/tools/hugo';cwd,command,outputs=legacy.nift_fixture(root,10000,exe) if engine=='Nift' else legacy.hugo_fixture(root,10000,exe);env=isolated_env(root/'home');env.update(GOMAXPROCS='1',CI='1')
  if engine=='Nift':
   c=cwd/'.nift/config.json';d=json.loads(c.read_text());d['config']['build-threads']=1;c.write_text(json.dumps(d));command=[exe,'build','--all']
  else:
   c=cwd/'hugo.toml';c.write_text(c.read_text().replace('["taxonomy"','["home", "taxonomy"')+'\n[markup.goldmark.renderer]\nunsafe = true\n')
  snapshots={};snapshots['initial']=snapshot(cwd)
  for mode in ('fresh','warm-full'):
   if mode=='warm-full':legacy.clean_outputs(cwd,outputs)
   snapshots[mode+'-before']=snapshot(cwd);p=subprocess.run(command,cwd=cwd,env=env,capture_output=True,timeout=180);assert p.returncode==0;v=validate(engine,cwd,10000);snapshots[mode+'-after']=snapshot(cwd)
  dest=R/engine;dest.mkdir();(dest/'manifests.json').write_text(json.dumps(snapshots,indent=2)+'\n')
  for p in cwd.rglob('*'):
   rel=str(p.relative_to(cwd))
   if p.is_file() and (rel in ('hugo.toml','.nift/config.json','.nift/tracked.json','templates/template.html','layouts/_default/single.html','content/index.html','content/page-1.html','content/page-0.md','content/page-1.md','public/index.html','public/page-1.html') or rel.startswith('.nift/') and p.stat().st_size<10000):
    if rel.startswith('.nift/') and rel not in ('.nift/config.json','.nift/tracked.json') and len(list(dest.glob('internal-*')))>4:continue
    (dest/('internal-'+rel.replace('/','_'))).write_bytes(p.read_bytes())
  counts={name:{'files':len(a),'bytes':sum(x['bytes'] for x in a),'by_top_directory':dict(collections.Counter(x['path'].split('/')[0] for x in a))} for name,a in snapshots.items()};rows.append({'engine':engine,'validation':v,'snapshots':counts,'semantic_source_note':'Nift HTML with explicit tracked JSON +template vs Hugo Markdown files with YAML front matter and Goldmark unsafe HTML pass-through; same resulting route/title/body contract, different parser/metadata work'})
(R/'summary.json').write_text(json.dumps({'kind':'untimed full fixture/internal metadata/output accounting after completed host timing','rows':rows},indent=2)+'\n');print(json.dumps(rows))
