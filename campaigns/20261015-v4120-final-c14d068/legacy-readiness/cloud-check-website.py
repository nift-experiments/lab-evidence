import sys,json,subprocess,tempfile,shutil
from pathlib import Path
root=Path('/opt/campaign/website-generator-benchmark');sys.path.insert(0,str(root/'scripts'))
from campaign import fixtures,validate,snapshot,legacy
from campaign_measure import isolated_env
candidate='/opt/nift/nift';hugo=str(Path('/opt/campaign/tools/bin/hugo'));rows=[]
def run(cmd,cwd,env):
 p=subprocess.run(cmd,cwd=cwd,env=env,capture_output=True,timeout=1200)
 if p.returncode:raise RuntimeError(p.stderr.decode(errors='replace')[-1500:])
with tempfile.TemporaryDirectory(prefix='legacy-refresh-website-') as td:
 base=Path(td);env=isolated_env(base/'home');env.update(GOMAXPROCS='1',CI='1')
 for pages in (100,1000,10000):
  fs=fixtures(base/str(pages),pages,candidate,hugo,root) if pages==100 else {'Nift':legacy.nift_fixture(base/str(pages),pages,candidate)}
  for name,(cwd,cmd,_) in fs.items():
   if name=='Nift':cmd=[candidate,'build','--all']
   run(cmd,cwd,env);rows.append({'engine':name,'pages':pages,'scenario':'full','correct':True,**validate(name,cwd,pages)})
   if name!='Nift':continue
   for case in ('noop','one-page','shared-template','targeted-one-page'):
    marker='pilot-'+case
    if case in ('one-page','targeted-one-page'):
     p=cwd/'content/page-1.html';p.write_text(f'<h1>Page 1</h1><p>Equivalent benchmark content.</p><!--{marker}-->');legacy.force_mtime_change(p,rows.__len__())
    if case=='shared-template':
     p=cwd/'templates/template.html';p.write_text(p.read_text()+f'<!--{marker}-->');legacy.force_mtime_change(p,rows.__len__())
    before=snapshot(cwd);run([candidate,'build',*(['page-1'] if case=='targeted-one-page' else [])],cwd,env)
    kwargs={'leaf_marker':marker} if case in ('one-page','targeted-one-page') else {'template_marker':marker} if case=='shared-template' else {}
    validate(name,cwd,pages,**kwargs);after=snapshot(cwd)
    if case in ('noop','targeted-one-page') and any(after[k]!=v for k,v in before.items() if case=='noop' or k!='page-1.html'):raise RuntimeError('unrelated page changed')
    run([candidate,'build','--all'],cwd,env)
    if snapshot(cwd)!=after:raise RuntimeError('incremental/target output differs from full rebuild')
    rows.append({'engine':name,'pages':pages,'scenario':case,'correct':True,'full_rebuild_parity':True})
    Path('/opt/campaign/evidence/website-correctness.json').write_text(json.dumps({'candidate':'c14d06835bca515a5281e41da0e40219c2d60ef0','kind':'cloud-correctness-only','rows':rows},indent=2)+'\n');print(rows[-1],flush=True)
print('COMPLETE',len(rows))
