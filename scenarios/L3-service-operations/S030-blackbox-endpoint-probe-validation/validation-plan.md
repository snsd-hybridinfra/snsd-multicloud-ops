# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Blackbox Exporter service status validation plan | Plan service status or endpoint availability review for `<blackbox-exporter-endpoint>`. | Blackbox Exporter service status can be reviewed through an approved path. | `commands.md`, `logs/blackbox-endpoint-probe-validation.log`, `validation.md` |
| V002 | Blackbox probe module existence validation plan | Review placeholder probe module mapping. | Required probe module placeholder is documented. | `commands.md`, `configs/blackbox-endpoint-probe-summary.md`, `validation.md` |
| V003 | Web endpoint probe success validation plan | Plan probe check for `<web-endpoint>`. | Web endpoint probe returns success. | `commands.md`, `configs/blackbox-target-mapping.md`, `logs/blackbox-endpoint-probe-validation.log`, `validation.md` |
| V004 | API endpoint probe success validation plan | Plan probe check for `<api-endpoint>`. | API endpoint probe returns success. | `commands.md`, `configs/blackbox-target-mapping.md`, `logs/blackbox-endpoint-probe-validation.log`, `validation.md` |
| V005 | Ingress endpoint probe success validation plan | Plan probe check for `<ingress-host>`. | Ingress endpoint probe returns success. | `commands.md`, `configs/blackbox-target-mapping.md`, `screenshots/blackbox-probe-result.png`, `validation.md` |
| V006 | Reverse Proxy endpoint probe success validation plan | Plan probe check for `<reverse-proxy-host>`. | Reverse proxy endpoint probe returns success. | `commands.md`, `configs/blackbox-target-mapping.md`, `screenshots/blackbox-probe-result.png`, `validation.md` |
| V007 | AWS endpoint placeholder probe validation plan | Map AWS service zone endpoint placeholder to a probe target. | AWS endpoint placeholder probe is documented. | `commands.md`, `configs/blackbox-target-mapping.md`, `validation.md` |
| V008 | Azure endpoint placeholder probe validation plan | Map Azure service zone endpoint placeholder to a probe target. | Azure endpoint placeholder probe is documented. | `commands.md`, `configs/blackbox-target-mapping.md`, `validation.md` |
| V009 | OpenStack endpoint placeholder probe validation plan | Map OpenStack service zone endpoint placeholder to a probe target. | OpenStack endpoint placeholder probe is documented. | `commands.md`, `configs/blackbox-target-mapping.md`, `validation.md` |
| V010 | HTTP status code validation plan | Plan expected status code review for each probe target. | Expected HTTP status code is documented and reviewable. | `commands.md`, `configs/blackbox-prometheus-query-mapping.md`, `validation.md` |
| V011 | Probe duration and latency validation plan | Plan review of probe duration metrics against an approved threshold. | Probe latency can be reviewed without real endpoint values in the repo. | `commands.md`, `configs/blackbox-prometheus-query-mapping.md`, `logs/blackbox-endpoint-probe-validation.log`, `validation.md` |
| V012 | Prometheus `probe_success` query validation plan | Plan Prometheus query evidence for probe success. | `probe_success` query evidence can be captured. | `commands.md`, `configs/blackbox-prometheus-query-mapping.md`, `screenshots/prometheus-blackbox-query-result.png`, `validation.md` |
| V013 | Prometheus `probe_http_status_code` query validation plan | Plan Prometheus query evidence for HTTP status code. | `probe_http_status_code` query evidence can be captured. | `commands.md`, `configs/blackbox-prometheus-query-mapping.md`, `screenshots/prometheus-blackbox-query-result.png`, `validation.md` |
| V014 | Failure condition for failed probe, HTTP 5xx, route timeout, DNS resolution failure, unexpected status code, excessive latency, or missing probe evidence | Evaluate findings against explicit failure conditions. | Endpoint probe failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates endpoint probing only; Prometheus target discovery is handled in S028, Grafana dashboards in S029, load balancing health checks in S025, Ingress routing in S023, and Nginx reverse proxy forwarding in S024.
