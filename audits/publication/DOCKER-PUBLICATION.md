# Docker Docs Labs publication

Public route: `/sites/docker/`. Published 8 October 2026, after the completed C7 migration experiment. Both experiment repositories are read-only during report publication: docker `77f79f065e3076d02bf591ee41f487bbbaa038e9`, docker-agent `78e7817c780913601db8af54b396aa4392d0624a`. Optimized runtime commits measured in fresh checkouts are preserved in the report evidence.

## Presentation and provenance

Inspected the live Cloudflare, Omarchy and Capgo migration pages and the scripting/website-generator/shell benchmark reports. The benchmark campaign was published independently before this report was integrated. Recurring conventions: independent report templates/palettes, Labs/catalogue return links, ordered editorial chapters, zero-origin graphs with adjacent ranges/boundaries, explicit maintenance assessment, pinned sources and reproducible evidence. The Docker design owns charcoal/rust/warm-ivory assets, stacked publication layers and pipeline diagrams. It does not borrow another experiment's stylesheet or imply Docker endorsement.

The order is premise → parity proof → source architectures → whole-pipeline measurements → profiling → changed inputs → maintainability → agent preferences → official migration judgment → methodology → evidence/reproduction. CSS-only visuals and native disclosures need no report JavaScript. The same published frontend JS in both experiments is disclosed; this report does not imply a client-JS reduction.

`scripts/render_docker.py` renders from retained committed C6/C7 sample snapshots in `content/sites/docker/data/`. It validates sample counts, all 60 changed-input semantic checks and twelve full comparisons, ten fresh-output checks, six lifecycle rows, both 192-state/pixel parity proofs and 8,622-file accepted-hash counts. Headline medians/RSS are independently calculated from the samples and checked against C7. Component and changed-input figures are calculated from the same samples; nested counters and search boundaries are labelled. Initial evidence is retained separately.

The report explains the maintained Markdown versus HTML distinction, bounded compatibility ports, non-native-@markup measurement, preserved frontend assets, publication entry point, accepted differences, inherited issues and remote-service mock boundaries. One/ten-page edit regressions are visible. Agent preferences distinguish agent-only implementation under human direction, mixed editing and maintenance with migration effort excluded. The official-migration assessment supports a serious evaluation, not an unconditional platform switch or measured long-term productivity claim.

## Validation

The report was prepared and checked in isolated source/deployment checkouts, then integrated with the newly committed benchmark campaign. Full and incremental Nift builds and normal Labs validation pass, including routes, anchors, metadata, local assets and dark/no-blue palette checks. Both experiment repositories and eleven pinned repository/evidence links are verified through GitHub API; results are retained in `docker-link-validation.json`.

Browser inspections cover 1440×1000 desktop, 768×1024 tablet, 390×844 mobile and 320×780 narrow mobile. No page-level horizontal overflow. Main chart labels and ranges remain readable; changed-input rows show both models on narrow screens. Pipeline diagrams preserve five human stages and three agent stages. Native disclosure opens by click and closes with Enter; anchor navigation and keyboard-focusable regions work. No report JavaScript warnings/errors observed. Live route, assets, homepage/catalogue integration and benchmark labels are checked after deployment.

Source and deployment histories are committed/pushed independently (`stage` and `main` respectively). The existing benchmark campaign is preserved. This publication adds Docker assets/report and updates the homepage/catalogue.

## Rebuild

```sh
python3 scripts/render_docker.py
nift build --all
nift build
python3 scripts/validate.py
nift status
```

Use the normal independent public checkout workflow for publication. Keep the experiment inputs/implementations and all accepted evidence unchanged.
