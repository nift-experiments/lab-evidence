# Expanded shell campaign: 20261010-v4100-shell-expanded

Nift 4.10.0 development build. This series adds substantial shell work while preserving startup and configuration methodology. It does not establish an overall fastest shell.

## Identity and counts

Nift source `2eaec7d70e9ce2e698d0ba23a605fb9cf85317ff`; measured suite `48a4a8e3e1f3e1ccf2c61fc7f8a7fd3a490ab4a1`. One fresh g6-standard-4 shared-CPU node, us-east, Ubuntu 24.04, 4 vCPU/8 GiB; all measurements serial and pinned to CPU 0. OS caches uncontrolled. Native Make defaults: `make -j2; make install PREFIX=/opt/campaign/tools`, C++17/C99 -O2, no architecture tuning.

141 workload jobs, 1275 measured observations, 255 retained warmups; startup prepared/fresh matrices 76 jobs, 4900 + 228. No sample or outlier discarded.

## Detected participants

- bash: GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu)
- zsh: zsh 5.9 (x86_64-ubuntu-linux-gnu)
- fish: fish, version 4.9.3
- nu: 0.116.1
- nift: Nift v4.10.0

CPU: AMD EPYC 7542 32-Core Processor. Kernel: 6.8.0-134-generic.
Nift binary SHA-256: `e7cb28d6150c797acbb52a618faff3cf981281b9ea4e91a8c478062242f0c3a2`.

## Startup

| Boundary / median ms | bash | zsh | fish | nu | nift |
|---|---:|---:|---:|---:|---:|
| interactive | 2.813 | 3.655 | 24.479 | 21.237 | 2.595 |
| trivial-command | 1.955 | 2.518 | 2.928 | 15.900 | 2.913 |
| external-100 | 95.381 | 110.680 | 83.250 | 108.335 | 107.212 |

## Selected workload tasks

| Task / median seconds | bash | zsh | fish | nu | nift | GNU baseline |
|---|---:|---:|---:|---:|---:|---:|
| create-empty-100000 | 3.848080 | 5.920048 | 6.397616 | 4.076042 | 4.139350 | — |
| create-small-100000 | 6.514450 | 7.848619 | 9.610063 | 5.863296 | 13.962735 | — |
| delete-selected-100000 | 2.760352 | 2.590502 | 2.544717 | 8.048720 | 2.759560 | 2.338075 |
| delete-tree-100000 | 2.614269 | 2.374244 | 2.347948 | 7.842287 | 3.020401 | 2.471873 |
| copy-small-10000 | 0.598233 | 0.606093 | 0.626105 | 1.937112 | 0.952684 | 0.664190 |
| rename-selected-10000 | 0.376204 | 0.382771 | 0.380598 | 1.316495 | 0.597152 | 0.364838 |
| concat-small-10000 | 0.121193 | 0.129335 | 0.125294 | 0.644528 | 0.278988 | — |
| traverse-100000 | 0.539545 | 0.496453 | 0.543076 | 0.261150 | 1.384550 | — |
| processes-1000 | 0.958254 | 1.087936 | 0.763099 | 0.900489 | 1.098721 | — |
| pipeline-8 | 0.013468 | 0.014317 | 0.011823 | 0.025797 | 0.013696 | — |
| arithmetic | 0.066413 | 0.026458 | 3.949487 | 0.034367 | 0.018232 | — |
| function-calls | 0.055273 | 0.186015 | 1.601062 | 0.048301 | 0.022586 | — |
| fibonacci-mod | 0.008145 | 0.004917 | 0.171346 | 0.017114 | 0.004800 | — |
| string-transform | 0.036517 | 0.015973 | 0.900116 | 0.052514 | 0.061131 | — |
| log-filter-group | 0.051084 | 0.056603 | 0.054998 | 0.079588 | 0.052763 | — |
| source-tree-report | 0.257104 | 0.255792 | 0.262325 | 0.273654 | 0.262672 | — |
| selected-cleanup | 0.036642 | 0.039564 | 0.039988 | 0.130495 | 0.050148 | — |

## Correctness and boundaries

All complete cloud smoke, RC-state certifications, workload tests and supervisor tests passed. Every official output and filesystem oracle passed. All distribution fields were independently recomputed exactly; the raw files passed validation. Frozen definitions, job identities, sample/warmup counts, affinity and binary hashes were checked. Fixture manifests, content recipes, implementation sources, exact commands, every observation and strict validation records are retained.

Native arithmetic/calls/Fibonacci/string cases compare bounded shell-code work. GNU log and source-report pipelines share the same external engines in all shells. Filesystem end-to-end tasks permit Nift/Nu native APIs versus traditional redirection/batched GNU utilities. Nift atomic saving performs temporary-file replacement. Direct GNU xargs baselines exclude shell launch but include utility work. These architectural differences are explicit, and the baseline is not subtracted. Uncontrolled caches, shared CPU scheduling and different internal semantics limit attribution. RSS is Linux waited-child high-water memory, not simultaneous aggregate process-tree memory.

The most informative additions remain exact 100k selected deletion with keeper preservation, native algorithm cases and process scaling. No one result should be treated as an overall shell-quality score.

## Publication and lifecycle

Result evidence is pushed before Labs. Prior immutable series remain unchanged and accessible. Local desktop/390/320, keyboard scrolling, route/fragment/assets, private-material and historical hash checks precede publication. Changed live bytes and historical evidence are checked before deleting only the campaign nodes. CLI absence and independent authenticated API HTTP 404 are required; temporary SSH/config/connection state is then removed. Final lifecycle records provide timestamps and publication commits.
