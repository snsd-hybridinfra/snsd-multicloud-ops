# Prerequisites

## Required Previous Scenarios

- S007-multi-cloud-inventory-validation: defines placeholder DB node inventory.
- S017-mariadb-access-control-validation: defines database access control assumptions.
- S026-mariadb-primary-replica-replication-validation: defines primary-replica replication assumptions.

## Required Tools or References

- MariaDB command planning capability, when future execution is approved.
- Placeholder replication topology for `db-primary-01`, `db-replica-01`, and `db-replica-02`.
- Evidence model from `docs/evidence-model.md`.
- Placeholder naming rules from `docs/naming-rules.md`.

## Safety Preconditions

- Do not add database passwords, credentials, private keys, tfstate, kubeconfig content, cloud account values, or account-specific values.
- Do not record real public IPs.
- Do not execute live MariaDB configuration changes as part of this scenario skeleton.
