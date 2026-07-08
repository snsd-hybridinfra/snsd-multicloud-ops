# Validation

Scenario: S018-kubernetes-rbac-validation
Level: L2-security-baseline
Capability: Kubernetes RBAC Least Privilege Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real Kubernetes RBAC output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Namespace existence validation plan | Required namespaces are identifiable by placeholder name. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-rbac-summary.md` |
| V002 | ServiceAccount existence validation plan | Required ServiceAccounts are identifiable by placeholder name. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-rbac-summary.md` |
| V003 | Role existence validation plan | Required Roles are identifiable and namespace-scoped. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-rbac-policy.md` |
| V004 | RoleBinding existence validation plan | Required RoleBindings bind intended ServiceAccounts to intended Roles. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-rbac-policy.md` |
| V005 | kubectl auth can-i allowed action validation plan | Required actions are allowed only for intended subjects. | TODO | NOT_RUN | `commands.md`; `logs/kubernetes-rbac-validation.log` |
| V006 | kubectl auth can-i denied action validation plan | Unnecessary actions are denied. | TODO | NOT_RUN | `commands.md`; `logs/kubernetes-rbac-validation.log` |
| V007 | No unnecessary cluster-admin binding validation plan | Application workloads and read-only validation accounts do not use cluster-admin. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-rbac-policy.md` |
| V008 | Secret read permission restriction validation plan | Secret read access is denied unless explicitly required and documented. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-rbac-policy.md` |
| V009 | Workload namespace boundary validation plan | Workload access is constrained to the intended namespace. | TODO | NOT_RUN | `commands.md`; `logs/kubernetes-rbac-validation.log`; `screenshots/kubernetes-rbac-validation.png` |
| V010 | Failure condition for missing RBAC objects, excessive permissions, cluster-admin misuse, unrestricted secret access, or namespace boundary violation | Unsafe RBAC patterns produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Kubernetes RBAC summary is captured: NOT_READY
- Kubernetes RBAC policy is captured: NOT_READY
- Kubernetes RBAC validation log is captured: NOT_READY
- Kubernetes RBAC screenshot is captured: NOT_READY

## Notes

This scenario validates Kubernetes RBAC least privilege design only. Kubernetes workload deployment validation is handled in S022, and Kubernetes manifest policy validation is handled in S044. Service mesh, Istio, Argo CD, and full GitOps are excluded from v1 scope.
