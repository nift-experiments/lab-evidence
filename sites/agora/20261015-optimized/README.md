# Agora Docs — Nift + TanStack Start

Prepared publication evidence, local only pending explicit release approval. This identified cohort appends evidence without mutating historical observations.

Two accepted upstream GLOBAL production observations: upstream-global-warm-1 and -2 at pinned AgoraIO/docs-portal 3c6552914e6cec74ab5d9c38b3bd4eeb51871d13. Initial/debug builds and interrupted warm-3 are not accepted observations. Upstream warm runs reused installed/build state; these are not matched Nift-fresh cache conditions.

Optimized Nift single observations: measured agora 1dcbbeb634d701821a598600f24357c856cf5163 and agora-agent cd1dc9e602add307b81b36258ca0481dd00348b8. Reviewed final source c6bbe6ed3be77358d327dfcf03920ed193179708 and a30d209836b4df3b34a711c841c7de5b5029f18b. Author adds raw-source hash invalidation after measurements, validated by a real YAML-comment test; agent later delta is documentation. No timing is attributed to the unmeasured revision.

## Reproduction and scope

Install Nift 4.12.0, Bun 1.4.3 and Node 22.22.1; clone the exact model revision, run `bun run install:app`, then `bun run build`. Fresh measurement retains installed dependencies but no application/content artifacts. Forced-full `bun run build:full` reuses valid compiled application/content/projections and renders/composes all pages. Normal `bun run build` is dependency-aware incremental/no-op. Fresh time excludes clone/dependency install; OS cache is uncontrolled. Source edit and manual agent projection coordination are untimed. `tools/final-campaign-optimized.py` records exact edits/restoration (paths reflect original workspace and must be adapted when rerunning). No new upstream build is needed for report regeneration.

`tools/measure.py` sums simultaneous RSS in the workload process group plus descendants, excluding the observer/GNU-time wrapper. Shared pages may be counted multiple times and short peaks missed; requested sleep20ms, actual sampling intervals longer. GNU-time maximum individual process RSS is separately recorded, not aggregate. Both upstream observations and Nift samples use the same observer.

`source-manifest.json` retains source/lockfile/toolchain/OS provenance. Hardware was not captured with the observations. `current-machine-snapshot.json` is explicitly a later review-time snapshot, not historical available-memory/CPU-load evidence.

Reference inventories and optimized fresh/restoration hashes preserve scope and comparison rules. HTML restoration normalization targets only13digit updatedAt fields inside `$tsr-stream-barrier`; production bytes are untouched. Non-HTML remains byte-identical. Search entries and LLM blocks match the reference despite inherited ordering changes; upstream-repeatability records a real upstream highlighting variation too.

## Certification boundary

Global output/content gates and representative browser interactions pass. Local Chinese Start hydration/Orama/navigation passes, not a full new CN production deployment. Retained393redirects/65conditionalroutes/1000bulkredirects and20local HTTP cases pass; provider precedence/cache/negotiation/schema/build-image remain unverified. Historical unit failures are classified independently; no unqualified full-suite green claim. See focused final architecture/correctness/methodology reviews. No private services or live indexing were mutated.

No Labs deployment, public announcement or maintainer contact. This local evidence commit must be reviewed and explicitly released before draft GitHub links become public.

Final matched saved-theme browser check confirms an inherited React#418 hydration defect: original frozen upstream and maintained-React migration both warn after a savedDark reload and recover. Theme/root implementation bytes are unchanged; light-state hydration and functional controls pass. The report does not claim clean hydration for all theme states. See final-theme-hydration-proof and updated correctness review.
