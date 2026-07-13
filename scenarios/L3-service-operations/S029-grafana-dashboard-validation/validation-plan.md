# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Required dashboard baseline files | Test five paths. | All exist. | commands; summary |
| V002 | Prometheus datasource definition | Match required YAML fields. | Complete. | datasource; summary |
| V003 | Dashboard JSON structure | Parse marker/title/UID. | Valid. | dashboard; summary |
| V004 | Required dashboard panels | Require ten exact titles. | Complete. | dashboard; summary |
| V005 | Panel datasource and query coverage | Check UID/metrics/alert placeholder. | Complete. | dashboard; summary |
| V006 | Dashboard rule matrix | Require nine areas/columns. | Complete. | matrix; summary |
| V007 | Dashboard command reference | Require three APIs/manual workflow. | Complete. | commands example; summary |
| V008 | Required sample evidence | Test three paths. | All exist. | samples; summary |
| V009 | Dashboard search evidence | Parse required title. | Present. | search sample; summary |
| V010 | Dashboard detail evidence | Parse ten titles. | Complete. | detail sample; summary |
| V011 | Datasource list evidence | Parse placeholder datasource/type. | Present. | datasource sample; summary |
| V012 | Credential token datasource and TLS safety | Scan sensitive content. | None. | log; summary |
| V013 | Monitoring URL address and domain safety | Scan concrete endpoints. | None. | log; summary |
| V014 | Dashboard UID and identity safety | Require placeholder UIDs/no IDs. | Safe. | artifacts; summary |
| V015 | Execution safety boundary | Reject client/import/mutation. | Safe. | script; summary |
| V016 | Validation mode and live Grafana result | Evaluate Static/live result. | Safe/pass or auth-required warn. | log; summary |
