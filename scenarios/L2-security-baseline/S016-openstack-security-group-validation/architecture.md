# Architecture

## Validation Flow

```text
Local PowerShell validator
  -> OpenStack Security Group policy baseline
  -> non-production rule matrix
  -> OpenStack Terraform structural placeholders
  -> safety and dangerous-rule checks
  -> evidence log and summary
```

## Trust Boundary

All inputs and outputs stay in the repository. No auth URL, identity, project, tenant, API, live Security Group, backend, state, or external endpoint participates.

## Logical Security Group Model

- `openstack-public-web-sg`: only public HTTP/HTTPS.
- `openstack-bastion-sg`: management access from approved placeholders.
- `openstack-private-service-sg`: internal application traffic.
- `openstack-database-sg`: database traffic from private service references.
- `openstack-monitoring-sg`: monitoring traffic from approved internal or management references.
