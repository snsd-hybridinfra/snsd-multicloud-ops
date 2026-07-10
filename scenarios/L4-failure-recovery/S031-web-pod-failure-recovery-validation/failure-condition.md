# Failure Condition

This scenario is considered failed or blocked if:

- Pre-failure Web Deployment, Pod, or Service endpoint status cannot be established.
- Failure injection targets more than one Pod or uses a non-placeholder workload value in documentation.
- No replacement Web Pod is created.
- Replacement Pod remains `Pending`, `CrashLoopBackOff`, or not Ready.
- Web Service endpoint is missing after recovery.
- HTTP health endpoint does not recover.
- Recovery time exceeds the CRITICAL threshold.
- Recovery evidence is missing, unexplained, or not mapped to validation criteria.
- Real kubeconfig, Kubernetes secrets, credentials, private keys, tfstate, cloud account values, or account-specific values are introduced.
