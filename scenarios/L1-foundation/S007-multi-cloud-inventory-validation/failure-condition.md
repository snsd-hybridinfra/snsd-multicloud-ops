# Failure Condition

## Critical Failure Conditions

- A required inventory or schema file is missing.
- A required group, host alias, schema field, provider-or-zone value, or component-type value is missing.
- An `ansible_host` value is not an approved placeholder or a numeric IP is present.
- A username, password, token, private-key path, access key, account identifier, UUID, subscription ID, tenant ID, or secret-like value is detected.
- A production, live inventory, hosts.ini, or vault file exists.
- The validator contains or executes an Ansible, host, cloud, network, Kubernetes, OpenStack, or EVE-NG command.

Any critical failure produces a non-zero exit and must be documented without exposing the unsafe value.
