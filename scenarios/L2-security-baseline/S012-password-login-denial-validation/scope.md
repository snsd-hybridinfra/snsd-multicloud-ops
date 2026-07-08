# Scope

## Included

- `sshd_config` `PasswordAuthentication` setting validation plan.
- `sshd -T` effective configuration validation plan.
- Bastion password login denial validation plan.
- On-Prem DB node password login denial validation plan.
- On-Prem Monitoring node password login denial validation plan.
- AWS service node password login denial validation plan.
- Azure service node password login denial validation plan.
- OpenStack service node password login denial validation plan.
- Authentication failure log capture plan.
- Failure condition for `PasswordAuthentication` enabled, password login success, missing sshd config, or missing failure evidence.

## Excluded

- SSH key authentication success validation, which is handled in S011.
- Root login denial validation, which is handled in S013.
- Creating real SSH private keys.
- Storing passwords, credentials, private keys, public IPs, cloud account values, subscription IDs, tenant IDs, tfstate, kubeconfig files, or account-specific files.
- Real Ansible automation implementation.
- Terraform, Kubernetes, monitoring, ML, backup, or cloud provisioning logic.

## Assumptions

- Use placeholders such as `<bastion-host>`, `<target-node>`, and `<target-user>`.
- Usernames are placeholders unless generic and non-account-specific.
- Future execution requires explicit approval before any real SSH authentication test.
