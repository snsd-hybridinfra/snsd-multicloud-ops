# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-security-rule-misconfiguration.ps1`.
2. Validate artifacts, placeholders/exclusions, criteria, rollback matrix, policy metadata, and command boundaries.
3. Parse least-privilege pre-state, manual misconfiguration, detection, impact, manual rollback, safe post-state, and final summary.
4. Warn when temporary-exception expiry remains placeholder-only.
5. Reject unsafe post-state, missing rollback/policy metadata, concrete identifiers/network values, secrets, or executable control-plane commands.
6. Review generated log and summary.

Cloud/network modifications are `NOT_RUN`.
