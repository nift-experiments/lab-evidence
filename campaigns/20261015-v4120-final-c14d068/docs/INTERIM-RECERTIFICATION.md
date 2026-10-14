# Interim final-candidate recertification

Audited official suites: scripting, template-engines. Exact-source three-way version diagnostics remain separate from current official peer results and historical cross-node trends. No publication or release is authorized.

## Best same-node wall improvements versus release — complete

| Rank | Suite / scenario | Release | Original | Final | Unit | Improvement vs release | Recovery vs original | Samples/version |
|---:|---|---:|---:|---:|---|---:|---:|---:|
| 1 | template-engines / loop-10000/source-render | 118.471604 | 33.514301 | 32.942846 | ms/render | 72.19% | +1.71% | 3 |
| 2 | template-engines / loop-10000/fresh | 158.529676 | 73.741216 | 77.354308 | ms/invocation | 51.21% | -4.90% | 3 |
| 3 | template-engines / article/source-render | 0.433770 | 0.267626 | 0.268566 | ms/render | 38.09% | -0.35% | 3 |
| 4 | template-engines / article/fresh | 3.689644 | 3.558491 | 3.507010 | ms/invocation | 4.95% | +1.45% | 3 |
| 5 | scripting / sanity/function-calls/small | 4.710201 | 7.374958 | 4.678490 | ms/invocation | 0.67% | +36.56% | 10 |

## Every measured positive same-node wall change — complete

| Rank | Suite / scenario | Baseline | Baseline value | Final | Increase | Classification |
|---:|---|---|---:|---:|---:|---|
| 1 | template-engines / loop-10000/fresh | original | 73.741216 | 77.354308 | 4.90% | descriptive same-node increase; not formal significance |
| 2 | scripting / sanity/function-calls/large | release | 193.600459 | 198.619788 | 2.59% | descriptive same-node increase; not formal significance |
| 3 | template-engines / article/source-render | original | 0.267626 | 0.268566 | 0.35% | descriptive same-node increase; not formal significance |

Every comparison above uses the same node, exact versions and frozen diagnostic boundaries. Template diagnostics have three measured observations/version and remain descriptive. Scripting has ten; final/release ranges overlap, and large calls are slower in eight of ten paired blocks. Overlapping ranges do not prove equality or eliminate a small regression. Major original call regressions have disjoint ranges and all ten final blocks faster. Near-flat changes are retained. Original/checkpoint and release baselines are explicitly distinguished.

## Current same-node peer wall deficits — complete

