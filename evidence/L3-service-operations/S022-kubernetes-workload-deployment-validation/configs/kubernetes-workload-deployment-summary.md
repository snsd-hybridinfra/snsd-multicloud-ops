# Kubernetes Workload Deployment Summary

- Scenario: S022-kubernetes-workload-deployment-validation
- Generated: 2026-07-13T11:39:18+09:00
- Validation mode: **Static**
- Required file check result: **PASS**
- Manifest safety check result: **PASS**
- Deployment evidence parsing result: **PASS** (1 row(s))
- Pod evidence parsing result: **PASS** (2 row(s), 0 restart(s))
- Secret-safety check result: **PASS**
- Final judgment: **PASS**

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Workload documentation | PASS | Baseline and command reference exist. |
| V002 | Required workload files | PASS | Namespace, Deployment, Service, and README files exist. |
| V003 | Sample workload evidence | PASS | Deployment and pod sample evidence exist. |
| V004 | Required command examples | PASS | All seven command examples are documented. |
| V005 | Deployment validation model | PASS | Objects, replicas, readiness, image, labels, probes, resources, evidence, and modes are documented. |
| V006 | Manifest kinds and namespace | PASS | Namespace, Deployment, and Service examples use snsd-example and are marked non-production. |
| V007 | Labels and selectors | PASS | Deployment metadata/template/selector and Service selector labels are consistent. |
| V008 | Runtime readiness controls | PASS | Readiness/liveness probes, requests/limits, and fixed image tag exist. |
| V009 | Unsafe manifest pattern denial | PASS | No hostNetwork, privileged, hostPath, Secret, imagePullSecrets, ClusterRoleBinding, or NodePort pattern exists. |
| V010 | Deployment evidence | PASS | All 1 deployment row(s) are fully ready and available. |
| V011 | Pod evidence | PASS | All 2 pod row(s) are Running and fully ready. |
| V012 | Pod restart awareness | PASS | No pod restart is present in evaluated evidence. |
| V013 | Kubernetes credential files | PASS | No kubeconfig, service-account token, certificate, or private-key file exists. |
| V014 | Manifest and evidence sensitive-content safety | PASS | No endpoint URL, numeric address, token, certificate data, key, password, or secret exists. |
| V015 | Execution safety boundary | PASS | Live argument sets contain only read-only deployment and pod listings guarded by LiveKubectl. |
| V016 | Validation mode | PASS | Static mode completed without invoking kubectl. |

## Safety Boundary

Static mode does not invoke kubectl. LiveKubectl mode runs only read-only workload listings and stores aggregate status rather than raw cluster details.
