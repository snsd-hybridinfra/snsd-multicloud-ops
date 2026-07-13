# Nginx Reverse Proxy Summary

- Scenario: S024-nginx-reverse-proxy-validation
- Generated: 2026-07-13T11:59:51+09:00
- Validation mode: **Static**
- Required file check result: **PASS**
- Reverse proxy directive check result: **PASS**
- Forwarded header check result: **PASS**
- Timeout directive check result: **PASS**
- Evidence parsing result: **PASS**
- Secret-safety check result: **PASS**
- Final judgment: **PASS**

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Required baseline files | PASS | Baseline, config example, rule matrix, and command reference exist. |
| V002 | Sample evidence files | PASS | Config test, HTTP response, and access log samples exist. |
| V003 | Reverse proxy baseline | PASS | Purpose, request path, placeholders, evidence model, and validation modes are documented. |
| V004 | Reverse proxy directives | PASS | Upstream, server, listener, symbolic server name, location, and proxy_pass are defined. |
| V005 | Forwarded headers | PASS | Host and three forwarding headers use the approved variables. |
| V006 | Proxy timeout baseline | PASS | Connect, send, and read timeouts are explicit. |
| V007 | Reverse proxy rule matrix | PASS | All thirteen required controls and matrix columns are documented. |
| V008 | Safe command reference | PASS | All five non-production command examples are documented. |
| V009 | Config-test sample parsing | PASS | The marked sample contains both Nginx success indicators. |
| V010 | HTTP response sample parsing | PASS | The marked sample contains HTTP 200 OK. |
| V011 | Access-log sample parsing | PASS | The marked sample contains symbolic client, request, and 200 status evidence. |
| V012 | TLS material safety | PASS | No certificate, private key, or TLS path/material exists. |
| V013 | Credential and header safety | PASS | No credential, token, cookie, authorization value, basic-auth directive, or secret assignment exists. |
| V014 | Address and domain safety | PASS | No numeric address, real domain, or non-placeholder URL exists. |
| V015 | Proxy example safety | PASS | No broad dynamic proxying, resolver, or TLS listener is defined. |
| V016 | Execution safety boundary | PASS | Nginx and curl are never invoked; guarded LiveHttp uses a cookie-free HEAD request. |
| V017 | Validation mode and live result | PASS | Static mode completed without running Nginx, curl, or a network request. |

## Safety Boundary

Static mode performs repository-side validation only. LiveHttp requires explicit operator input, sends one HEAD request without cookies or authorization, and stores neither the target nor response content.
