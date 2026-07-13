# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Required artifacts | Complete | files/summary |
| V002 | Runbook placeholders and boundary | Complete/manual | runbook/summary |
| V003 | Criteria matrix | Twelve phases | criteria/summary |
| V004 | Ansible placeholder safety | Debug only | playbook/summary |
| V005 | Metric placeholder documentation | Symbolic | metrics/summary |
| V006 | Pre-failure replica health | Threads Yes, lag 0 | pre sample |
| V007 | Manual failure injection evidence | Manual-only | injection sample |
| V008 | Replica failure detection | No/NULL/error | detection sample |
| V009 | Primary availability | Reachable/read-write | primary sample |
| V010 | Post-recovery replica health | Threads Yes, lag 0 | post sample |
| V011 | Replication catch-up | Healthy/no error | catch-up sample |
| V012 | Recovery timing | Numeric or WARN | injection sample |
| V013 | Recovered-state failure indicators | None | post/catch-up |
| V014 | Database evidence safety | No sensitive content | log/summary |
| V015 | Execution safety boundary | No execution | validator/summary |
