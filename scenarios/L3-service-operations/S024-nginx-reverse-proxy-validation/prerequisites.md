# Prerequisites

## Required Previous Scenarios

- S001-control-plane-toolchain-validation: confirms local command planning.
- S008-bastion-reachability-validation: defines management path assumptions.
- S019-nginx-security-header-validation: defines security header validation separately.
- S023-ingress-routing-validation: defines Kubernetes Ingress routing assumptions.

## Required Tools or References

- Nginx service status and syntax validation command planning, when future execution is approved.
- HTTP response capture capability, when future execution is approved.
- Evidence model from `docs/evidence-model.md`.
- Placeholder naming rules from `docs/naming-rules.md`.

## Safety Preconditions

- Do not add TLS private keys, certificates, credentials, secrets, private keys, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.
- Do not record real public IPs.
- Do not implement Nginx, TLS, ingress, or load balancing configuration as part of this scenario skeleton.
