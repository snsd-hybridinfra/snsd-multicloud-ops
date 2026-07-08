# Prerequisites

## Required Previous Scenarios

- S001-control-plane-toolchain-validation: confirms local command planning.
- S018-kubernetes-rbac-validation: defines access separation assumptions.
- S021-kubernetes-node-readiness-validation: defines node readiness assumptions.
- S022-kubernetes-workload-deployment-validation: defines workload and Service object assumptions.

## Required Tools or References

- `kubectl` command planning capability, when future execution is approved.
- HTTP response capture capability, when future execution is approved.
- Evidence model from `docs/evidence-model.md`.
- Placeholder naming rules from `docs/naming-rules.md`.

## Safety Preconditions

- Do not add kubeconfig files, Kubernetes Secrets, TLS private keys, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values.
- Do not record real public IPs or real DNS records.
- Do not implement TLS, ingress manifests, or load balancing behavior as part of this scenario skeleton.
