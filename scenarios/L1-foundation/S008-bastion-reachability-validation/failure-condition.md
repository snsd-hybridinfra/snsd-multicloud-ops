# Failure Condition

## Failure Conditions

- Bastion inventory entry is missing or invalid.
- Management Zone to Bastion reachability path is undefined.
- Bastion to on-prem DB, monitoring, AWS, Azure, or OpenStack target path is undefined.
- SSH ProxyJump pattern includes real users, hosts, private keys, or credentials.
- Evidence collection path through Bastion is unclear.
- SSH hardening is attempted in this L1 scenario.
- Real public IPs, private IPs, credentials, SSH private keys, provider account IDs, subscription IDs, tenant IDs, tfstate, kubeconfig files, or account-specific values are present.

## Evidence of Failure

Record failed or blocked checks in `validation.md`, with supporting TODO references to `configs/bastion-reachability-path-summary.md`, `configs/ssh-jump-pattern-summary.md`, or `logs/bastion-reachability-validation.log`.

## Follow-Up Requirement

Create a follow-up task to correct inventory entries, routing assumptions, bastion path documentation, or SSH access design before future execution proceeds.
