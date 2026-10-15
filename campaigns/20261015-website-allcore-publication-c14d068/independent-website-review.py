from pathlib import Path
import json,hashlib,statistics,math,re,subprocess
B=Path(__file__).resolve().parent;D=B/'official-allcore';collection=json.loads((B/'COLLECTION-PASS.json').read_text());assert collection['pass'];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();plan=json.loads((B/'PLAN.json').read_text());candidate=plan['candidate'];rows=[];files=[];adapters=[]
for f,h in collection['files_sha256'].items():assert sha(B/f)==h,f
identity=json.loads((B/'host/identity.json').read_text());assert identity['source_clean'] and identity['candidate']==candidate and identity['suite']==plan['suite_sha'];assert identity['plan_sha256']==sha(B/'PLAN.json');assert identity['tools']['Nift']['sha256']==plan['candidate_cli_sha256'];assert identity['worker_policy']==plan['policy']
assert identity['tools']['Nift']['version']=='Nift v4.12.0';assert identity['tools']['Node']['version']=='v24.21.0';assert identity['tools']['Hugo']['version'].startswith('hugo v0.167.0');assert identity['tools']['Hugo']['sha256']=='8f6ddd98ff4a21a27b86530eb2e40d305673c26f72b1d57734ef68505cd28f89'
bound=json.loads((B/'COMMAND-BOUNDARIES.json').read_text())
for filename in ['website-100.json','website-1000.json','website-10000.json','targeted-builds.json']:
 d=json.loads((D/filename).read_text());target=filename.startswith('targeted');assert d['schema']==5 and d['publishable'];assert d['machine']['cpu_affinity']==[0,1,2,3] and not d['machine']['dirty'] and d['machine']['revision']==plan['suite_sha'];assert d['tools']['Nift']['sha256']==plan['candidate_cli_sha256'];assert d['tools']['Nift']['version']=='Nift v4.12.0';assert d['samples']==5 and d['warmups']==1
 expected={f'Nift/{n}/{c}' for n in [100,1000,10000] for c in ['fresh-full','targeted-one-page']} if target else {f'{engine}/{mode}' for engine in ['Nift','Hugo','Astro','VitePress'] for mode in ['application-cold','warm-full']}|{f'Nift/incremental/{c}' for c in ['no-op','one-page','shared-template']}
 assert len(d['jobs'])==len(expected) and {j['id'] for j in d['jobs']}==expected
 if not target:
  pages=int(filename.removeprefix('website-').removesuffix('.json'));assert d['pages']==pages;assert d['tools']['Astro']=='7.3.6' and d['tools']['VitePress']=='1.6.4';assert d['tools']['Node.js']==identity['tools']['Node'];assert d['tools']['Hugo']==identity['tools']['Hugo']
 for j in d['jobs']:
  expectedcmd=bound['explicit_target']['argv' if j['id'].endswith('/targeted-one-page') else 'reference_argv'] if target else bound['normal_publish']['argv'] if '/incremental/' in j['id'] else bound['full_builds'][j['id'].split('/')[0]]['argv'];assert j['command']==expectedcmd
  samples=j['samples'];assert len(samples)==6 and [r['round'] for r in samples]==list(range(6));assert [r['warmup'] for r in samples]==[True,False,False,False,False,False]
  for r in samples:
   assert r['correct'] and r['exit_code']==0 and not r['timeout'];assert all(math.isfinite(r[k]) and r[k]>=0 for k in ['wall_ms','cpu_ms','peak_rss_kib']);assert all(re.fullmatch('[0-9a-f]{64}',r[k]) for k in ['stdout_sha256','stderr_sha256'])
   if 'command' in r:assert r['command']==expectedcmd
   if not target and '/incremental/' not in j['id']:assert r['validation']=={'routes':pages,'content_checked':pages}
  m=samples[1:];v=sorted(r['wall_ms'] for r in m);s=j['summary'];assert s['samples']==5
  expectedstats={'median_ms':statistics.median(v),'min_ms':min(v),'max_ms':max(v),'median_peak_rss_kib':statistics.median(r['peak_rss_kib'] for r in m)}
  for k,q in [('p90_ms',.9),('p95_ms',.95),('p99_ms',.99)]:t=4*q;i=int(t);expectedstats[k]=v[i]+(v[min(i+1,4)]-v[i])*(t-i)
  for k,val in expectedstats.items():assert math.isclose(s[k],val,rel_tol=1e-12,abs_tol=1e-9),(filename,j['id'],k)
  rows.append({'file':filename,'job':j['id'],'measured':5,'warmups':1,'median_ms':s['median_ms'],'median_peak_rss_kib':s['median_peak_rss_kib']})
 adapter=json.loads((D/filename).with_suffix('.adapter.json').read_text());mode='targeted_campaign' if target else 'campaign';expected_diff=(B/(mode+'-expected-adapter.diff')).read_text();oldrepo=Path('/home/nick/Repositories/nift/nift-benchmarks/website-generator-benchmark');source=subprocess.check_output(['git','-C',str(oldrepo),'show',plan['suite_sha']+':scripts/'+mode+'.py'],text=True);assert adapter['original_sha256']==hashlib.sha256(source.encode()).hexdigest();assert adapter['affinity']==[0,1,2,3] and adapter['GOMAXPROCS']=='unset' and adapter['plan_sha256']==sha(B/'PLAN.json')
 # Header paths differ; compare every context/add/remove line after unified headers.
 assert adapter['diff'].splitlines()[2:]==expected_diff.splitlines()[2:]
 adapted=source.replace("c['config']['build-threads']=1","c['config']['build-threads']=-1")
 if not target:adapted=adapted.replace("env['GOMAXPROCS']='1'","env.pop('GOMAXPROCS',None)").replace('One CPU affinity recommended; Nift build threads=1; GOMAXPROCS=1.','All-core publication: CPU affinity0-3; Nift build threads=-1; Hugo GOMAXPROCS unset.')
 else:adapted=adapted.replace('one CPU, one build thread','CPU0-3, build threads=-1')
 assert adapter['adapted_sha256']==hashlib.sha256(adapted.encode()).hexdigest();adapters.append({'file':filename,'exact_worker_only_diff':True,'source_sha256':adapter['original_sha256'],'adapted_sha256':adapter['adapted_sha256']});files.append({'file':filename,'sha256':sha(D/filename)})
