# Lab Evidence Collection Guide

**Status: ACTIVE — retired-numbered-case has READY authoritative sanitized runtime evidence;
all other scenario evidence remains subject to the truth-state reset.**

## Purpose

This guide defines how evidence from the disposable reference lab is collected, sanitized, named, and mapped to the existing retired numbered scenario framework directories. Collection must follow the owning scenario's validation plan and the rules in `docs/lab-sanitization-rules.md`.

## Collection Workflow

1. Identify the owning scenario and its expected validation check.
2. Review the scenario `scope.md`, `validation-plan.md`, and `evidence-map.md`.
3. Collect the minimum command output, screenshot, config excerpt, or validator log needed for that check.
4. Save the raw artifact outside the repository while sanitization is pending.
5. Remove or mask sensitive and environment-specific values.
6. Place the sanitized artifact in the matching evidence directory.
7. Update `commands.md` and `validation.md` with the collection method, result, and evidence filename.
8. Run repository validators before committing.

## Command Evidence

- Capture the command purpose, sanitized command line, execution time, validation mode, exit status, and relevant output.
- Remove shell history, prompts, usernames, working-directory details, addresses, identifiers, and authentication material.
- Prefer narrow queries over full environment or configuration dumps.
- Never capture environment variables, credential stores, kubeconfig, provider profiles, or complete database dumps.

Recommended filename:

```text
YYYYMMDD-HHMM-<scenario-id>-<evidence-type>.txt
```

Example with placeholders:

```text
YYYYMMDD-HHMM-retired-numbered-case-node-readiness.txt
```

## Screenshots

- Capture only the panel, terminal region, or state needed by the validation check.
- Mask browser address bars, usernames, hostnames, IP addresses, datasource names, resource IDs, timestamps that reveal unrelated activity, and any token or cookie value.
- Crop unrelated applications and personal information.
- Review the final image at full size before moving it into the repository.
- Do not create screenshots solely for decoration; each image must map to a validation check.

Recommended filename:

```text
YYYYMMDD-HHMM-<scenario-id>-<screenshot-name>.png
```

## Config Evidence

- Collect the smallest relevant configuration excerpt.
- Replace addresses, hostnames, usernames, resource names, IDs, URLs, tokens, and secret references with documented placeholders.
- Preserve syntax and comments needed to understand the control.
- Do not commit generated state, kubeconfig, private keys, provider credentials, or production configuration.

Recommended filename:

```text
YYYYMMDD-HHMM-<scenario-id>-<config-name>.yml
```

Use the actual text format when YAML is not appropriate, while preserving the same timestamp/scenario/name pattern.

## Validation Logs

- Run the scenario's local `tools/validate-*.ps1` script when available.
- Keep the exit code, PASS/WARN/FAIL summary, and mapped check IDs.
- Do not turn a static or sample result into a claim of live validation.
- If a live lab step was performed manually, label the sanitized evidence mode explicitly and retain the rollback/post-check result where applicable.
- Repository-wide results belong under retired-numbered-case; scenario-specific results remain under their owning scenario.

## Evidence Path Mapping

Every artifact must be stored under the same level and scenario name as its definition:

```text
evidence/<level>/<scenario>/logs/
evidence/<level>/<scenario>/screenshots/
evidence/<level>/<scenario>/configs/
```

Examples of evidence types:

| Evidence Type | Destination | Typical Contents |
|---|---|---|
| Command output | `logs/` | Sanitized status, reachability, health, failure, or recovery output |
| Validator output | `logs/` | Local validation log and check summary |
| Screenshot | `screenshots/` | Masked dashboard, topology, or service-state view |
| Configuration excerpt | `configs/` | Sanitized non-production config or policy excerpt |
| Structured summary | `configs/` | Markdown, JSON, YAML, or CSV summary without secrets |

## Evidence Replacement Rule

- Keep existing sample files when they remain useful for explaining expected structure.
- Add real sanitized lab files alongside samples using the timestamped naming convention.
- Do not overwrite original sample evidence unless the replacement is intentional, reviewed, and documented.
- Never rename sample evidence to imply it came from a live lab.
- If real lab evidence contradicts a sample, preserve both and explain the difference in `validation.md`.

## Review Checklist

- The owning scenario and check ID are recorded.
- The filename follows the timestamp/scenario/evidence naming convention.
- The artifact contains no real address, hostname, username, identifier, URL, or authentication material.
- Screenshots are visually inspected after masking.
- The validation result distinguishes static, sample, and sanitized-lab evidence.
- Rollback and post-check evidence are present for failure/recovery experiments.
- Repository structure and quality validators pass.

## Non-Production Boundary

Evidence collected through this guide demonstrates behavior in a disposable reference lab only. It is not production evidence, compliance certification, an external audit artifact, or permission to query cloud accounts or organizational infrastructure.
