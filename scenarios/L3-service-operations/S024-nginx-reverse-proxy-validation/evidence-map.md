# Evidence Map

| Check ID | Validation Item | Evidence File |
|---|---|---|
| V001 | Required baseline files | `commands.md`; `configs/nginx-reverse-proxy-summary.md` |
| V002 | Sample evidence files | three `logs/*.sample.txt`; summary |
| V003 | Reverse proxy baseline | `traffic-management/nginx-reverse-proxy-validation.md`; summary |
| V004 | Reverse proxy directives | `traffic-management/nginx-reverse-proxy.example.conf`; summary |
| V005 | Forwarded headers | config example; summary |
| V006 | Proxy timeout baseline | config example; summary |
| V007 | Reverse proxy rule matrix | `traffic-management/nginx-reverse-proxy-rule-matrix.example.md`; summary |
| V008 | Safe command reference | `traffic-management/nginx-reverse-proxy-commands.example.md`; summary |
| V009 | Config-test sample parsing | `logs/nginx-config-test.sample.txt`; summary |
| V010 | HTTP response sample parsing | `logs/reverse-proxy-http-response.sample.txt`; summary |
| V011 | Access-log sample parsing | `logs/nginx-access-log.sample.txt`; summary |
| V012 | TLS material safety | generated validation log; summary |
| V013 | Credential and header safety | generated validation log; summary |
| V014 | Address and domain safety | generated validation log; summary |
| V015 | Proxy example safety | config example; summary |
| V016 | Execution safety boundary | `tools/validate-nginx-reverse-proxy.ps1`; summary |
| V017 | Validation mode and live result | generated validation log; summary |

`validation.md` records every check. The generated `.log` is local/ignored; the committed summary and sanitized samples provide durable evidence. No live target or response content is evidence.
