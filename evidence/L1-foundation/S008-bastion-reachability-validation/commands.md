# Commands

Scenario: S008-bastion-reachability-validation

Level: L1-foundation

## Run Validation

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-bastion-reachability-model.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L1-foundation\S008-bastion-reachability-validation\logs\bastion-reachability-validation.log
Get-Content evidence\L1-foundation\S008-bastion-reachability-validation\configs\bastion-reachability-summary.md
```

## Safety Notes

No planned command executes SSH or Ansible, connects to a host, reads a key or credential, resolves DNS, tests a port, or queries a cloud provider, cluster, OpenStack endpoint, or EVE-NG lab. The validator reads repository text only.
