# Validation Plan

Implemented checks: `V001` required artifacts, `V002` command safety, `V003` schema, `V004` rules/mappings, `V005` inputs, `V006` load, `V007` pass, `V008` fail, `V009` exception, `V010` classification, `V011` summary, `V012` manifest, `V013` Terraform artifact safety, `V014` sensitive safety, `V015` execution safety, and `V016` evidence maturity.

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Policy input artifact validation plan | Review placeholder policy input artifacts. | Policy input is identified or marked missing. | `commands.md`, `configs/policy-as-code-summary.md`, `validation.md` |
| V002 | Public SSH exposure policy validation plan | Check `<denied-cidr>` and SSH rule placeholders. | Public SSH exposure is prohibited. | `commands.md`, `configs/policy-control-mapping.md`, `validation.md` |
| V003 | Public DB port exposure policy validation plan | Check DB port policy placeholders. | Public DB exposure is prohibited. | `commands.md`, `configs/policy-control-mapping.md`, `validation.md` |
| V004 | Least privilege security rule policy validation plan | Review security rule policy placeholders. | Security rule scope is least privilege. | `configs/policy-control-mapping.md`, `validation.md` |
| V005 | Required tag or label policy validation plan | Review `<required-tag>` placeholder. | Required tag or label is present or violation is recorded. | `configs/policy-control-mapping.md`, `validation.md` |
| V006 | Resource naming convention policy validation plan | Compare `<resource-name>` against naming rules. | Naming convention result is recorded. | `configs/policy-control-mapping.md`, `validation.md` |
| V007 | Approved region or zone placeholder policy validation plan | Review approved location placeholder. | Region or zone result is recorded without account-specific values. | `configs/policy-control-mapping.md`, `validation.md` |
| V008 | Terraform configuration policy placeholder validation plan | Review Terraform-managed resource placeholder. | Terraform configuration policy result is recorded without running Terraform. | `commands.md`, `configs/policy-as-code-summary.md`, `validation.md` |
| V009 | Cost guardrail reference validation plan | Reference S045 boundary. | Cost policy remains a reference and is not validated here. | `configs/policy-as-code-summary.md`, `validation.md` |
| V010 | Policy judgment state validation plan | Apply policy judgment states. | Result is classified as `POLICY_PASS`, `POLICY_FAIL`, `POLICY_WARNING`, `POLICY_NOT_APPLICABLE`, or `POLICY_INCONCLUSIVE`. | `configs/policy-judgment-model.md`, `validation.md` |
| V011 | Policy evidence capture plan | Review required command, config, log, screenshot, and validation evidence. | Policy evidence is mapped and reviewable. | `commands.md`, `logs/policy-as-code-validation.log`, `screenshots/policy-validation-result.png`, `screenshots/policy-violation-example.png`, `validation.md` |
| V012 | Failure condition for missing policy input, public SSH allowed, public DB allowed, missing required tag, naming violation, ambiguous result, unsupported policy claim, or missing evidence | Evaluate findings against explicit failure conditions. | Policy issues produce `FAIL` or `BLOCKED` status. | `validation.md` |

Every validation item must map to evidence. This scenario validates the policy governance model only.
