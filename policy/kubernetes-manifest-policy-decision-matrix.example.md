# Kubernetes Manifest Policy Decision Matrix

| Evaluation Result | Example Evidence | Operational Meaning | Required Action | Exception Handling | Final Judgment |
|---|---|---|---|---|---|
| Manifest compliant | compliant sample | Baseline met | Record | None | K8S_POLICY_PASS |
| Critical security violation | privileged sample | Unsafe | Reject | Not allowed | K8S_POLICY_FAIL |
| High policy violation | missing resources | Material risk | Reject/review | Controlled | K8S_POLICY_FAIL |
| Warning-only violation | probe warning | Review | Correct | Possible | K8S_POLICY_WARNING |
| Approved exception | complete exception | Temporary acceptance | Track expiry | Complete fields | K8S_POLICY_EXCEPTION_APPROVED |
| Missing evidence | incomplete sample | Cannot judge | Collect | None | K8S_POLICY_EVIDENCE_INCOMPLETE |
| Missing owner | incomplete exception | No accountability | Reject | Reject | K8S_POLICY_REVIEW_REQUIRED |
| Missing expiry | incomplete exception | Unbounded | Reject | Reject | K8S_POLICY_REVIEW_REQUIRED |
| Missing approval | incomplete exception | Unauthorized | Reject | Reject | K8S_POLICY_FAIL |
| Unsupported manifest kind | unknown kind | Not mapped | Review | None | K8S_POLICY_REVIEW_REQUIRED |
| Malformed manifest | parse failure | Cannot evaluate | Correct | None | K8S_POLICY_EVIDENCE_INCOMPLETE |