| Rank | Suite / scenario / boundary | Nift | Best peer | Peer | Unit | Nift / peer |
|---:|---|---:|---|---:|---|---:|
| 1 | scripting / arrays-strings-hash/frequency-count/large | 416.5421 | luajit | 3.0221 | ms/invocation | 137.83× |
| 2 | scripting / sanity/function-calls/large | 193.7259 | luajit | 1.4189 | ms/invocation | 136.53× |
| 3 | scripting / arrays-strings-hash/sliding-window/large | 250.1156 | luajit | 2.4040 | ms/invocation | 104.04× |
| 4 | scripting / arrays-strings-hash/map-set/large | 212.6967 | luajit | 2.6333 | ms/invocation | 80.77× |
| 5 | scripting / dynamic-programming/fibonacci/large | 141.5248 | luajit | 2.0596 | ms/invocation | 68.72× |
| 6 | scripting / arrays-strings-hash/scan/large | 82.8741 | luajit | 1.3739 | ms/invocation | 60.32× |
| 7 | scripting / sanity/loops/large | 72.5922 | luajit | 1.4192 | ms/invocation | 51.15× |
| 8 | scripting / graphs-trees-search/bfs/large | 799.3592 | luajit | 16.9315 | ms/invocation | 47.21× |
| 9 | scripting / arrays-strings-hash/sort-index/large | 511.6308 | python | 23.0522 | ms/invocation | 22.19× |
| 10 | template-engines / loop-10000/source-render | 34.0847 | handlebars | 2.2486 | ms/render | 15.16× |
| 11 | template-engines / collection/source-render | 7.1487 | handlebars | 0.8673 | ms/render | 8.24× |
| 12 | scripting / structured-data/json-transform/large | 462.8532 | node | 74.5456 | ms/invocation | 6.21× |
| 13 | scripting / graphs-trees-search/bfs/small | 11.4051 | lua54 | 1.8680 | ms/invocation | 6.11× |
| 14 | scripting / structured-data/json-traverse/large | 370.4149 | node | 68.6082 | ms/invocation | 5.40× |
| 15 | scripting / arrays-strings-hash/frequency-count/small | 7.0682 | luajit | 1.3125 | ms/invocation | 5.39× |
| 16 | template-engines / loop-1000/source-render | 3.2934 | handlebars | 0.6493 | ms/render | 5.07× |
| 17 | scripting / arrays-strings-hash/sort-index/small | 6.8471 | luajit | 1.5076 | ms/invocation | 4.54× |
| 18 | template-engines / literal/source-render | 0.0152 | liquid | 0.0036 | ms/render | 4.21× |
| 19 | scripting / arrays-strings-hash/sliding-window/small | 5.2873 | luajit | 1.3394 | ms/invocation | 3.95× |
| 20 | scripting / sanity/function-calls/small | 4.6504 | luajit | 1.3011 | ms/invocation | 3.57× |
| 21 | scripting / arrays-strings-hash/map-set/small | 4.7012 | luajit | 1.3955 | ms/invocation | 3.37× |
| 22 | scripting / filesystem/traverse/large | 25.0047 | luajit | 7.6408 | ms/invocation | 3.27× |
| 23 | scripting / arrays-strings-hash/scan/small | 3.5558 | luajit | 1.2906 | ms/invocation | 2.76× |
| 24 | scripting / structured-data/json-parse/large | 182.0766 | node | 66.9882 | ms/invocation | 2.72× |
| 25 | scripting / sanity/loops/small | 3.3463 | luajit | 1.2815 | ms/invocation | 2.61× |
| 26 | scripting / dynamic-programming/fibonacci/small | 2.8171 | luajit | 1.2633 | ms/invocation | 2.23× |
| 27 | template-engines / many-templates-100/source-render | 0.0214 | liquid | 0.0102 | ms/render | 2.09× |
| 28 | template-engines / nested-loops/source-render | 1.0676 | nunjucks | 0.5115 | ms/render | 2.09× |
| 29 | scripting / sanity/output/small | 2.5214 | luajit | 1.2174 | ms/invocation | 2.07× |
| 30 | template-engines / many-templates-1000/source-render | 0.0215 | liquid | 0.0105 | ms/render | 2.06× |
| 31 | scripting / sanity/noop/large | 2.3885 | luajit | 1.1839 | ms/invocation | 2.02× |
| 32 | scripting / sanity/noop/small | 2.4628 | luajit | 1.2283 | ms/invocation | 2.01× |
| 33 | scripting / sanity/output/large | 2.4649 | luajit | 1.2294 | ms/invocation | 2.00× |
| 34 | template-engines / many-templates-10/source-render | 0.0212 | liquid | 0.0108 | ms/render | 1.96× |
| 35 | template-engines / many-renders-1000/source-render | 0.0225 | liquid | 0.0151 | ms/render | 1.49× |
| 36 | template-engines / loop-100/source-render | 0.3643 | nunjucks | 0.2449 | ms/render | 1.49× |
| 37 | template-engines / many-renders-100/source-render | 0.0218 | liquid | 0.0161 | ms/render | 1.35× |
| 38 | template-engines / includes-8/source-render | 0.1629 | nunjucks | 0.1315 | ms/render | 1.24× |
| 39 | template-engines / includes-4/source-render | 0.0890 | liquid | 0.0859 | ms/render | 1.04× |
| 40 | scripting / filesystem/traverse/small | 3.1041 | luajit | 4.6138 | ms/invocation | 0.67× |
| 41 | scripting / structured-data/json-transform/small | 7.1862 | python | 24.4697 | ms/invocation | 0.29× |
| 42 | scripting / structured-data/json-traverse/small | 6.2346 | python | 23.9809 | ms/invocation | 0.26× |
| 43 | scripting / structured-data/json-parse/small | 4.2690 | python | 23.7024 | ms/invocation | 0.18× |

## Large gains but still behind

| Scenario | Improvement vs release | Derived old deficit | Current official deficit | Verdict |
|---|---:|---:|---:|---|
| template-engines / loop-10000/source-render | 72.19% | 52.69× | 15.16× | Still behind handlebars |

Derived old deficits divide controlled old Nift diagnostic medians by the current official peer median on the same host and matching boundary. These are cross-phase diagnostics, not a simultaneously interleaved old-Nift/peer benchmark. Current deficits use official Nift/peer medians from the same cohort. No cross-node peer denominator is substituted.

## Memory and capabilities remain separate

Supervisor allocation0→64MiB moves noopraw16.75→80.75MiB, proving inherited floor; raw retained/unranked.

Raw scripting call peak-memory diagnostics are retained separately; small quantized differences do not establish a leak or superiority. Nift public parse-only/prepared-AST template modes remain unsupported in this frozen public-API matrix. Nift has lower medians than the best other template engine in 30 of 43 supported matching fresh/source-render cells; this is not an overall engine ranking. Practitioner judgments and the release recommendation remain pending the wider sweep.
