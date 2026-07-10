# Scope

## Included

- Pre-failure API Deployment status validation plan.
- Pre-failure API Pod Ready status validation plan.
- Pre-failure API Service endpoint validation plan.
- API failure injection plan using placeholder commands.
- API route failure response validation plan.
- API health endpoint failure validation plan.
- Ingress API path failure validation plan.
- Nginx Reverse Proxy API forwarding validation reference.
- Blackbox API probe failure validation reference.
- Prometheus target or probe metric reference.
- API workload restoration validation plan.
- API health recovery validation plan.
- Recovery time measurement plan.

## Failure Injection Scope

- Simulate API workload failure using placeholder commands only.
- Validate API route failure behavior.
- Validate failed or degraded health response.
- Validate recovery after rollback or workload restoration.
- Capture before, failure, and after state evidence using TODO placeholders.

## Failure and Recovery Threshold Model

- DETECTED: API failure visible within `< 60 seconds`.
- WARNING: recovery within `60-180 seconds`.
- CRITICAL: recovery failed or exceeds `180 seconds`.

These are provisional validation thresholds and must be replaced only when an approved operational threshold is documented.

## Excluded

- Real Kubernetes manifest implementation.
- Real kubeconfig files, Kubernetes secrets, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values.
- Kubernetes workload deployment validation, which is handled in S022.
- Ingress routing validation, which is handled in S023.
- Nginx Reverse Proxy forwarding validation, which is handled in S024.
- Load balancing health check validation, which is handled in S025.
- Blackbox endpoint probe validation, which is handled in S030.
- Web Pod failure recovery validation, which is handled in S031.
- Full GitOps, Argo CD, service mesh, and automatic cross-cloud failover.
- Changes outside this scenario directory, its matching evidence directory, and the required tracking documents.
