# Expected Result

## Success Conditions

- Inventory model includes all required groups.
- Provider, zone, role, and validation target are distinguishable.
- Placeholder hostnames and placeholder IPs are used consistently.
- On-prem DB primary and replica roles are separated.
- Observability and evidence collection targets are documented.
- Real credentials, private keys, public IPs, private IPs, tfstate, kubeconfig files, and account-specific values are prohibited.

## Required Evidence

- `commands.md`
- `validation.md`
- `configs/inventory-structure-summary.md`
- `configs/inventory-sanitization-check.md`
- `logs/inventory-validation.log`

## Completion Criteria

The scenario can move from `PLANNED` to `VALIDATED` only after approved, sanitized evidence confirms the inventory structure and sanitization checks. Real Ansible automation is not part of this skeleton.
