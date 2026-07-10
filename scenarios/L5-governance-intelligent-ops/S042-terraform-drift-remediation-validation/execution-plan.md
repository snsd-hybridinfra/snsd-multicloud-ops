# Execution Plan

1. Confirm that S041 drift detection evidence is available or mark the remediation workflow as blocked.
2. Identify `<terraform-env>`, `<provider>`, `<resource-name>`, and `<drifted-resource>` using placeholders only.
3. Record `<expected-state>` and `<actual-state>` from sanitized drift evidence.
4. Draft `<remediation-plan>` and record why Terraform remediation is or is not safe.
5. Review Terraform plan placeholder output before remediation.
6. Record the manual approval placeholder and remediation decision state.
7. Document Terraform apply placeholder behavior without running real Terraform against cloud accounts.
8. Map AWS, Azure, OpenStack, security rule, tag/label, network route, and subnet remediation placeholders.
9. Review post-remediation Terraform plan placeholder output.
10. Classify the remediation result as `REMEDIATION_READY`, `REMEDIATION_APPLIED`, `REMEDIATION_BLOCKED`, `REMEDIATION_FAILED`, or `OUT_OF_SCOPE`.
11. Capture TODO evidence references in `commands.md`, `validation.md`, `configs/`, `logs/`, and `screenshots/`.

No real Terraform commands are executed as part of this skeleton.
