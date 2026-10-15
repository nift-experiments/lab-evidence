import json,statistics,sys
from pathlib import Path
P=Path(__file__).resolve().parent;d=json.loads((P/'host-a/evidence-v3/raw.json').read_text());b=json.loads((P/'host-b/evidence/raw.json').read_text());rows=d['observations'];linked=d['linked_replay_observations']
def st(a):
 w=[o['wall_ms'] for o in a];cpu=[o['cpu_ms'] for o in a];return {'samples':len(a),'median_ms':statistics.median(w),'min_ms':min(w),'max_ms':max(w),'median_cpu_ms':statistics.median(cpu),'cpu_wall_percent':100*statistics.median(cpu)/statistics.median(w),'median_peak_rss_kib':statistics.median(o['peak_rss_kib'] for o in a)}
def select(engine,mode,phase,source=rows,**extra):return [o for o in source if not o['spec']['warmup'] and o['spec']['engine']==engine and o['spec']['mode']==mode and o['spec']['phase']==phase and all(o['spec'].get(k)==v for k,v in extra.items())]
main={e:{m:st(select(e,m,'defaults-main')) for m in ('fresh','warm-full')} for e in ('Nift','Hugo')}
for e in main:main[e]['fresh_minus_warm_ms']=main[e]['fresh']['median_ms']-main[e]['warm-full']['median_ms']
controls=[]
for e in ('Nift','Hugo'):
 for m in ('fresh','warm-full'):
  base=st(select(e,m,'default-observer-controls',observer='none'))
  for observer in ('none','GNU-time-only','proc50ms+GNU-time'):
   a=select(e,m,'default-observer-controls',observer=observer);x={'engine':e,'mode':m,'observer':observer,**st(a)};x['median_delta_vs_unobserved_ms']=x['median_ms']-base['median_ms'];x['percent_vs_unobserved']=100*(x['median_ms']/base['median_ms']-1)
   if observer!='none':x['median_user_ms']=statistics.median(o['user_ms'] for o in a);x['median_system_ms']=statistics.median(o['system_ms'] for o in a)
   if observer=='proc50ms+GNU-time':x['median_max_total_sampled_threads_including_time_wrapper']=statistics.median(o['max_sampled_threads'] for o in a);x['proc_sample_counts']=[o['proc_sample_count'] for o in a]
   controls.append(x)
replay={h:{m:st(select('Hugo',m,'replay',rows+linked,harness=h)) for m in ('fresh','warm-full')} for h in ('historical','current')}
variance={e:{'host_a':main[e]['fresh'],'host_b':st(select(e,'fresh','replication',b['observations'],workers='default'))} for e in ('Nift','Hugo')}
for e in variance:variance[e]['A_over_B_percent']=100*(variance[e]['host_a']['median_ms']/variance[e]['host_b']['median_ms']-1)
telemetry=[]
for host,obs in [('A',rows),('B',b['observations'])]:
 for o in obs:
  def cpu(t):return list(map(int,t['stat'].splitlines()[0].split()[1:9]))
  x=cpu(o['telemetry_before']);y=cpu(o['telemetry_after']);v=[b-a for a,b in zip(x,y)];total=sum(v);telemetry.append({'host':host,'id':o['spec']['id'],'steal_percent':100*v[7]/total if total else None,'iowait_percent':100*v[4]/total if total else None})
out={'main':main,'Nift_over_Hugo_fresh':main['Nift']['fresh']['median_ms']/main['Hugo']['fresh']['median_ms'],'Nift_over_Hugo_warm':main['Nift']['warm-full']['median_ms']/main['Hugo']['warm-full']['median_ms'],'observer_controls':controls,'necessary_CPU0_Hugo_replay':replay,'default_host_variance_separate_cohorts':variance,'host_telemetry_preparation_inclusive_not_timed_only':telemetry,'qualifications':['No pooling of PLANv2 samples into new default-main','Hugo GOMAXPROCS is distinct from worker pool multiplier and OS thread count','Observer outer Python wall includes wrapper/wait/poll overhead; primary C clock remains authoritative','Different nominal hosts and sequential phases cannot prove causes of historic47.59% shift','Profiles and untimed work accounting are separate from measured runs']};(P/'ANALYSIS-v3.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'main':main,'ratios':{k:out[k] for k in ('Nift_over_Hugo_fresh','Nift_over_Hugo_warm')}},indent=2))
