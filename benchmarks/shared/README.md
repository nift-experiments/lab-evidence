# Campaign evidence

The three reports link the validated official raw runs, including every warmup
and measured observation. Summaries are regenerated per run; machines, tool
pins and workload/method revisions are never merged.

`diagnostics.tar.gz` preserves superseded series:

- `diagnostic-python-pty`: Python fork latency grew with the retained result heap.
  The complete prepared series and partial fresh-state series remain evidence
  of the old method, not intrinsic shell startup. The compiled PTY bridge
  replaces this timing boundary in the official runs.
- `diagnostic-earlier-website-pins`: the first 100-page series used older
  Hugo/Astro pins before the final version freeze. All three official corpus
  sizes use the same newer frozen pins.
- `diagnostic-workload-audit`: the first scripting series predates streaming
  Nift frequency counters, the accurate sort-index label, and omission of the
  endpoint-only two-pointer test. The corrected complete corpus was rerun.

A historical `publishable` flag expresses its original harness gates, not
approval for mixing that run into the corrected campaign. No corrected samples
were removed selectively.

`provisioning.json` records the plan and verified teardown HTTP 404 without
publishing connection details. Package/compiler/download manifests, installer
source and startup-file hashes support acquiring the recorded environment.

Website state boundary: the raw enum `application-cold` means a newly recreated
project fixture. Shared pinned `node_modules` and generated dependency caches
persist; see `dependency-cache-inventory.json`. The report calls this **fresh
fixture**, not a complete application-cache reset. Warm full removes each tool's
specified output/cache directories while retaining other project state; the
article lists those exact directories. OS caches remain uncontrolled in both.
