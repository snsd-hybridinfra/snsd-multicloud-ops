# Validation

Scenario: S018-kubernetes-rbac-validation

Level: L2-security-baseline

Date: 2026-07-13

Overall status: PASS

| Check ID | Validation Item | Expected Condition | Actual Result | Evidence File | Status |
|---|---|---|---|---|---|
| V001 | RBAC baseline | File exists. | Baseline exists. | generated log and summary | PASS |
| V002 | RBAC rule matrix | File exists. | Matrix exists. | generated log and summary | PASS |
| V003 | RBAC manifest directory | Directory exists. | Directory exists. | generated log and summary | PASS |
| V004 | Required manifest examples | All files exist. | All files found. | generated log and summary | PASS |
| V005 | Policy statements and subjects | Required controls and subjects exist. | All found. | generated log and summary | PASS |
| V006 | Namespace-scoped RBAC structure | Kinds and namespace are correct. | Structure is correct. | generated log and summary | PASS |
| V007 | Cluster-wide privilege denial | No forbidden cluster binding. | None detected. | generated log and summary | PASS |
| V008 | Wildcard permission denial | No wildcard permission. | None detected. | generated log and summary | PASS |
| V009 | Application account restrictions | Dedicated account; no secrets. | Restrictions pass. | generated log and summary | PASS |
| V010 | Default ServiceAccount denial | No default account use or approval. | None detected. | generated log and summary | PASS |
| V011 | Monitoring read-only role | get, list, watch only. | Role is read-only. | generated log and summary | PASS |
| V012 | Kubernetes credential files | No forbidden credential file. | None detected. | generated log and summary | PASS |
| V013 | Manifest sensitive-content safety | No Secret, token, endpoint, or address. | None detected. | generated log and summary | PASS |
| V014 | Execution safety boundary | No live cluster or network command. | None detected. | generated log and summary | PASS |

## Generated Result

All fourteen checks passed using repository files only. Evidence is recorded in `logs/kubernetes-rbac-validation.log` and `configs/kubernetes-rbac-summary.md`.
