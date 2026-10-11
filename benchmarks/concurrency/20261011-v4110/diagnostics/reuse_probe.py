"""Separate diagnostic, never pooled into accepted booted-isolated timings."""
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent));import run
c=next(c for c in json.loads((run.R/'docs/SCENARIOS.json').read_text()) if c['name']=='schedule-1000');dest=run.R/'work/diagnostics';dest.mkdir(exist_ok=True);rows=[]
for e in run.ENGINES:
 p,reader,err=run.persistent(e)
 try:
  for request in range(10):
   x=run.trial(e,c,(p,reader),timeout=60);x.update(engine=e,request=request,case=c['name'],accepted_timing=False);rows.append(x);print(e,request,round(x['wall_ms'],2),flush=True)
 finally:p.stdin.close();p.wait(timeout=10);err.close()
(dest/'reused-runtime.json').write_text(json.dumps(rows,indent=2)+'\n')
