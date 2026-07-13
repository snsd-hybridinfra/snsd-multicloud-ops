# Evidence Map

Implemented mapping: `V001`-`V015` map to required artifacts, command reference, rule set, four manifest examples, six evidence samples, manifest config, generated log, validator source, and generated summary.

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Manifest input artifact validation plan | `commands.md`; `configs/kubernetes-manifest-policy-summary.md`; `validation.md` | review plan, policy summary, validation record | yes |
| Namespace explicit definition validation plan | `commands.md`; `configs/kubernetes-manifest-control-mapping.md`; `validation.md` | review plan, control mapping, validation record | yes |
| Image tag not latest validation plan | `configs/kubernetes-manifest-control-mapping.md`; `validation.md` | control mapping, validation record | yes |
| Resource requests validation plan | `configs/kubernetes-manifest-control-mapping.md`; `validation.md` | control mapping, validation record | yes |
| Resource limits validation plan | `configs/kubernetes-manifest-control-mapping.md`; `validation.md` | control mapping, validation record | yes |
| Privileged container prohibition validation plan | `configs/kubernetes-manifest-control-mapping.md`; `validation.md` | control mapping, validation record | yes |
| hostNetwork / hostPID / hostIPC restriction validation plan | `configs/kubernetes-manifest-control-mapping.md`; `validation.md` | control mapping, validation record | yes |
| HostPath volume restriction validation plan | `configs/kubernetes-manifest-control-mapping.md`; `validation.md` | control mapping, validation record | yes |
| Embedded secret value prohibition validation plan | `commands.md`; `configs/kubernetes-manifest-control-mapping.md`; `validation.md` | review plan, control mapping, validation record | yes |
| ConfigMap and Secret reference placeholder validation plan | `configs/kubernetes-manifest-control-mapping.md`; `validation.md` | control mapping, validation record | yes |
| Ingress host/path mapping validation plan | `configs/kubernetes-manifest-control-mapping.md`; `validation.md` | control mapping, validation record | yes |
| RBAC dependency reference validation plan | `configs/kubernetes-manifest-policy-summary.md`; `validation.md` | policy summary, validation record | yes |
| Manifest judgment state validation plan | `configs/kubernetes-manifest-judgment-model.md`; `validation.md` | judgment model, validation record | yes |
| Failure condition for missing manifest, latest image tag, missing resource limits, privileged container, embedded secret, unrestricted host access, unjustified HostPath volume, unsupported enforcement claim, or missing evidence | `validation.md`; `logs/kubernetes-manifest-policy-validation.log`; `screenshots/kubernetes-manifest-policy-result.png`; `screenshots/kubernetes-manifest-policy-failure-example.png` | failure criteria, validation log, screenshot reference | yes |

No real manifest validation output has been collected. Use TODO placeholders until execution is approved and outputs are sanitized.
