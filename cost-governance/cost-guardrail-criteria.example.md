# Cost Guardrail Criteria

| Guardrail Area | Evaluation Input | Expected Condition | Violation Condition | Severity | Exception Requirement | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|---|
| Monthly budget threshold | estimate | within placeholder | exceeded | High | Full fields | S045 | `<evidence-path>` |
| Daily budget threshold | estimate | within placeholder | exceeded | High | Full fields | S045 | `<evidence-path>` |
| Incremental cost delta | delta | within placeholder | exceeded | High | Full fields | S045 | `<evidence-path>` |
| Cost-impacting Terraform change | plan metadata | S045 mapped | missing | Medium | Review | S041/S045 | `<evidence-path>` |
| Drift remediation cost impact | S042 evidence | cost review | missing | High | Approval | S042/S045 | `<evidence-path>` |
| Public IP cost exposure | classification | owner/exposure review | missing | Medium | Full fields | S045 | `<evidence-path>` |
| Persistent volume cost exposure | classification | owner/retention | missing | Medium | Full fields | S045 | `<evidence-path>` |
| Object storage retention | classification | retention/cleanup | missing | Medium | Full fields | S045/S046 | `<evidence-path>` |
| Oversized compute placeholder | estimate | reviewed | unreviewed | Medium | Approval | S045 | `<evidence-path>` |
| Orphaned resource cleanup mapping | mapping | S046 | absent | High | Not allowed | S046 | `<evidence-path>` |
| Missing owner | exception | present | absent | High | Reject | S043 | `<evidence-path>` |
| Missing expiry | exception | present | absent | High | Reject | S043 | `<evidence-path>` |
| Missing approval | exception | present | absent | Critical | Reject | S043 | `<evidence-path>` |
| Missing S046 cleanup mapping | cleanup | present | absent | High | Review | S046/S050 | `<evidence-path>` |
