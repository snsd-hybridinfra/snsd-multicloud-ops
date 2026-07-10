# Failure Condition

This scenario is considered failed or blocked if:

- Pre-failure API Deployment, Pod, or Service endpoint status cannot be established.
- API failure is not detected within the provisional detection threshold.
- API route unexpectedly succeeds during the planned failure state when failure should be visible.
- API health endpoint does not show failed or degraded status during failure.
- API Pod remains `CrashLoopBackOff`, `Pending`, or not Ready after restoration.
- API Service endpoint is missing after restoration.
- HTTP 5xx responses persist after recovery.
- Recovery time exceeds the CRITICAL threshold.
- Evidence is missing, unexplained, or not mapped to validation criteria.
- Real kubeconfig, Kubernetes secrets, credentials, private keys, tfstate, cloud account values, or account-specific values are introduced.
