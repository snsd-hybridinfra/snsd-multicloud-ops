# Architecture

Implemented flow: sanitized rules/manifests/evidence -> `validate-kubernetes-manifest-policy.ps1` -> local log/summary, with no cluster or engine edge.

S044 models manifest policy validation as a static review workflow.

## Components

- Namespace placeholder: `<namespace>`.
- Manifest file placeholder: `<manifest-file>`.
- Deployment placeholder: `<deployment-name>`.
- Service placeholder: `<service-name>`.
- Ingress placeholder: `<ingress-name>`.
- Container image placeholder: `<container-image>`.
- Policy result placeholder: `<policy-result>`.
- Evidence directory: `evidence/L5-governance-intelligent-ops/S044-kubernetes-manifest-policy-validation/`.

## Flow

1. Identify manifest input artifacts using placeholders.
2. Map each manifest type to the relevant baseline controls.
3. Review namespace, image tag, resource request, resource limit, privileged mode, host access, HostPath, secret, ConfigMap, Ingress, and RBAC reference controls.
4. Classify each result using the Manifest Policy Judgment Model.
5. Capture TODO evidence references in commands, validation notes, configs, logs, and screenshots.

This architecture does not create manifests, run Kubernetes commands, use kubeconfig, or enforce admission policies.
