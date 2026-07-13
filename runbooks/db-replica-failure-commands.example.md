# DB Replica Failure Command Reference

The following are documentation placeholders only.

```text
systemctl status <replica-service-name-placeholder>
mysql -h <db-replica-host-placeholder> -e "SHOW REPLICA STATUS placeholder"
mysql -h <db-primary-host-placeholder> -e "SHOW MASTER STATUS placeholder"
```

## MANUAL FAULT INJECTION ONLY

```text
systemctl stop <replica-service-name-placeholder>
```

## MANUAL RECOVERY ACTION ONLY

```text
systemctl start <replica-service-name-placeholder>
```

Stop/start and SQL examples must never be executed by the validator. Use a disposable lab, never production, and never store passwords, connection strings, dumps, hosts, IPs, GTIDs, binlog values, or credentials.
