from pathlib import Path
import subprocess,tempfile,os,json,sys,hashlib
if '--child' in sys.argv:
 size=int(sys.argv[-1]);payload=bytearray(b'x')*(size*1048576);fields={x.split(':')[0]:x.split(':')[1].strip() for x in Path('/proc/self/status').read_text().splitlines() if x.startswith(('VmRSS:','VmHWM:'))};rows=[]
 for _ in range(3):
  with tempfile.TemporaryFile() as out,tempfile.TemporaryFile() as err:
   p=subprocess.Popen(['taskset','-c',str(min(os.sched_getaffinity(0))),'/usr/bin/true'],stdout=out,stderr=err);_,status,usage=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status);assert p.returncode==0;rows.append(usage.ru_maxrss/1024)
 print(json.dumps({'allocated_parent_mib':size,'parent_fields':fields,'true_taskset_child_maxrss_mib':rows}));sys.exit()
rows=[]
for size in [0,64]:rows.append(json.loads(subprocess.check_output([sys.executable,__file__,'--child',str(size)],text=True)))
result={'scope':'Post-campaign launch-accounting control only; no benchmark rerun or accepted raw edits','boundary':'Same Popen/taskset/tempfile/wait4 launch pattern as frozen template fresh runner','control':'/usr/bin/true does no template work; independent supervisors with0/64MiB allocated payload','pass':min(rows[1]['true_taskset_child_maxrss_mib'])-max(rows[0]['true_taskset_child_maxrss_mib'])>50,'rows':rows,'interpretation':'wait4 child peak inherits launch-supervisor memory floor; cannot subtract medians or rank runtimes from floored cells'}
Path('/opt/template-engines/work/refresh-launch-floor-control.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
