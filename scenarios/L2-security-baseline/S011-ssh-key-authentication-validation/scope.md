# Scope

## Included

- SSH key-authentication baseline documentation.
- Non-production sshd example settings.
- Public-key authentication, password denial, root denial, challenge-response denial, keyboard-interactive denial, and authorized-keys path references.
- Bastion, public-key placement, private-key storage, rotation, authorized-user, and evidence placeholders.
- Repository-wide private-key filename/material and `authorized_keys` filename checks.
- Local sensitive-content and execution-command checks.
- Generated log and summary evidence.

## Excluded

- Modification of local or remote sshd configuration.
- SSH service restart or reload.
- Live SSH connection or authentication tests.
- Real private or public keys, `authorized_keys` content, usernames, passwords, paths, and credentials.
- Password-login enforcement validation, which belongs to S012.
- Root-login enforcement validation, which belongs to S013.
- Bastion reachability, which belongs to S008.
- Cloud security-group validation, which belongs to S014-S016.

## Assumptions

- The example represents a review baseline and is not directly deployable.
- Required denial settings are references here; scenario-specific enforcement remains separate.
