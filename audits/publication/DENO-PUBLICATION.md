# Deno Docs Labs publication

Route: `/sites/deno/`. Both migration repositories are read-only during publication: deno `7d663e4212d8f976b8ba0b29d819b9331db24522`, deno-agent `0b42efec8239f49214c821e32fe5f0cc8e389f15`. Their measured implementation revisions and pinned upstream are recorded in the page. Nift core is unchanged.

## Presentation and evidence

Inspected the Docker/Capgo migration reports, website-generator/scripting/shell benchmark reports, shared Labs index/navigation conventions and the Deno D9/init reviews before implementation. Deno owns separate templates and static assets: dark black/bone/olive, circular source/derive/compose/publish geometry, zero-origin profiler-style charts, visible reading order and native disclosures. No Deno brand assets, endorsement implication, blue palette or borrowed experiment stylesheet.

The order is premise → parity → architectures → prominent changed-input loop → whole-publication/native boundaries → OG correction/history → profiling → memory → maintenance/agent judgment → official evaluation → init dogfooding → methodology → evidence/reproduction. The common body-edit observations and unchanged median are prominent; slower shared-input/lifecycle rows remain visible. Source-editing/review time is excluded, and native changed-input production is explicitly not an unmeasured dev-server/HMR comparison.

`scripts/render_deno.py` generates tables and charts from committed JSON snapshots in `content/sites/deno/data/`. It checks 30 migration and 20 native samples, five samples per headline mode, final medians, memory headlines, historical medians, twenty changed-versus-forced cases, fresh-clone parity and the retained 104-state browser differences/20 interactions. The publication contract is 2,573 files, 834 HTML, 481 Markdown downloads, 834 images and 11,567 local search records. Browser screenshots are not claimed universally pixel-identical.

Full native reference regeneration and prepared-input native publication remain separate from migration forced and cached builds. Maintained frontend/image inputs, frozen live std inputs/clocks, local search versus remote service boundaries, exact WASM dependency delivery with compilation/startup inside timing, active-host/OS variance and process/phase RSS are visible. Remaining invalidation/search/DOM/memory costs are future profiling targets, not hidden or ascribed entirely to Markdown.

## Local validation

Full and incremental Labs builds pass; all eleven tracked pages are current. The general validator checks 217 local references, routes/fragments, assets, metadata and dark/no-blue CSS. Read-only GitHub API verification passes all seventeen repository/pinned evidence links (`deno-link-validation.json`).

Responsive checks cover CSS viewports 1440×1000, 768×1024, 390×844 and 320×780. All final observations have zero page/element/cell overflow, all ten changed-input rows present and dark mode. A long revision initially forced narrow-grid overflow; wrapping was fixed and the actual page rechecked. The temporary preview session also terminated between checks; only successful settled page observations count in the ledger. Native disclosure opens by click and closes by Enter; section anchors work. No warning/error logs on the recovered report. Screenshot bitmap dimensions are not conflated with CSS viewport dimensions.

Retained captures: `deno-desktop.png`, `deno-mobile-loop.png`, `deno-mobile-table.png`, `deno-tablet-benchmarks.png`; structured observations: `deno-browser-validation.json`. The report needs no JavaScript. Homepage and catalogue obtain the new entry through their existing shared JSON source; other reports and benchmark pages are unchanged.

## Publication workflow

The existing GitHub Pages configuration publishes the separate deployment checkout's `main` branch root. Source remains on `stage`. Commit/push source and deployment independently, preserving both histories. Live route/asset/index verification and exact commit IDs are recorded in the subsequent live closeout ledger.

```sh
python3 scripts/render_deno.py
nift build --all
nift build
python3 scripts/validate.py
python3 scripts/check_deno_links.py
nift status
```

## Live closeout

Published https://lab.nift.dev/sites/deno/ from deployment `7e639c91abc9ddf11da72a3dfc074e4ffa17efc9` (GitHub Pages built successfully). Live report, CSS, favicon, homepage and catalogue match the committed publication byte for byte. All 17 evidence links pass; live desktop/mobile inspection has no horizontal overflow and retains all ten changed-input rows. Temporary browser viewport reset. See `deno-live-validation.json`. No migration or Nift core changes were made.
