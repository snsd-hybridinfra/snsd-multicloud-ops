# Architecture

## Relevant Components

- Control Plane: planned origin for `kubectl` node readiness checks.
- Bastion: optional management path for node reachability checks.
- Kubernetes/k3s runtime: target service runtime for node readiness validation.
- AWS service node: represented by `<aws-k8s-node>`.
- Azure service node: represented by `<azure-k8s-node>`.
- OpenStack service node: represented by `<openstack-k8s-node>`.
- Evidence directory: stores sanitized node readiness plans and future outputs.

## Readiness Model

- `kubectl` must be available before node readiness checks can run.
- `<cluster-context>` must identify the intended cluster context without storing kubeconfig content.
- Expected nodes must appear in `kubectl get nodes` output.
- Nodes must report Ready status.
- Roles, labels, conditions, capacity, and versions must be captured for review.
- Node reachability from the Control Plane or Bastion must be planned without recording real endpoints.

## Boundary Notes

This scenario validates node readiness only. Workload deployment, ingress routing, RBAC, manifest policy, and managed Kubernetes production operations are separate responsibilities.
