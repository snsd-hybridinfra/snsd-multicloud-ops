# Kubernetes Manifest Policy Criteria

| Policy Area | Manifest Field | Expected Condition | Violation Condition | Severity | Exception Requirement | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|---|
| Privileged container | privileged | false | true | Critical | Not allowed | retired-numbered-case | `<evidence-path>` |
| Privilege escalation | allowPrivilegeEscalation | false | true | High | Not allowed | retired-numbered-case | `<evidence-path>` |
| Run as root | runAsNonRoot/runAsUser | true/nonzero | zero | High | Full fields | retired-numbered-case | `<evidence-path>` |
| Read-only root filesystem | readOnlyRootFilesystem | true | false | Medium | Full fields | retired-numbered-case | `<evidence-path>` |
| Resource requests | resources.requests | present | missing | High | Not allowed | retired-numbered-case/retired-numbered-case | `<evidence-path>` |
| Resource limits | resources.limits | present | missing | High | Not allowed | retired-numbered-case/retired-numbered-case | `<evidence-path>` |
| Liveness probe | livenessProbe | present | missing | Medium | Full fields | retired-numbered-case | `<evidence-path>` |
| Readiness probe | readinessProbe | present | missing | Medium | Full fields | retired-numbered-case | `<evidence-path>` |
| Image tag latest | image | explicit placeholder | latest | High | Not allowed | retired-numbered-case | `<evidence-path>` |
| Private registry placeholder | image | approved placeholder/digest | unknown private registry | High | Full fields | retired-numbered-case | `<evidence-path>` |
| hostNetwork | hostNetwork | false | true | Critical | Not allowed | retired-numbered-case | `<evidence-path>` |
| hostPID | hostPID | false | true | Critical | Not allowed | retired-numbered-case | `<evidence-path>` |
| hostIPC | hostIPC | false | true | Critical | Not allowed | retired-numbered-case | `<evidence-path>` |
| hostPath volume | volumes | absent | hostPath | High | Full fields | retired-numbered-case | `<evidence-path>` |
| Service exposure | spec.type | ClusterIP | NodePort/LoadBalancer | High | Full fields | retired-numbered-case | `<evidence-path>` |
| Secret handling | env/value | references only | hardcoded | Critical | Not allowed | retired-numbered-case | `<evidence-path>` |
| ConfigMap secret-like value | data | nonsecret only | secret-like | Critical | Not allowed | retired-numbered-case | `<evidence-path>` |
| RBAC boundary reference | Role rules | delegated | wildcard | High | retired-numbered-case | retired-numbered-case | `<evidence-path>` |
