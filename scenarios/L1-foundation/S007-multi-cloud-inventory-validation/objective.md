# Objective

Validate the planned multi-cloud inventory model for managing AWS, Azure, OpenStack, EVE-NG, and on-prem nodes.

The inventory model must support:

- AWS service nodes
- Azure service nodes
- OpenStack service nodes
- EVE-NG network devices
- On-Prem bastion node
- On-Prem internal DB nodes
- On-Prem monitoring nodes
- Kubernetes service nodes
- Exporter targets
- Evidence collection targets

Success means all required groups are documented, provider and role boundaries are clear, placeholders are used consistently, and the inventory is suitable for future Ansible validation tasks without adding real credentials, private keys, public IPs, or account-specific values.
