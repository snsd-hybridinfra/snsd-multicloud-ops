# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Pre-failure load balancer endpoint validation plan | Plan HTTP check for `<load-balancer-endpoint>`. | Load balancer endpoint responds before failure. | `commands.md`, `screenshots/load-balancer-before-failure.png`, `validation.md` |
| V002 | Pre-failure backend health validation plan | Review `<backend-service>` health. | Backend service is healthy before frontend failure. | `commands.md`, `configs/load-balancer-failure-summary.md`, `validation.md` |
| V003 | Pre-failure Ingress route validation reference plan | Reference S023 Ingress route behavior. | Ingress route baseline is documented without reimplementing S023. | `commands.md`, `configs/load-balancer-failure-summary.md`, `validation.md` |
| V004 | Load balancer failure injection plan | Plan entrypoint outage using placeholder commands. | Failure injection targets the load balancer or reverse proxy entrypoint only. | `commands.md`, `logs/load-balancer-failure-validation.log`, `validation.md` |
| V005 | Endpoint failure detection validation plan | Plan checks for `<web-endpoint>` and `<api-endpoint>` during outage. | Endpoint failure or degradation is detected. | `commands.md`, `screenshots/load-balancer-during-failure.png`, `validation.md` |
| V006 | Health check failure validation plan | Plan health check review for `<health-endpoint>`. | Health check failure is detected. | `commands.md`, `logs/load-balancer-failure-validation.log`, `validation.md` |
| V007 | Blackbox probe failure reference validation plan | Reference S030 Blackbox probe behavior. | Blackbox probe failure reference is documented. | `commands.md`, `configs/load-balancer-failure-summary.md`, `validation.md` |
| V008 | Backend service health during frontend failure validation plan | Review backend health while entrypoint is failed. | Backend service health is known and separated from frontend failure. | `commands.md`, `configs/load-balancer-failure-summary.md`, `validation.md` |
| V009 | Manual recovery decision point validation plan | Review manual decision point checklist. | Decision points are explicit and do not claim automatic cross-cloud failover. | `commands.md`, `configs/load-balancer-decision-points.md`, `validation.md` |
| V010 | Load balancer restoration validation plan | Plan entrypoint restoration using placeholder action. | Restoration path is documented. | `commands.md`, `logs/load-balancer-failure-validation.log`, `validation.md` |
| V011 | Post-recovery HTTP response validation plan | Plan HTTP response checks after restoration. | Web/API endpoints return expected responses after recovery. | `commands.md`, `screenshots/load-balancer-after-recovery.png`, `validation.md` |
| V012 | Recovery time measurement plan | Measure failure detection and endpoint restoration duration. | Detection and recovery timing is recorded and compared with thresholds. | `commands.md`, `configs/load-balancer-recovery-threshold.md`, `validation.md` |
| V013 | Failure condition for load balancer failure not detected, wrong backend diagnosis, all endpoints unavailable, backend health unknown, recovery procedure unclear, recovery threshold exceeded, or missing evidence | Evaluate findings against explicit failure conditions. | Load balancer recovery issues produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates load balancer failure behavior only; health check baseline is handled in S025, Ingress routing in S023, Nginx Reverse Proxy forwarding in S024, Blackbox probing in S030, Web Pod failure in S031, and API service failure in S032.
