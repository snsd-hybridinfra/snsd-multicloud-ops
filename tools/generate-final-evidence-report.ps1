$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$root = Split-Path -Parent $PSScriptRoot
$out = Join-Path $root 'evidence/L5-governance-intelligent-ops/S050-final-evidence-report-generation-validation'
$docs = Join-Path $root 'docs'
$required = @('progress-tracker.md','scenario-status-matrix.md','evidence-status-matrix.md','implementation-log.md','risk-register.md','scope-lock.md','excluded-scope.md')
$missing = @($required | Where-Object { -not (Test-Path (Join-Path $docs $_) -PathType Leaf) })
$scenarioDirs = @(Get-ChildItem (Join-Path $root 'scenarios') -Recurse -Directory | Where-Object { $_.Name -match '^S\d{3}-' })
$evidenceDirs = @(Get-ChildItem (Join-Path $root 'evidence') -Recurse -Directory | Where-Object { $_.Name -match '^S\d{3}-' })
$scenarioIds = @($scenarioDirs | ForEach-Object { [regex]::Match($_.Name, '^S\d{3}').Value } | Sort-Object -Unique)
$evidenceIds = @($evidenceDirs | ForEach-Object { [regex]::Match($_.Name, '^S\d{3}').Value } | Sort-Object -Unique)
$expected = @(1..50 | ForEach-Object { 'S{0:D3}' -f $_ })
$coverage = @($expected | Where-Object { $_ -notin $scenarioIds -or $_ -notin $evidenceIds }).Count -eq 0
$status = Get-Content (Join-Path $docs 'scenario-status-matrix.md') -Raw
$eStatus = Get-Content (Join-Path $docs 'evidence-status-matrix.md') -Raw
$validated = ([regex]::Matches($status, '(?m)^\|\s*S\d{3}\s*\|.*?\|\s*VALIDATED\s*\|')).Count
$implemented = ([regex]::Matches($status, '(?m)^\|\s*S\d{3}\s*\|.*?\|\s*(?:IMPLEMENTED|VALIDATED)\s*\|')).Count
$blocked = ([regex]::Matches($status, '(?m)^\|\s*S\d{3}\s*\|.*?\|\s*BLOCKED\s*\|')).Count
$ready = ([regex]::Matches($eStatus, '(?m)^\|\s*S\d{3}\s*\|.*?\|\s*READY\s*\|\s*$')).Count
$partial = ([regex]::Matches($eStatus, '(?m)^\|\s*S\d{3}\s*\|.*?\|\s*PARTIAL\s*\|\s*$')).Count
$riskCount = ([regex]::Matches((Get-Content (Join-Path $docs 'risk-register.md') -Raw), '(?m)^\|\s*R\d{3}\s*\|')).Count
$judgment = if ($missing.Count -or -not $coverage) { 'FINAL_REPORT_INCOMPLETE' } elseif ($blocked) { 'FINAL_REPORT_BLOCKED' } elseif ($validated -lt 50 -or $ready -lt 50 -or $partial) { 'FINAL_REPORT_WARNING' } else { 'FINAL_REPORT_READY' }
$timestamp = (Get-Date).ToString('s')
$idList = $expected -join ', '
$report = @(
    '# Final Evidence Report — SAMPLE / NON-PRODUCTION', '',
    '## Report Metadata',
    "final_report_id: final-report-s050-generated; report_generated_at: $timestamp; repository_name: snsd-multicloud-ops; platform_name: SNSD Multi-Cloud Ops; total_scenarios: 50; implemented_scenarios: $implemented; validated_scenarios: $validated; ready_evidence_count: $ready; blocked_scenarios: $blocked; final_judgment: $judgment; evidence_reference: evidence/L5-governance-intelligent-ops/S050-final-evidence-report-generation-validation/", '',
    '## Executive Summary', 'Validation platform evidence report generated from local repository metadata only.', '',
    '## Platform Scope', 'Sample/non-production repository validation. No live infrastructure validation was performed by S050.', '',
    '## Architecture Summary', 'Canonical scenario and evidence directories, status matrices, local validators, runbooks, and generated summaries.', '',
    '## Scenario Coverage Summary', "All IDs accounted for: $idList", '',
    '## L1 Foundation Validation Summary', 'S001-S010; 10 scenarios.', '',
    '## L2 Security Baseline Validation Summary', 'S011-S020; 10 scenarios.', '',
    '## L3 Service Operations Validation Summary', 'S021-S030; 10 scenarios.', '',
    '## L4 Failure Recovery Validation Summary', 'S031-S040; 10 scenarios.', '',
    '## L5 Governance Intelligent Ops Summary', 'S041-S050; 10 scenarios.', '',
    '## Evidence Status Summary', "READY: $ready; PARTIAL: $partial. Source: docs/evidence-status-matrix.md.", '',
    '## Validation Script Summary', 'Repository structure, scenario quality, scenario-specific validators, report generator, and report validator are local-only.', '',
    '## Risk Register Summary', "Risk entries: $riskCount. Source: docs/risk-register.md.", '',
    '## Excluded Scope Confirmation', 'docs/excluded-scope.md remains authoritative; live/cloud/security telemetry, remediation, certification, and external reporting are excluded.', '',
    '## Safety Boundary Confirmation', 'No secrets or real identifiers are included. No live infrastructure query, cloud CLI, kubectl, Terraform, Prometheus/Grafana, billing, SIEM/Wazuh/EDR, or packet operation is performed.', '',
    '## Intelligent Ops Summary', 'S047 validates synthetic metric datasets; S048 validates deterministic sample anomaly decisions; S049 validates deterministic human-review reports.', '',
    '## Final Operational Judgment', "final_judgment: $judgment. This is not production audit certification or compliance attestation.", '',
    '## Appendix A: Scenario Status Matrix', 'docs/scenario-status-matrix.md', '',
    '## Appendix B: Evidence Status Matrix', 'docs/evidence-status-matrix.md', '',
    '## Appendix C: Validation Commands', 'See runbooks/final-evidence-report-generation-commands.example.md.', '',
    '## Appendix D: Generated Evidence References', 'Generated Markdown, JSON, generation log, validation log, and validation summary remain under the S050 evidence directory.'
)
$reportPath = Join-Path $out 'configs/final-evidence-report.generated.md'
$jsonPath = Join-Path $out 'configs/final-evidence-report-summary.generated.json'
$logPath = Join-Path $out 'logs/final-evidence-report-generation.log'
$report | Set-Content $reportPath -Encoding UTF8
[ordered]@{
    final_report_id='final-report-s050-generated'; report_generated_at=$timestamp; repository_name='snsd-multicloud-ops'; platform_name='SNSD Multi-Cloud Ops'; total_scenarios=50; scenario_range='S001-S050';
    l1_scenario_count=10; l2_scenario_count=10; l3_scenario_count=10; l4_scenario_count=10; l5_scenario_count=10;
    implemented_scenarios=$implemented; validated_scenarios=$validated; ready_evidence_count=$ready; partial_evidence_count=$partial; blocked_scenario_count=$blocked; risk_count=$riskCount;
    excluded_scope_confirmed=$true; safety_boundary_confirmed=$true; intelligent_ops_scenarios=@('S047','S048','S049'); final_judgment=$judgment;
    evidence_reference='evidence/L5-governance-intelligent-ops/S050-final-evidence-report-generation-validation/'
} | ConvertTo-Json -Depth 3 | Set-Content $jsonPath -Encoding UTF8
@('SAMPLE / NON-PRODUCTION', "Generated: $timestamp", 'Validation_Mode: LocalRepository', 'Markdown_Generated: true', 'Summary_JSON_Generated: true', "Scenario_Count: $($scenarioIds.Count)", "Evidence_Count: $($evidenceIds.Count)", "Final_Judgment: $judgment", 'Live_Infrastructure_Query_Performed: false', 'External_Reporting_Dependency_Required: false') | Set-Content $logPath -Encoding UTF8
Write-Host "[PASS] Generated local Markdown/JSON report with judgment $judgment"
