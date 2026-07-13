# Evidence Map

| Check ID | Validation Item | Evidence File | Required |
|---|---|---|---|
| V001 | Node-readiness baseline | `logs/kubernetes-node-readiness-validation.log`; `configs/kubernetes-node-readiness-summary.md` | yes |
| V002 | Command reference | same generated evidence | yes |
| V003 | Sample node evidence | `logs/kubectl-get-nodes.sample.txt`; generated evidence | yes |
| V004 | Required command examples | generated log and summary | yes |
| V005 | Readiness model and placeholders | generated log and summary | yes |
| V006 | Required sample nodes | sample, generated log and summary | yes |
| V007 | Node readiness evidence | sample or sanitized live counts, generated summary | yes |
| V008 | SchedulingDisabled awareness | generated log and summary | yes |
| V009 | Kubernetes credential files | generated log and summary | yes |
| V010 | Evidence sensitive-content safety | generated log and summary | yes |
| V011 | Execution safety boundary | generated log and summary | yes |
| V012 | Validation mode | generated log and summary | yes |

`commands.md` documents both modes and `validation.md` records the completed static result. Raw live node rows are not repository evidence.
