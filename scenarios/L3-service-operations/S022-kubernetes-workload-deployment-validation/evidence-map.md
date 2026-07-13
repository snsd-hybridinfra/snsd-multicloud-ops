# Evidence Map

| Check ID | Validation Item | Evidence File | Required |
|---|---|---|---|
| V001 | Workload documentation | `logs/kubernetes-workload-deployment-validation.log`; `configs/kubernetes-workload-deployment-summary.md` | yes |
| V002 | Required workload files | manifests; generated evidence | yes |
| V003 | Sample workload evidence | both sample files; generated evidence | yes |
| V004 | Required command examples | generated evidence | yes |
| V005 | Deployment validation model | generated evidence | yes |
| V006 | Manifest kinds and namespace | manifests; generated evidence | yes |
| V007 | Labels and selectors | manifests; generated evidence | yes |
| V008 | Runtime readiness controls | deployment; generated evidence | yes |
| V009 | Unsafe manifest pattern denial | manifests; generated evidence | yes |
| V010 | Deployment evidence | deployment sample or sanitized live counts | yes |
| V011 | Pod evidence | Pod sample or sanitized live counts | yes |
| V012 | Pod restart awareness | Pod sample or sanitized live counts | yes |
| V013 | Kubernetes credential files | generated evidence | yes |
| V014 | Manifest/evidence content safety | generated evidence | yes |
| V015 | Execution safety boundary | generated evidence | yes |
| V016 | Validation mode | generated evidence | yes |

`commands.md` documents both modes and `validation.md` records the completed static result. Raw live workload rows are not repository evidence.
