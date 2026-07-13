# Failure Condition

## Critical Failure Conditions

- A required baseline file, directive, policy statement, or placeholder is missing.
- Root login is enabled or a root-password assignment, root credential, or sshpass value is present.
- A private-key filename, private-key material, or `authorized_keys` file is present.
- A sensitive assignment, numeric IP, account ID, subscription ID, tenant ID, UUID, public-key material, or token value is detected.
- The validator contains or executes SSH changes, restart, root attempt, privilege escalation, network, Ansible, cloud, or Kubernetes commands.
- Documentation implies the example proves live sshd or sudo enforcement.

Any critical failure produces a non-zero exit and must be documented without exposing unsafe content.
