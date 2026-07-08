# Prerequisites

## Required Previous Scenarios

- S001-control-plane-toolchain-validation: confirms local toolchain planning.
- S008-bastion-reachability-validation: defines management access assumptions.
- S018-kubernetes-rbac-validation: defines RBAC assumptions for future Kubernetes runtime access where applicable.

## Required Tools or References

- Nginx syntax validation command planning capability, when future execution is approved.
- `curl` or equivalent HTTP header capture capability, when future execution is approved.
- Evidence model from `docs/evidence-model.md`.
- Placeholder naming rules from `docs/naming-rules.md`.

## Safety Preconditions

- Do not add TLS private keys, certificates, credentials, tfstate, kubeconfig content, or account-specific values.
- Do not record real public IPs.
- Do not implement Nginx or TLS configuration as part of this scenario skeleton.
