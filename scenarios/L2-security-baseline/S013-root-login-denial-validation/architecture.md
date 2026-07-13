# Architecture

## Repository Components

- `ssh-root-login-denial-baseline.md`: root denial, non-root administration, sudo, storage, placeholder, and evidence rules.
- `sshd_config.root-login-denial.example`: non-production denial directives.
- `validate-ssh-root-login-denial-baseline.ps1`: directive, root-password, key-safety, secret, and execution-boundary checks.
- S013 evidence directory: generated log and summary.

## Baseline Model

Direct root login is denied. Administrators use an approved non-root placeholder and controlled privilege escalation. Public-key authentication remains required while password and interactive methods remain disabled.

## Validation Flow

The validator reads the two baseline files, verifies directives and policy statements, scans for enabled root login and root-password values, checks repository key safety, and prevents active SSH or sudo commands. It does not inspect or change a running SSH service.
