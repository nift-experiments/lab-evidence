"""Independent closed-form oracle and complete coverage audit; no adapter imports."""
from pathlib import Path
import json,hashlib,statistics,math,sys
r=Path(__file__).resolve().parents[1];source=r/(sys.argv[1] if len(sys.argv)>1 else 'work/official');cert='--certify' in sys.argv;cs=json.loads((r/'docs/SCENARIOS.json').read_text());engines=['nift','python','node','bun','go'];rows=[json.loads(l) for l in (source/'observations.jsonl').read_text().splitlines()];groups={};want_unsupported=[]
def oracle(c):
 k,n,it,e=(c[x] for x in ['kind','n','iterations','extra'])
 if k in ['atomic','mutex']:return [[0,n*(it if k=='mutex' else 1)]]
 out=[]
 for i in range(n*it if k=='nested' else n):
  x=((i+1)*pow(48271,8 if k=='nested' else it,2147483647))%2147483647
  if k in ['wait','stagger','mixed-wait','memory']:v=i
  elif k=='files':
   data=(r/f'work/fixtures/{i}.dat').read_bytes();assert data==bytes((i*7+j*13)%128 for j in range(128));v=sum(b*pow(31,127-j,1000000007) for j,b in enumerate(data))%1000000007
  elif k=='queue':v=i*17+3
  elif k.startswith('process') or k=='mixed':v={'value':i*17+3+(x if k=='mixed' else 0),'exit':7 if k=='process-fail' and i<e else 0}
  elif k=='failure' and i<e:v={'error':'task.failure'}
  else:v=x
  out.append([i,v])
 return out
for row in rows:groups.setdefault((row['case'],row['mode'],row['engine']),[]).append(row)
summary=[];expected_order=[]
for ci,c in enumerate(cs):
 expected=oracle(c);digest=hashlib.sha256(json.dumps(expected,separators=(',',':'),sort_keys=True).encode()).hexdigest()
 for mode in ['fresh','persistent']:
  for round in range(1 if cert else c['samples']+c['warmups']):
   order=engines[(ci+round)%5:]+engines[:(ci+round)%5]
   for e in order:
    unsupported=(e=='python' and c['kind']=='atomic') or (e in ['node','bun'] and c['kind']=='mutex') or (e=='nift' and c['kind']=='memory' and c['n']==10000)
    if not unsupported:expected_order.append((c['name'],mode,round,e))
  for e in engines:
   key=(c['name'],mode,e);g=groups.pop(key,[]);unsupported=(e=='python' and c['kind']=='atomic') or (e in ['node','bun'] and c['kind']=='mutex') or (e=='nift' and c['kind']=='memory' and c['n']==10000)
   if unsupported:assert not g;want_unsupported.append(key);continue
   assert len(g)==(1 if cert else c['samples']+c['warmups']),(key,len(g))
   assert [x['round'] for x in g]==list(range(len(g))),key
   for x in g:
    assert x['correct'] and x['result_sha256']==digest and x['count']==len(expected),key
    assert x['warmup']==(not cert and x['round']<c['warmups']),key
    assert all(x[p]==c[p] for p in ['n','workers','iterations','extra']),key
    assert math.isfinite(x['wall_ms']) and x['wall_ms']>0 and x['cpu_ms']>=0,key
    if c['kind']=='memory':assert x['held_tree_rss_mib']>0,key
   accepted=[x for x in g if not x['warmup']];walls=sorted(x['wall_ms'] for x in accepted)
   stat={'case':c['name'],'kind':c['kind'],'mode':mode,'engine':e,'n':c['n'],'workers':c['workers'],'samples':len(accepted),'median_ms':statistics.median(walls),'min_ms':min(walls),'max_ms':max(walls),'p95_ms':walls[math.ceil(.95*len(walls))-1],'cpu_ms':statistics.median(x['cpu_ms'] for x in accepted),'tree_rss_mib':statistics.median(x['sampled_tree_rss_mib'] for x in accepted),'max_child_rss_mib':statistics.median(x['max_child_rss_mib'] for x in accepted) if mode=='fresh' else None,'held_rss_mib':statistics.median(x['held_tree_rss_mib'] for x in accepted) if c['kind']=='memory' else None,'process_count':max(x['sampled_process_count'] for x in accepted),'thread_count':max(x['sampled_thread_count'] for x in accepted),'tasks_per_second':c['n']*1000/statistics.median(walls),'result_sha256':digest};summary.append(stat)
assert not groups
assert [(x['case'],x['mode'],x['round'],x['engine']) for x in rows]==expected_order,'Rotation/order mismatch'
u=json.loads((source/'unsupported.json').read_text());assert sorted((x['case'],x['mode'],x['engine']) for x in u)==sorted(want_unsupported)
receipt={'pass':True,'supported_cells':len(summary),'unsupported_cells':len(u),'measured_observations':sum(not x['warmup'] for x in rows),'retained_warmups':sum(x['warmup'] for x in rows),'total_observations':len(rows),'oracle':'Independent modular closed-form CPU oracle and polynomial fixture hash; exact canonical result digest/count in every observation','coverage':'Exact sample rounds, warmup flags, parameters and rotated participant order; no omitted/outlier observations','observations_sha256':hashlib.sha256((source/'observations.jsonl').read_bytes()).hexdigest()}
(source/'audit.json').write_text(json.dumps(receipt,indent=2)+'\n');(source/'summary.json').write_text(json.dumps(summary,separators=(',',':'))+'\n');print(json.dumps(receipt))
