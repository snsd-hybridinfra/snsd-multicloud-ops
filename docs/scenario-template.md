# Scenario Documentation Template

This template defines the standard documentation structure for every scenario under `scenarios/`.

Use operational language. Do not write marketing copy. Do not claim implementation is complete unless matching evidence exists.

## Required Scenario Files

Every scenario directory must include:

1. `README.md`
2. `objective.md`
3. `scope.md`
4. `architecture.md`
5. `prerequisites.md`
6. `execution-plan.md`
7. `validation-plan.md`
8. `expected-result.md`
9. `failure-condition.md`
10. `rollback-plan.md`
11. `evidence-map.md`

## Required Scenario Metadata

Every scenario must define:

- Scenario ID
- Scenario Name
- Level
- Category
- Primary Domain
- Related Components
- Validation Type
- Evidence Directory
- Status

## Scenario Status Values

- `NOT_STARTED`
- `PLANNED`
- `IN_PROGRESS`
- `IMPLEMENTED`
- `VALIDATED`
- `PARTIAL`
- `BLOCKED`
- `DEPRECATED`

## Validation Type Examples

- Infrastructure Validation
- Security Validation
- Service Operation Validation
- Failure Recovery Validation
- Governance Validation
- ML Anomaly Detection Validation

## Standard File Definitions

### README.md

Purpose: provide the scenario overview and current state.

Required sections:

- Scenario ID
- Scenario Name
- Level
- Category
- Objective summary
- Scope summary
- Related components
- Validation summary
- Evidence output summary
- Status

Writing rules:

- Keep the summary factual and operational.
- Link to the matching evidence directory.
- Do not state that validation passed unless `validation.md` contains supporting evidence.

Example content pattern:

```markdown
# <scenario-id>

| Field | Value |
| --- | --- |
| Scenario ID | <scenario-id> |
| Scenario Name | <scenario-name> |
| Level | <level> |
| Category | <category> |
| Primary Domain | <domain> |
| Related Components | <component-a>, <component-b> |
| Validation Type | <validation-type> |
| Evidence Directory | evidence/<level>/<scenario-id>/ |
| Status | NOT_STARTED |

## Objective Summary

Validate <operational-capability>.

## Scope Summary

This scenario covers <included-scope> and excludes implementation changes.

## Validation Summary

Validation will confirm <expected-behavior>.

## Evidence Output Summary

Evidence will be stored in `evidence/<level>/<scenario-id>/`.
```

### objective.md

Purpose: explain what operational capability the scenario validates.

Required sections:

- Objective
- Operational capability
- Success definition

Writing rules:

- State the capability in measurable terms.
- Avoid design promises that are not validated.

Example content pattern:

```markdown
# Objective

Validate that <operational-capability> behaves as expected for <target-scope>.

Success means <measurable-success-condition>.
```

### scope.md

Purpose: define included and excluded boundaries.

Required sections:

- Included
- Excluded
- Assumptions

Writing rules:

- Use explicit boundaries.
- Do not include secrets, real credentials, account IDs, subscription IDs, tenant IDs, private keys, or tfstate.
- Use placeholders such as `<aws-vpc-id>`, `<azure-vnet-name>`, `<openstack-network-name>`, and `<target-node>`.

Example content pattern:

```markdown
# Scope

## Included

- Validate <included-item>.

## Excluded

- Provisioning real cloud resources.
- Storing credentials, private keys, kubeconfig files, or tfstate.

## Assumptions

- Placeholder identifiers such as `<target-node>` represent sanitized values.
```

### architecture.md

Purpose: describe only the components relevant to the scenario.

Required sections:

- Relevant components
- Logical flow
- Out-of-scope components

Writing rules:

- Keep the description implementation-neutral.
- Do not add new technologies.
- Use placeholders for environment-specific identifiers.

Example content pattern:

```markdown
# Architecture

## Relevant Components

- `<target-node>`
- `<aws-vpc-id>`
- `<azure-vnet-name>`

## Logical Flow

1. <component-a> sends or receives <operation>.
2. <component-b> exposes <validated-behavior>.

## Out-of-Scope Components

- Components not required to validate this scenario.
```

