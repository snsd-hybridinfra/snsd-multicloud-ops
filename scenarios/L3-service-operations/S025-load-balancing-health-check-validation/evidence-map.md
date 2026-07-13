# Evidence Map

| Check ID | Validation Item | Evidence File |
|---|---|---|
| V001 | Required baseline files | `commands.md`; summary |
| V002 | Sample evidence files | three `logs/*.sample.txt`; summary |
| V003 | Health-check baseline | baseline; summary |
| V004 | Backend pool definition | Nginx example; summary |
| V005 | Health endpoint and expected status | config/baseline; summary |
| V006 | Timeout retry and unhealthy handling | config/baseline; summary |
| V007 | Health-check rule matrix | matrix; summary |
| V008 | Safe command reference | command example; summary |
| V009 | Load-balancer health evidence | load-balancer sample; summary |
| V010 | Backend health evidence | backend sample; summary |
| V011 | Access-log health evidence | access sample; summary |
| V012 | TLS material safety | generated log; summary |
| V013 | Credential and header safety | generated log; summary |
| V014 | Address and domain safety | generated log; summary |
| V015 | Active-health and failover boundary | baseline/config; summary |
| V016 | Execution safety boundary | validator script; summary |
| V017 | Validation mode and live health result | generated log; summary |

`validation.md` records all outcomes. The generated `.log` is ignored; the committed summary and sanitized samples provide durable evidence without targets or response content.
