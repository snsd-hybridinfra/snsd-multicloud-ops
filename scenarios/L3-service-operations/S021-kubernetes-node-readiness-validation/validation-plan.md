# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Node-readiness baseline | Baseline exists. | generated log and summary |
| V002 | Command reference | Reference exists. | generated log and summary |
| V003 | Sample node evidence | Sample exists. | sample, generated log and summary |
| V004 | Required command examples | Five examples exist. | generated log and summary |
| V005 | Readiness model and placeholders | Required conditions, roles, and modes exist. | generated log and summary |
| V006 | Required sample nodes | Three placeholder nodes exist. | sample, generated log and summary |
| V007 | Node readiness evidence | All nodes Ready; none NotReady. | sample or live counts, generated summary |
| V008 | SchedulingDisabled awareness | PASS when absent; WARN when present. | generated log and summary |
| V009 | Kubernetes credential files | No forbidden credential file. | generated log and summary |
| V010 | Evidence sensitive-content safety | No endpoint, address, token, key, or secret. | generated log and summary |
| V011 | Execution safety boundary | Only guarded read-only live arguments. | generated log and summary |
| V012 | Validation mode | Static succeeds without kubectl; requested live command succeeds read-only. | generated log and summary |

Every validation item maps to stable evidence by check ID.
