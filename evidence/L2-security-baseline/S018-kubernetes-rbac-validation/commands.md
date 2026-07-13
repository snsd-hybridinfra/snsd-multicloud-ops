# Commands

Scenario: S018-kubernetes-rbac-validation

Level: L2-security-baseline

## Run Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-kubernetes-rbac-baseline.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L2-security-baseline\S018-kubernetes-rbac-validation\logs\kubernetes-rbac-validation.log
Get-Content evidence\L2-security-baseline\S018-kubernetes-rbac-validation\configs\kubernetes-rbac-summary.md
```

## Safety Notes

These commands do not run kubectl, read kubeconfig, connect to a cluster, query an API server, apply manifests, read credentials, or contact external systems. No planned or `NOT_RUN` live-cluster output is required.
