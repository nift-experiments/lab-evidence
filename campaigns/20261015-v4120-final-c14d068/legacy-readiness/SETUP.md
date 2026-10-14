# Frozen cloud preparation

Do not execute until parent authorizes provisioned hosts and /opt/nift exact final build. Upload provision-pinned-comparators.sh, capture-comparators.py and the corresponding setup-*.sh to /opt. Execute `bash /opt/setup-SUITE.sh`. Scripts clone public HTTPS with credential helpers disabled and interactive credential prompting disabled, then explicitly checkout frozen commits. Stage branches need no credential material; failures stop rather than falling back to another ref.

The source-built candidate is mandatory; no installer fallback. Prior Node 24.21.0, Fish 4.9.3, Nu 0.116.1 and Hugo 0.167.0 assets/checksums are preserved. Ubuntu Python/Ruby/Lua/LuaJIT/Bash/Zsh exact installed package versions and binary hashes are captured before gates. Any version divergence from accepted pins must be reviewed before measurement, not silently treated as identical. Website npm ci uses the frozen lockfile (Astro 7.3.6/VitePress 1.6.4).

Then execute the corresponding cloud-check script, collect all correctness receipts, and have parent authorize official timing. Set NIFT_CANDIDATE_BINARY_SHA256 from /opt/candidate-built.json when executing official-SUITE.sh; wrapper verifies exact final SHA/version/hash and frozen suite/tool inventory. Full official plans and three-way diagnostics remain distinct; no installs/profile run during timing.