### prerequisites.md

Purpose: list required previous scenarios or tools.

Required sections:

- Required previous scenarios
- Required tools
- Required access assumptions

Writing rules:

- Reference prior scenario IDs where needed.
- Do not include credentials or live account details.

Example content pattern:

```markdown
# Prerequisites

## Required Previous Scenarios

- <scenario-id> or `None`

## Required Tools

- <tool-name> available in a controlled validation context

## Required Access Assumptions

- Access to `<target-node>` is available through approved lab procedures.
```

### execution-plan.md

Purpose: define the step-by-step operational flow.

Required sections:

- Preparation
- Execution steps
- Evidence capture

Writing rules:

- Use numbered steps.
- Describe actions without embedding secrets or executable implementation code.

Example content pattern:

```markdown
# Execution Plan

## Preparation

1. Review scope and prerequisites.
2. Confirm evidence directory exists.

## Execution Steps

1. Inspect <target-state>.
2. Run or perform <approved-validation-action>.
3. Capture outputs.

## Evidence Capture

Record commands in `commands.md` and validation results in `validation.md`.
```

### validation-plan.md

Purpose: define how validation will be judged.

Required sections:

- Validation table
- Review notes

Writing rules:

- Every validation item must map to evidence.
- Use clear expected results.

Required table format:

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|

Example content pattern:

```markdown
# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | <validation-item> | <method> | <expected-result> | evidence/<level>/<scenario-id>/validation.md |
```

### expected-result.md

Purpose: define success conditions.

Required sections:

- Success conditions
- Required evidence
- Completion criteria

Writing rules:

- Use observable conditions.
- Do not claim success without evidence.

Example content pattern:

```markdown
# Expected Result

## Success Conditions

- <validated-behavior> is confirmed.

## Required Evidence

- `commands.md`
- `validation.md`

## Completion Criteria

The scenario can be marked `VALIDATED` only when evidence supports every validation item.
```

### failure-condition.md

Purpose: define explicit failure conditions.

Required sections:

- Failure conditions
- Evidence of failure
- Follow-up requirement

Writing rules:

- Every failure condition must be explicit.
- Include incomplete evidence and blocked execution as possible outcomes.

Example content pattern:

```markdown
# Failure Condition

## Failure Conditions

- <expected-behavior> is not observed.
- Required evidence is missing.
- Sensitive data is captured.

## Evidence of Failure

Record failed checks in `validation.md`.

## Follow-Up Requirement

Create a follow-up item before retrying validation.
```

### rollback-plan.md

Purpose: define rollback or recovery steps.

Required sections:

- Stop condition
- Rollback steps
- Recovery validation

Writing rules:

- Every rollback plan must be realistic.
- Do not rely on unavailable tools or undocumented access.

Example content pattern:

```markdown
# Rollback Plan

## Stop Condition

Stop if <unsafe-or-failed-condition> occurs.

## Rollback Steps

1. Revert <changed-state> using the approved lab procedure.
2. Remove unsafe evidence.
3. Record rollback notes in `validation.md`.

## Recovery Validation

Confirm <baseline-state> is restored.
```

### evidence-map.md

Purpose: map validation checks to evidence files.

Required sections:

- Evidence map table
- Evidence notes

Writing rules:

- Every validation item must map to evidence.
- Evidence files must use clear kebab-case names.

Required table format:

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|

Example content pattern:

```markdown
# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| <validation-item> | evidence/<level>/<scenario-id>/validation.md | validation record | yes |
| <command-output> | evidence/<level>/<scenario-id>/commands.md | command record | yes |
```

## Global Writing Rules

- Use operational language.
- Do not write marketing copy.
- Do not claim implementation is complete unless evidence exists.
- Do not include secrets, real credentials, account IDs, subscription IDs, tenant IDs, private keys, or tfstate.
- Use placeholders like `<aws-vpc-id>`, `<azure-vnet-name>`, `<openstack-network-name>`, and `<target-node>`.
- Every validation item must map to evidence.
- Every rollback plan must be realistic.
- Every failure condition must be explicit.
