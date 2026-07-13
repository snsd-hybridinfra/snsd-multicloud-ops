# Evidence Map

| Check ID | Validation Item | Evidence File |
|---|---|---|
| V001 | Required baseline and sample files | `commands.md`; summary |
| V002 | Replication lag threshold model | runbook/matrix; summary |
| V003 | Prometheus metric placeholders | metric reference; summary |
| V004 | Normal lag evidence | normal sample; summary |
| V005 | Warning lag evidence | warning sample; summary |
| V006 | Critical lag negative fixture | critical sample; summary |
| V007 | NULL lag negative fixture | NULL sample; summary |
| V008 | Thread health parsing | four samples; summary |
| V009 | Replication error parsing | four samples; summary |
| V010 | Replication terminology | four samples; summary |
| V011 | Database credential and connection safety | generated log; summary |
| V012 | Database dump file safety | generated log; summary |
| V013 | Observability credential safety | generated log; summary |
| V014 | Address and account-specific safety | generated log; summary |
| V015 | Static execution boundary | validator; summary |
| V016 | Validation mode | four samples; summary |

The generated `.log` is ignored. The committed summary and four sanitized fixtures are durable evidence; critical/NULL files are explicitly negative fixtures.
