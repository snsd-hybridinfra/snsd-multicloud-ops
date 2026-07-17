# Maturity Assessment Method

## Assessment Record

Every record includes: assessed capability, environment, scope, current level, target level, evidence references, evaluator, validation date, confidence, exceptions, gaps, and next action.

## Decision Method

1. Select one capability ID and its source maturity table.
2. Bound the environment; one lab is not an organization-wide assessment.
3. Enumerate each source-defined characteristic for the candidate level.
4. Link evidence and authority to every claimed characteristic.
5. Record contrary evidence, exceptions, and missing lower-level characteristics.
6. Assign `Traditional`, `Initial`, `Advanced`, or `Optimal` only when supported; otherwise use `UNASSESSED` or `NOT_APPLICABLE`.
7. Assign confidence `LOW`, `MEDIUM`, or `HIGH` based on evidence quality, freshness, independence, and scope completeness.
8. Reassess after material changes or evidence expiry.

## Evidence Thresholds

- `DESIGN`: alignment only; cannot establish implementation.
- `CONFIGURATION`: control exists in a bounded environment; does not prove behavior.
- `RUNTIME`: observed behavior for stated paths; does not prove continuous operation.
- `CONTINUOUS`: repeated or continuously collected evidence with defined coverage and review.

No aggregate maturity is published unless the formula, weighting, missing-data rule, minimum evidence threshold, exceptions, and scope are documented. The current repository publishes no overall score.

