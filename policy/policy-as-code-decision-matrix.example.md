# Policy as Code Decision Matrix

| Evaluation Result | Example Evidence | Operational Meaning | Required Action | Exception Handling | Final Judgment |
|---|---|---|---|---|---|
| All policies pass | pass sample | Controls satisfied | Record | None | POLICY_PASS |
| Critical policy violation | critical placeholder | Unsafe | Stop/escalate | Approval cannot hide risk | POLICY_FAIL |
| High policy violation | high placeholder | Material risk | Review | Controlled only | POLICY_FAIL |
| Warning-only violation | warning placeholder | Noncritical | Review | Optional | POLICY_WARNING |
| Approved exception | complete exception | Temporary acceptance | Track expiry | Complete fields | POLICY_EXCEPTION_APPROVED |
| Missing evidence | incomplete input | Cannot judge | Collect evidence | Not allowed | POLICY_EVIDENCE_INCOMPLETE |
| Missing owner | exception incomplete | No accountability | Reject | Reject | POLICY_REVIEW_REQUIRED |
| Missing expiry | exception incomplete | Unbounded exception | Reject | Reject | POLICY_REVIEW_REQUIRED |
| Missing approval | exception incomplete | Unauthorized | Reject | Reject | POLICY_FAIL |
| Out-of-scope policy domain | delegated domain | Route owner | Map scenario | Not applicable | POLICY_REVIEW_REQUIRED |
| Policy input malformed | parse failure | Cannot evaluate | Correct input | Not applicable | POLICY_EVIDENCE_INCOMPLETE |
