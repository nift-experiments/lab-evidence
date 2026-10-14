import json,hashlib,statistics,copy
from pathlib import Path
R=Path(__file__).resolve().parent
S=Path('/home/nick/Repositories/nift/nift-benchmarks/scripting-benchmark')
P=Path('/home/nick/Repositories/nift/nift-benchmarks/lab-evidence/benchmarks/scripting/20261010-v4100/scripting.json')
raw=R/'official-refresh/scripting.json';d=json.loads(raw.read_text());old=json.loads(P.read_text());ready=json.loads((R/'refresh-readiness.json').read_text());manifest=json.loads((S/'benchmarks/manifest.json').read_text())
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def percentile(v,p):
 rank=(len(v)-1)*p;i=int(rank);f=rank-i
 return v[i]+(v[min(i+1,len(v)-1)]-v[i])*f
expected=set()
for l in manifest['languages']:
 for fam in d['families']:
  cat,bench=fam.split('/')
  if cat not in l.get('excluded_categories',[]):
   expected.update(f'{fam}/{size}/{l["id"]}' for size in manifest['sizes'])
assert len(expected)==188 and d['samples']==10 and d['warmups']==2
assert d['schema']==3 and d['publishable'] and d['mode']=='fresh-process-repeated'
assert ready['suite_sha']==d['machine']['revision']=='f889fff4af94658259932f611d4b0ad681c1eebf'
assert not d['machine']['dirty'] and d['machine']['cpu_affinity']==[0]
assert d['tools']['nift']['sha256']==ready['comparators']['nift']['sha256']=='7dd42dcee5ca4a6965f0823c0ae59198282da1eb77e0fcd4cae93a537870a6fb'
assert ready['candidate']['candidate_sha']=='c14d06835bca515a5281e41da0e40219c2d60ef0'
assert {j['id'] for j in d['jobs']}==expected and len(d['jobs'])==188
normalized=[]
def auditjob(j):
 cat,bench,size,lang=j['id'].split('/');l=next(x for x in manifest['languages'] if x['id']==lang)
 src=S/'benchmarks/sources'/cat/bench/(size+'.'+l['extension']);gold=S/'benchmarks/golden'/f'{cat}__{bench}__{size}.txt'
 assert j['source_sha256']==h(src) and j['oracle_sha256']==h(gold)
 assert j['workload_version']==manifest.get('benchmark_versions',{}).get(bench,1)
 rows=j['samples'];assert len(rows)==12 and {r['round'] for r in rows}==set(range(12))
 assert all(r['correct'] and r['exit_code']==0 and not r['timeout'] for r in rows)
 assert all(r['warmup']==(r['round']<2) for r in rows)
 measured=[r for r in rows if not r['warmup']];assert len(measured)==10
 times=sorted(r['wall_ms'] for r in measured)
 stats={'samples':10,'median_ms':statistics.median(times),'min_ms':min(times),'max_ms':max(times),'p90_ms':percentile(times,.9),'p95_ms':percentile(times,.95),'p99_ms':percentile(times,.99),'median_peak_rss_kib':statistics.median(r['peak_rss_kib'] for r in measured if r['peak_rss_kib'] is not None)}
 assert stats==j['summary']
 return {'id':j['id'],'family':cat+'/'+bench,'size':size,'engine':lang,'samples':10,'wall_ms':{k:stats[k+'_ms'] for k in ('median','min','max','p90','p95','p99')},'cpu_ms_median':statistics.median(r['cpu_ms'] for r in measured),'child_peak_rss_mib_median':stats['median_peak_rss_kib']/1024,'source_sha256':j['source_sha256'],'oracle_sha256':j['oracle_sha256']}
for j in d['jobs']:normalized.append(auditjob(j))
assert json.loads((R/'official-refresh/scripting-summary.json').read_text())=={j['id']:j['summary'] for j in d['jobs']}
plan=json.loads((S/'docs/REFRESH-20261013-READINESS.json').read_text())
assert d['families']==plan['commands'][0].split('--families ')[1].split(' --samples')[0].split(',')
negative={}
for name,mut in [('wrong-summary',lambda j:j['summary'].__setitem__('median_ms',j['summary']['median_ms']+1)),('wrong-correctness',lambda j:j['samples'][0].__setitem__('correct',False)),('wrong-count',lambda j:j['samples'].pop()),('wrong-source',lambda j:j.__setitem__('source_sha256','invalid'))]:
 j=copy.deepcopy(d['jobs'][0]);mut(j)
 try:auditjob(j)
 except AssertionError:negative[name]='rejected'
 else:raise RuntimeError('negativeaudit accepted '+name)
