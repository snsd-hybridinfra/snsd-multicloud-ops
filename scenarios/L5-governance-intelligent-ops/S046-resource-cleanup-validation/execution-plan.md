# Execution Plan

1. Confirm that cleanup validation is governance review only.
2. Identify `<provider>`, `<resource-name>`, `<resource-id>`, `<resource-type>`, `<environment>`, `<cleanup-candidate>`, and `<cleanup-decision>`.
3. Review cleanup input artifact placeholders.
4. Review resource inventory placeholders.
5. Validate resource ownership.
6. Validate environment tag or label.
7. Review resource usage state.
8. Review dependency impact.
9. Document cleanup candidate status.
10. Document manual cleanup approval decision.
11. Document cleanup command or runbook placeholder without execution.
12. Plan post-cleanup inventory validation.
13. Document rollback or recreation notes where applicable.
14. Classify each result as `CLEANUP_NOT_REQUIRED`, `CLEANUP_CANDIDATE`, `CLEANUP_APPROVED`, `CLEANUP_COMPLETED`, `CLEANUP_BLOCKED`, or `CLEANUP_INCONCLUSIVE`.
15. Capture TODO evidence references in `commands.md`, `validation.md`, `configs/`, `logs/`, and `screenshots/`.

No real Terraform destroy, cloud delete, Kubernetes delete, or cleanup command is executed in this skeleton.
