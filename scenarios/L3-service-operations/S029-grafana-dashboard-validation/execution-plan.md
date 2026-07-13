# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-grafana-dashboard.ps1`.
2. Verify five baseline artifacts and three samples.
3. Validate datasource fields and placeholder URL.
4. Parse dashboard JSON and require ten panels, datasource references, metrics, and alert placeholder.
5. Validate matrix and command workflow.
6. Parse search/detail/datasource evidence.
7. Reject credentials, tokens, cookies, authorization, datasource secrets, TLS material, concrete endpoints/domains/addresses, real UIDs/IDs, and mutation/import execution.
8. Review generated log and summary.
9. Optionally run LiveGrafana after explicit approval.

LiveGrafana is `NOT_RUN` in committed Static evidence.
