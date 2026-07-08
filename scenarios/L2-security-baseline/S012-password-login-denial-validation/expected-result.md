# Expected Result

## Success Conditions

- `PasswordAuthentication` denial validation is documented.
- `sshd -T` effective configuration validation is documented.
- Password login denial is planned for Bastion, on-prem, AWS, Azure, and OpenStack targets.
- Authentication failure evidence capture is planned.
- SSH key authentication success is explicitly separated to S011.
- Root login denial is explicitly separated to S013.
- No passwords, private keys, credentials, public IPs, or account-specific values are added.

## Required Evidence

- `commands.md`
- `validation.md`
- `configs/sshd-password-authentication-summary.md`
- `configs/sshd-effective-config-summary.md`
- `logs/password-login-denial-validation.log`
- `screenshots/password-login-denial-test.png`

## Completion Criteria

The scenario can move from `PLANNED` to `VALIDATED` only after approved, sanitized evidence confirms password login denial across planned targets.
