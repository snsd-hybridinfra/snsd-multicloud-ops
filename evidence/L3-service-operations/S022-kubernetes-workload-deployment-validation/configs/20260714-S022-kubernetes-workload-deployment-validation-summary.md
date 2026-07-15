# S022 Real-Lab Workload Deployment Validation Summary

| Field | Result |
|---|---|
| Evidence source | Pasted terminal output |
| Validation mode | Real lab evidence, sanitized |
| Namespace creation | PASS - the masked namespace was created and reported `Active` |
| Deployment creation | PASS - one masked Deployment was created and reported `2/2` ready, current, and available |
| ReplicaSet | PASS - desired, current, and ready replica counts were all `2` |
| Pod Running | PASS - two masked Pods reported `1/1 Running` with zero restarts |
| Service | PASS - one masked `ClusterIP` Service was present |
| Events | PASS - normal schedule, scale, create, pull, and start lifecycle events were observed |
| Sensitive data sanitization | PASS - user, host/node, namespace, workload, ReplicaSet/Pod identifiers, image, and all addresses are masked; unrelated image/DNS output and the password prompt were omitted |
| Raw output | Not committed |
| Kubeconfig, tokens, certificates, keys, passwords, and secrets | Not committed |
| Final judgment | **READY** |

## Judgment Basis

The Deployment existed with both desired replicas available, its ReplicaSet was
fully ready, and both observed Pods were `Running` and ready. The Service and
normal lifecycle events were also present. This satisfies the real-lab READY
criteria without retaining raw terminal output or sensitive cluster material.

## Evidence Reference

- `logs/20260714-S022-kubernetes-workload-deployment.sanitized.txt`
