# Commands

Scenario: S021-kubernetes-node-readiness-validation
Level: L3-service-operations
Capability: Kubernetes/k3s Node Readiness Validation
Target: `<cluster-context>`
Execution timestamp: TODO

Record sanitized output only. Do not include kubeconfig files, Kubernetes Secrets, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | kubectl client availability validation plan | Plan `kubectl version --client` or approved equivalent. | Confirm kubectl can be used for future node readiness checks. | TODO: record sanitized output after approved execution. |
| V002 | Kubernetes context availability validation plan | Plan context lookup for `<cluster-context>` without recording kubeconfig content. | Confirm intended cluster context is available. | TODO: record sanitized output after approved execution. |
| V003 | kubectl get nodes validation plan | Plan `kubectl get nodes --context <cluster-context>`. | Confirm expected nodes are listed. | TODO: record sanitized output after approved execution. |
| V004 | AWS Kubernetes/k3s node Ready status validation plan | Review Ready status for `<aws-k8s-node>`. | Confirm AWS service node is Ready. | TODO: record sanitized output after approved execution. |
| V005 | Azure Kubernetes/k3s node Ready status validation plan | Review Ready status for `<azure-k8s-node>`. | Confirm Azure service node is Ready. | TODO: record sanitized output after approved execution. |
| V006 | OpenStack Kubernetes/k3s node Ready status validation plan | Review Ready status for `<openstack-k8s-node>`. | Confirm OpenStack service node is Ready. | TODO: record sanitized output after approved execution. |
| V007 | Node role and label validation plan | Review node roles and labels for expected service runtime placement. | Confirm role and label consistency. | TODO: record sanitized output after approved execution. |
| V008 | Node condition validation plan | Review node conditions for pressure or readiness blockers. | Confirm no readiness-blocking conditions are present. | TODO: record sanitized output after approved execution. |
| V009 | Node resource capacity validation plan | Review node CPU, memory, and allocatable capacity. | Confirm capacity is visible and reviewable. | TODO: record sanitized output after approved execution. |
| V010 | Node version consistency validation plan | Review Kubernetes/k3s version values across nodes. | Confirm versions are consistent or documented. | TODO: record sanitized output after approved execution. |
| V011 | Failure condition for missing node, NotReady node, unreachable cluster, invalid context, or inconsistent node role | Review validation findings against failure criteria. | Confirm node readiness failures result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/kubernetes-node-readiness-summary.md`
- `configs/kubernetes-node-role-label-summary.md`
- `logs/kubernetes-node-readiness-validation.log`
- `screenshots/kubernetes-node-status.png`
