# Objective

Validate that S001 through S050 have one-to-one scenario and evidence paths and that every evidence directory contains the canonical evidence structure required for repeatable validation.

Success means all structural, sensitive-file, ID-coverage, uniqueness, and Evidence Readiness Status checks pass.

Repository-wide scenario quality is handled by `tools/validate-scenario-quality.ps1`. Scenario-specific validation remains in each scenario, and final evidence report generation belongs to S050.
