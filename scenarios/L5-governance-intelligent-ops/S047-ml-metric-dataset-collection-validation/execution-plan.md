# Execution Plan

1. Confirm that dataset collection validation is placeholder-only.
2. Identify `<prometheus-endpoint>`, `<metric-query>`, `<dataset-file>`, `<dataset-window>`, `<target-job>`, `<target-instance>`, and `<collection-script>`.
3. Reference Prometheus source availability from S028.
4. Review metric query input placeholders.
5. Map node, Kubernetes, MariaDB, Blackbox, and HTTP endpoint metric placeholders.
6. Define required dataset fields.
7. Review timestamp field placeholder.
8. Review metric value field placeholder.
9. Review target label consistency.
10. Document dataset file existence placeholder.
11. Classify dataset quality as `DATASET_READY`, `DATASET_PARTIAL`, `DATASET_INVALID`, `DATASET_EMPTY`, or `DATASET_INCONCLUSIVE`.
12. Capture TODO evidence references in `commands.md`, `validation.md`, `configs/`, `logs/`, and `screenshots/`.

No real Prometheus queries, dataset exports, ML training, or anomaly detection are performed in this skeleton.
