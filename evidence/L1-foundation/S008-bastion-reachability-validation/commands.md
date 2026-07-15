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

## Lab Phase 2 Manual Evidence Collection

The commands below are for a separately authorized disposable lab. They are not executed by `validate-bastion-reachability-model.ps1`, and their output is not considered committed evidence until it has been sanitized and reviewed.

Confirm the Host PC SSH client:

```powershell
Get-Command ssh
ssh -V
```

Collect a minimal read-only result manually:

```powershell
ssh -o BatchMode=yes -o StrictHostKeyChecking=yes <ssh-user-placeholder>@<bastion-ip-placeholder> "hostname; whoami; uptime; systemctl is-active ssh"
```

Or use the non-production sample collector with an output directory outside the repository:

```powershell
powershell -ExecutionPolicy Bypass -File tools\collect-bastion-evidence.example.ps1 `
  -BastionHost '<bastion-ip-placeholder>' `
  -SshUser '<ssh-user-placeholder>' `
  -OutputRoot '<local-output-root-placeholder>'
```

Inspect the generated `.sanitized.txt` file in the external output directory, then copy only the reviewed sanitized file to:

```text
<evidence-path>/logs/
```

Never commit the `.raw.txt` file. The collector uses `BatchMode=yes`, does not prompt for a password, and does not read private keys, `/etc/shadow`, tokens, cloud credentials, kubeconfig, or secret stores.
