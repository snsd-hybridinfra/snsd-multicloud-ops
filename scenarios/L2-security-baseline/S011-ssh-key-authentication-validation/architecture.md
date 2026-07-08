# Architecture

## Relevant Components

- Control Plane: source host for management access.
- Bastion: controlled SSH entry point represented by `<bastion-host>`.
- On-Prem DB node: target represented by `<db-primary-node>`.
- On-Prem Monitoring node: target represented by `<monitoring-node>`.
- AWS service node: target represented by `<aws-service-node>`.
- Azure service node: target represented by `<azure-service-node>`.
- OpenStack service node: target represented by `<openstack-service-node>`.
- SSH private key placeholder: `<ssh-private-key-path>`.
- SSH public key placement: target `authorized_keys` planning only.
- ProxyJump pattern: `ssh -J <bastion-user>@<bastion-host> <target-user>@<target-node>`.

## Logical Flow

1. Control Plane authenticates to Bastion using placeholder SSH key material.
2. Bastion authenticates to on-prem DB and monitoring targets using placeholder SSH key paths.
3. Bastion authenticates to AWS, Azure, and OpenStack service targets using placeholder SSH key paths.
4. ProxyJump pattern defines future indirect access from Control Plane through Bastion.
5. Evidence records commands and expected results without real key material.

## Out-of-Scope Components

Password authentication denial, root login denial, SSH hardening implementation beyond key-auth design, real private keys, real public IPs, and account-specific users are not part of S011.
