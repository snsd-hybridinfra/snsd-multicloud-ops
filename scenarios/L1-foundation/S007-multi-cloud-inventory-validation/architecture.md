# Architecture

## Relevant Components

- `aws_nodes`: AWS service node placeholders such as `<aws-app-node-ip>`.
- `azure_nodes`: Azure service node placeholders such as `<azure-app-node-ip>`.
- `openstack_nodes`: OpenStack service node placeholders such as `<openstack-app-node-ip>`.
- `eve_ng_network`: EVE-NG router, firewall, and switch placeholders.
- `onprem_bastion`: on-prem bastion placeholder such as `<bastion-node-ip>`.
- `onprem_db_primary`: primary database placeholder such as `<db-primary-ip>`.
- `onprem_db_replicas`: database replica placeholders such as `<db-replica-01-ip>`.
- `onprem_monitoring`: monitoring node placeholders such as `<monitoring-node-ip>`.
- `kubernetes_nodes`: Kubernetes service node placeholders such as `<k8s-node-01-ip>`.
- `observability_targets`: exporter and metrics endpoint placeholders.
- `evidence_targets`: systems from which validation evidence may be collected.

## Logical Flow

1. Inventory groups separate provider domains.
2. Host variables identify zone, role, and validation target using sanitized values.
3. On-prem DB groups distinguish primary and replica roles.
4. Observability targets identify scrape or probe targets without real endpoint data.
5. Evidence targets identify approved collection points for future scenario outputs.

## Out-of-Scope Components

No real Ansible playbooks, SSH keys, host credentials, kubeconfig files, public IPs, private IPs, tfstate files, or account-specific values are used by this scenario.
