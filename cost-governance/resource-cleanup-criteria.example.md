# Resource Cleanup Criteria

| Cleanup Area | Candidate Evidence | Expected Condition | Cleanup Condition | Block Condition | Required Approval | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|---|
| Orphaned compute resource | inventory | owner absent/idle | review | dependency | Required | S045/S046 | `<evidence-path>` |
| Stopped compute resource placeholder | inventory | lifecycle reviewed | expired | active owner | Required | S046 | `<evidence-path>` |
| Unattached volume | inventory | retention reviewed | orphaned | backup dependency | Required | S046 | `<evidence-path>` |
| Unused public IP | inventory | exposure/cost reviewed | unused | dependency | Required | S045/S046 | `<evidence-path>` |
| Unused load balancer | inventory | traffic dependency reviewed | unused | active traffic | Required | S046 | `<evidence-path>` |
| Empty object storage bucket | inventory | retention reviewed | empty/expired | retention | Required | S046 | `<evidence-path>` |
| Expired temporary resource | lifecycle | expired | cleanup ready | exception | Required | S046 | `<evidence-path>` |
| Missing owner | metadata | owner present | review | missing | Required | S043/S046 | `<evidence-path>` |
| Missing retention class | metadata | present | review | missing | Required | S046 | `<evidence-path>` |
| Missing cost classification | S045 | present | review | missing | Required | S045 | `<evidence-path>` |
| Active exception | exception | honored | not cleanup | active | Required | S046 | `<evidence-path>` |
| Critical dependency risk | impact | low | none | critical | Required | S046 | `<evidence-path>` |
| Missing rollback evidence | plan | present | none | missing | Required | S042/S046 | `<evidence-path>` |
| Missing S045 cost mapping | mapping | present | none | missing | Required | S045 | `<evidence-path>` |
| Missing S050 final report mapping | mapping | present | none | missing | Required | S050 | `<evidence-path>` |

Drift detection maps S041, remediation S042, Policy as Code S043, cost S045, and reporting S050.
