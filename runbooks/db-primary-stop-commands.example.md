# DB Primary Stop Command Reference

Documentation placeholders only:

```text
systemctl status <primary-service-name-placeholder>
mysql -h <db-primary-host-placeholder> -e "SHOW MASTER STATUS placeholder"
mysql -h <db-replica-host-placeholder> -e "SHOW REPLICA STATUS placeholder"
```

## MANUAL FAULT INJECTION ONLY

```text
systemctl stop <primary-service-name-placeholder>
```

## MANUAL RECOVERY ACTION ONLY

```text
systemctl start <primary-service-name-placeholder>
```

The validator never executes these commands. Use only a disposable lab; never store credentials, payloads, rows, connection strings, hosts, IPs, GTIDs, or real binlog values.
