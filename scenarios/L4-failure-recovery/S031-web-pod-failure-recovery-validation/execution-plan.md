# Execution Plan

1. Confirm that only placeholder workload names, namespaces, and endpoints are used.
2. Capture the pre-failure Web Deployment status for `<web-deployment>`.
3. Capture the pre-failure Web Pod Ready status for `<web-pod>`.
4. Capture the pre-failure Web Service endpoint status for `<web-service>`.
5. Capture a pre-failure HTTP health check plan for `<health-endpoint>`.
6. Plan the failure injection command: `kubectl delete pod <web-pod> -n <namespace>`.
7. Observe Deployment/ReplicaSet replacement behavior.
8. Validate replacement Pod creation and Ready state recovery.
9. Validate Web Service endpoint recovery.
10. Validate HTTP health endpoint recovery.
11. Measure recovery time and compare it to provisional NORMAL, WARNING, and CRITICAL thresholds.
12. Capture post-recovery workload status.
13. Record future command output placeholders in `commands.md`.
14. Record future validation results in `validation.md`.
