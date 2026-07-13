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

## Safety Notes

Default mode invokes neither kubectl nor curl. Live mode is planned only when explicitly requested, runs four read-only queries, and stores no raw resource rows, kubeconfig details, tokens, certificates, TLS keys, endpoints, or secrets.
