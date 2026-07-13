# Validation

Scenario: S030-blackbox-endpoint-probe-validation
Level: L3-service-operations
Mode: Static
Date: 2026-07-13
Overall status: PASS

| Check ID | Check Description | Expected Condition | Actual Result | Status | Evidence File |
|---|---|---|---|---|---|
| V001 | Required probe baseline files | Five artifacts. | All exist. | PASS | summary |
| V002 | Blackbox module definitions | HTTP/TCP settings. | Complete. | PASS | exporter; summary |
| V003 | Prometheus Blackbox scrape placeholder | Probe/relabel model. | Complete. | PASS | scrape; summary |
| V004 | Probe metrics and threshold model | Metrics/ranges. | Complete. | PASS | baseline/matrix; summary |
| V005 | Probe rule matrix | Nine areas. | Complete. | PASS | matrix; summary |
| V006 | Probe command reference | Four examples. | Complete. | PASS | commands; summary |
| V007 | Required probe samples | Four samples. | All exist. | PASS | samples; summary |
| V008 | Healthy probe evidence | Success/status/duration normal. | Healthy. | PASS | success; summary |
| V009 | Warning duration evidence | Duration 2-5. | WARNING at 3.20. | WARN | warning; summary |
| V010 | Failure negative fixture | Failure/timeout detected. | Expected failure detected. | PASS | failure; summary |
| V011 | Prometheus probe query sample | Three healthy metrics. | Valid. | PASS | query; summary |
| V012 | Credential token cookie and TLS safety | None. | None detected. | PASS | log; summary |
| V013 | Endpoint URL address and domain safety | None concrete. | None detected. | PASS | log; summary |
| V014 | Account and identifier safety | None. | None detected. | PASS | log; summary |
| V015 | Execution safety boundary | No client/reload; guarded live. | Confirmed. | PASS | script; summary |
| V016 | Validation mode and live probe result | Static no network. | Completed safely. | PASS | log; summary |

## Generated Result

- Critical failures: 0
- Warnings: 1 (expected duration fixture)
- Failure fixture: EXPECTED_FAILURE_DETECTED
- LiveBlackbox: NOT_RUN
- Final judgment: PASS
- No live probe/query, reload, real URL/endpoint, credential, token, cookie, authorization, TLS material, address, domain, or network operation occurred.
