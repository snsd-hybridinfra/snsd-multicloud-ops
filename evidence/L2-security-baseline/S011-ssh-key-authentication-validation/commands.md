# Commands

Scenario: S011-ssh-key-authentication-validation

Level: L2-security-baseline

## Run Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-ssh-key-authentication-baseline.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L2-security-baseline\S011-ssh-key-authentication-validation\logs\ssh-key-authentication-validation.log
Get-Content evidence\L2-security-baseline\S011-ssh-key-authentication-validation\configs\ssh-key-authentication-summary.md
```

## Safety Notes

No planned command modifies sshd configuration, restarts SSH, connects to a host, reads a private key or credential, or requires live network access. The validator reads repository files only.
