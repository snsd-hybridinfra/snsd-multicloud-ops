# Scope

## Included

- Pre-failure Prometheus service status validation plan.
- Pre-failure target UP status validation plan.
- Target failure injection plan using placeholder commands.
- Prometheus `/targets` DOWN status validation plan.
- Prometheus query-based detection evidence plan.
- Target failure timestamp capture plan.
- Exporter or endpoint restoration validation plan.
- Post-recovery target UP validation plan.
- Detection and recovery time evidence collection plan.

## Target Categories

- Node Exporter target.
- DB Exporter target.
- Blackbox Exporter target.
- kube-state-metrics target.
- AWS service node target placeholder.
- Azure service node target placeholder.
- OpenStack service node target placeholder.
- On-Prem infrastructure node target placeholder.

## Failure Injection Scope

- Simulate one exporter or monitored endpoint outage using placeholder commands.
- Validate Prometheus marks the target as DOWN.
- Validate Prometheus query result reflects target state change.
- Validate target returns to UP after restoration.
- Capture before, failure, and after evidence using TODO placeholders.

## Important Boundary

- Do not claim Alertmanager integration.
- Do not claim automated alert notification.
- Do not claim SOAR-style response.
- This scenario validates target DOWN detection through Prometheus target state and query evidence only.

## Detection and Recovery Threshold Model

- DETECTED: target DOWN visible within `< 60 seconds`.
- WARNING: target recovery visible within `60-300 seconds`.
- CRITICAL: target remains DOWN or recovery exceeds `300 seconds`.

These are provisional validation thresholds and must be replaced only when an approved operational threshold is documented.

## Excluded

- Real Prometheus configuration implementation.
- Alertmanager integration, automated alert notification, and SOAR-style response.
- Real public IPs, credentials, secrets, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, or account-specific values.
- Prometheus target discovery validation, which is handled in S028.
- Grafana dashboard validation, which is handled in S029.
- Blackbox endpoint probe validation, which is handled in S030.
- Changes outside this scenario directory, its matching evidence directory, and the required tracking documents.
