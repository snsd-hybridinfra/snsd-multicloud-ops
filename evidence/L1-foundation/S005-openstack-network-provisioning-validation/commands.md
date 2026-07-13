# Commands

Scenario: S005-openstack-network-provisioning-validation

Level: L1-foundation

## Run Validation

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-openstack-network-provisioning.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L1-foundation\S005-openstack-network-provisioning-validation\logs\openstack-network-provisioning-validation.log
Get-Content evidence\L1-foundation\S005-openstack-network-provisioning-validation\configs\openstack-network-provisioning-summary.md
```

## Safety Notes

No planned command authenticates to OpenStack, reads credentials, `clouds.yaml`, openrc, or kubeconfig, contacts cloud APIs, or runs Terraform init, validate, plan, apply, or destroy. The validator reads repository files and optionally runs `terraform fmt -check` only.
