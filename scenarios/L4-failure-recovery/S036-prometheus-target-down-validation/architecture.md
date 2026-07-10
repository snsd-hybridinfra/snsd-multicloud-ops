# Architecture

This scenario models Prometheus target state detection for one monitored endpoint failure. It does not model alert routing, notification, or automated response.

## Relevant Components

- Prometheus endpoint placeholder: `<prometheus-endpoint>`.
- Target job placeholder: `<target-job>`.
- Target instance placeholder: `<target-instance>`.
- Node Exporter target placeholder: `<node-exporter-target>`.
- DB Exporter target placeholder: `<db-exporter-target>`.
- Blackbox Exporter target placeholder: `<blackbox-exporter-target>`.
- Recovery threshold placeholder: `<recovery-threshold-seconds>`.
- Prometheus query mapping for `up{job="<target-job>"}`.
- Evidence store: `evidence/L4-failure-recovery/S036-prometheus-target-down-validation/`.

## Failure and Recovery Flow

1. Capture pre-failure Prometheus service and target UP state.
2. Simulate one exporter or endpoint outage using placeholder commands.
3. Validate the target appears DOWN on the Prometheus `/targets` page.
4. Validate `up{job="<target-job>"}` reflects the target state change.
5. Capture target failure timestamp evidence.
6. Restore the exporter or endpoint using placeholder action.
7. Validate the target returns to UP.
8. Measure detection and recovery timing against provisional thresholds.

The evidence model is limited to Prometheus target state and query output.
