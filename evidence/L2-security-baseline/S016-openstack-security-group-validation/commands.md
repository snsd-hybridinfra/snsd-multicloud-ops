# Commands

Scenario: S016-openstack-security-group-validation

Level: L2-security-baseline

## Run Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-openstack-security-group-baseline.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L2-security-baseline\S016-openstack-security-group-validation\logs\openstack-security-group-validation.log
Get-Content evidence\L2-security-baseline\S016-openstack-security-group-validation\configs\openstack-security-group-summary.md
```

## Safety Notes

These commands do not authenticate to OpenStack, invoke OpenStack CLI, query Security Groups, initialize Terraform, create a plan, apply changes, read credentials, or contact external systems. No planned or `NOT_RUN` live-cloud output is required.
