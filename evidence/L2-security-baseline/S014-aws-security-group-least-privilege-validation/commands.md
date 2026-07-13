# Commands

Scenario: S014-aws-security-group-least-privilege-validation

Level: L2-security-baseline

## Run Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-aws-security-group-least-privilege.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L2-security-baseline\S014-aws-security-group-least-privilege-validation\logs\aws-security-group-least-privilege-validation.log
Get-Content evidence\L2-security-baseline\S014-aws-security-group-least-privilege-validation\configs\aws-security-group-least-privilege-summary.md
```

## Safety Notes

No planned command authenticates to AWS, runs AWS CLI, queries Security Groups, initializes Terraform, creates a plan, applies changes, reads credentials, or contacts external systems. The validator reads repository files only.
