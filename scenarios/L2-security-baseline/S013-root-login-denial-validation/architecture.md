# Architecture

## Relevant Components

- Bastion host: root login denial target represented by `<bastion-host>`.
- On-Prem DB node: root login denial target represented by `<db-primary-node>`.
- On-Prem Monitoring node: root login denial target represented by `<monitoring-node>`.
- AWS service node: root login denial target represented by `<aws-service-node>`.
- Azure service node: root login denial target represented by `<azure-service-node>`.
- OpenStack service node: root login denial target represented by `<openstack-service-node>`.
- `sshd_config`: planned source configuration review.
- `sshd -T`: planned effective configuration review.
- Authentication failure logs: planned evidence for denied direct root login.

## Logical Flow

1. Static SSH daemon configuration is reviewed for `PermitRootLogin`.
2. Effective SSH daemon configuration is reviewed using `sshd -T`.
3. Direct root login denial is planned for Bastion, on-prem, and cloud service nodes.
4. Failure logs are planned as supporting evidence.
5. Results are recorded without passwords, credentials, private keys, or real hosts.

## Out-of-Scope Components

SSH key authentication success, password login denial, sudo policy validation, key generation, private key handling, and account-specific usernames are not part of S013.
