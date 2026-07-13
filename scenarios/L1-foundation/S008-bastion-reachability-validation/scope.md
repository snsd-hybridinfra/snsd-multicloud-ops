# Scope

## Included

- Placeholder control-plane-to-bastion and bastion-to-zone paths.
- Required target aliases and symbolic address tokens.
- Bastion-only administrative access policy.
- Direct public SSH denial, key authentication requirement, password-login denial, and root-login denial statements.
- Local checks for numeric IPs, key paths, credential assignments, account identifiers, and active external commands.
- Generated local log and Markdown summary evidence.

## Excluded

- Real host existence, connectivity, routing, port, or SSH validation.
- Ansible execution, ping, facts, inventory connection, or playbooks.
- Private keys, authorized-key content, usernames, passwords, credentials, or real addresses.
- Cloud provider, Kubernetes, OpenStack, EVE-NG, or network queries.
- Multi-cloud inventory validation, which belongs to S007.
- DNS and hostname resolution, which belongs to S009.
- SSH key, password-denial, and root-denial enforcement, which belong to S011-S013.
- Security-group least-privilege validation, which belongs to S014-S016.

## Assumptions

- Paths describe intended administrative trust boundaries only.
- Placeholder targets do not assert that instances, routes, or policies exist.
