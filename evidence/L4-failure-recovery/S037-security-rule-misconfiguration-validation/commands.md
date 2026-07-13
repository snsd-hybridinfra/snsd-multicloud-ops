# Commands

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-security-rule-misconfiguration.ps1
Get-Content evidence/L4-failure-recovery/S037-security-rule-misconfiguration-validation/logs/security-rule-misconfiguration-validation.log
Get-Content evidence/L4-failure-recovery/S037-security-rule-misconfiguration-validation/configs/security-rule-misconfiguration-summary.md
```

To collect future evidence, use only a separately approved disposable lab and sanitize every identifier/network value. Real SG, NSG, OpenStack SG, firewall, NetworkPolicy, Terraform, and routing modification is out of scope. Rollback is sanitized sample evidence only. All cloud/network actions are `NOT_RUN` by this validator.
