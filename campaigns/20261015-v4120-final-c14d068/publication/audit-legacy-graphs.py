"""Regenerate in memory and inventory final-only shell/scripting graph assets."""
from pathlib import Path
import ast,json,hashlib,io,re,sys,html
R=Path(__file__).resolve().parents[4]/'lab'
# Evidence repo is a sibling of the benchmark suite repos, while Labs is outside that parent.
E=Path(__file__).resolve().parents[3];R=E.parents[1]/'lab'
S='20261015-v4120-final-c14d068';sys.path.insert(0,str(R/'scripts'))
from plot_startup import draw_shell_plot,draw_comparison
from shell_visuals import workload_sections,LABELS
from matplotlib.figure import Figure
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
raw=lambda slug,file:json.loads((E/'benchmarks'/slug/S/'official-refresh'/file).read_text())
out={'campaign':S,'nift_source_sha':'c14d06835bca515a5281e41da0e40219c2d60ef0','evidence_pin':'19e390183b9bcb039abe6aa553ad88a2305b49ee','scope':'Current final-only official shell/scripting plots; no recovery samples plotted','graphs':[],'checks':[]}
save=Figure.savefig;pending={}
def capture(self,output,*args,**kwargs):
 p=Path(output);b=io.BytesIO();save(self,b,*args,format=p.suffix[1:],**kwargs)
 assert b.getvalue()==p.read_bytes(),str(p)
 source=pending[str(p.with_suffix('.svg'))]
 out['graphs'].append({**source,'asset':str(p.relative_to(R)),'format':p.suffix[1:],'sha256':sha(p),'expected_vs_plotted':'PASS byte-for-byte regeneration from exact current raw values','regeneration':'selected renderer completed; independent in-memory byte comparison passed','publication':'SVG local; PNG retained locally pending parent canonical pin/finalization'})
Figure.savefig=capture
names=('bash','zsh','fish','nu','nift');display=[n if n!='nift' else 'Nift v4.12 final' for n in names]
d=raw('shell','shell-repeated.json');by={j['id']:j['summary'] for j in d['jobs']}
def source(slug,file,generator,values,ids):
 d=raw(slug,file);p=E/'benchmarks'/slug/S/'official-refresh'/file
 return {'suite':slug,'dataset':str(p.relative_to(E)),'dataset_sha256':sha(p),'suite_source_sha':d['machine']['revision'],'comparators':list(d['tools']),'comparator_versions':{n:(v.get('version','').splitlines()[0] if isinstance(v,dict) else str(v)) for n,v in d['tools'].items()},'generator_sha256':sha(R/generator.split(':')[0]),'generator':generator,'campaign':S,'expected_values':values,'source_job_ids':ids}
p=R/'public/benchmarks/shell/assets/startup-distributions.svg';pending[str(p)]=source('shell','shell-repeated.json','scripts/plot_startup.py:draw_shell_plot',{n:{key:by[f'{n}/bare/interactive'][key] for key in ['min_ms','median_ms','max_ms','p95_ms']} for n in names},[f'{n}/bare/interactive' for n in names]);draw_shell_plot(d,p)
for asset,series,title,unit in [('rc-prepared',{sc:[by[f'{n}/{sc}/interactive']['median_ms'] for n in names] for sc in ('bare','empty','light','moderate')},'Prepared first-prompt startup','Median latency (ms)'),('external-work',{'External-100':[by[f'{n}/bare/external-100']['median_ms'] for n in names]},'Launching 100 external commands','Whole invocation median (ms)')]:
 p=R/f'public/benchmarks/shell/assets/{asset}.svg';pending[str(p)]=source('shell','shell-repeated.json','scripts/plot_startup.py:draw_comparison',series,[f'{n}/{sc}/interactive' for sc in ('bare','empty','light','moderate') for n in names] if asset=='rc-prepared' else [f'{n}/bare/external-100' for n in names]);draw_comparison(display,series,p,title,unit,'shell')
g={}
for j in raw('scripting','scripting.json')['jobs']:
 family,size,lang=j['id'].rsplit('/',2);g.setdefault((family,size),{})[lang]=j
