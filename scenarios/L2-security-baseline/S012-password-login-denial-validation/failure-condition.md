# Failure Condition

## Critical Failure Conditions

- A required baseline file, directive, policy statement, or placeholder is missing.
- Password authentication is enabled or a password assignment, sshpass value, or embedded credential is present.
- A private-key filename, private-key material, or `authorized_keys` file is present.
- A sensitive assignment, numeric IP, account ID, subscription ID, tenant ID, UUID, public-key material, or token value is detected.
- The validator contains or executes SSH configuration changes, restart, password attempt, connection, network, Ansible, cloud, or Kubernetes commands.
- Documentation implies the example proves live sshd enforcement.

Any critical failure produces a non-zero exit and must be documented without exposing unsafe content.
