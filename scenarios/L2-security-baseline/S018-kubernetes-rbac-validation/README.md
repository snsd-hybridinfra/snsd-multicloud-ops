# S018-kubernetes-rbac-validation

| Field | Value |
|---|---|
| Scenario ID | S018 |
| Scenario Name | Kubernetes RBAC Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Primary Domain | Kubernetes access security |
| Related Components | Kubernetes/k3s runtime, namespaces, ServiceAccounts, Roles, RoleBindings, Secrets, workload namespaces |
| Validation Type | Security Validation |
| Evidence Directory | evidence/L2-security-baseline/S018-kubernetes-rbac-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate the Kubernetes RBAC least privilege model for the SNSD Multi-Cloud Ops Kubernetes/k3s service runtime.

## Scope Summary

This scenario validates Kubernetes RBAC design only. It covers namespace separation, ServiceAccount separation, Role and RoleBinding review, least privilege workload access, read-only validation account placeholders, denial of unnecessary cluster-admin access, `kubectl auth can-i` checks, Secret access restrictions, workload namespace boundaries, and RBAC evidence collection.

## Validation Summary

Validation checks confirm that RBAC objects are defined with placeholder names, that allowed and denied actions can be tested, that Secret access is restricted, and that excessive permissions or cluster-admin misuse are treated as failures.

## Evidence Output Summary

Evidence must be recorded under `evidence/L2-security-baseline/S018-kubernetes-rbac-validation/`, with command plans in `commands.md`, validation results in `validation.md`, and future sanitized supporting artifacts under `configs/`, `logs/`, and `screenshots/`.
