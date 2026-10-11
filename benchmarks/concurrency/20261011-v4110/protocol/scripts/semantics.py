from pathlib import Path
import subprocess,json,os,sys
sys.path.insert(0,str(Path(__file__).resolve().parent));import run
r=run.R;dest=r/'work/semantics';dest.mkdir(exist_ok=True)
subprocess.run([str(r/'work/tools/go/bin/go'),'build','-o','work/go-probe','probes/go.go'],env=dict(os.environ,GOCACHE='/tmp/concurrency-go-cache'),check=True)
for e in run.ENGINES:
 cmd=run.command(e);cmd[-1]={'nift':'probes/nift-limits.f','python':'probes/python.py','node':'probes/js.mjs','bun':'probes/js.mjs','go':str(r/'work/go-probe')}[e]
 p=subprocess.run(cmd,capture_output=True,text=True,timeout=30,preexec_fn=run.pin);(dest/f'{e}.txt').write_text(p.stdout+p.stderr);assert p.returncode==0,(e,p.stderr)
 print(e,p.stdout.strip(),flush=True)
(dest/'acceptance.json').write_text(json.dumps({'pass':True,'affinity':run.AFFINITY,'nift_cancel':'No public future/thread cancellation API in frozen source; explicit cooperative atomic stop token required','nift_error':'Recoverable future error arrives on await; successful sibling finishes; repeated await re-observes same error','worker_limits':'Nift/JS/Go active concurrency never exceeds 1/2/4; Python distinct worker process count <= requested max_workers'},indent=2)+'\n')
