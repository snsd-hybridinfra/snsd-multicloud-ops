# Integrated Capability Assessment after ZT-CV-001

The accepted CV cycle evaluated 12 capability records at a bounded laboratory
scope. Each retained `UNASSESSED` maturity. The package adds evidence-processing
support for `ZT-7.1`, `ZT-8.1`, and `ZT-8.2`; it does not implement every mapped
control or promote any capability to a repository-wide maturity state.

All nine predecessor execution records were fresh at the cycle assessment
time. The history contained one accepted execution per exact group, so all
groups remained EC3 and none reached EC4 or EC5. The regression scan found no
tracked evidence-hash drift, failed accepted record, expired evidence, or
sanitization failure.

FND, NET, VIS, and ID passed their configured bounded gates. DEV, APP, DATA,
SYS, AUTO, and CV remain partially accepted or partially runtime validated
with their recorded limitations. This assessment is a reviewed presentation
of machine authorities, not an independent implementation, certification, or
Phase 1 completion claim.

## Repeatability recommendation

Exactly one candidate is recommended for `ZT-RV-001`: `ZT-4.1.1` 접근통제,
using `ZTCV-VAL-SYS` through `ZT-CV-WF-001` at the unchanged
`ZT_SYS_001_SEVEN_SYSTEMS_FIXED_VALIDATORS` scope. It is the highest-ranked
dependency-ready EC3 capability whose existing acceptance record already binds
the fixed read-only validator and workflow. The campaign must retain at most
five accepted warning categories, require zero blocking failures, and collect
three consecutive independent successes at least 24 hours apart.

`ZT-8.1`, `ZT-8.2`, `ZT-7.1`, and `ZT-3.1.1` remain valid future candidates,
but were not selected because they are lower in the current overlay or would
blur the narrow EC4 pilot with automation or continuous-observation objectives.
