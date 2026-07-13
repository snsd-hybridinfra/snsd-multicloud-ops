# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Required baseline files | Test four paths. | All exist. | commands; summary |
| V002 | Scrape job definitions | Match six jobs. | Complete. | config; summary |
| V003 | Target and Kubernetes discovery model | Match targets and endpoints role. | Complete. | config; summary |
| V004 | Target discovery rule matrix | Match six jobs/rules/labels/auth boundary. | Complete. | matrix; summary |
| V005 | Prometheus API command reference | Match three symbolic commands. | Complete. | command reference; summary |
| V006 | Authentication and TLS config safety | Scan auth/token/TLS material. | None. | config/log; summary |
| V007 | Endpoint address and domain safety | Scan concrete URLs/addresses/domains. | None. | log; summary |
| V008 | Required sample evidence | Test three paths. | All exist. | samples; summary |
| V009 | Targets JSON syntax | Parse marked success JSON. | Valid. | targets sample; summary |
| V010 | Target discovery and health evidence | Require six jobs at up. | Healthy. | targets sample; summary |
| V011 | UP query JSON syntax | Parse marked success JSON. | Valid. | up sample; summary |
| V012 | UP query required job values | Require six jobs at 1. | Healthy. | up sample; summary |
| V013 | Job label evidence | Require six values. | Complete. | labels sample; summary |
| V014 | Credential token and account safety | Scan sensitive assignments/IDs. | None. | log; summary |
| V015 | Execution safety boundary | Reject clients/reload; require live guard. | Safe. | script; summary |
| V016 | Validation mode and live API result | Evaluate Static or explicit live result. | Safe/pass or lab-incomplete warn. | log; summary |
