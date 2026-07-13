# Architecture

## Replication Model

```text
<db-primary-host>
  -> binary log / <replication-channel>
  -> replica IO thread
  -> replica SQL thread
  -> <db-replica-host>
```

The evidence model uses `<replication-db-user>`, symbolic binlog file/position, and optional GTID placeholders. Healthy evidence requires IO and SQL threads at `Yes`, numeric non-NULL delay within threshold, and empty IO/SQL errors.

## Validation Boundary

The validator reads six repository artifacts and writes aggregate evidence. No database, host, network, credential store, inventory target, or SQL engine is accessed. The Ansible example only emits explanatory debug text.
