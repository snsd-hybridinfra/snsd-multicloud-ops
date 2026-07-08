# Failure Condition

## Failure Conditions

- Any required inventory group is missing.
- Provider, zone, role, or validation target is unclear.
- Real public IPs, private IPs, credentials, SSH private keys, tokens, tfstate, kubeconfig files, or account-specific values are present.
- Hostnames are inconsistent, ambiguous, or tied to real environments.
- On-prem DB primary and replica roles are not separated.
- Observability targets or evidence targets are missing or not clearly scoped.
- Inventory content becomes executable automation instead of a validation model.

## Evidence of Failure

Record failed or blocked checks in `validation.md`, with supporting TODO references to `configs/inventory-structure-summary.md`, `configs/inventory-sanitization-check.md`, or `logs/inventory-validation.log`.

## Follow-Up Requirement

Create a follow-up task to correct inventory grouping, sanitize values, or clarify host role metadata before future Ansible validation proceeds.
