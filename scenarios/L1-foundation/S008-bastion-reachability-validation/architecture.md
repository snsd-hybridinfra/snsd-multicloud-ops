# Architecture

## Relevant Components

- Management Zone: administrative source represented by `<management-node>`.
- Bastion Zone: controlled entry point represented by `<bastion-host>` and `<bastion-ip>`.
- On-Prem Internal Server Zone: internal service nodes represented by `<db-primary-ip>` and related placeholders.
- On-Prem Monitoring Zone: monitoring nodes represented by `<monitoring-node-ip>`.
- AWS Service Zone: AWS service nodes represented by `<aws-app-node-ip>`.
- Azure Service Zone: Azure service nodes represented by `<azure-app-node-ip>`.
- OpenStack Service Zone: OpenStack service nodes represented by `<openstack-app-node-ip>`.
- Evidence collection path: controlled route from operator to target through the bastion placeholder.

## Logical Flow

1. Management Zone reaches the Bastion Zone.
2. Bastion reaches on-prem internal DB nodes.
3. Bastion reaches on-prem monitoring nodes.
4. Bastion reaches AWS, Azure, and OpenStack service node placeholders.
5. SSH ProxyJump pattern describes future access without exposing credentials or keys.
6. Evidence collection paths follow the same bastion access model.

## Out-of-Scope Components

SSH hardening, firewall rule implementation, real host login, private key management, Ansible playbooks, and provider-specific secrets are not part of S008.
