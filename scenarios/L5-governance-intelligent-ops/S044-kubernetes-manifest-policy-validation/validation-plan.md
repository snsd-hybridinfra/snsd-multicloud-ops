# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Manifest input artifact validation plan | Review `<manifest-file>` placeholder. | Manifest input is identified or marked missing. | `commands.md`, `configs/kubernetes-manifest-policy-summary.md`, `validation.md` |
| V002 | Namespace explicit definition validation plan | Review namespace placeholder. | Namespace is explicitly defined. | `commands.md`, `configs/kubernetes-manifest-control-mapping.md`, `validation.md` |
| V003 | Image tag not latest validation plan | Review `<container-image>` placeholder. | Image tag is pinned and not `latest`. | `configs/kubernetes-manifest-control-mapping.md`, `validation.md` |
| V004 | Resource requests validation plan | Review request placeholders. | CPU and memory requests are defined. | `configs/kubernetes-manifest-control-mapping.md`, `validation.md` |
| V005 | Resource limits validation plan | Review limit placeholders. | CPU and memory limits are defined. | `configs/kubernetes-manifest-control-mapping.md`, `validation.md` |
| V006 | Privileged container prohibition validation plan | Review security context placeholder. | Privileged mode is not enabled. | `configs/kubernetes-manifest-control-mapping.md`, `validation.md` |
| V007 | hostNetwork / hostPID / hostIPC restriction validation plan | Review host access placeholders. | Host namespace access is disabled or justified. | `configs/kubernetes-manifest-control-mapping.md`, `validation.md` |
| V008 | HostPath volume restriction validation plan | Review volume placeholders. | HostPath is absent or justified. | `configs/kubernetes-manifest-control-mapping.md`, `validation.md` |
| V009 | Embedded secret value prohibition validation plan | Review manifest placeholder for embedded secret values. | Secret values are not embedded directly. | `commands.md`, `configs/kubernetes-manifest-control-mapping.md`, `validation.md` |
| V010 | ConfigMap and Secret reference placeholder validation plan | Review ConfigMap and Secret reference placeholders. | References are documented without secret values. | `configs/kubernetes-manifest-control-mapping.md`, `validation.md` |
| V011 | Ingress host/path mapping validation plan | Review `<ingress-name>` host/path placeholders. | Ingress host and path mapping is documented. | `configs/kubernetes-manifest-control-mapping.md`, `validation.md` |
| V012 | RBAC dependency reference validation plan | Reference S018 boundary. | RBAC dependency is referenced but not revalidated. | `configs/kubernetes-manifest-policy-summary.md`, `validation.md` |
| V013 | Manifest judgment state validation plan | Apply manifest judgment states. | Result is classified as `MANIFEST_PASS`, `MANIFEST_FAIL`, `MANIFEST_WARNING`, `MANIFEST_NOT_APPLICABLE`, or `MANIFEST_INCONCLUSIVE`. | `configs/kubernetes-manifest-judgment-model.md`, `validation.md` |
| V014 | Failure condition for missing manifest, latest image tag, missing resource limits, privileged container, embedded secret, unrestricted host access, unjustified HostPath volume, unsupported enforcement claim, or missing evidence | Evaluate findings against explicit failure conditions. | Manifest policy issues produce `FAIL` or `BLOCKED` status. | `validation.md`, `logs/kubernetes-manifest-policy-validation.log`, `screenshots/kubernetes-manifest-policy-result.png`, `screenshots/kubernetes-manifest-policy-failure-example.png` |

Every validation item must map to evidence. This scenario validates manifest policy through static review only.
