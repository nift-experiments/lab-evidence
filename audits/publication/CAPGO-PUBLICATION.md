# Capgo case study publication

Route: `/sites/capgo/`. First complete publication: source c436c1b / deployment f774be6. Experiment repositories were read only during publication; faithful remains frozen at 590c1eec, Agent final dd95a37 / measured 6371356.

Information architecture: experiment premise → two maintenance philosophies → repeated measurements with adjacent workload caveat → golden-reference migration process → corpus and validation limits → maintenance tradeoffs → expandable methodology → pinned evidence → lessons and proposed future migration scaffolding.

Statistics were checked against faithful `docs/FAITHFUL-FINAL-REPORT.md` and `evidence/final-benchmarks/{summary,methodology}.json`, and Agent `docs/THREE-WAY-COMPARISON.md`, `evidence/final-benchmarks/{summary,methodology}.json` and runtime architecture evidence. Public report data is in `content/sites/capgo/data/report.json`. Ratios use final medians and raw KiB maxima (not rounded GiB labels): 18.7, 47.6, 2.54 for elapsed; 15.7 and 36.3 for RSS. The disjoint corpus counts sum to 1,347. Cold preparation, warm caches, private services and non-equivalent workloads remain explicit.

Design: independent charcoal/plum/ivory report, related to the Labs editorial language without reusing another experiment's CSS. No raster recreation of Capgo or generic dashboard styling. The canonical table is sufficient; extra charts were omitted to avoid redundant visual encoding. Mobile measurement rows expose both time and memory without sideways scrolling. Larger comparison tables retain labelled keyboard-focusable scrolling regions. Disclosures use semantic details/summary; no JS is required for this report. Existing catalogue pagination remains JS.

Validation: normal Nift full/incremental builds; `python3 scripts/validate.py` passes five HTML pages and 61 local references, including routes, fragments, assets, metadata and dark/no-blue CSS literals. Browser checked 1280 desktop, 390 mobile and narrow 320 viewport; no page overflow; mobile benchmark memory visible; disclosure click/Enter opens/closes; no browser errors observed. Source and deployment histories are committed/pushed separately.

## Maintenance claim correction

The original unconditional Astro recommendation was replaced by the source-backed investigation at Agent report revision 7d45594. Upstream builds English only; runtime translation is a separate Cloudflare worker. Schema/discovery and scoped-style/compiler conveniences survive scrutiny as concrete current tooling differences. No intrinsic Nift content/composition/i18n/interoperability deficit was established. Integration inventory distinguishes retained/completed/unported seams. Long-term editing productivity, ecosystem scale and team familiarity remain unmeasured. Public copy now presents workflow-dependent choices. This checkpoint changes reports only.


## 2026-10-06 — graphs and visible iteration evidence

Added linear, zero-origin build-time and peak-process-memory graphs. Ordinary edits/no-op and explicit-target edits are visible, with workflow-specific maintenance recommendations. Three real edits per family for both migrations are recorded at capgo-agent b555abe (24 samples); historical ordinary cases are not paired with this new suite. Astro edit/HMR remains unmeasured. Faithful ordinary restoration left targeted test output in some cases; an unmeasured full rebuild restored complete parity. Cause remains unestablished; caveat and raw gates are published. No migration implementation changed.