oldby={j['id']:j for j in old['jobs']};comparisons=[]
for j in d['jobs']:
 if not j['id'].endswith('/nift'):continue
 b=oldby[j['id']];same=j['source_sha256']==b['source_sha256'] and j['oracle_sha256']==b['oracle_sha256'] and j['workload_version']==b['workload_version']
 prior=b['summary']['median_ms'];current=j['summary']['median_ms'];comparisons.append({'id':j['id'],'same_workload_contract':same,'prior_median_ms':prior,'current_median_ms':current,'percent_improvement':100*(prior-current)/prior,'prior_over_current':prior/current,'current_over_prior':current/prior,'qualification':'Different disposable virtual machines and observation dates; contextual version trend, not isolated causal effect.'})
peer_changes={k:{'version_changed':d['tools'][k]['version']!=old['tools'][k]['version'],'binary_changed':d['tools'][k]['sha256']!=old['tools'][k]['sha256']} for k in d['tools'] if k!='nift'}
(R/'independent-audit.json').write_text(json.dumps({'pass':True,'raw_sha256':h(raw),'summary_sha256':h(R/'official-refresh/scripting-summary.json'),'jobs':188,'measured':1880,'warmups':376,'observations':2256,'complete_expected_matrix':True,'every_source_oracle_checked':True,'all_distribution_fields_exactly_recomputed':True,'correctness':'Every recorded observation correct, exit0 and nottimeout; source/oracle hashes independently checked. Raw stdout text is not retained by this legacy harness; correctness execution gate remains necessary.','negative_checks':negative,'suite_sha':ready['suite_sha'],'candidate_sha':ready['candidate']['candidate_sha'],'comparator_changes_from_prior':peer_changes},indent=2)+'\n')
(R/'normalized-current-metrics.json').write_text(json.dumps({'unit':'ms except explicitly labelled MiB','mode':d['mode'],'rss_policy':d['machine']['rss_policy'],'percentile_policy':'linear interpolation at (n-1)*p; legacy contract preserved','tools':d['tools'],'rows':normalized},indent=2)+'\n')
(R/'prior-comparable-mapping.json').write_text(json.dumps({'prior_series':'20261010-v4100','prior_raw_sha256':h(P),'qualification':'Same sources/oracles/sample policy; different virtual hosts and dates. Do not attribute trend solely to Nift.','comparator_changes':peer_changes,'rows':comparisons},indent=2)+'\n')
headline=[('sanity/noop','small'),('sanity/loops','large'),('sanity/function-calls','large'),('arrays-strings-hash/sort-index','large'),('graphs-trees-search/bfs','large'),('structured-data/json-parse','large'),('filesystem/traverse','large')]
(R/'compact-headline.json').write_text(json.dumps({'candidate_sha':ready['candidate']['candidate_sha'],'source':'independently audited normalized-current-metrics.json','selected_classes_not_overall_ranking':True,'unit':'ms median, fresh runtime process','rows':[{'family':f,'size':s,'values':{l['id']:next((r['wall_ms']['median'] for r in normalized if r['family']==f and r['size']==s and r['engine']==l['id']),None) for l in manifest['languages']}} for f,s in headline]},indent=2)+'\n')
(R/'collection.json').write_text(json.dumps({'archive_sha256':'059f278a6e540fca60b0dbcebb4caa1999dfb8ef3d9c9197705bf7ae33d17fc1','source':'scripting-benchmark:/opt/scripting-official-products.tar.gz','source_hash_verified':True,'preservation':'All complete official observations and warmups, summaries, exact tools/packages, plans and logs retained; node remains running.'},indent=2)+'\n')
print('AUDIT_PASS 188jobs 1880measured 376warmups; priorcontracts',sum(x['same_workload_contract'] for x in comparisons),'/',len(comparisons));print('comparator changes',peer_changes)
