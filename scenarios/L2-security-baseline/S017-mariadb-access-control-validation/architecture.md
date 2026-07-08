# Architecture

## Relevant Components

- Control Plane: records validation commands and evidence.
- On-Prem DB Primary: authoritative MariaDB instance for access control validation.
- On-Prem DB Replicas: replica nodes with separate access policy review.
- Application access path: placeholder access from approved App/API nodes.
- Replication access path: placeholder access using `<replication-user>`.
- Backup access path: placeholder access using `<backup-user>`.
- Bastion or management path: approved administrative access boundary.

## Access Model

- `<app-db-user>` must be scoped to required application databases and approved host patterns only.
- `<replication-user>` must be separated from application and backup users.
- `<backup-user>` must be separated from application and replication users.
- Root remote access must be denied.
- DB port `3306` must not be reachable from public sources.
- Direct Web node DB access must be denied unless later explicitly approved.
- Cloud App/API node access must use placeholders such as `<app-node-cidr>`.

## Boundary Notes

This scenario validates access control design only. Replication function, replication lag, backup creation, and restore execution are separate scenario responsibilities.
