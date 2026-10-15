# Supplemental website investigation — amended defaults-only cohort

This supplements the frozen official campaign; it does not replace or pool its CPU-0 results. Exact final core c14d068, normal GCC13.3/O2 CLI7dd42dce…, and Hugo0.167.0 binary8f6ddd98… are unchanged. Both new g6-standard-4 hosts expose four CPUs and EPYC7642. The user stopped future 1/2/4 scaling: original A120 checkpointed plus one completed boundary observation, and B48, remain intact under PLANv2. PLANv3 separately contains 107 new observations plus references to13 unchanged necessary replay observations. No uncollected original sample was silently classified as a failure or discarded for being slow.

## Actual defaults, all four CPUs

Five measured plus one warmup per engine/mode; Nift build-threads=-1, Hugo GOMAXPROCS unset, affinity0–3. These are the **new PLANv3 default-main** medians:

| Engine | Fresh wall ms | Warm-full wall ms | Fresh CPU ms | Warm CPU ms | Fresh child RSS KiB |
|---|---:|---:|---:|---:|---:|
| Nift |1194.468|803.743|3938.726|2718.638|17468|
| Hugo |1635.544|1436.616|3841.195|3250.870|250088|

Nift uses27.0% less fresh wall time and44.1% less warm wall time in this small cohort. Fresh observed ranges overlap (Nift1122.922–1458.843; Hugo1324.989–2667.728), with Nift faster in four of five matched rounds. Warm ranges are disjoint and Nift faster in all five rounds. No outlier was removed, and these are descriptive observations rather than a population significance claim.

CPU/wall is329.7%/338.2% for Nift fresh/warm and234.9%/226.3% for Hugo. Thus Nift's shorter fresh wall time is not evidence of lower total CPU work: its fresh CPU total is slightly higher. The observed concurrent execution is different. The separate50ms process-sampling controls show median maximum **target** OS threads5 for Nift and7 for Hugo, one target process each; the time wrapper adds one process/thread. OS threads are not equivalent to active workers. Nift resolves -1 through hardware_concurrency (observed4). Exact Hugo source uses CPU-limit-aware maxprocs.Set and a separate HUGO_NUMWORKERMULTIPLIER/runtime.NumCPU worker multiplier; unset/default is not invented `-j` behavior.

HostB's already-collected PLANv2 **default-only subset**, kept as separate host-variance context, gives fresh Nift1088.733/Hugo1460.816ms. A is9.71% slower for Nift and11.96% slower for Hugo. Both hosts favor Nift under their defaults; this is not a cross-host pooled estimate. The other previously collected scaling rows remain available but no further scaling was scheduled after the user amendment.

## Fresh versus warm: measured work and supported mechanism

New main fresh-minus-warm gaps are390.725ms for Nift and198.928ms for Hugo. In the separate GNU-time-only controls, median Nift user/system CPU is1070/2660ms fresh versus1230/1630ms warm. This points to a substantial system-side difference, not a claim that every390ms is explained by a single function. Observer values are coarse separate specimens, not substitutes for the primary C-supervised clock.

Untimed full project accounting collected on B before the scope amendment (one-worker fixture, explicitly labelled) finds initial Nift10003files/1376973bytes, versus Hugo10002files/1046878bytes. Both produce10000 correct HTML routes: Nift1317780public bytes and Hugo1327780bytes (one additional byte/page). Nift also persists10001 additional internal files totaling6584541bytes; Hugo adds a zero-byte build lock. Nift's actual info artifact records ownership/output/template/content and dependencies, not meaningless data. Source formats differ: Nift HTML plus tracked JSON/template versus Hugo Markdown/frontmatter/Goldmark pass-through. Matching semantic output is not identical parser/metadata work.

