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

## Real Virtual-Lab Evidence Command Categories

The following placeholder commands document the operator-provided local-lab
workflow. They were not executed by the repository validator. Sanitize all
captured values before commit.

```text
kubectl get deploy,rs,pods,svc,ingress,endpoints -n <namespace-placeholder> -o wide
kubectl describe svc <service-placeholder> -n <namespace-placeholder>
kubectl describe ingress <ingress-placeholder> -n <namespace-placeholder>
curl -i -H "Host: <ingress-host-placeholder>" http://<node-address-placeholder>/
curl -i -H "Host: <ingress-host-placeholder>" http://<node-address-placeholder>/healthz
kubectl logs -n <namespace-placeholder> deployment/<deployment-placeholder>
kubectl get events -n <namespace-placeholder> --sort-by=.lastTimestamp
```

The supplied evidence did not include Nginx or Traefik log output. No log result
is inferred. The v1 Endpoints warning is retained only as a non-blocking API
deprecation note; future collection should prefer EndpointSlice.

Inspect the sanitized real-lab record:

```powershell
Get-Content evidence/L3-service-operations/S024-nginx-reverse-proxy-validation/logs/20260715-S024-nginx-reverse-proxy.sanitized.txt
Get-Content evidence/L3-service-operations/S024-nginx-reverse-proxy-validation/configs/20260715-S024-nginx-reverse-proxy-validation-summary.md
```

Only aggregate and masked response judgments are committed. Raw terminal output,
target addresses, response bodies, kubeconfig, tokens, credentials, certificates,
keys, passwords, cookies, Authorization headers, and secrets are not committed.
