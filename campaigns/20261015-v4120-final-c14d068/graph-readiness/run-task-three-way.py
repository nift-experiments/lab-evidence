#!/usr/bin/env python3
import os,sys,json,subprocess,hashlib,statistics,shutil
from pathlib import Path
ROOT=Path('/opt/suites/task-runners-official');sys.path[:0]=[str(ROOT/'scripts'),str(ROOT/'generators')]
from workflow import generate
from oracle import certify
from probe import ENV
out=Path(os.environ['DIAGNOSTIC_OUTPUT']);assert not out.exists();out.mkdir(parents=True)
os.sched_setaffinity(0,{0,1,2,3})
identity=json.loads(Path(os.environ['DIAGNOSTIC_IDENTITY']).read_text());identity.update(suite_sha='f37b63bd13cf71256607ba4652bcc911e270f94e',affinity=[0,1,2,3],plan={'tiny':True,'size':100,'jobs':4,'case':'full','samples':5,'warmups':1},boundary='unchanged C CLOCK_MONOTONIC before fork/exec through wait4; mutation/certification outside timing')
(out/'identity.json').write_text(json.dumps(identity,indent=2)+'\n');rows=[];fixtures={}
for label,b in identity['binaries'].items():
 r=ROOT/'work'/('diagnostic-three-way-'+label);assert not r.exists();g=generate(r,100,'nift',4,tiny=True);fixtures[label]=r
 z=subprocess.run([b['path'],'build'],cwd=r,env=ENV,capture_output=True,text=True);assert z.returncode==0;certify(r,[t['id'] for t in g['tasks']],4)
(out/'graph.json').write_text(json.dumps(g,indent=2)+'\n')
for roundno in range(6):
 order=['release','original','final'];offset=roundno%3;order=order[offset:]+order[:offset]
 for label in order:
  r=fixtures[label];names=[t['id'] for t in g['tasks']]
  for name in names:
   f=r/'inputs'/(name+'.json');v=json.loads(f.read_text());v['value']+=1+(1900000 if roundno==0 else 0);f.write_text(json.dumps(v)+'\n')
  (r/'trace.jsonl').unlink(missing_ok=True);stem=f'{len(rows)+1:06}';metric=out/(stem+'.metrics.json')
  with (out/(stem+'.stdout')).open('w') as stdout,(out/(stem+'.stderr')).open('w') as stderr:
   z=subprocess.run([str(ROOT/'work/measure'),str(metric),identity['binaries'][label]['path'],'build'],cwd=r,env=ENV,stdout=stdout,stderr=stderr);assert z.returncode==0
  proof=certify(r,names,4);trace=(r/'trace.jsonl').read_bytes();(out/(stem+'.trace.jsonl')).write_bytes(trace)
  inputs={name:(r/'inputs'/(name+'.json')).read_text() for name in names};(out/(stem+'.inputs.json')).write_text(json.dumps(inputs,sort_keys=True)+'\n')
  row={'id':stem,'variant':label,'round':roundno,'warmup':roundno==0,'order':order,'metrics':json.loads(metric.read_text()),'proof':proof,'trace_sha256':hashlib.sha256(trace).hexdigest()};rows.append(row)
  with (out/'observations.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
summary=[]
for label in ['release','original','final']:
 rs=[x for x in rows if x['variant']==label and not x['warmup']];c={'variant':label,'samples':5}
 for field in ['wall_ms','cpu_ms','peak_rss_kib']:
  vs=[x['metrics'][field] for x in rs];c[field]={'median':statistics.median(vs),'min':min(vs),'max':max(vs)}
 summary.append(c)
(out/'summary.json').write_text(json.dumps({'observations':18,'measured':15,'warmups':3,'cohorts':summary},indent=2)+'\n');(out/'complete.json').write_text(json.dumps({'all_correct':True,'observations':18})+'\n')
