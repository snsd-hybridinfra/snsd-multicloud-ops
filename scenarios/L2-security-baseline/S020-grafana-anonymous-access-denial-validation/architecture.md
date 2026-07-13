# Architecture

## Validation Flow

```text
Local PowerShell validator
  -> Grafana anonymous-denial policy
  -> access-control rule matrix
  -> non-production INI example
  -> section, value, credential, and safety checks
  -> evidence log and summary
```

## Access Model

- Anonymous authentication is explicitly disabled.
- Viewer access requires an authenticated user, team, or role placeholder.
- Admin and datasource credentials and API tokens remain outside the repository.
- Public dashboard exposure requires a separate decision outside S020.

## Trust Boundary

All inspection is repository-local; no Grafana process, container, endpoint, credential source, datasource, or network path participates.
