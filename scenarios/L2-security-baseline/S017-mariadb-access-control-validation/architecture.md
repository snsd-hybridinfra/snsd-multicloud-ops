# Architecture

## Validation Flow

```text
Local PowerShell validator
  -> MariaDB access-control policy
  -> grant matrix
  -> non-production SQL example
  -> inventory placeholder safety
  -> grant and sensitive-content checks
  -> evidence log and summary
```

## Account Model

- `<application-db-user>`: required DML only on `<application-database>`.
- `<replication-db-user>`: replication privileges only.
- `<monitoring-db-user>`: read-only metadata/status access.
- `<admin-db-user>`: separate approved administration boundary.
- Root: never used by applications and unavailable for remote login.

## Trust Boundary

All inspection is repository-local; no database endpoint, client, credential store, or network path participates.
