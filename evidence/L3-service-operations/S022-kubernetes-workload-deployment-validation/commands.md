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

## Real-Lab Evidence Command Categories

The following commands describe the operator-provided disposable-lab workflow.
They are references for evidence interpretation; this repository validation did
not execute them. Substitute placeholders locally and sanitize all output before
commit.

```text
kubectl create namespace <namespace-placeholder>
kubectl apply -f <workload-manifest-placeholder>
kubectl get deploy -n <namespace-placeholder> -o wide
kubectl get rs -n <namespace-placeholder> -o wide
kubectl get pods -n <namespace-placeholder> -o wide
kubectl get svc -n <namespace-placeholder> -o wide
kubectl get events -n <namespace-placeholder> --sort-by=.lastTimestamp
```

Inspect the sanitized real-lab evidence and its judgment summary:

```powershell
Get-Content evidence\L3-service-operations\S022-kubernetes-workload-deployment-validation\logs\20260714-S022-kubernetes-workload-deployment.sanitized.txt
Get-Content evidence\L3-service-operations\S022-kubernetes-workload-deployment-validation\configs\20260714-S022-kubernetes-workload-deployment-validation-summary.md
```

## Safety Notes

Default mode does not invoke kubectl. Live mode is planned only when explicitly requested, runs two read-only listings, and stores no raw workload rows, kubeconfig details, tokens, certificates, endpoints, or secrets. The 2026-07-14 real-lab record was prepared from user-provided output after execution; raw output, kubeconfig, service-account tokens, certificates, keys, passwords, and secrets are not committed.
