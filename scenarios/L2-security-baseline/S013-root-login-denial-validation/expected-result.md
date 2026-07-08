# Expected Result

## Success Conditions

- `PermitRootLogin` denial validation is documented.
- `sshd -T` effective configuration validation is documented.
- Direct root login denial is planned for Bastion, on-prem, AWS, Azure, and OpenStack targets.
- Authentication failure evidence capture is planned.
- SSH key authentication success is explicitly separated to S011.
- Password login denial is explicitly separated to S012.
- Sudo policy validation is explicitly excluded.
- No passwords, private keys, credentials, public IPs, or account-specific values are added.

## Required Evidence

- `commands.md`
- `validation.md`
- `configs/sshd-root-login-summary.md`
- `configs/sshd-effective-config-summary.md`
- `logs/root-login-denial-validation.log`
- `screenshots/root-login-denial-test.png`

## Completion Criteria

The scenario can move from `PLANNED` to `VALIDATED` only after approved, sanitized evidence confirms direct root login denial across planned targets.
