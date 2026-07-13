# Commands

Scenario: S024-nginx-reverse-proxy-validation
Level: L3-service-operations
Validation mode executed: Static

## Static Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-nginx-reverse-proxy.ps1
```

This is the default and performs no Nginx, curl, or network execution.

## Optional Live HTTP Validation

Run only after explicit approval with a safe operator-supplied target:

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-nginx-reverse-proxy.ps1 -LiveHttp -TargetUrl "http://<reverse-proxy-host-placeholder>/"
```

This optional action is `NOT_RUN` for the committed Static evidence. The validator sends one HEAD request without credentials, cookies, or authorization and does not retain the target, body, or headers.

## Inspect Evidence

```powershell
Get-Content evidence/L3-service-operations/S024-nginx-reverse-proxy-validation/logs/nginx-reverse-proxy-validation.log
Get-Content evidence/L3-service-operations/S024-nginx-reverse-proxy-validation/configs/nginx-reverse-proxy-summary.md
```

The generated `.log` is ignored by Git. The summary and three sanitized `.sample.txt` files are the committed evidence.
