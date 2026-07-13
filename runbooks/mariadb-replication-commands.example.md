# MariaDB Replication Command Examples

NON-PRODUCTION EXAMPLES. These SQL statements are documentation references and are not executed by the validator.

```sql
SHOW REPLICA STATUS\G
SHOW SLAVE STATUS\G
SHOW MASTER STATUS;
SHOW BINARY LOGS;
SELECT @@read_only;
SELECT @@server_id;
```

Collect output manually only in an approved lab, then sanitize it using `<db-primary-host>`, `<db-replica-host>`, `<replication-db-user>`, `<replication-channel>`, `<binlog-file-placeholder>`, `<binlog-position-placeholder>`, and `<gtid-placeholder>`.

Do not document client connection strings, usernames, passwords, or command-line credential flags.
