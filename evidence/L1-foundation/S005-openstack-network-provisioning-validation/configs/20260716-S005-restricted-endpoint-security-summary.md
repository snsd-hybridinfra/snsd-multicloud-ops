# S005 Restricted OpenStack Validation Endpoint Summary

## Authority and Scope

- Validation date: 2026-07-16
- Validation mode: Codex-executed, forced-command, read-only inspection
- Local entry point: SSH alias `openstack-validator`
- Remote account: dedicated restricted validator account
- Allowed original command: `validate-all` only
- OpenStack credential content exposed: no
- SSH private key stored in repository: no

## Installed Boundary

| Control | Result |
|---|---|
| Dedicated ED25519 identity outside repository | PASS |
| Forced dispatcher command | PASS |
| Empty/interactive request denied | PASS |
| Arbitrary command denied | PASS |
| Credential-file read request denied | PASS |
| Agent forwarding disabled | PASS |
| Port forwarding disabled | PASS |
| X11 forwarding disabled | PASS |
| PTY disabled | PASS |
| User SSH startup file disabled | PASS |
| Sudo limited to the root-owned read-only validator | PASS |
| Validator and dispatcher syntax checks | PASS |
| Validator ownership/mode: root-owned, `0755` | PASS |
| Sudoers syntax and exact-command rule | PASS |

## Access Cleanup

The audited obsolete unrestricted validation key was backed up and removed
from the bootstrap account only after the new endpoint and all boundary tests
passed. Both the dedicated restricted key and the obsolete key were then
denied for direct bootstrap-account login. The restricted alias continued to
run `validate-all` successfully. Unrelated keys were not modified.

## Live Result

| Item | Result |
|---|---|
| Read-only checks passed | 50 |
| Read-only checks failed | 0 |
| Command exit status | 0 |
| Interactive shell | BLOCKED |
| Harmless arbitrary command | BLOCKED |
| Direct credential-read request | BLOCKED |

## Final Judgment

`READY`: the endpoint provides one non-interactive, read-only validation path
and does not grant general shell, arbitrary sudo, credential access, forwarding,
or OpenStack/Docker/Kolla mutation authority.
