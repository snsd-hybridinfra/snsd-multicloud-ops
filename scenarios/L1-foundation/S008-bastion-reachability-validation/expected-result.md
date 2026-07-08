# Expected Result

## Success Conditions

- Bastion reachability model is documented by zone and provider.
- Management Zone to Bastion Zone path is defined.
- Bastion to on-prem DB, monitoring, AWS, Azure, and OpenStack service node paths are defined.
- SSH ProxyJump command pattern is documented using placeholders only.
- Evidence collection through Bastion path is mapped.
- SSH hardening is explicitly excluded from this scenario.
- Real credentials, private keys, public IPs, account-specific values, tfstate, and kubeconfig files are prohibited.

## Required Evidence

- `commands.md`
- `validation.md`
- `configs/bastion-reachability-path-summary.md`
- `configs/ssh-jump-pattern-summary.md`
- `logs/bastion-reachability-validation.log`
- `screenshots/bastion-path-diagram.png`

## Completion Criteria

The scenario can move from `PLANNED` to `VALIDATED` only after approved, sanitized evidence confirms the bastion reachability design checks. Real host access and SSH hardening are not part of this skeleton.