for family,size in [('sanity/noop','small'),('sanity/loops','large'),('filesystem/traverse','large')]:
 group=g[(family,size)];key=family.split('/')[-1];series={'Median':[j['summary']['median_ms'] for j in group.values()]};p=R/f'public/benchmarks/scripting/assets/{key}.svg';pending[str(p)]=source('scripting','scripting.json','scripts/plot_startup.py:draw_comparison',series,[j['id'] for j in group.values()]);draw_comparison([n if n!='nift' else 'Nift v4.12 final' for n in group],series,p,family+' / '+size,'Invocation latency (ms)','scripting',log=key!='noop')
# Regenerate the complete inline layer and compare exact geometry/numeric/source markup.
ns={'html':html,'re':re,'esc':lambda x:html.escape(str(x))}
for n in ast.parse((R/'scripts/render_benchmarks.py').read_text()).body:
 if isinstance(n,ast.FunctionDef) and n.name in ('table','section','p','f'):exec(compile(ast.Module(body=[n],type_ignores=[]),'helpers','exec'),ns)
d=raw('shell','shell-workloads.json');page=(R/'content/benchmarks/shell/index.html').read_text();expected=workload_sections(d,ns['section'],ns['p'],ns['table']);assert expected in page
by={j['id']:j['summary'] for j in d['jobs']};models=[]
for category in ('filesystem','processes','pipelines','text','algorithms','real-world'):
 if category=='filesystem':
  for prefix in ('create-empty','delete-selected'):
   defs=[c for c in d['definitions'] if c['id'].startswith(prefix+'-')]
   for n in list(names)+(['external-baseline'] if prefix=='delete-selected' else []):models.append((prefix+' scaling',n,[c['id']+'/'+n for c in defs]))
 if category in ('processes','pipelines'):
  defs=[c for c in d['definitions'] if c['category']==category]
  for n in names:models.append((category+' scaling',n,[c['id']+'/'+n for c in defs]))
 for c in d['definitions']:
  if c['category']!=category or category in ('processes','pipelines') or c['id'].startswith(('create-empty-','delete-selected-')):continue
  for n in list(names)+(['external-baseline'] if c['id']+'/external-baseline' in by else []):models.append((c['id'],n,[c['id']+'/'+n]))
svgs=re.findall(r'<svg\b.*?</svg>',expected,re.S);assert len(models)==len(svgs)==94
base=source('shell','shell-workloads.json','scripts/shell_visuals.py:workload_sections / aligned_chart / aligned_scaling',{},[])
for i,((case,n,ids),svg) in enumerate(zip(models,svgs)):
 out['graphs'].append({**base,'asset':'content/benchmarks/shell/index.html#inline-svg-'+str(i+1),'format':'inlineSVG','case':case,'participant':n,'source_job_ids':ids,'expected_values':{j:{k:by[j][k] for k in ('median_ms','p95_ms','min_ms','max_ms')} for j in ids},'plotted_unit':'seconds (raw milliseconds / 1000)','sha256':hashlib.sha256(svg.encode()).hexdigest(),'expected_vs_plotted':'PASS exact inline geometry and associated numeric tables match final raw regeneration','regeneration':'selected final-only renderer completed and independent whole-layer byte comparison passed'})
for slug in ('shell','scripting'):
 page=(R/f'content/benchmarks/{slug}/index.html').read_text();assert 'id="version-check"' not in page and 'Separate recovery diagnostic' not in page
 out['checks'].append({'suite':slug,'current_only':True,'html_sha256':sha(R/f'content/benchmarks/{slug}/index.html'),'current_nift_identity':'v4.12.0 final / c14d068','raw_cells':293 if slug=='shell' else 188})
out['historical_source_trees']=[{'path':str(p.relative_to(R)),'status':'Historical source only; not a current dataset; parent removes public/tracked historical routes'} for p in (R/'content/benchmarks/archives').rglob('index.html') if any('/'+n+'/' in str(p) for n in ('shell','scripting'))]
out['historical_public_assets']=[str(p.relative_to(R)) for slug in ('shell','scripting') for p in (R/f'public/benchmarks/{slug}/series').rglob('*') if p.is_file()]
out['historical_policy']='No historical/recovery result belongs on current public pages; canonical evidence is retained. Historical public assets listed here must be removed by parent before final publication.'
assert not out['historical_public_assets'] and not out['historical_source_trees']
out['counts']={'static_assets':12,'inline_svg':94,'total_graph_assets':106,'current_raw_cells':481};out['pass']=True
p=Path(__file__).with_name('graph-audit-legacy-suites.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['counts']));print('Saved',p)
