# Failure Condition

## Critical Failure Conditions

- A required model file, alias, domain placeholder, address token, or policy statement is missing.
- A numeric IP, credential assignment, key, access key, account ID, subscription ID, tenant ID, UUID, password value, or token value is detected.
- A DNS zone or resolver export artifact is present.
- The validator contains or executes a DNS, host, network, cloud, SSH, Ansible, or Kubernetes command.
- Documentation implies that placeholders prove real DNS or host state.

Any critical failure produces a non-zero exit and must be documented without exposing unsafe content.
