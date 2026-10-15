"""Untimed fresh-build workload accounting, only after all official timing ends."""
from pathlib import Path
import sys,json,os,tempfile,subprocess,hashlib
R=Path('/opt/website-publication');assert (R/'evidence/official-allcore/PASS').exists();assert json.loads((R/'evidence/official-allcore/independent-audit.json').read_text())['pass'];assert sorted(os.sched_getaffinity(0))==[0,1,2,3]
sys.path.insert(0,str(R/'suite/scripts'));from campaign import fixtures,validate,output_root;from campaign_measure import isolated_env
DEST=R/'evidence/work-accounting';DEST.mkdir(parents=True,exist_ok=True)
def inventory(root):
 result={};links={}
 for p in sorted(root.rglob('*')):
  if p.is_symlink():links[str(p.relative_to(root))]=os.readlink(p)
  elif p.is_file():result[str(p.relative_to(root))]={'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 return result,links
rows=[]
with tempfile.TemporaryDirectory(prefix='website-work-accounting-') as td:
 base=Path(td);env=isolated_env(base/'home');env.pop('GOMAXPROCS',None);env['CI']='1'
 for n in (100,1000,10000):
  fs=fixtures(base/str(n),n,'/opt/nift/nift',str(R/'tools/bin/hugo'),R/'suite');cfg=fs['Nift'][0]/'.nift/config.json';c=json.loads(cfg.read_text());c['config']['build-threads']=-1;cfg.write_text(json.dumps(c))
  for name,(cwd,cmd,cleanup) in fs.items():
   initial,links=inventory(cwd);label=f'{name.lower()}-{n}';log=DEST/(label+'.log')
   with log.open('wb') as f:subprocess.run(cmd,cwd=cwd,env=env,stdout=f,stderr=subprocess.STDOUT,check=True,timeout=1200)
   oracle=validate(name,cwd,n);after,afterlinks=inventory(cwd);out=output_root(name,cwd);public={str(p.relative_to(out)):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(out.rglob('*')) if p.is_file()};new={k:v for k,v in after.items() if k not in initial and not k.startswith(str(out.relative_to(cwd))+'/')}
   manifest={'initial_files':initial,'external_dependency_symlinks':links,'all_after_build_files':after,'public_output_files':public,'new_non_public_files':new};(DEST/(label+'-manifest.json')).write_text(json.dumps(manifest,indent=2)+'\n')
   source={'Nift':'HTML content + explicit tracked JSON + template expansion; tracking metadata ownership/dependencies included','Hugo':'Markdown/frontmatter + Go template; Goldmark unsafeHTML enabled; homekind disabled','Astro':'Astro file routes; generated HTML source + minimal build config; bundler machinery retained','VitePress':'Markdown + Vue minimal theme; hydration assets and validated404 retained'}[name]
   row={'engine':name,'pages':n,'argv':cmd,'worker_policy':{'affinity':[0,1,2,3],'nift_build_threads':-1,'Hugo_GOMAXPROCS':'unset'},'untimed':True,'correct':True,'semantic_oracle':oracle,'input_files':len(initial),'input_bytes':sum(x['bytes'] for x in initial.values()),'public_files':len(public),'public_bytes':sum(x['bytes'] for x in public.values()),'public_html_files':sum(k.endswith('.html') for k in public),'new_non_public_files':len(new),'new_non_public_bytes':sum(x['bytes'] for x in new.values()),'external_dependency_links':links,'source_model':source,'output_extras':'VitePress adds validated404 and hydration/build assets; Astro may retain buildassets; exact paths inmanifest','manifest':label+'-manifest.json'};rows.append(row);(DEST/'summary.json').write_text(json.dumps({'kind':'untimed freshfixture workaccounting, not an extra timing cohort','rows':rows},indent=2)+'\n');print(name,n,'ACCOUNTED',flush=True)
assert len(rows)==12 and all(x['correct'] for x in rows);(DEST/'PASS').write_text('WORK_ACCOUNTING12_PASS\n')
