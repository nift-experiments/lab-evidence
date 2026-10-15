from pathlib import Path
import sys,os,json,hashlib,statistics,subprocess
root=Path('/opt/filesystem/suite');sys.path.insert(0,str(root/'scripts'));import run,fixtures
out=root/'work/diagnostic-threeway';out.mkdir(exist_ok=False);scratch=out/'suite';(scratch/'work').mkdir(parents=True);(scratch/'adapters').symlink_to(root/'adapters');run.R=scratch
versions={v:Path('/opt/recert-threeway')/v/'nift' for v in ['prior','checkpoint','candidate']};rows=[]
meta={'candidate_sha':'c14d06835bca515a5281e41da0e40219c2d60ef0','prior_sha':'c8d9c266518d115e4f289c5c6a2b94ddd7ee9968','scope':'separate3pairbooteddiagnostic','sources':{'prior':'c8d9c266518d115e4f289c5c6a2b94ddd7ee9968','checkpoint':'7f7e487c47a87e871dfef53345e2b71288008bff','candidate':'c14d06835bca515a5281e41da0e40219c2d60ef0'},'binary_sha256':{k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in versions.items()},'build_flags':'normal Makefile O2','cases':['walk-10000','stat-10000','filter-size-10000']};(out/'launch.json').write_text(json.dumps(meta,indent=2)+'\n')
for name in meta['cases']:
 protocol=root if not name.startswith('filter-') else Path('/opt/filesystem/filter-supplement')
 cases=json.loads((protocol/'docs/SCENARIOS.json').read_text());c=next(c for c in cases if c['id']==name)
 fixture=root/'work/fixtures/10000';dest=scratch/'work/destination';expect=fixtures.expected(c['kind'],fixture,dest,c['n'],c['variant'])
 if name.startswith('filter-'):
  import importlib.util
  spec=importlib.util.spec_from_file_location('filterfixtures',protocol/'scripts/fixtures.py');ff=importlib.util.module_from_spec(spec);spec.loader.exec_module(ff);expect=ff.expected(c['kind'],fixture,dest,c['n'],c['variant'])
 for pair in range(-1,3):
  for label in (list(versions)[pair%3:]+list(versions)[:pair%3]):
   run.commands=lambda:{'nift':[str(versions[label]),str(protocol/'adapters/nift.f')]}
   before=fixtures.prepare(c['kind'],fixture,dest,c['n'],c['variant']);actual,metrics=run.measure('nift',f"{c['kind']}|{fixture}|{dest}|{c['n']}|{c['variant']}\n",'booted',timeout=60);assert actual==expect;fixtures.verify_output(c['kind'],fixture,dest,before,c['n']);rec=dict(case=name,version=label,pair=pair,warmup=pair<0,count=len(actual),result_sha256=run.digest(actual),correct=True,**metrics);rows.append(rec)
   with (out/'observations.jsonl').open('a') as f:f.write(json.dumps(rec)+'\n')
   print(name,label,pair,metrics['wall_ms'],flush=True)
summary=[]
for name in meta['cases']:
 med={label:statistics.median(r['wall_ms'] for r in rows if r['case']==name and r['version']==label and not r['warmup']) for label in versions};summary.append(dict(case=name,median_ms=med,candidate_percent_lower=100*(1-med['candidate']/med['prior'])))
(out/'summary.json').write_text(json.dumps({'pass':True,'rows':len(rows),'cases':summary,'qualification':'three pairs descriptive, not formal significance; same frozen adapter on both versions'},indent=2)+'\n')
