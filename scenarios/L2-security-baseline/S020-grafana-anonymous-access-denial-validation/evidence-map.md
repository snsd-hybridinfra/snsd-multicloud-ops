# Evidence Map

| Check ID | Validation Item | Evidence File | Required |
|---|---|---|---|
| V001 | Anonymous access denial baseline | `logs/grafana-anonymous-access-denial-validation.log`; `configs/grafana-anonymous-access-denial-summary.md` | yes |
| V002 | Access-control rule matrix | same generated evidence | yes |
| V003 | Grafana config example | same generated evidence | yes |
| V004 | Anonymous configuration section | same generated evidence | yes |
| V005 | Anonymous access disabled | same generated evidence | yes |
| V006 | Anonymous enablement denial | same generated evidence | yes |
| V007 | Baseline denial documentation | same generated evidence | yes |
| V008 | Access-control matrix completeness | same generated evidence | yes |
| V009 | Admin password storage safety | same generated evidence | yes |
| V010 | Grafana API token safety | same generated evidence | yes |
| V011 | Datasource credential safety | same generated evidence | yes |
| V012 | URL, address, and account safety | same generated evidence | yes |
| V013 | Generic secret safety | same generated evidence | yes |
| V014 | Execution safety boundary | same generated evidence | yes |

`commands.md` documents execution and `validation.md` records final results. The generated log is ignored; the sanitized summary is tracked.
