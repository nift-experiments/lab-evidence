import json,sys,statistics,hashlib,math
from pathlib import Path
root=Path(sys.argv[1]);expected={f'website-{n}.json':11 for n in (100,1000,10000)};expected['targeted-builds.json']=6;rows=[]
def close(a,b):return abs(a-b)<1e-8*max(1,abs(a),abs(b))
for file,jobs in expected.items():
 d=json.loads((root/file).read_text());assert d['publishable'] and len(d['jobs'])==jobs;assert len({j['id'] for j in d['jobs']})==jobs
 assert d['machine']['cpu_affinity']==[0,1,2,3] and not d['machine']['dirty']
 ids={j['id'] for j in d['jobs']}
 expected_ids=({f'{name}/{mode}' for name in ('Nift','Hugo','Astro','VitePress') for mode in ('application-cold','warm-full')}|{f'Nift/incremental/{case}' for case in ('no-op','one-page','shared-template')}) if file!='targeted-builds.json' else {f'Nift/{n}/{case}' for n in (100,1000,10000) for case in ('fresh-full','targeted-one-page')}
 assert ids==expected_ids
 assert d['tools']['Nift']['sha256']=='7dd42dcee5ca4a6965f0823c0ae59198282da1eb77e0fcd4cae93a537870a6fb'
 for j in d['jobs']:
  samples=j['samples'];m=[r for r in samples if not r['warmup']];assert len(samples)==6 and len(m)==5 and sorted(r['round'] for r in samples)==list(range(6));assert all(r['correct'] and r['exit_code']==0 and not r['timeout'] for r in samples)
  v=sorted(r['wall_ms'] for r in m);s=j['summary'];assert s['samples']==5
  for key,val in [('median_ms',statistics.median(v)),('min_ms',min(v)),('max_ms',max(v)),('median_peak_rss_kib',statistics.median(r['peak_rss_kib'] for r in m))]:assert close(s[key],val),(j['id'],key)
  for key,q in [('p90_ms',.9),('p95_ms',.95),('p99_ms',.99)]:
   t=(len(v)-1)*q;k=int(t);val=v[k]+(v[min(k+1,len(v)-1)]-v[k])*(t-k);assert close(s[key],val),(j['id'],key)
  rows.append({'file':file,'job':j['id'],'median_ms':s['median_ms'],'median_peak_rss_kib':s['median_peak_rss_kib'],'measured':5,'warmups':1})
 assert json.loads((root/file).with_suffix('.adapter.json').read_text())['affinity']==[0,1,2,3]
assert len(rows)==39
(root/'independent-audit.json').write_text(json.dumps({'pass':True,'jobs':39,'measured':195,'warmups':39,'observations':234,'checks':['complete counts','all correctness','independent min/max/median/p90/p95/p99/RSS','worker-only adapter receipts','CPU0-3'],'rows':rows},indent=2)+'\n');print('AUDIT_PASS234')
