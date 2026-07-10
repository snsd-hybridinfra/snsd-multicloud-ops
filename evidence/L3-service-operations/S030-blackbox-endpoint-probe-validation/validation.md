# Validation

Scenario: S030-blackbox-endpoint-probe-validation
Level: L3-service-operations
Capability: Blackbox Endpoint Probe Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real Blackbox Exporter or Prometheus query output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Blackbox Exporter service status validation plan | Blackbox Exporter service status can be reviewed through an approved path. | TODO | NOT_RUN | `commands.md`; `logs/blackbox-endpoint-probe-validation.log` |
| V002 | Blackbox probe module existence validation plan | Required probe module placeholder is documented. | TODO | NOT_RUN | `commands.md`; `configs/blackbox-endpoint-probe-summary.md` |
| V003 | Web endpoint probe success validation plan | Web endpoint probe returns success. | TODO | NOT_RUN | `commands.md`; `configs/blackbox-target-mapping.md`; `logs/blackbox-endpoint-probe-validation.log` |
| V004 | API endpoint probe success validation plan | API endpoint probe returns success. | TODO | NOT_RUN | `commands.md`; `configs/blackbox-target-mapping.md`; `logs/blackbox-endpoint-probe-validation.log` |
| V005 | Ingress endpoint probe success validation plan | Ingress endpoint probe returns success. | TODO | NOT_RUN | `commands.md`; `configs/blackbox-target-mapping.md`; `screenshots/blackbox-probe-result.png` |
| V006 | Reverse Proxy endpoint probe success validation plan | Reverse proxy endpoint probe returns success. | TODO | NOT_RUN | `commands.md`; `configs/blackbox-target-mapping.md`; `screenshots/blackbox-probe-result.png` |
| V007 | AWS endpoint placeholder probe validation plan | AWS endpoint placeholder probe is documented. | TODO | NOT_RUN | `commands.md`; `configs/blackbox-target-mapping.md` |
| V008 | Azure endpoint placeholder probe validation plan | Azure endpoint placeholder probe is documented. | TODO | NOT_RUN | `commands.md`; `configs/blackbox-target-mapping.md` |
| V009 | OpenStack endpoint placeholder probe validation plan | OpenStack endpoint placeholder probe is documented. | TODO | NOT_RUN | `commands.md`; `configs/blackbox-target-mapping.md` |
| V010 | HTTP status code validation plan | Expected HTTP status code is documented and reviewable. | TODO | NOT_RUN | `commands.md`; `configs/blackbox-prometheus-query-mapping.md` |
| V011 | Probe duration and latency validation plan | Probe latency can be reviewed without real endpoint values in the repo. | TODO | NOT_RUN | `commands.md`; `configs/blackbox-prometheus-query-mapping.md`; `logs/blackbox-endpoint-probe-validation.log` |
| V012 | Prometheus `probe_success` query validation plan | `probe_success` query evidence can be captured. | TODO | NOT_RUN | `commands.md`; `configs/blackbox-prometheus-query-mapping.md`; `screenshots/prometheus-blackbox-query-result.png` |
| V013 | Prometheus `probe_http_status_code` query validation plan | `probe_http_status_code` query evidence can be captured. | TODO | NOT_RUN | `commands.md`; `configs/blackbox-prometheus-query-mapping.md`; `screenshots/prometheus-blackbox-query-result.png` |
| V014 | Failure condition for failed probe, HTTP 5xx, route timeout, DNS resolution failure, unexpected status code, excessive latency, or missing probe evidence | Endpoint probe failures produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Blackbox endpoint probe summary is captured: NOT_READY
- Blackbox target mapping is captured: NOT_READY
- Blackbox Prometheus query mapping is captured: NOT_READY
- Blackbox endpoint probe validation log is captured: NOT_READY
- Blackbox and Prometheus screenshots are captured: NOT_READY

## Notes

This scenario validates endpoint probing only. Prometheus target discovery is handled in S028, Grafana dashboard validation in S029, load balancing health checks in S025, Ingress routing in S023, and Nginx Reverse Proxy forwarding in S024. TLS certificate validation is excluded from this scenario.
