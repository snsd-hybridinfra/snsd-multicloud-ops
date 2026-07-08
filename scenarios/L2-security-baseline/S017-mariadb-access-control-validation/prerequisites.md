# Prerequisites

## Required Previous Scenarios

- S001-control-plane-toolchain-validation: confirms local toolchain planning.
- S007-multi-cloud-inventory-validation: defines placeholder database and application targets.
- S008-bastion-reachability-validation: defines the management path to On-Prem nodes.
- S014, S015, and S016: define cloud-side network source placeholders for app-to-DB access paths.

## Required Tools or References

- MariaDB command review capability, when future execution is approved.
- Network reachability or firewall evidence source, when future execution is approved.
- Evidence model from `docs/evidence-model.md`.
- Placeholder naming rules from `docs/naming-rules.md`.

## Safety Preconditions

- Do not add database passwords, credentials, private keys, tfstate, kubeconfig content, or account-specific values.
- Do not record real public IPs.
- Do not execute live MariaDB configuration changes as part of this scenario skeleton.
