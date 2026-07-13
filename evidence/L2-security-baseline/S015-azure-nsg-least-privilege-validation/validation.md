# Validation

Scenario: S015-azure-nsg-least-privilege-validation

Level: L2-security-baseline

Date: 2026-07-13

Overall status: PASS

| Check ID | Validation Item | Expected Condition | Actual Result | Evidence File | Status |
|---|---|---|---|---|---|
| V001 | Least privilege baseline | File exists. | Baseline exists. | generated log and summary | PASS |
| V002 | NSG rule matrix | File exists. | Matrix exists. | generated log and summary | PASS |
| V003 | Required NSG placeholders | Five NSGs exist. | All are documented. | generated log and summary | PASS |
| V004 | Least privilege statements | Required statements exist. | All are documented. | generated log and summary | PASS |
| V005 | Terraform NSG placeholder | Safe structure exists. | NSG, association, and documented rule intent exist. | generated log and summary | PASS |
| V006 | Terraform state and variables | No unsafe artifact exists. | None detected. | generated log and summary | PASS |
| V007 | Azure identity and secret safety | No forbidden content exists. | None detected. | generated log and summary | PASS |
| V008 | Public IP safety | No real public address exists. | None detected. | generated log and summary | PASS |
| V009 | Dangerous public inbound rules | No dangerous port is public. | None detected. | generated log and summary | PASS |
| V010 | Public web exception | Only public-web 80/443 is public. | Exception is correctly limited. | generated log and summary | PASS |
| V011 | Egress justification | Egress is documented. | Policy and review row exist. | generated log and summary | PASS |
| V012 | Remote backend | No backend exists. | None detected. | generated log and summary | PASS |
| V013 | Execution safety boundary | No live Azure or Terraform mutation exists. | None detected. | generated log and summary | PASS |

## Generated Result

All thirteen checks passed using repository files only. Evidence is recorded in `logs/azure-nsg-least-privilege-validation.log` and `configs/azure-nsg-least-privilege-summary.md`.
