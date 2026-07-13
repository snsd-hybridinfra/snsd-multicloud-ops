# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-backup-creation.ps1`.
2. Validate artifacts, placeholders, criteria, retention policy, and debug-only Ansible.
3. Parse completion, metadata/size, checksum, listing, manifest fields, and final summary.
4. Reject real backup/dump/archive files, storage paths/URIs, credentials, or executable backup logic.
5. Review generated log and summary.

All real backup operations are `NOT_RUN`.
