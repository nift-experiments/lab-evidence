from pathlib import Path
import sys,json,hashlib,math
P=Path(sys.argv[1]);d=json.loads((P/'postexec-memory.json').read_text());assert d['pass'] and len(d['rows'])==15;order=[(n,e) for n in [1000,10000,100000] for e in ['nift','python','node','bun','go']];assert [(x['files'],x['engine']) for x in d['rows']]==order
oracles={}
for n in [1000,10000,100000]:
 dirs=set();expected=[]
 for i in range(n):
  rel=f'group{i%20:02d}/depth{i%3}/bucket{i//1000:03d}/f{i:06d}.'+['md','json','cpp','txt','dat'][i%5];parts=rel.split('/');dirs.update('/'.join(parts[:j]) for j in range(1,len(parts)));expected.append([rel,0,0])
 expected.extend([x,-1,0] for x in dirs);oracles[n]=hashlib.sha256(json.dumps(sorted(expected),separators=(',',':'),sort_keys=True).encode()).hexdigest()
for x in d['rows']:
 assert x['correct'] and x['output_sha256']==oracles[x['files']]
 for k in ['postexec_vmhwm_mib','postexec_vmrss_mib']:assert math.isfinite(x[k]) and x[k]>0
 assert x['postexec_vmhwm_mib']>=x['postexec_vmrss_mib']
m=json.loads((P/'postexec-identity.json').read_text());assert m['candidate_sha']=='c14d06835bca515a5281e41da0e40219c2d60ef0' and m['suite_sha']=='75e77bb4bb6fb0b8c49920f641c77b394aec5985';assert len(m['affinity'])==4
r={'pass':True,'cells':15,'samples_per_cell':1,'warmups':0,'independent_closed_form_inventory_sha256':oracles,'exact_order':True,'candidate_sha':m['candidate_sha'],'metric':'postexec /procVmHWM, diagnostic single observations; no distributions/significance claim','observations_sha256':hashlib.sha256((P/'postexec-memory.json').read_bytes()).hexdigest()};(P/'independent-audit.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
