# Commands

Scenario: S003-aws-network-provisioning-validation

Level: L1-foundation

Target: repository-side AWS network Terraform definitions

## Run Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-aws-network-provisioning.ps1
```

## Inspect Generated Log

```powershell
Get-Content evidence\L1-foundation\S003-aws-network-provisioning-validation\logs\aws-network-provisioning-validation.log
```

## Inspect Generated Summary

```powershell
Get-Content evidence\L1-foundation\S003-aws-network-provisioning-validation\configs\aws-network-provisioning-summary.md
```

## Safety Notes

No planned command runs Terraform init, validate, plan, apply, or destroy; authenticates to AWS; reads credentials; configures a backend; or accesses cloud APIs.
