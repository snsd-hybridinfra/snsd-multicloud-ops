# Validation

Scenario: S021-kubernetes-node-readiness-validation

Level: L3-service-operations

Date: 2026-07-13

Overall status: PASS

Validation mode: Static

| Check ID | Validation Item | Expected Condition | Actual Result | Evidence File | Status |
|---|---|---|---|---|---|
| V001 | Node-readiness baseline | File exists. | Baseline exists. | generated log and summary | PASS |
| V002 | Command reference | File exists. | Reference exists. | generated log and summary | PASS |
| V003 | Sample node evidence | File exists. | Sample exists. | sample, generated evidence | PASS |
| V004 | Required command examples | Five examples exist. | All documented. | generated log and summary | PASS |
| V005 | Readiness model and placeholders | Required model exists. | All terms found. | generated log and summary | PASS |
| V006 | Required sample nodes | Three nodes exist. | All found. | sample, generated evidence | PASS |
| V007 | Node readiness evidence | All Ready; none NotReady. | Three Ready nodes. | sample, generated evidence | PASS |
| V008 | SchedulingDisabled awareness | PASS absent; WARN present. | None present. | generated log and summary | PASS |
| V009 | Kubernetes credential files | No forbidden file. | None detected. | generated log and summary | PASS |
| V010 | Evidence sensitive-content safety | No endpoint, address, token, key, or secret. | None detected. | generated log and summary | PASS |
| V011 | Execution safety boundary | Guarded read-only live arguments only. | Boundary confirmed. | generated log and summary | PASS |
| V012 | Validation mode | Static without kubectl. | Static completed; kubectl not invoked. | generated log and summary | PASS |

## Generated Result

Static validation passed all twelve checks with three Ready placeholder nodes, zero NotReady findings, and zero SchedulingDisabled findings. Optional LiveKubectl mode was not run.

## Real-Lab Evidence Intake

| Check | Expected Condition | Actual Result | Status | Evidence |
|---|---|---|---|---|
| Real-lab source | Sanitized pasted terminal output is available | Required command categories are present in sanitized form | PASS | `logs/20260714-S021-k3s-node-readiness.sanitized.txt` |
| k3s service | `systemctl is-active k3s` reports active | active (running) | PASS | Sanitized evidence and validation summary |
| Node readiness | `kubectl get nodes -o wide` reports the node as Ready | Node reports Ready | PASS | Sanitized evidence and validation summary |
| kube-system pods | `kubectl get pods -A` provides kube-system status | Observed Pods are Running or Completed; no failed Pod shown | PASS | Sanitized evidence and validation summary |
| kubectl client | Client version output is present | Client and Kustomize versions present | PASS | Sanitized evidence and validation summary |
| Sensitive data | No raw user, address, hostname, token, certificate, kubeconfig, key, password, secret, header, cookie, or credential is committed | Repository evidence contains placeholders and omission notices only | PASS | `configs/20260714-S021-k3s-node-readiness-validation-summary.md` |

Real-lab final judgment: **READY**.

Raw terminal output is not committed. The static repository model and sanitized real-lab readiness evidence are validated. This judgment covers the observed node-readiness state only and does not expose kubeconfig or cluster credentials.
