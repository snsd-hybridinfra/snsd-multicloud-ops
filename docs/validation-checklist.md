# Validation Checklist

Use this checklist before marking scenario work complete.

## Repository Foundation Checklist

- [ ] Required top-level files exist: `README.md`, `AGENTS.md`, `.gitignore`.
- [ ] Required docs exist under `docs/`.
- [ ] Required top-level directories exist.
- [ ] Scope lock and excluded scope remain unchanged unless explicitly approved.
- [ ] Repository structure validation script passes.

## Scenario Structure Checklist

- [ ] Scenario directory is under the correct validation level.
- [ ] Scenario directory name follows `S###-kebab-case-description`.
- [ ] All required scenario markdown files exist.
- [ ] Scenario status matrix is updated.
- [ ] Progress tracker is updated.

## Evidence Structure Checklist

- [ ] Matching evidence directory exists under the same validation level.
- [ ] `commands.md` exists.
- [ ] `validation.md` exists.
- [ ] `logs/.gitkeep` exists.
- [ ] `screenshots/.gitkeep` exists.
- [ ] `configs/.gitkeep` exists.
- [ ] Evidence status matrix is updated.

## Security and Sensitive File Checklist

- [ ] No secrets are committed.
- [ ] No credentials are committed.
- [ ] No private keys are committed.
- [ ] No tfstate files are committed.
- [ ] No kubeconfig files are committed.
- [ ] No account-specific identifiers are committed.
- [ ] Evidence is sanitized before review.

## Implementation Readiness Checklist

- [ ] Scenario objective is clear.
- [ ] Scope includes explicit included and excluded items.
- [ ] Prerequisites are documented.
- [ ] Execution plan is step-by-step.
- [ ] Validation plan maps every check to evidence.
- [ ] Expected result is measurable.
- [ ] Failure conditions are explicit.
- [ ] Rollback plan is realistic.
- [ ] Implementation log is updated.
