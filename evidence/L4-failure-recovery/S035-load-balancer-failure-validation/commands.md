# Commands

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-load-balancer-failure.ps1
powershell -ExecutionPolicy Bypass -File tools/validate-load-balancer-failure.ps1 -LiveHttp -LoadBalancerUrl "http://<load-balancer-url-placeholder>" -BackendAUrl "http://<backend-a-url-placeholder>" -BackendBUrl "http://<backend-b-url-placeholder>"
Get-Content evidence/L4-failure-recovery/S035-load-balancer-failure-validation/logs/load-balancer-failure-validation.log
Get-Content evidence/L4-failure-recovery/S035-load-balancer-failure-validation/configs/load-balancer-failure-summary.md
```

LiveHttp and service actions are `NOT_RUN` in committed evidence. Stop/start are MANUAL FAULT/RECOVERY ONLY and never validator-executed.
