# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Required baseline files | Test four paths. | All exist. | commands; summary |
| V002 | Sample evidence files | Test three paths. | All exist. | sample logs; summary |
| V003 | Health-check baseline | Match path, settings, evidence, recovery, and modes. | Complete. | baseline; summary |
| V004 | Backend pool definition | Parse upstream and two members. | Pool complete. | config; summary |
| V005 | Health endpoint and expected status | Parse `/health`, proxy target, status placeholder. | Complete. | config/baseline; summary |
| V006 | Timeout retry and unhealthy handling | Parse retry, tries, timeouts, threshold. | Complete. | config/baseline; summary |
| V007 | Health-check rule matrix | Match ten controls and columns. | Complete. | matrix; summary |
| V008 | Safe command reference | Match five symbolic commands. | Complete. | commands example; summary |
| V009 | Load-balancer health evidence | Parse marked 200 and reject failure indicators. | Healthy. | LB sample; summary |
| V010 | Backend health evidence | Require both backends at 200 and reject failures. | Both healthy. | backend sample; summary |
| V011 | Access-log health evidence | Parse symbolic `/health` 200. | Sanitized. | access sample; summary |
| V012 | TLS material safety | Scan for key/certificate material/paths. | None. | log; summary |
| V013 | Credential and header safety | Scan for secrets and sensitive headers. | None. | log; summary |
| V014 | Address and domain safety | Scan for numeric/concrete targets. | None. | log; summary |
| V015 | Active-health and failover boundary | Verify passive-only statements and no active directive. | Boundary explicit. | baseline/config; summary |
| V016 | Execution safety boundary | Inspect guarded request implementation. | No Nginx/curl; HEAD only. | script; summary |
| V017 | Validation mode and live health result | Evaluate Static or explicit live checks. | Safe/pass or documented warning. | log; summary |
