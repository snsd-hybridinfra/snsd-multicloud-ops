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

## Real Virtual-Lab Evidence Command Categories

The following placeholder commands document the operator-provided disposable
lab workflow. The repository validator did not execute them. The two `kubectl
exec` commands intentionally toggle only the readiness sentinel file inside one
lab Pod; they do not delete a Pod or test S031 recovery.

```text
kubectl get deploy,rs,pods,svc,ingress,endpoints -n <namespace-placeholder> -o wide
kubectl get endpointslice -n <namespace-placeholder> -l kubernetes.io/service-name=<service-placeholder>
kubectl describe deployment <deployment-placeholder> -n <namespace-placeholder>
kubectl exec -n <namespace-placeholder> <backend-pod-placeholder> -- rm -f /tmp/ready
kubectl exec -n <namespace-placeholder> <backend-pod-placeholder> -- touch /tmp/ready
curl -H "Host: <ingress-host-placeholder>" http://<node-address-placeholder>/
kubectl get events -n <namespace-placeholder> --sort-by=.lastTimestamp
```

The v1 Endpoints command emitted a deprecation warning. EndpointSlice is the
preferred API for future evidence, but degraded per-endpoint readiness must be
captured with a condition-bearing output rather than inferred from a wide list.

Inspect the sanitized state records and summary:

```powershell
Get-Content evidence/L3-service-operations/S025-load-balancing-health-check-validation/logs/20260715-S025-load-balancing-normal-state.sanitized.txt
Get-Content evidence/L3-service-operations/S025-load-balancing-health-check-validation/logs/20260715-S025-unhealthy-backend-exclusion.sanitized.txt
Get-Content evidence/L3-service-operations/S025-load-balancing-health-check-validation/logs/20260715-S025-backend-health-restoration.sanitized.txt
Get-Content evidence/L3-service-operations/S025-load-balancing-health-check-validation/configs/20260715-S025-load-balancing-health-check-validation-summary.md
```

Commit only sanitized output. Do not commit raw response bodies, addresses,
kubeconfig, service-account tokens, certificates, keys, passwords, cookies,
Authorization headers, credentials, or secrets.
