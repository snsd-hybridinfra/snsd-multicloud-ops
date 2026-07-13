# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Required baseline and sample files | Test seven paths. | All exist. | commands; summary |
| V002 | Replication lag threshold model | Match ranges, fields, threads, errors, matrix. | Complete. | runbook/matrix; summary |
| V003 | Prometheus metric placeholders | Match four names and S028/S029 boundaries. | Complete. | metric reference; summary |
| V004 | Normal lag evidence | Parse healthy threads/errors and lag 0-5. | PASS. | normal sample; summary |
| V005 | Warning lag evidence | Parse healthy threads/errors and lag 6-30. | Expected WARN. | warning sample; summary |
| V006 | Critical lag negative fixture | Detect healthy threads with lag above 30. | Expected critical detected. | critical sample; summary |
| V007 | NULL lag negative fixture | Detect NULL, stopped thread, placeholder error. | Expected failure detected. | NULL sample; summary |
| V008 | Thread health parsing | Distinguish positive and negative thread states. | Correct. | samples; summary |
| V009 | Replication error parsing | Distinguish empty and placeholder error. | Correct. | samples; summary |
| V010 | Replication terminology | Detect modern or accepted legacy fields. | Modern pass/legacy warn. | samples; summary |
| V011 | Database credential and connection safety | Scan assignments/URLs/client flags. | None. | log; summary |
| V012 | Database dump file safety | Scan dump/export names. | None. | log; summary |
| V013 | Observability credential safety | Scan credential assignments/URLs. | None. | log; summary |
| V014 | Address and account-specific safety | Scan addresses, IDs, UUIDs, URLs. | None. | log; summary |
| V015 | Static execution boundary | Reject DB/web clients and destructive commands. | Safe. | script; summary |
| V016 | Validation mode | Require four sample markers. | StaticEvidence. | samples; summary |
