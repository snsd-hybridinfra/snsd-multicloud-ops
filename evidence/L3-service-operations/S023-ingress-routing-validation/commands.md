# Commands

Scenario: S023-ingress-routing-validation

Level: L3-service-operations

## Run Static Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-ingress-routing.ps1
```

## Run Optional Explicit Live Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-ingress-routing.ps1 -LiveKubectl
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L3-service-operations\S023-ingress-routing-validation\logs\ingress-routing-validation.log
Get-Content evidence\L3-service-operations\S023-ingress-routing-validation\configs\ingress-routing-summary.md
```

## Real-Lab Evidence Command Categories

The following placeholder commands document the operator-provided local-lab
workflow. They were not executed by the repository validator. Sanitize every
captured value before commit.

```text
kubectl get deploy,rs,pods,svc,ingress -n <namespace-placeholder> -o wide
kubectl describe ingress <ingress-name-placeholder> -n <namespace-placeholder>
kubectl get pods -n kube-system
curl -I -H "Host: <ingress-host-placeholder>" http://<k3s-node-ip-placeholder>/
curl -s -H "Host: <ingress-host-placeholder>" http://<k3s-node-ip-placeholder>/
kubectl get events -n <namespace-placeholder> --sort-by=.lastTimestamp
```

Inspect the sanitized real-lab record:

```powershell
Get-Content evidence\L3-service-operations\S023-ingress-routing-validation\logs\20260714-S023-ingress-routing.sanitized.txt
Get-Content evidence\L3-service-operations\S023-ingress-routing-validation\configs\20260714-S023-ingress-routing-validation-summary.md
```

## Safety Notes

Default mode invokes neither kubectl nor curl. Live mode is planned only when explicitly requested, runs four read-only queries, and stores no raw resource rows, kubeconfig details, tokens, certificates, TLS keys, endpoints, or secrets. The dated real-lab record was derived from operator-provided output after execution. It validates local-lab routing only and does not demonstrate public internet exposure.
