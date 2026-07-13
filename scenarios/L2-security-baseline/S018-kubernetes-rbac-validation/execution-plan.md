# Execution Plan

1. Run `tools/validate-kubernetes-rbac-baseline.ps1` from the repository root.
2. Confirm the baseline, matrix, example directory, and required files.
3. Validate policy subjects and top-level YAML resource kinds file by file.
4. Reject ClusterRoleBinding, cluster-admin, wildcard permission, default ServiceAccount, and application secrets access.
5. Confirm monitoring verbs are limited to get, list, and watch.
6. Reject kubeconfig, token, certificate, key, Secret, endpoint, address, or account-specific content.
7. Confirm the validator contains no kubectl, Helm, API, or network command and inspect generated evidence.

## Execution Boundary

The script does not run kubectl, read kubeconfig, connect to a cluster, query an API server, apply manifests, or create resources.
