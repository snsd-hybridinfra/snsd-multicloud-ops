# Commands

Scenario: S044-kubernetes-manifest-policy-validation
Level: L5-governance-intelligent-ops
Capability: Kubernetes Manifest Policy Validation

Record approved commands or manual review actions used during validation. Do not include real manifest validation output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Review Records

| Check ID | Purpose | Planned Review Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Validate manifest input artifact placeholder. | Review `<manifest-file>` placeholder | `<manifest-file>` | `configs/kubernetes-manifest-policy-summary.md` |
| V002 | Validate explicit namespace definition. | Review `<namespace>` placeholder in manifest | `<namespace>` | `configs/kubernetes-manifest-control-mapping.md` |
| V003 | Validate image tag is not latest. | Review `<container-image>` placeholder | `<deployment-name>` | `configs/kubernetes-manifest-control-mapping.md` |
| V004 | Validate resource requests. | Review CPU and memory request placeholders | `<deployment-name>` | `configs/kubernetes-manifest-control-mapping.md` |
| V005 | Validate resource limits. | Review CPU and memory limit placeholders | `<deployment-name>` | `configs/kubernetes-manifest-control-mapping.md` |
| V006 | Validate privileged container prohibition. | Review security context placeholder | `<deployment-name>` | `configs/kubernetes-manifest-control-mapping.md` |
| V007 | Validate host namespace restrictions. | Review `hostNetwork`, `hostPID`, and `hostIPC` placeholders | `<deployment-name>` | `configs/kubernetes-manifest-control-mapping.md` |
| V008 | Validate HostPath volume restriction. | Review volume placeholders | `<deployment-name>` | `configs/kubernetes-manifest-control-mapping.md` |
| V009 | Validate embedded secret prohibition. | Review manifest placeholder for direct secret values | `<manifest-file>` | `configs/kubernetes-manifest-control-mapping.md` |
| V010 | Validate ConfigMap and Secret references. | Review placeholder references without secret values | ConfigMap and Secret placeholders | `configs/kubernetes-manifest-control-mapping.md` |
| V011 | Validate Ingress host/path mapping. | Review `<ingress-name>` host and path placeholders | `<ingress-name>` | `configs/kubernetes-manifest-control-mapping.md` |
| V012 | Validate RBAC dependency reference. | Confirm RBAC is referenced to S018 only | RBAC placeholder | `configs/kubernetes-manifest-policy-summary.md` |
| V013 | Apply manifest judgment state. | Classify result as `MANIFEST_PASS`, `MANIFEST_FAIL`, `MANIFEST_WARNING`, `MANIFEST_NOT_APPLICABLE`, or `MANIFEST_INCONCLUSIVE` | `<policy-result>` | `configs/kubernetes-manifest-judgment-model.md` |

## Manifest Judgment Placeholder

```text
Namespace: <namespace>
Manifest file: <manifest-file>
Deployment name: <deployment-name>
Service name: <service-name>
Ingress name: <ingress-name>
Container image: <container-image>
Policy result: <policy-result>
Judgment: TODO (MANIFEST_PASS | MANIFEST_FAIL | MANIFEST_WARNING | MANIFEST_NOT_APPLICABLE | MANIFEST_INCONCLUSIVE)
Reviewer: TODO
Timestamp: TODO
```

## Output Placeholder

```text
TODO: Paste sanitized manifest policy review summaries or manual validation notes here after approval.
TODO: Do not paste kubeconfig content, real Kubernetes secrets, private registry credentials, tfstate content, cloud account values, subscription IDs, tenant IDs, private keys, public IPs, or account-specific values.
```
