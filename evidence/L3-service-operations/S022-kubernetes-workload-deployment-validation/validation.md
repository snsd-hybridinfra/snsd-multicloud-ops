# Validation

Scenario: S022-kubernetes-workload-deployment-validation

Level: L3-service-operations

Date: 2026-07-13

Overall status: PASS

Validation mode: Static

| Check ID | Validation Item | Expected Condition | Actual Result | Evidence File | Status |
|---|---|---|---|---|---|
| V001 | Workload documentation | Baseline and commands exist. | Both exist. | generated evidence | PASS |
| V002 | Required workload files | Four files exist. | All found. | manifests, generated evidence | PASS |
| V003 | Sample workload evidence | Two samples exist. | Both found. | samples, generated evidence | PASS |
| V004 | Required command examples | Seven examples exist. | All documented. | generated evidence | PASS |
| V005 | Deployment validation model | Required model exists. | All terms found. | generated evidence | PASS |
| V006 | Manifest kinds and namespace | Kinds and namespace correct. | All pass. | manifests, generated evidence | PASS |
| V007 | Labels and selectors | Labels align. | Consistent. | manifests, generated evidence | PASS |
| V008 | Runtime readiness controls | Probes/resources/fixed image. | All present. | deployment, generated evidence | PASS |
| V009 | Unsafe manifest pattern denial | No unsafe pattern. | None detected. | manifests, generated evidence | PASS |
| V010 | Deployment evidence | Fully ready and available. | One row at 2/2, available 2. | sample, generated evidence | PASS |
| V011 | Pod evidence | Running and ready. | Two rows at 1/1 Running. | sample, generated evidence | PASS |
| V012 | Pod restart awareness | Zero restarts. | Zero. | sample, generated evidence | PASS |
| V013 | Kubernetes credential files | No forbidden file. | None detected. | generated evidence | PASS |
| V014 | Manifest/evidence content safety | No endpoint, address, token, key, secret. | None detected. | generated evidence | PASS |
| V015 | Execution safety boundary | Guarded read-only live listings only. | Boundary confirmed. | generated evidence | PASS |
| V016 | Validation mode | Static without kubectl. | Static completed; kubectl not invoked. | generated evidence | PASS |

## Generated Result

Static validation passed all sixteen checks with one fully available Deployment, two Running/ready Pods, and zero restarts. Optional LiveKubectl mode was not run.
