# Failure Condition

S022 fails if Kubernetes/k3s workload deployment state cannot be validated or expected workload objects are unhealthy.

## Failure Conditions

- `<namespace>` is missing.
- `<web-deployment>` is missing.
- `<api-deployment>` is missing.
- Deployment rollout fails or times out.
- Pods are not Running or not Ready.
- Pods enter CrashLoopBackOff, ImagePullBackOff, or another unresolved error state.
- Available replicas do not match desired replicas.
- `<web-service>` or `<api-service>` is missing.
- Required ConfigMap reference is missing.
- Secret template reference is missing where required, or real Secret values are stored.
- Resource requests or limits are missing.
- Container image tag uses `latest`.
- Evidence contains kubeconfig files, Kubernetes Secrets, private registry credentials, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder workload model exists.
- Future `kubectl` workload output is unavailable.
- Required evidence files are missing.
