# Expected Result

## Success Conditions

- Both baseline files exist and the example is marked non-production.
- All five required sshd directives and policy statements exist.
- No enabled password authentication, password value, private key, `authorized_keys`, sensitive value, account identifier, or prohibited execution command is detected.
- The validator exits zero and generates evidence.

## Required Evidence

- `logs/password-login-denial-validation.log`
- `configs/password-login-denial-summary.md`
- `commands.md`
- `validation.md`

The result proves repository baseline safety only; it does not prove live password denial or SSH enforcement.
