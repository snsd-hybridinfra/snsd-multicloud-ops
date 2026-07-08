# Prerequisites

## Required Previous Scenarios

- S001-control-plane-toolchain-validation: confirms `kubectl` planning.
- S018-kubernetes-rbac-validation: defines RBAC separation assumptions.
- S021-kubernetes-node-readiness-validation: defines node readiness assumptions.

## Required Tools or References

- `kubectl` command planning capability, when future execution is approved.
- Placeholder workload names and image references.
- Evidence model from `docs/evidence-model.md`.
- Placeholder naming rules from `docs/naming-rules.md`.

## Safety Preconditions

- Do not add kubeconfig files, Kubernetes Secrets, private registry credentials, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values.
- Do not execute live Kubernetes changes as part of this scenario skeleton.
- Do not introduce service mesh, Istio, Argo CD, or full GitOps scope.
