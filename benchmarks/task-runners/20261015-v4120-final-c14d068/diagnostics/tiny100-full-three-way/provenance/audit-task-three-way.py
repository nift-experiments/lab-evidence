#!/usr/bin/env python3
import json,sys,hashlib,math,statistics
from pathlib import Path
r=Path(sys.argv[1]);identity=json.loads((r/'identity.json').read_text());assert identity['sources']=={'release':'c8d9c266518d115e4f289c5c6a2b94ddd7ee9968','original':'7f7e487c47a87e871dfef53345e2b71288008bff','final':'c14d06835bca515a5281e41da0e40219c2d60ef0'} and identity['affinity']==[0,1,2,3]
assert all(b['source_sha']==identity['sources'][label] and not b['status'] and len(b['sha256'])==64 for label,b in identity['binaries'].items())
rows=[json.loads(x) for x in (r/'observations.jsonl').read_text().splitlines()];assert len(rows)==18
names={f'tiny-{i:05}' for i in range(100)}
for index,row in enumerate(rows):
 roundno=index//3;order=['release','original','final'];offset=roundno%3;order=order[offset:]+order[:offset]
 assert row['id']==f'{index+1:06}' and row['round']==roundno and row['warmup']==(roundno==0) and row['order']==order and row['variant']==order[index%3]
 metric=json.loads((r/(row['id']+'.metrics.json')).read_text());assert row['metrics']==metric and metric['exit_code']==0
 assert all(math.isfinite(metric[k]) and metric[k]>=0 for k in ['wall_ms','cpu_ms','peak_rss_kib'])
 trace=(r/(row['id']+'.trace.jsonl')).read_bytes();assert hashlib.sha256(trace).hexdigest()==row['trace_sha256'];events=[json.loads(x) for x in trace.splitlines()];starts=set();done=set();active=0
 for e in sorted(events,key=lambda x:x['time_ns']):
  n=e['task'];assert n in names
  if e['event']=='start':assert n not in starts;starts.add(n);active+=1
  else:assert e['event']=='complete' and n in starts and n not in done;done.add(n);active-=1
  assert 0<=active<=4
 assert not active and starts==done==names
 inputs=json.loads((r/(row['id']+'.inputs.json')).read_text());assert set(inputs)==names
 for n,text in inputs.items():
  assert json.loads(text)['value']==1900002+roundno
  h=14695981039346656037
  for byte in text.encode():h=((h^byte)*1099511628211)&((1<<64)-1)
  assert row['proof']['output_hashes'][n]==hashlib.sha256((str(h)+'\n').encode()).hexdigest()
s=json.loads((r/'summary.json').read_text());assert s['observations']==18 and s['measured']==15 and s['warmups']==3 and len(s['cohorts'])==3
for c in s['cohorts']:
 obs=[x for x in rows if x['variant']==c['variant'] and not x['warmup']];assert len(obs)==c['samples']==5
 for m in ['wall_ms','cpu_ms','peak_rss_kib']:
  vs=[x['metrics'][m] for x in obs];assert c[m]=={'median':statistics.median(vs),'min':min(vs),'max':max(vs)}
print(json.dumps({'all_passed':True,'observations':18,'measured':15,'warmups':3,'variants':3,'tiny_FNV_outputs_independently_recomputed':True,'rotation_counts_distributions_verified':True}))
