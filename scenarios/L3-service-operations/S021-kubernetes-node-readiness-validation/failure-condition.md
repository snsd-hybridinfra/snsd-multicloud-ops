# Failure Condition

S021 fails if Kubernetes/k3s node readiness cannot be verified or the node model is inconsistent.

## Failure Conditions

- `kubectl` client is unavailable for planned validation.
- `<cluster-context>` is missing, invalid, or cannot be selected.
- Cluster is unreachable from the Control Plane or approved management path.
- Expected node is missing from `kubectl get nodes` output.
- `<aws-k8s-node>`, `<azure-k8s-node>`, or `<openstack-k8s-node>` reports NotReady.
- Node roles or labels are missing, inconsistent, or do not match the expected service runtime model.
- Node conditions report readiness blockers such as pressure, unavailable runtime, or scheduling issues.
- Node capacity cannot be reviewed.
- Node version inconsistency is unexplained.
- Evidence contains kubeconfig files, Kubernetes Secrets, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder node model exists.
- Future `kubectl` output is unavailable.
- Required evidence files are missing.
