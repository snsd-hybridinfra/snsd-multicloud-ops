# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Scenario directory set | Count IDs and check coverage and duplicates. | Exactly 50 unique directories contain S001-S050. | `logs/evidence-directory-structure-validation.log`, `configs/evidence-directory-structure-summary.md` |
| V002 | Evidence directory set | Count IDs and check coverage and duplicates. | Exactly 50 unique directories contain S001-S050. | `logs/evidence-directory-structure-validation.log`, `configs/evidence-directory-structure-summary.md` |
| V003 | Scenario and evidence path mirroring | Compare relative paths. | Every path mirrors one-to-one. | `logs/evidence-directory-structure-validation.log`, `configs/evidence-directory-structure-summary.md` |
| V004 | Required evidence files | Test `commands.md` and `validation.md`. | Both files exist in all evidence directories. | `logs/evidence-directory-structure-validation.log`, `configs/evidence-directory-structure-summary.md` |
| V005 | Required evidence subdirectories | Test `logs`, `screenshots`, and `configs`. | All three directories exist everywhere. | `logs/evidence-directory-structure-validation.log`, `configs/evidence-directory-structure-summary.md` |
| V006 | Sensitive evidence files | Scan evidence filenames and suspected private certificate content. | No forbidden artifact exists. | `logs/evidence-directory-structure-validation.log`, `configs/evidence-directory-structure-summary.md` |
| V007 | Evidence matrix ID coverage | Parse scenario rows. | Matrix contains S001-S050. | `logs/evidence-directory-structure-validation.log`, `configs/evidence-directory-structure-summary.md` |
| V008 | Evidence matrix ID uniqueness | Group parsed IDs. | No duplicate ID exists. | `logs/evidence-directory-structure-validation.log`, `configs/evidence-directory-structure-summary.md` |
| V009 | Evidence readiness status values | Validate all matrix status cells. | Only NOT_READY, PARTIAL, READY, or REVIEWED appears. | `logs/evidence-directory-structure-validation.log`, `configs/evidence-directory-structure-summary.md` |

## Review Notes

All checks are required and any failure produces a non-zero exit.
