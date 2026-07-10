# Execution Plan

1. Confirm that only placeholder target names, endpoints, and thresholds are used.
2. Capture pre-failure Prometheus service status for `<prometheus-endpoint>`.
3. Capture pre-failure target UP state for `<target-job>` and `<target-instance>`.
4. Plan one target failure injection using placeholder commands.
5. Validate Prometheus `/targets` shows the selected target as DOWN.
6. Validate `up{job="<target-job>"}` query evidence reflects the DOWN state.
7. Capture failure timestamp evidence.
8. Plan exporter or endpoint restoration using an approved placeholder action.
9. Validate Prometheus `/targets` shows the target as UP after recovery.
10. Validate query evidence reflects recovered UP state.
11. Measure detection and recovery timing against provisional thresholds.
12. Record future command output placeholders in `commands.md`.
13. Record future validation results in `validation.md`.
