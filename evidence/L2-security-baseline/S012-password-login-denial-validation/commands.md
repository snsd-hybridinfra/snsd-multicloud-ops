# Commands

Scenario: S012-password-login-denial-validation

Level: L2-security-baseline

## Run Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-ssh-password-login-denial-baseline.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L2-security-baseline\S012-password-login-denial-validation\logs\password-login-denial-validation.log
Get-Content evidence\L2-security-baseline\S012-password-login-denial-validation\configs\password-login-denial-summary.md
```

## Safety Notes

No planned command modifies sshd, restarts SSH, performs a password-login attempt, connects to a host, reads a key or credential, or requires live network access. The validator reads repository files only.
