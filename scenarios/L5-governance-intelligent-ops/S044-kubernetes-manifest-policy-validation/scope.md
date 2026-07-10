# Scope

## Included

- Deployment manifest policy validation placeholder.
- Service manifest policy validation placeholder.
- Ingress manifest policy validation placeholder.
- Namespace manifest policy validation placeholder.
- Resource requests and limits policy validation.
- Image tag policy validation.
- Privileged container prohibition validation.
- HostPath volume usage restriction validation.
- Secret reference validation placeholder.
- Namespace boundary validation reference.
- Manifest evidence collection plan.

## Target Manifest Categories

- Namespace manifests.
- Web Deployment manifest.
- API Deployment manifest.
- Kubernetes Service manifest.
- Ingress manifest.
- ConfigMap placeholder.
- Secret reference placeholder.
- RBAC object reference placeholder.

## Required Manifest Policy Checks

- Namespace is explicitly defined.
- Image tag is not `latest`.
- Resource requests are defined.
- Resource limits are defined.
- Privileged container is not enabled.
- `hostNetwork` is not enabled unless justified.
- `hostPID` and `hostIPC` are not enabled unless justified.
- HostPath volume is not used unless justified.
- Secret values are not embedded directly in manifest.
- ConfigMap and Secret references are documented as placeholders.
- Ingress host and path mapping is documented.
- RBAC dependency is referenced but not revalidated here.

## Manifest Policy Judgment Model

- `MANIFEST_PASS`: Manifest satisfies the defined baseline.
- `MANIFEST_FAIL`: Manifest violates one or more required controls.
- `MANIFEST_WARNING`: Manifest is acceptable but requires review.
- `MANIFEST_NOT_APPLICABLE`: Policy does not apply to this manifest type.
- `MANIFEST_INCONCLUSIVE`: Required manifest or evidence is missing.

## Excluded

- Real Kubernetes manifest implementation.
- kubeconfig files, real Kubernetes secrets, private registry credentials, cloud account values, subscription IDs, tenant IDs, tfstate, private keys, credentials, or account-specific values.
- New policy tools or technologies.
- Admission controller enforcement.
- OPA Gatekeeper, Kyverno, Conftest, Argo CD, GitOps, service mesh, Istio, real-time blocking, or automated remediation.
- Kubernetes RBAC validation, handled in S018.
- Kubernetes node readiness validation, handled in S021.
- Kubernetes workload deployment validation, handled in S022.
- Ingress routing validation, handled in S023.
- General Policy as Code validation, handled in S043.
