# Scope Boundary Review

The QA check distinguishes an unsupported capability claim from a term used in an exclusion, failure condition, or out-of-scope statement.

## Unsupported Claim Checks

| Unsupported Claim Check | Result | Affected File Or Scenario | Recommended Correction | Severity |
|---|---|---|---|---|
| Production-grade HA | PASS | retired-numbered-case contains explicit exclusion language | Keep as an exclusion; fail QA if later asserted as implemented | LOW |
| Automatic DR | PASS | retired-numbered-case contains explicit exclusion language | Keep recovery validation manual and scenario-bounded | LOW |
| Automatic cross-cloud failover | PASS | retired-numbered-case, retired-numbered-case, retired-numbered-case, retired-numbered-case, retired-numbered-case contain exclusions | Keep continuity and recovery checks distinct from automated failover | LOW |
| SIEM, Wazuh, Elastic SIEM, EDR, or SOAR capability | PASS | retired-numbered-case, retired-numbered-case, retired-numbered-case-retired-numbered-case contain exclusions or out-of-scope states | Do not add integrations without ADR and scope update | LOW |
| Threat hunting or malware detection | PASS | retired-numbered-case-retired-numbered-case contain exclusions | Keep ML scope limited to sanitized operational metrics | LOW |
| Packet payload analysis | PASS | retired-numbered-case-retired-numbered-case contain exclusions | Keep packet content outside the dataset and detection model | LOW |
| Deep-learning intrusion detection | PASS | retired-numbered-case-retired-numbered-case contain exclusions | Keep the model statistical or threshold-placeholder based | LOW |
| Formal compliance certification | PASS | retired-numbered-case explicitly denies certification and production audit readiness | Keep final output a portfolio-grade operational validation summary | LOW |
| Terraform Cloud, Atlantis, or Spacelift | PASS | retired-numbered-case-retired-numbered-case contain explicit exclusions | Keep Terraform workflow local and documentation-only until scope changes | LOW |
| GitOps, Argo CD, Istio, or service mesh | PASS | retired-numbered-case, retired-numbered-case, retired-numbered-case, retired-numbered-case, retired-numbered-case, retired-numbered-case-retired-numbered-case contain exclusions | Keep deployment and policy validation tool-neutral | LOW |
| Real-time automated blocking | PASS | retired-numbered-case, retired-numbered-case, retired-numbered-case contain explicit exclusions | Keep detection, review, approval, and rollback manual | LOW |

## Governance Boundary Findings

| Check | Affected File | Recommended Correction | Severity |
|---|---|---|---|
| Canonical scenario IDs and titles do not match repository | `docs/scenario-model.md` | Replace the legacy Lx-Syy catalog with the locked retired numbered scenario framework scenario list and current level placement | HIGH |
| Documented naming format conflicts with directory names | `docs/naming-rules.md` | Define `S###-kebab-case-name` and mirrored evidence paths as canonical | HIGH |
| Scenario lifecycle status vocabularies differ | `docs/scenario-model.md`, `docs/scenario-template.md`, tracking documents | Adopt one lifecycle model and include or remove `IMPLEMENTED` consistently | MEDIUM |
| Validation status and evidence readiness use overlapping terminology | `docs/evidence-model.md`, `docs/evidence-status-matrix.md` | Name these separately as validation result and evidence readiness | MEDIUM |

## Conclusion

No unsupported implementation claim was found. Scope language is conservative and explicit. The repository boundary is still operationally ambiguous until the canonical scenario, naming, and status contracts are aligned.