assert len(rows)==39 and sum(r['measured']+r['warmups'] for r in rows)==234
# The retained controller stdout records participant sequence for every main sample.
log=(B/'host/official.log').read_text();observed=re.findall(r'^(Nift|Hugo|Astro|VitePress) (application-cold|warm-full) ([0-5]) ',log,re.M);expectedorder=[]
for size in [100,1000,10000]:
 for mode in ['application-cold','warm-full']:
  for rnd in range(6):
   names=['Nift','Hugo','Astro','VitePress'];names=names[rnd%4:]+names[:rnd%4];expectedorder.extend((name,mode,str(rnd)) for name in names)
assert observed==expectedorder,(len(observed),len(expectedorder))
result={'pass':True,'kind':'independent local acceptance review','candidate':candidate,'suite_sha':plan['suite_sha'],'plan_sha256':sha(B/'PLAN.json'),'observations':234,'measured':195,'warmups':39,'jobs':39,'files':files,'adapters':adapters,'checks':['collection byte hashes','exact candidate/suite clean identity','pinned Node/Hugo/Astro/VitePress','all-core worker policy and affinity','all39job IDs and all3sizes','all234 successful correctness flags','full-mode per-page route/content counts','all39 exact argv','all rounds/warmup classifications','independent median/min/max/p90/p95/p99/RSS recomputation','exact worker-only adapter diffs and adapted hashes','main144participant rotation order from retained log'],'rows':rows,'oracle_boundary':'Frozen collector runs full-route/title/h1/body assertions and incremental/target full-rebuild byte parity. Retained booleans/validation counts certify those executions; rendered output trees are not retained for a second independent HTML oracle replay.','no_cloud_access':True}
(B/'independent-website-acceptance.json').write_text(json.dumps(result,indent=2)+'\n');print('INDEPENDENT_ACCEPTANCE_PASS234')
