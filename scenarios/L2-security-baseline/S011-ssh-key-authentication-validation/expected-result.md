# Expected Result

## Success Conditions

- SSH key authentication plan is documented for Control Plane to Bastion.
- SSH key authentication plan is documented for Bastion to on-prem DB and monitoring nodes.
- SSH key authentication plan is documented for Bastion to AWS, Azure, and OpenStack service nodes.
- SSH ProxyJump command pattern is documented using placeholders only.
- Private key permission and public key placement validation plans are defined.
- Password login denial and root login denial are explicitly excluded from S011.
- No real private keys, credentials, public IPs, or account-specific values are added.

## Required Evidence

- `commands.md`
- `validation.md`
- `configs/ssh-key-authentication-plan.md`
- `configs/ssh-proxyjump-pattern-summary.md`
- `logs/ssh-key-authentication-validation.log`
- `screenshots/ssh-key-authentication-test.png`

## Completion Criteria

The scenario can move from `PLANNED` to `VALIDATED` only after approved, sanitized evidence confirms SSH key authentication checks. Real private keys must never be committed.
