# Architecture

## Validation Flow

```text
Local PowerShell validator
  -> Kubernetes RBAC policy and rule matrix
  -> namespace and dedicated ServiceAccounts
  -> namespace-scoped Roles and RoleBindings
  -> privilege and sensitive-content checks
  -> evidence log and summary
```

## RBAC Model

- Application: dedicated account with limited configmap operations and deployment reads.
- Monitoring: dedicated account with read-only workload visibility.
- Binding: RoleBinding within `snsd-example`; no cluster-wide binding.
- Tokens: automatic token mounting disabled in examples.

## Trust Boundary

All inspection is repository-local; no kubeconfig, API server, cluster endpoint, credential, or external network participates.
