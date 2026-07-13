# Expected Result

## Success Conditions

- Both SSH baseline files exist and the example is marked non-production.
- All six required sshd settings and baseline policy statements exist.
- No private-key filename, private-key material, or `authorized_keys` file exists.
- No sensitive value, account identifier, numeric IP, real key, or prohibited execution command is detected.
- The validator exits zero and generates evidence.

## Required Evidence

- `logs/ssh-key-authentication-validation.log`
- `configs/ssh-key-authentication-summary.md`
- `commands.md`
- `validation.md`

The result proves repository baseline safety only; it does not prove live SSH authentication or enforcement.
