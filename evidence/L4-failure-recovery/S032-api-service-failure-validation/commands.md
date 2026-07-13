# Commands

## Static validation

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-api-service-failure.ps1
```

## Optional read-only modes

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-api-service-failure.ps1 -LiveKubectl -Namespace "snsd-example" -DeploymentName "sample-api-placeholder" -ServiceName "sample-api-service-placeholder"
powershell -ExecutionPolicy Bypass -File tools/validate-api-service-failure.ps1 -LiveHttp -ApiHealthUrl "http://<api-url-placeholder>/health"
```

## Inspect generated evidence

```powershell
Get-Content evidence/L4-failure-recovery/S032-api-service-failure-validation/logs/api-service-failure-validation.log
Get-Content evidence/L4-failure-recovery/S032-api-service-failure-validation/configs/api-service-failure-summary.md
```

Manual collection must use a disposable lab, sanitize all output, and store no payloads or credentials. `kubectl delete pod` and `kubectl scale --replicas=0` are MANUAL FAULT INJECTION ONLY and are never executed by the validator.

LiveKubectl and LiveHttp output are `NOT_RUN` in the committed Static result.
