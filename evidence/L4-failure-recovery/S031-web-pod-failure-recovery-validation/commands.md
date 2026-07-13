# Commands

Scenario: S031-web-pod-failure-recovery-validation
Level: L4-failure-recovery
Validation mode executed: Static
LiveKubectl and real fault injection: NOT_RUN

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-web-pod-failure-recovery.ps1
```

Optional read-only validation:

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-web-pod-failure-recovery.ps1 -LiveKubectl -Namespace "snsd-example" -DeploymentName "sample-web-placeholder"
```

Inspect evidence:

```powershell
Get-Content evidence/L4-failure-recovery/S031-web-pod-failure-recovery-validation/logs/web-pod-failure-recovery-validation.log
Get-Content evidence/L4-failure-recovery/S031-web-pod-failure-recovery-validation/configs/web-pod-failure-recovery-summary.md
```

WARNING: `kubectl delete pod` is manual fault injection only, requires separate approval and a disposable lab namespace, and is never executed by this validator. Sanitize all manually collected cluster details before repository review.
