"""Read-only independent corrected-clone accounting; no build or source mutation."""
from pathlib import Path
from collections import Counter
import hashlib,json,re,subprocess,sys
BASE=Path('/home/nick/Repositories/nift/nift-experiments/agora-baseline')
FROZEN=BASE/'frozen/global-initial'
CERT=BASE/(sys.argv[1] if len(sys.argv)>1 else 'certification-corrected')

# Exact restriction proved against two actual Node SSR rerenders. Comparison
# only: never change production Router cache/freshness state.
TSR_SCRIPT=re.compile(rb'(<script\b[^>]*\bid="\$tsr-stream-barrier"[^>]*>)([\s\S]*?)(</script>)')
TSR_UPDATED_AT=re.compile(rb'(\{i:"(?:\\.|[^"\\])*",u:)\d{13}(,s:)')
def normalize_router_timestamps(data):
    count=0
    def replace(match):
        nonlocal count
        body,n=TSR_UPDATED_AT.subn(lambda field:field.group(1)+b'0'+field.group(2),match.group(2))
        count+=n
        return match.group(1)+body+match.group(3)
    return TSR_SCRIPT.sub(replace,data),count

def files(root):
    return {p.relative_to(root).as_posix():p for p in root.rglob('*') if p.is_file()}
def json_value(path,name):
    value=json.loads(path.read_text())
    # Only this inherited nondeterministic array ordering is normalized.
    if name.startswith('__static/docs-search/'):
        return sorted(value,key=lambda row:row['url'])
    return value
def llm_blocks(path):
    return Counter(block.strip() for block in re.split(r'(?m)(?=^# .+ \(/en/[^\n]+\)\n)',path.read_text()) if block.strip())
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def git(repo,*args):return subprocess.check_output(['git','-C',str(repo),*args],text=True).strip()

reference=files(FROZEN)
reference_html=[p for p in reference if p.endswith('.html')]
nonbundle=[p for p in reference if not p.endswith('.html') and not p.startswith('assets/')]
static_json=[p for p in reference if p.startswith('__static/') and p.endswith('.json')]
markdown=[p for p in reference if p.endswith('.md')]
reference_llm=llm_blocks(FROZEN/'llms-full.txt')
report={'referenceHtml':len(reference_html),'referenceNonHtmlNonbundle':len(nonbundle),'models':{}}
publications={}
for name in ['agora','agora-agent']:
    repo=CERT/name;public=repo/'public';publication=files(public);publications[name]=publication
    missing_html=[p for p in reference_html if p not in publication]
    missing_static=[p for p in nonbundle if p not in publication]
    byte_diffs=[p for p in nonbundle if p in publication and digest(reference[p])!=digest(publication[p])]
    json_diffs=[p for p in static_json if p not in publication or json_value(reference[p],p)!=json_value(publication[p],p)]
    md_diffs=[p for p in markdown if p not in publication or digest(reference[p])!=digest(publication[p])]
    llm=llm_blocks(public/'llms-full.txt')
    report['models'][name]={
        'commit':git(repo,'rev-parse','HEAD'),'gitStatus':git(repo,'status','--porcelain'),
        'publicationFiles':len(publication),'htmlReferencePathsPresent':len(reference_html)-len(missing_html),
        'missingHtml':missing_html,'missingNonHtmlNonbundle':missing_static,
        'nonbundleByteDifferences':byte_diffs,'staticJsonSemanticDifferences':json_diffs,
        'markdownByteDifferences':md_diffs,'llmBlocks':sum(llm.values()),
        'llmMissingBlocks':sum((reference_llm-llm).values()),'llmExtraBlocks':sum((llm-reference_llm).values()),
    }
a=publications['agora'];b=publications['agora-agent']
ma=json.loads(a['__nift/content-manifest.json'].read_text());mb=json.loads(b['__nift/content-manifest.json'].read_text())
report['crossModel']={
    'staticJsonByteDifferences':[p for p in static_json if p in a and p in b and digest(a[p])!=digest(b[p])],
    'markdownByteDifferences':[p for p in markdown if p in a and p in b and digest(a[p])!=digest(b[p])],
    'llmFullByteEqual':digest(a['llms-full.txt'])==digest(b['llms-full.txt']),
    'moduleKeysEqual':set(ma)==set(mb),'modules':len(ma),
    'moduleByteDifferences':[key for key in ma if key not in mb or digest(a[ma[key].lstrip('/')])!=digest(b[mb[key].lstrip('/')])],
}
output=BASE/(sys.argv[2] if len(sys.argv)>2 else 'investigation/final-corrected-independent-accounting.json')
output.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
fail=any(v['missingHtml'] or v['missingNonHtmlNonbundle'] or v['staticJsonSemanticDifferences'] or v['markdownByteDifferences'] or v['llmMissingBlocks'] or v['llmExtraBlocks'] for v in report['models'].values())
if fail:raise SystemExit(1)
