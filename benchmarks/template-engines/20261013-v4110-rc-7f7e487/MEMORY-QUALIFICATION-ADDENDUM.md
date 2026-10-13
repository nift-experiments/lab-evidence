# Post-freeze memory qualification

The accepted payload at 2b98e06 retained the suspected launch-floor qualification. The subsequent separate no-work true/taskset control confirms the mechanism:16.75 MiB child maxRSS with the empty supervisor versus 80.75 MiB after the supervisor allocates 64 MiB. The frozen Popen/taskset/wait 4 pattern is reproduced; no template work occurs in the child.

All accepted raw memory values remain unchanged. Fresh wait 4 values sharing the supervisor floor are not ranked as runtime memory efficiency; subtracting a constant would not repair them. Persistent lifetime peaks also include preparation, batch/output retention and validation. Correctness and wall-time acceptance is unchanged. The full control and source are retained in provenance/launch-floor-control.* and campaign runtime-diagnostics. Practitioner opinions remain drafts and no Labs publication is authorized.
