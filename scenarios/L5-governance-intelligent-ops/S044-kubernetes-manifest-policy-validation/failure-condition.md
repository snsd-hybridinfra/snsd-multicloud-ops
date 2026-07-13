# Failure Condition

The validator fails for missing controls/examples/evidence/mappings, incomplete exceptions, unsafe runtime claims, kubeconfig, real endpoints/registries/networks, credentials, certificates, keys, or secrets.

S044 fails or is blocked if any of the following occur:

- Manifest input artifact is missing.
- Image tag is `latest`.
- Resource requests or limits are missing.
- Privileged container mode is enabled.
- `hostNetwork`, `hostPID`, or `hostIPC` is enabled without justification.
- HostPath volume is used without justification.
- Secret values are embedded directly in a manifest.
- ConfigMap or Secret references are not documented.
- Ingress host or path mapping is ambiguous.
- RBAC is revalidated here instead of referenced to S018.
- Evidence is missing or cannot be mapped to validation checks.
- The scenario claims admission controller enforcement, OPA Gatekeeper, Kyverno, Conftest, Argo CD, GitOps, real-time blocking, automated remediation, or another unsupported enforcement path.
- kubeconfig, real Kubernetes secrets, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values are present.

If a failure is found, stop validation, preserve sanitized notes, and classify the manifest result as `MANIFEST_FAIL`, `MANIFEST_INCONCLUSIVE`, or `MANIFEST_NOT_APPLICABLE` as appropriate.
