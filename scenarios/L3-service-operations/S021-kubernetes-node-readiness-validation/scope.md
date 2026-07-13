# Scope

## Included

- Node readiness purpose, Ready/NotReady behavior, kubelet signal, role placeholders, and scheduling awareness.
- Static parsing of non-production `kubectl get nodes`-style evidence.
- Optional explicit `-LiveKubectl` read-only node listing.
- Credential-file, endpoint, address, secret-content, and mutation-command safety checks.
- Sanitized evidence generation.

## Excluded

- Default-mode kubectl execution or any implicit cluster access.
- Apply, delete, patch, cordon, drain, taint, edit, or other resource mutation.
- Kubeconfig, tokens, certificates, secrets, endpoints, node addresses, or raw live rows in evidence.
- Workload deployment (S022), ingress routing (S023), RBAC (S018), and manifest policy (S044).
