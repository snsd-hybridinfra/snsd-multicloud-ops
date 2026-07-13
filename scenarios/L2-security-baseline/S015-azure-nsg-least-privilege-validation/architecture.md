# Architecture

## Validation Flow

```text
Local PowerShell validator
  -> Azure NSG policy baseline
  -> non-production rule matrix
  -> Azure Terraform structural placeholders
  -> safety and dangerous-rule checks
  -> evidence log and summary
```

## Trust Boundary

All inputs and outputs stay in the repository. No Azure identity, subscription, tenant, API, live NSG, backend, state, or external endpoint participates.

## Logical NSG Model

- `azure-public-web-nsg`: only public HTTP/HTTPS.
- `azure-bastion-nsg`: management access from approved placeholders.
- `azure-private-service-nsg`: internal application traffic.
- `azure-database-nsg`: database traffic from private service references.
- `azure-monitoring-nsg`: monitoring traffic from approved internal or management references.
