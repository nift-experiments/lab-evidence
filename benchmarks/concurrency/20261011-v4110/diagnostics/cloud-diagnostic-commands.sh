set -euo pipefail
cd /root/concurrency
mkdir -p work/diagnostics
sha256sum work/helper work/go-adapter work/go-probe work/nift-source/nift >work/diagnostics/binary-identities.txt
stat -c "%n %y %s" work/official/observations.jsonl work/official/audit.json >work/diagnostics/accepted-file-times.txt
sha256sum work/diagnostics/growth-3000.f scripts/reuse_probe.py >work/diagnostics/supplemental-source-identities.txt
strace -f -c -o work/diagnostics/schedule-syscalls.txt work/nift-source/nift probes/scheduling-growth.f >work/diagnostics/schedule-output.txt 2>work/diagnostics/strace-errors.txt
perfbin=$(command -v perf || true)
if [ -n "$perfbin" ]; then
 "$perfbin" record -e cpu-clock -F 99 --call-graph dwarf -o work/diagnostics/schedule-perf.data -- work/nift-source/nift work/diagnostics/growth-3000.f >work/diagnostics/perf-output.txt 2>work/diagnostics/perf-errors.txt || true
 "$perfbin" report --stdio -i work/diagnostics/schedule-perf.data >work/diagnostics/perf-report.txt 2>work/diagnostics/perf-report-errors.txt || true
 for diagnostic_kind in cpu queue; do
  if [ "$diagnostic_kind" = cpu ]; then printf 'cpu|64|4|200000|0\n' >work/diagnostics/cpu-request.txt; else printf 'queue|10000|4|0|4\n' >work/diagnostics/queue-request.txt; fi
  "$perfbin" record -e cpu-clock -F 99 --call-graph dwarf -o "work/diagnostics/$diagnostic_kind-perf.data" -- work/nift-source/nift adapters/nift.f <"work/diagnostics/$diagnostic_kind-request.txt" >"work/diagnostics/$diagnostic_kind-output.txt" 2>"work/diagnostics/$diagnostic_kind-perf-errors.txt" || true
  "$perfbin" report --stdio -i "work/diagnostics/$diagnostic_kind-perf.data" >"work/diagnostics/$diagnostic_kind-perf-report.txt" 2>"work/diagnostics/$diagnostic_kind-perf-report-errors.txt" || true
 done
fi
python3 - <<'CHECK'
from pathlib import Path
import json,hashlib
receipt={}
for kind,n,it in [('cpu',64,200000),('queue',10000,0)]:
 p=Path('work/diagnostics')/(kind+'-output.txt')
 if not p.exists() or not p.read_text().strip():receipt[kind]={'available':False,'reason':'Perf did not execute participant; see retained error'};continue
 lines=p.read_text().splitlines();assert lines[0]=='BOOT';rows=json.loads(lines[1]);rows.sort(key=lambda x:x[0]);want=[[i,((i+1)*pow(48271,it,2147483647))%2147483647 if kind=='cpu' else i*17+3] for i in range(n)];assert rows==want
 receipt[kind]={'available':True,'correct':True,'count':n,'diagnostic_only':True,'result_sha256':hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()}
Path('work/diagnostics/profile-correctness.json').write_text(json.dumps(receipt,indent=2)+'\n')
CHECK
printf 'Diagnostic only; not accepted timing. strace scheduler-1000; perf separate minimal scheduler-3000 at99Hz software CPU clock.\n' >work/diagnostics/README.txt
tar -czf /root/concurrency-diagnostics.tar.gz work/diagnostics
