# Scope

## Included

- OpenStack private network and subnet Terraform definitions.
- External network reference placeholder.
- Router and router interface definitions.
- Baseline security group and one management rule placeholder.
- Safe non-production example CIDRs, documentation DNS address, and metadata tags.
- Local checks for required files, resource blocks, unsafe files, authentication artifacts, backend blocks, account assignments, and credential-like content.
- Optional `terraform fmt -check` when Terraform is locally available.
- Generated local log and Markdown summary evidence.

## Excluded

- OpenStack authentication, CLI execution, or cloud API access.
- `clouds.yaml`, openrc, provider credentials, authentication URLs, project IDs, tenant IDs, usernames, passwords, tokens, and application credentials.
- Provider initialization or download.
- `terraform init`, `validate`, `plan`, `apply`, or `destroy` execution.
- Real variable files, backend configuration, state, public IPs, or account-specific values.
- Real OpenStack resource creation, modification, lookup, or deletion.
- Terraform provider validation, which belongs to S006.
- OpenStack security group validation, which belongs to S016.
- Terraform drift detection, which belongs to S041.
- Cost guardrail validation, which belongs to S045.
- OpenStack multi-node HA, Ceph, Octavia, and production-grade private cloud HA.

## Assumptions

- Definitions are non-production repository artifacts only.
- The external network is represented only by `<external-network-name>`.
- Later provider or cloud execution requires a separately approved scenario.
