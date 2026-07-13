# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-restore-execution.ps1`.
2. Validate artifacts, placeholders, criteria, policy, and debug-only Ansible.
3. Parse precheck, checksum, manual-lab command, positive-size metadata, consistency, manifest fields, and completion summary.
4. Reject real restore/dump/archive artifacts, storage paths/URIs, credentials, or executable restore logic.
5. Review generated log and summary.

All real restore operations are `NOT_RUN`.
