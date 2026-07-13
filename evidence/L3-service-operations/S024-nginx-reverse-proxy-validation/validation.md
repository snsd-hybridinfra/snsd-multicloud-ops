# Validation

Scenario: S024-nginx-reverse-proxy-validation
Level: L3-service-operations
Mode: Static
Date: 2026-07-13
Overall status: PASS

| Check ID | Check Description | Expected Condition | Actual Result | Status | Evidence File |
|---|---|---|---|---|---|
| V001 | Required baseline files | Four baseline artifacts exist. | All exist. | PASS | summary |
| V002 | Sample evidence files | Three sanitized samples exist. | All exist. | PASS | sample logs |
| V003 | Reverse proxy baseline | Path, placeholders, modes, and evidence are defined. | Complete. | PASS | baseline; summary |
| V004 | Reverse proxy directives | Required routing directives exist. | Complete. | PASS | config; summary |
| V005 | Forwarded headers | Four exact header directives exist. | Complete. | PASS | config; summary |
| V006 | Proxy timeout baseline | Three explicit timeouts exist. | Complete. | PASS | config; summary |
| V007 | Reverse proxy rule matrix | Thirteen controls and required columns exist. | Complete. | PASS | matrix; summary |
| V008 | Safe command reference | Five example commands exist. | Complete. | PASS | command example; summary |
| V009 | Config-test sample parsing | Marked sample has two success indicators. | Parsed successfully. | PASS | config-test sample; summary |
| V010 | HTTP response sample parsing | Marked sample contains HTTP 200 OK. | Parsed successfully. | PASS | HTTP sample; summary |
| V011 | Access-log sample parsing | Symbolic request has 200 status. | Parsed successfully. | PASS | access sample; summary |
| V012 | TLS material safety | No key/certificate material or path. | None detected. | PASS | log; summary |
| V013 | Credential and header safety | No sensitive assignment/header/auth directive. | None detected. | PASS | log; summary |
| V014 | Address and domain safety | No numeric address, domain, or concrete URL. | None detected. | PASS | log; summary |
| V015 | Proxy example safety | No broad proxy, resolver, or TLS listener. | None detected. | PASS | config; summary |
| V016 | Execution safety boundary | No Nginx/curl invocation; live HEAD is guarded. | Boundary confirmed. | PASS | script; summary |
| V017 | Validation mode and live result | Static performs no network request. | Static completed safely. | PASS | log; summary |

## Generated Result

- Critical failures: 0
- Warnings: 0
- Optional LiveHttp: NOT_RUN
- Final judgment: PASS
- No Nginx process, curl command, network request, target URL, response content, credential, cookie, token, TLS material, domain, or numeric address was used or stored.
