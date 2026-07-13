# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Required documentation and evidence | Test six paths. | All exist. | commands; summary |
| V002 | Replication topology documentation | Match placeholders, threads, modes, and S027 boundary. | Complete. | runbook; summary |
| V003 | Replication command reference | Match six SHOW/SELECT references. | Complete. | command reference; summary |
| V004 | Non-production Ansible placeholder | Validate host/debug and reject execution/credentials. | Safe. | playbook; summary |
| V005 | Replica IO thread | Parse modern/legacy IO `Yes`; reject `No`. | Healthy. | replica sample; summary |
| V006 | Replica SQL thread | Parse modern/legacy SQL `Yes`; reject `No`. | Healthy. | replica sample; summary |
| V007 | Replication delay | Parse numeric/non-NULL delay and threshold. | Zero/pass or bounded warning. | samples; summary |
| V008 | Replication error fields | Require present, empty IO/SQL errors. | Empty. | replica sample; summary |
| V009 | Master status placeholders | Match file, position, GTID placeholders. | Symbolic. | master sample; summary |
| V010 | Sanitized replication notes | Match topology/account/channel placeholders. | Sanitized. | notes sample; summary |
| V011 | Replication terminology | Detect modern or accepted legacy fields. | Modern pass / legacy warn. | replica sample; summary |
| V012 | Database credential and connection safety | Scan assignments, URLs, and client flags. | None. | log; summary |
| V013 | Database dump file safety | Scan dump/export filenames with marked example exception. | None. | log; summary |
| V014 | Address and account-specific safety | Scan addresses, IDs, UUIDs, hosts. | None. | log; summary |
| V015 | Static execution boundary | Reject client invocation, SQL tasks, destructive commands. | Safe. | script/playbook; summary |
| V016 | Validation mode | Require all sample markers. | StaticEvidence. | samples; summary |
