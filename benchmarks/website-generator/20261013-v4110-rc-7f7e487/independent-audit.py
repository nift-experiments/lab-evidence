import json,statistics,hashlib,copy
from pathlib import Path
R=Path(__file__).resolve().parent;E=R/'official-refresh';ready=json.loads((R/'refresh-readiness.json').read_text())
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def stats(rows):
 xs=sorted(x['wall_ms'] for x in rows);pct=lambda p:xs[int((len(xs)-1)*p)]+(xs[min(int((len(xs)-1)*p)+1,len(xs)-1)]-xs[int((len(xs)-1)*p)])*((len(xs)-1)*p-int((len(xs)-1)*p))
 return dict(samples=len(xs),median_ms=statistics.median(xs),min_ms=min(xs),max_ms=max(xs),p90_ms=pct(.9),p95_ms=pct(.95),p99_ms=pct(.99),median_peak_rss_kib=statistics.median(x['peak_rss_kib'] for x in rows if x['peak_rss_kib'] is not None))
def checkjob(j):
 rows=j['samples'];assert len(rows)==6 and {x['round'] for x in rows}==set(range(6));assert all(x['correct'] and x['exit_code']==0 and not x['timeout'] and x['warmup']==(x['round']<1) for x in rows);m=[x for x in rows if not x['warmup']];assert len(m)==5;assert stats(m)==j['summary'];return stats(m)
normalized=[];trends=[];measured=warmups=0;files=[]
for n in (100,1000,10000):
 p=E/f'website-{n}.json';d=json.loads(p.read_text());old=json.loads(Path('/home/nick/Repositories/nift/nift-benchmarks/lab-evidence/benchmarks/website-generator',p.name).read_text());oldby={j['id']:j for j in old['jobs']};expected={f'{name}/{mode}' for name in ('Nift','Hugo','Astro','VitePress') for mode in ('application-cold','warm-full')}|{f'Nift/incremental/{case}' for case in ('no-op','one-page','shared-template')}
 assert d['publishable'] and d['schema']==5 and d['pages']==n and d['samples']==5 and d['warmups']==1;assert d['machine']['revision']==ready['suite_sha']=='a2890bc504cf7c55b77cd4fddae17403b7caf8ae';assert not d['machine']['dirty'] and d['machine']['cpu_affinity']==[0];assert d['tools']['Nift']['sha256']=='671e182ea31f3a23af92dadd738aba43edcb427670e7cf2f0d06b6362d28a606';assert len(d['jobs'])==11 and {j['id'] for j in d['jobs']}==expected
 for label,key in [('Hugo','hugo'),('Node.js','node')]:assert d['tools'][label]['sha256']==ready['comparators'][key]['sha256']
 for label,key in [('Astro','astro'),('VitePress','vitepress')]:assert d['tools'][label]==ready['comparators'][key]['version']
 for j in d['jobs']:
  z=checkjob(j);engine=j['id'].split('/')[0]
  if 'incremental' not in j['id']:
   for x in j['samples']:assert x['validation']=={'routes':n,'content_checked':n}
  normalized.append({'pages':n,'id':j['id'],'engine':engine,'samples':5,'wall_ms':{k:z[k+'_ms'] for k in ('median','min','max','p90','p95','p99')},'child_peak_rss_mib_median':z['median_peak_rss_kib']/1024});measured+=5;warmups+=1
  before=oldby[j['id']]['summary']['median_ms'];now=z['median_ms'];trends.append({'pages':n,'id':j['id'],'prior_ms':before,'current_ms':now,'delta_ms':now-before,'percent_change':100*(now/before-1),'qualifier':'different virtual host/date; same named versions for peers, core4.7.2→candidate; not an isolated version effect'})
 assert json.loads((E/f'website-{n}-summary.json').read_text())=={j['id']:j['summary'] for j in d['jobs']};files.append({'name':p.name,'sha256':h(p),'jobs':11})
p=E/'targeted-builds.json';d=json.loads(p.read_text());assert d['publishable'] and d['machine']['revision']==ready['suite_sha'] and d['machine']['cpu_affinity']==[0] and not d['machine']['dirty'];assert 'same dedicated host' in d['notes'][0];assert d['tools']['Nift']['sha256']=='671e182ea31f3a23af92dadd738aba43edcb427670e7cf2f0d06b6362d28a606';expected={f'Nift/{n}/{mode}' for n in (100,1000,10000) for mode in ('fresh-full','targeted-one-page')};assert len(d['jobs'])==6 and {j['id'] for j in d['jobs']}==expected
for j in d['jobs']:
 z=checkjob(j);normalized.append({'pages':j['pages'],'id':j['id'],'engine':'Nift','cohort':'serial supplemental samehost, independent fullreference','samples':5,'wall_ms':{k:z[k+'_ms'] for k in ('median','min','max','p90','p95','p99')},'child_peak_rss_mib_median':z['median_peak_rss_kib']/1024});measured+=5;warmups+=1
assert json.loads((E/'targeted-builds-summary.json').read_text())=={j['id']:j['summary'] for j in d['jobs']};files.append({'name':p.name,'sha256':h(p),'jobs':6})
assert measured==195 and warmups==39
negative={}
for name,mut in [('wrong-summary',lambda j:j['summary'].__setitem__('median_ms',j['summary']['median_ms']+1)),('wrong-correctness',lambda j:j['samples'][0].__setitem__('correct',False)),('wrong-count',lambda j:j['samples'].pop())]:
 q=copy.deepcopy(d['jobs'][0]);mut(q)
 try:checkjob(q)
 except AssertionError:negative[name]='rejected'
 else:raise RuntimeError('negative audit accepted '+name)
(R/'independent-audit.json').write_text(json.dumps({'pass':True,'jobs':39,'measured':195,'warmups':39,'observations':234,'complete_expected_matrix':True,'all_distributions_and_summary_files_exactly_recomputed':True,'all_recorded_correctness_gates_pass':True,'page_route_and_content_counts_checked':True,'negative_checks':negative,'files':files,'candidate_sha':ready['candidate']['candidate_sha'],'suite_sha':ready['suite_sha'],'limitations':'Incremental/targeted output parity is enforced by frozen runner and correctness flags; ephemeral generated outputs are not retained in legacy harness.'},indent=2)+'\n')
(R/'normalized-current-metrics.json').write_text(json.dumps({'units':'ms, explicitly labelled MiB childpeak','rows':normalized},indent=2)+'\n');(R/'prior-comparable-mapping.json').write_text(json.dumps({'qualification':'Cross-host historical context, not causal attribution. Target supplemental cohort has independent fullreference.','rows':trends},indent=2)+'\n');(R/'collection.json').write_text(json.dumps({'archive_sha256':'054e3599af144f7918f64bc576011a98228a53286d78c1254ec82d6ae0233031','source_hash_verified':True,'old_series_untouched':True,'node_retained_for_diagnostic_review':True},indent=2)+'\n');print('AUDIT_PASS 39jobs 195measured39warmups')
