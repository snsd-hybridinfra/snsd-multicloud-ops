# Scope

## Included

- `sshd_config` `PermitRootLogin` setting validation plan.
- `sshd -T` effective configuration validation plan.
- Bastion root login denial validation plan.
- On-Prem DB node root login denial validation plan.
- On-Prem Monitoring node root login denial validation plan.
- AWS service node root login denial validation plan.
- Azure service node root login denial validation plan.
- OpenStack service node root login denial validation plan.
- Authentication failure log capture plan.
- Failure condition for `PermitRootLogin` enabled, root login success, missing sshd config, or missing failure evidence.

## Excluded

- SSH key authentication success validation, which is handled in S011.
- Password login denial validation, which is handled in S012.
- Sudo policy validation.
- Creating real SSH private keys.
- Storing passwords, credentials, private keys, public IPs, cloud account values, subscription IDs, tenant IDs, tfstate, kubeconfig files, or account-specific files.
- Real Ansible automation implementation.
- Terraform, Kubernetes, monitoring, ML, backup, or cloud provisioning logic.

## Assumptions

- Use placeholders such as `<bastion-host>`, `<target-node>`, and `<target-user>`.
- Privileged administration must use a non-root account with sudo, but sudo policy validation is outside this scenario.
- Future execution requires explicit approval before any real SSH authentication test.
