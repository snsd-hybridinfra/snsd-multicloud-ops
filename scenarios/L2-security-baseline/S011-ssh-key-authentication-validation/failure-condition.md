# Failure Condition

## Critical Failure Conditions

- A required baseline file, setting, policy statement, or placeholder is missing.
- A private-key filename, private-key material, or `authorized_keys` file is present.
- A password value, key material, credential assignment, numeric IP, account ID, subscription ID, tenant ID, UUID, or token value is detected.
- The validator contains or executes SSH configuration changes, restart, connection, network, Ansible, cloud, or Kubernetes commands.
- Documentation implies the example proves live sshd enforcement.

Any critical failure produces a non-zero exit and must be documented without exposing unsafe content.
