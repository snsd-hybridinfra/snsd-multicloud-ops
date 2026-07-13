# Commands

Scenario: S007-multi-cloud-inventory-validation

Level: L1-foundation

## Run Validation

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-multicloud-inventory.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L1-foundation\S007-multi-cloud-inventory-validation\logs\multicloud-inventory-validation.log
Get-Content evidence\L1-foundation\S007-multi-cloud-inventory-validation\configs\multicloud-inventory-summary.md
```

## Safety Notes

No planned command executes Ansible, connects to a host, reads a key or credential, resolves DNS, or queries a cloud provider, cluster, OpenStack endpoint, or EVE-NG lab. The validator reads repository text only.
