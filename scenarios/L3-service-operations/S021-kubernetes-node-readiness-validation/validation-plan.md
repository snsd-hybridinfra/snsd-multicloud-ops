# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | kubectl client availability validation plan | Document planned `kubectl version --client` or approved equivalent. | `kubectl` client is available for future node readiness checks. | `commands.md`, `logs/kubernetes-node-readiness-validation.log`, `validation.md` |
| V002 | Kubernetes context availability validation plan | Document planned context check for `<cluster-context>`. | Intended context is available without storing kubeconfig content. | `commands.md`, `configs/kubernetes-node-readiness-summary.md`, `validation.md` |
| V003 | kubectl get nodes validation plan | Plan `kubectl get nodes` against `<cluster-context>`. | Expected Kubernetes/k3s nodes are listed. | `commands.md`, `logs/kubernetes-node-readiness-validation.log`, `screenshots/kubernetes-node-status.png`, `validation.md` |
| V004 | AWS Kubernetes/k3s node Ready status validation plan | Review Ready status for `<aws-k8s-node>`. | AWS service node reports Ready. | `commands.md`, `configs/kubernetes-node-readiness-summary.md`, `validation.md` |
| V005 | Azure Kubernetes/k3s node Ready status validation plan | Review Ready status for `<azure-k8s-node>`. | Azure service node reports Ready. | `commands.md`, `configs/kubernetes-node-readiness-summary.md`, `validation.md` |
| V006 | OpenStack Kubernetes/k3s node Ready status validation plan | Review Ready status for `<openstack-k8s-node>`. | OpenStack service node reports Ready. | `commands.md`, `configs/kubernetes-node-readiness-summary.md`, `validation.md` |
| V007 | Node role and label validation plan | Review roles and labels for expected node functions. | Node roles and labels are consistent with service runtime expectations. | `commands.md`, `configs/kubernetes-node-role-label-summary.md`, `validation.md` |
| V008 | Node condition validation plan | Review node conditions for pressure or availability issues. | Node conditions do not show readiness blockers. | `commands.md`, `logs/kubernetes-node-readiness-validation.log`, `validation.md` |
| V009 | Node resource capacity validation plan | Review CPU, memory, and allocatable capacity summary. | Node capacity is visible and reviewable. | `commands.md`, `configs/kubernetes-node-readiness-summary.md`, `validation.md` |
| V010 | Node version consistency validation plan | Review node Kubernetes/k3s version values. | Node versions are consistent or documented. | `commands.md`, `configs/kubernetes-node-readiness-summary.md`, `validation.md` |
| V011 | Failure condition for missing node, NotReady node, unreachable cluster, invalid context, or inconsistent node role | Evaluate findings against explicit failure conditions. | Node readiness failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates node readiness only; workload deployment is handled in S022, ingress routing in S023, RBAC in S018, and manifest policy in S044.
