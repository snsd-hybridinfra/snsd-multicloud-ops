# Commands

Scenario: S025-load-balancing-health-check-validation
Level: L3-service-operations
Validation mode executed: Static

## Static Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-load-balancing-health-check.ps1
```

## Optional Live HTTP Validation

Run only after explicit approval:

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-load-balancing-health-check.ps1 -LiveHttp -LoadBalancerHealthUrl "http://<load-balancer-placeholder>/health" -BackendHealthUrls "http://<backend-a-placeholder>/health","http://<backend-b-placeholder>/health"
```

Optional LiveHttp is `NOT_RUN` for committed Static evidence. It sends cookie-free HEAD requests and stores no target, header, body, or credential.

## Inspect Evidence

```powershell
Get-Content evidence/L3-service-operations/S025-load-balancing-health-check-validation/logs/load-balancing-health-check-validation.log
Get-Content evidence/L3-service-operations/S025-load-balancing-health-check-validation/configs/load-balancing-health-check-summary.md
```

The generated `.log` is ignored; the summary and three samples are committed.
