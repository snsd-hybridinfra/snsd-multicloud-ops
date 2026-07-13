# Scope

## Included

- Non-production example YAML inventory.
- Required groups and placeholder host aliases.
- Placeholder `ansible_host` values only.
- Inventory schema fields and allowed classification values.
- Local checks for real-looking addresses, sensitive assignments, account identifiers, unsafe inventory filenames, and active execution commands.
- Generated local log and Markdown summary evidence.

## Excluded

- Host connection, reachability, login, or existence validation.
- Ansible inventory execution, ping, facts, playbooks, or dynamic inventory.
- Private-key, credential, vault, environment, or account-file access.
- AWS, Azure, OpenStack, Kubernetes, EVE-NG, or network queries.
- Real hostnames, IP addresses, cloud instance IDs, account IDs, subscription IDs, or tenant IDs.
- Provisioning validation, which belongs to S003-S005.
- Terraform provider validation, which belongs to S006.
- Bastion reachability, which belongs to S008.
- DNS and hostname resolution, which belongs to S009.

## Assumptions

- The inventory is a documentation and validation model, not a deployable live inventory.
- Host aliases are stable portfolio placeholders and do not assert that instances exist.
