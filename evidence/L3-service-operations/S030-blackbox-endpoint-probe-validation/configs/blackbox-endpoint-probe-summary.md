# Blackbox Endpoint Probe Summary

- Scenario: S030-blackbox-endpoint-probe-validation
- Generated: 2026-07-13T12:48:05+09:00
- Validation mode: **Static**
- Required file check result: **PASS**
- Blackbox module check result: **PASS**
- Prometheus scrape config placeholder check result: **PASS**
- Probe metric documentation check result: **PASS**
- Success sample parsing result: **HEALTHY**
- Warning sample parsing result: **WARNING**
- Failure sample parsing result: **EXPECTED_FAILURE_DETECTED**
- Prometheus probe query sample parsing result: **PASS**
- Secret-safety check result: **PASS**
- Final judgment: **PASS**

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Required probe baseline files | PASS | Baseline, exporter config, scrape config, matrix, and commands exist. |
| V002 | Blackbox module definitions | PASS | HTTP 2xx and TCP connect modules contain required safe settings. |
| V003 | Prometheus Blackbox scrape placeholder | PASS | Probe path, module, symbolic target, relabeling, and exporter placeholder exist. |
| V004 | Probe metrics and threshold model | PASS | Probe metrics and normal/warning/failure thresholds are documented. |
| V005 | Probe rule matrix | PASS | All nine probe areas and required columns are documented. |
| V006 | Probe command reference | PASS | Exporter and three Prometheus query examples exist. |
| V007 | Required probe samples | PASS | Success, warning, failure, and query samples exist. |
| V008 | Healthy probe evidence | PASS | probe_success=1, acceptable status, and normal duration were parsed. |
| V009 | Warning duration evidence | WARN | Expected warning fixture was classified above 2.0 through 5.0 seconds. |
| V010 | Failure negative fixture | PASS | Failed probe and timeout/refusal placeholder were correctly rejected operationally. |
| V011 | Prometheus probe query sample | PASS | Valid JSON contains all three required healthy probe metrics. |
| V012 | Credential token cookie and TLS safety | PASS | No auth config, credential, token, cookie, authorization, certificate, or key exists. |
| V013 | Endpoint URL address and domain safety | PASS | No real endpoint, Prometheus/Blackbox URL, address, or domain exists. |
| V014 | Account and identifier safety | PASS | No account ID or UUID exists. |
| V015 | Execution safety boundary | PASS | Static mode invokes no client; live mode is explicit, cookie-free, and non-mutating. |
| V016 | Validation mode and live probe result | PASS | Static mode completed without curl, Prometheus/Blackbox query, reload, or network access. |
