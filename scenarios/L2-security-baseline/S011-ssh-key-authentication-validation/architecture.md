# Architecture

## Repository Components

- `ssh-key-authentication-baseline.md`: administrative access and key-management rules.
- `sshd_config.key-auth.example`: non-production example directives.
- `validate-ssh-key-authentication-baseline.ps1`: local completeness, key-safety, secret, and execution-boundary checks.
- S011 evidence directory: generated log and summary.

## Baseline Model

Administrative access uses public-key authentication through the bastion model. Password, root, challenge-response, and keyboard-interactive authentication are disabled in the example. Key contents, real users, and real paths remain outside the repository.

## Validation Flow

The validator reads the baseline files, verifies required settings and policy text, scans repository filenames and selected text for key material, checks for `authorized_keys`, and prevents active SSH-related commands. It does not inspect or change a running SSH service.
