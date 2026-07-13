# Commands

Scenario: S022-kubernetes-workload-deployment-validation

Level: L3-service-operations

## Run Static Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-kubernetes-workload-deployment.ps1
```

## Run Optional Explicit Live Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-kubernetes-workload-deployment.ps1 -LiveKubectl
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L3-service-operations\S022-kubernetes-workload-deployment-validation\logs\kubernetes-workload-deployment-validation.log
Get-Content evidence\L3-service-operations\S022-kubernetes-workload-deployment-validation\configs\kubernetes-workload-deployment-summary.md
```

## Safety Notes

Default mode does not invoke kubectl. Live mode is planned only when explicitly requested, runs two read-only listings, and stores no raw workload rows, kubeconfig details, tokens, certificates, endpoints, or secrets.
