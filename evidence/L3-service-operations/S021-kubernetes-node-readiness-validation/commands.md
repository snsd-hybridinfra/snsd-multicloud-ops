# Commands

Scenario: S021-kubernetes-node-readiness-validation

Level: L3-service-operations

## Run Static Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-kubernetes-node-readiness.ps1
```

## Run Optional Explicit Live Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-kubernetes-node-readiness.ps1 -LiveKubectl
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L3-service-operations\S021-kubernetes-node-readiness-validation\logs\kubernetes-node-readiness-validation.log
Get-Content evidence\L3-service-operations\S021-kubernetes-node-readiness-validation\configs\kubernetes-node-readiness-summary.md
```

## Safety Notes

Default mode does not invoke kubectl. Live mode is planned only when explicitly requested, runs one read-only node listing, and stores no raw node rows, kubeconfig details, tokens, certificates, endpoints, or addresses.
