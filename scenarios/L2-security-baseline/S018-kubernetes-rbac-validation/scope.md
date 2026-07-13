# Scope

## Included

- RBAC least-privilege policy and subject matrix validation.
- Namespace, dedicated ServiceAccount, Role, and RoleBinding example inspection.
- ClusterRoleBinding, cluster-admin, wildcard, default ServiceAccount, application secrets, and monitoring write-verb denial.
- Kubeconfig, token, certificate, private-key, Secret resource, endpoint, and address safety checks.
- Safe local evidence generation.

## Excluded

- Cluster connections, kubectl, Helm, API queries, or manifest application.
- Real cluster configuration, kubeconfig, tokens, certificates, namespace secrets, or endpoints.
- Node readiness (S021), workload deployment (S022), manifest policy (S044), Prometheus/Grafana (S028/S029), and cloud network access controls (S014-S016).
