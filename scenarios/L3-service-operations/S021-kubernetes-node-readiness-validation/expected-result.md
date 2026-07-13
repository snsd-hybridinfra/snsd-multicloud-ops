# Expected Result

## Static Pass Criteria

- V001 through V012 return PASS with zero warnings for the current sample.
- Three required placeholder nodes are parsed as Ready.
- No NotReady or SchedulingDisabled sample row is present.
- No kubectl process is invoked.

## Optional Live Criteria

- kubectl is available and the read-only command succeeds.
- Every returned status includes Ready and none includes NotReady.
- SchedulingDisabled is reported as WARN without modifying the node.

## Evidence Criteria

Evidence contains mode, file results, row count, readiness judgment, finding counts, secret-safety result, and final judgment without raw live cluster details.
