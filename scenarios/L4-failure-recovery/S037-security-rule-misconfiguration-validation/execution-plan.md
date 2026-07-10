# Execution Plan

1. Confirm that only placeholder rule names, CIDRs, ports, and resource identifiers are used.
2. Capture the pre-change security rule baseline.
3. Plan a controlled placeholder misconfiguration.
4. Validate public SSH exposure detection.
5. Validate public DB exposure detection.
6. Validate overly broad inbound CIDR detection.
7. Validate required service access breakage detection.
8. Validate unauthorized source access behavior.
9. Validate authorized source access behavior.
10. Document manual rollback decision points.
11. Plan rollback to the pre-change baseline using placeholder actions.
12. Validate post-rollback security rules.
13. Validate post-rollback service reachability.
14. Measure detection and rollback timing against provisional thresholds.
15. Record future command output placeholders in `commands.md`.
16. Record future validation results in `validation.md`.
