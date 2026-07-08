# Scope

## Included

- Bastion inventory entry validation plan.
- Management Zone to Bastion Zone reachability plan.
- Bastion SSH reachability plan using placeholder command patterns.
- Bastion to On-Prem DB node reachability plan.
- Bastion to On-Prem Monitoring node reachability plan.
- Bastion to AWS service node reachability plan.
- Bastion to Azure service node reachability plan.
- Bastion to OpenStack service node reachability plan.
- SSH ProxyJump command pattern validation plan.
- Evidence collection through Bastion path validation plan.
- Failure condition for unreachable Bastion, missing route, blocked SSH, or invalid inventory entry.

## Excluded

- Real Ansible automation implementation.
- SSH hardening implementation.
- SSH key generation or storage.
- Real public IPs, private IPs, credentials, SSH private keys, public cloud account IDs, subscription IDs, tenant IDs, provider-specific secrets, tfstate, kubeconfig files, or account-specific files.
- Live host connectivity checks.
- Terraform, Kubernetes, monitoring, ML, backup, or cloud provisioning logic.

## Assumptions

- All addresses and hostnames use placeholders such as `<bastion-ip>`, `<db-primary-ip>`, `<aws-app-node-ip>`, `<azure-app-node-ip>`, and `<openstack-app-node-ip>`.
- SSH hardening belongs to L2 scenarios and is not implemented here.
- Future reachability execution requires explicit approval before connecting to any real host.
