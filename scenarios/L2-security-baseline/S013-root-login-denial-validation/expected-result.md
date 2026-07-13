# Expected Result

## Success Conditions

- Both baseline files exist and the example is marked non-production.
- All six required sshd directives and root-denial policy statements exist.
- No enabled root login, root-password value, private key, `authorized_keys`, sensitive value, account identifier, or prohibited execution command is detected.
- The validator exits zero and generates evidence.

## Required Evidence

- `logs/root-login-denial-validation.log`
- `configs/root-login-denial-summary.md`
- `commands.md`
- `validation.md`

The result proves repository baseline safety only; it does not prove live root-login denial or privilege controls.
