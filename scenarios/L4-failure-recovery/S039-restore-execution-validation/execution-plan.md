# Execution Plan

1. Confirm that only placeholder backup paths, filenames, restore targets, and logs are used.
2. Select the backup artifact from `<backup-root>`.
3. Verify the backup checksum using `<checksum-file>`.
4. Confirm the restore target `<restore-target>`.
5. Plan the MariaDB logical restore placeholder.
6. Plan the Kubernetes manifest restore placeholder.
7. Plan the Nginx configuration restore placeholder.
8. Plan the observability configuration restore placeholder.
9. Capture restore command or runbook invocation placeholders.
10. Capture restore execution log placeholders.
11. Perform restore result sanity check planning.
12. Define restore abort conditions.
13. Define restore rollback placeholders.
14. Record future command output placeholders in `commands.md`.
15. Record future validation results in `validation.md`.
