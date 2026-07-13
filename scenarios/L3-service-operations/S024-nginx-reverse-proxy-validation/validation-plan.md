# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Required baseline files | Test four baseline paths. | All exist. | `commands.md`, summary |
| V002 | Sample evidence files | Test three sample paths. | All exist. | sample logs, summary |
| V003 | Reverse proxy baseline | Match request path, placeholders, modes, and evidence terms. | Complete baseline. | baseline, summary |
| V004 | Reverse proxy directives | Parse upstream, server, listen, server_name, location, and proxy_pass. | Approved directives present. | config, summary |
| V005 | Forwarded headers | Match four exact proxy header directives. | Approved variables used. | config, summary |
| V006 | Proxy timeout baseline | Match connect, send, and read timeouts. | All explicit. | config, summary |
| V007 | Reverse proxy rule matrix | Match columns and thirteen controls. | Complete matrix. | matrix, summary |
| V008 | Safe command reference | Match five example commands. | Complete reference. | command example, summary |
| V009 | Config-test sample parsing | Match both success indicators and sample marker. | Successful sample. | config-test sample, summary |
| V010 | HTTP response sample parsing | Match marked HTTP 200 OK. | Acceptable sample. | HTTP sample, summary |
| V011 | Access-log sample parsing | Match symbolic client/request and 200. | Sanitized sample. | access sample, summary |
| V012 | TLS material safety | Scan artifacts for key/certificate material and paths. | None detected. | log, summary |
| V013 | Credential and header safety | Scan for assignments, auth directives, and sensitive headers. | None detected. | log, summary |
| V014 | Address and domain safety | Scan for numeric addresses, domains, and concrete URLs. | None detected. | log, summary |
| V015 | Proxy example safety | Reject broad dynamic proxying, resolver, and TLS listener. | Safe example. | config, summary |
| V016 | Execution safety boundary | Inspect validator invocation guards. | No Nginx/curl; guarded HEAD only. | script, summary |
| V017 | Validation mode and live result | Evaluate Static or explicit LiveHttp result. | Static safe or acceptable live status. | log, summary |
