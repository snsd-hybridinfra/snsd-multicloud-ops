# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Workload documentation | Baseline and commands exist. | generated log and summary |
| V002 | Required workload files | Namespace, Deployment, Service, README exist. | manifests, generated evidence |
| V003 | Sample workload evidence | Deployment and Pod samples exist. | samples, generated evidence |
| V004 | Required command examples | Seven examples exist. | generated evidence |
| V005 | Deployment validation model | Required objects and controls documented. | generated evidence |
| V006 | Manifest kinds and namespace | Correct kinds, marker, `snsd-example`. | manifests, generated evidence |
| V007 | Labels and selectors | All application labels align. | manifests, generated evidence |
| V008 | Runtime readiness controls | Probes, resources, fixed image exist. | deployment, generated evidence |
| V009 | Unsafe manifest pattern denial | No prohibited pattern. | manifests, generated evidence |
| V010 | Deployment evidence | All desired replicas ready/available. | deployment sample or live counts |
| V011 | Pod evidence | All Pods Running and ready. | Pod sample or live counts |
| V012 | Pod restart awareness | PASS at zero; WARN above zero. | Pod sample or live counts |
| V013 | Kubernetes credential files | No forbidden credential file. | generated evidence |
| V014 | Manifest/evidence content safety | No endpoint, address, token, key, or secret. | generated evidence |
| V015 | Execution safety boundary | Two guarded read-only live argument sets only. | generated evidence |
| V016 | Validation mode | Static without kubectl or successful explicit live read. | generated evidence |

Every validation item maps to stable evidence by check ID.
