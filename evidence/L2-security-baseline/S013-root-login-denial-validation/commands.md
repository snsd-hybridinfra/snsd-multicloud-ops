# Commands

Scenario: S013-root-login-denial-validation

Level: L2-security-baseline

## Run Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-ssh-root-login-denial-baseline.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L2-security-baseline\S013-root-login-denial-validation\logs\root-login-denial-validation.log
Get-Content evidence\L2-security-baseline\S013-root-login-denial-validation\configs\root-login-denial-summary.md
```

## Safety Notes

No planned command modifies sshd, restarts SSH, performs a root-login or privilege-escalation attempt, connects to a host, reads a key or credential, or requires live network access. The validator reads repository files only.
