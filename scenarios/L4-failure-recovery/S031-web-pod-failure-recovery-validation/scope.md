# Scope

## Included

- Pre-failure Web Deployment status validation plan.
- Pre-failure Web Pod Ready status validation plan.
- Pre-failure Web Service endpoint validation plan.
- Manual Web Pod delete failure injection plan using placeholders.
- Deployment/ReplicaSet replacement behavior validation plan.
- Replacement Pod creation validation plan.
- Web Pod Ready recovery validation plan.
- Service endpoint recovery validation plan.
- HTTP health endpoint recovery validation plan.
- Recovery time evidence collection plan.
- Post-recovery workload status validation plan.

## Failure Injection Scope

- Delete one Web Pod manually using a placeholder `kubectl` command.
- Observe Deployment/ReplicaSet replacement behavior.
- Validate that the Service endpoint remains available or recovers within a provisional threshold.
- Capture before, failure, and after state evidence using TODO placeholders.

## Recovery Threshold Model

- NORMAL: recovery within `< 60 seconds`.
- WARNING: recovery within `60-180 seconds`.
- CRITICAL: recovery failed or exceeds `180 seconds`.

These are provisional validation thresholds and must be replaced only when an approved operational threshold is documented.

## Excluded

- Real Kubernetes manifest implementation.
- Real kubeconfig files, Kubernetes secrets, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values.
- Kubernetes workload deployment validation, which is handled in S022.
- Ingress routing validation, which is handled in S023.
- Load balancing health check validation, which is handled in S025.
- Blackbox endpoint probe validation, which is handled in S030.
- API service failure validation, which is handled in S032.
- Kubernetes manifest policy validation, which is handled in S044.
- Full GitOps, Argo CD, service mesh, and automatic cross-cloud failover.
- Changes outside this scenario directory, its matching evidence directory, and the required tracking documents.