The bounded strace specimens corroborate a specific fresh/warm distinction. Nift fresh performs20002writes,10000renames and20000chmod calls; warm performs10001writes,10000utimensat and10000chmod calls. Frozen FileSystem.cpp:365–390 explains why: byte-identical retained metadata is read/checked and its mtime refreshed instead of a temporary write/atomic replacement. Public HTML is removed before every full build and must still be rendered/written. Warm nevertheless has **more** stat/open/read operations (e.g.190026stat versus140033), demonstrating why raw syscall count is not a cost model. We have not performed a core-change counterfactual that assigns an exact millisecond fraction to metadata persistence.

Strace greatly perturbs multithreaded scheduling; its summed syscall seconds include waiting and are not product latency/CPU measurements. All8 default fresh/warm syscall/software-CPU profiles pass correctness. Perf has368/265 Nift and382/394 Hugo samples, zero lost; filesystem/path/locking functions appear in kernel samples. Hugo's supplied stripped binary limits reliable userspace symbol attribution, so no unsupported Markdown/GC percentage is claimed. Hardware counters were not used or claimed; software CPU profiles succeeded without a permission workaround.

## Historical47.59% movement and frozen replay

The historical accepted10k fresh numbers are Nift3853.309/Hugo5005.257ms (Hugo/Nift1.299), not a2x Nift advantage in this particular dataset. Final official CPU-0 numbers remain Nift3015.980/Hugo2623.337ms, a1.1497 Nift/Hugo ratio. The separate Nift-only three-way2951.495ms must not be inserted into that peer ratio.

Historical and current campaign.py, benchmark.py, campaign_measure.py and measure.c hashes are identical, as verified from exact4947b42/a2890bc clones. The selected-engine replay wrapper calls those frozen fixture/clock/validation helpers and reproduces the Hugo configuration and persistent-warm cleanup policy; it is not the entire interleaved four-engine campaign. Input fingerprinting reads files outside the measured clock and can condition caches. The same prehash policy is applied to both source snapshots; this remains a supplemental control, not a literal machine-cold or full-schedule reproduction of the historical run. Hugo's binary is also identical. Necessary same-host CPU-0/Hugo GOMAXPROCS1 replay (five measured/one warmup, some exact old observations linked rather than rerun) yields historical fresh2750.020/warm2697.703ms and current fresh2644.857/warm2779.250ms. Fresh ranges2609.360–4021.924 versus2474.044–3287.218 overlap widely. That small replay difference is not evidence of a source/harness version effect: source bytes are identical.

The original host exposed EPYC7601; current official and both supplemental hosts EPYC7642. New preparation-inclusive pre/post counters show low observed steal (maximum~0.30%) and iowait (~0.23%); frequency control is not exposed and cpu.max is unavailable. Cgroup receipt reports no throttling, cpuset0–3. These observations describe the new runs, not the historical machine's timed interval. We cannot retrospectively prove which hardware, storage/cache, scheduling or host-load component caused exactly47.59% of historical movement. Software/fixture drift is unsupported; environment change is consistent with the evidence but its exact contribution is unresolved. No further timing is needed to manufacture an unwarranted causal claim.

## Boundaries and judgment

Observer controls are separate: Python outer wall includes wrapper/wait/poll completion delays up to roughly50ms, including the GNU-time-only case. Some observed controls are faster than their unobserved comparison because noise/order effects outweigh this overhead; that is not negative observer cost. Full reports and primary C timings remain distinct. The warm regime retains internal state and source paths but launches a fresh process; it is not Hugo's live development server.

The all-core default evidence strengthens Nift's case for authored, agent-maintained, mixed website/asset/procedural workflows. Its explicit ownership/dependency/lifecycle metadata can be useful even when it has a measurable persistence cost. Conventional Hugo content/theme workflows can still favor Hugo's model or an existing Hugo estate. This campaign does not provide a matched authoring-error/recovery experiment proving one product automatically safer. Full-output parity and route checks here are harness validations, not universal product-native guarantees. No core or Labs edits, selective reruns, or official evidence replacement occurred.
