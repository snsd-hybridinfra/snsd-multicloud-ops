# Prerequisites

## Required Previous Scenarios

- S001-control-plane-toolchain-validation: confirms `kubectl` planning.
- S007-multi-cloud-inventory-validation: defines placeholder Kubernetes node inventory.
- S008-bastion-reachability-validation: defines optional Bastion reachability path.
- S018-kubernetes-rbac-validation: defines RBAC separation assumptions for future cluster access.

## Required Tools or References

- `kubectl` command planning capability, when future execution is approved.
- Placeholder Kubernetes context reference such as `<cluster-context>`.
- Evidence model from `docs/evidence-model.md`.
- Placeholder naming rules from `docs/naming-rules.md`.

## Safety Preconditions

- Do not add kubeconfig files, Kubernetes Secrets, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values.
- Do not execute live Kubernetes changes as part of this scenario skeleton.
- Do not introduce EKS or AKS production-grade managed Kubernetes operations.
