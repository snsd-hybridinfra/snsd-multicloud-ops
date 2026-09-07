$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$failures = [System.Collections.Generic.List[string]]::new()

$requiredFiles = @(
    "README.md",
    "AGENTS.md",
    "docs/scope-lock.md",
    "docs/excluded-scope.md",
    "docs/platform/README.md",
    "docs/platform/target-architecture.md",
    "docs/platform/implementation-roadmap.md",
    "docs/platform/architecture-baseline.yaml",
    "docs/platform/asset-reconciliation.yaml",
    "docs/platform/composite-service-catalog.yaml",
    "docs/platform/ai-agent-sandbox.yaml",
    "docs/platform/ai-agent-runtime-readiness.yaml",
    "docs/platform/financial-saas-development-paas.yaml",
    "docs/platform/terraform-supply-chain.yaml",
    "docs/platform/container-supply-chain.yaml",
    "docs/adr/0022-managed-terraform-supply-chain.md",
    "docs/adr/0023-container-image-supply-chain-and-k3s-delivery.md",
    "applications/internal-iaas-portal/terraform/supply-chain-lock.json",
    "applications/internal-iaas-portal/supply-chain/container-supply-chain-lock.json",
    "applications/internal-iaas-portal/supply-chain/runner-requirements.json",
    "applications/internal-iaas-portal/supply-chain/README.md",
    "applications/internal-iaas-portal/supply-chain/runner-bundle-source-lock.json",
    "applications/internal-iaas-portal/supply-chain/runner-bundle/install.sh",
    "applications/internal-iaas-portal/supply-chain/runner-bundle/idp-egress-policy-apply",
    "applications/internal-iaas-portal/supply-chain/runner-bundle/idp-egress-policy-check",
    "schemas/idp-runner-bundle-manifest.schema.json",
    "tools/local-vm/New-IdpSupplyChainRunnerVm.ps1",
    "tools/supply-chain/Build-IdpSupplyChainRunnerBundle.ps1",
    "applications/internal-iaas-portal/supply-chain/container_pipeline.py",
    "applications/internal-iaas-portal/kubernetes/releases/kustomization.yaml",
    "applications/internal-iaas-portal/kubernetes/gitops/idp-container-release-application.yaml",
    ".github/workflows/idp-container-supply-chain.yml",
    "tools/validate_container_supply_chain.py",
    "tests/test_container_supply_chain.py",
    "docs/platform/container-supply-chain-runtime-readiness.yaml",
    "tools/validate_container_runtime_readiness.py",
    "tests/test_container_runtime_readiness.py",
    "applications/internal-iaas-portal/services/terraform-runner/terraform_runner/supply_chain.py",
    "applications/internal-iaas-portal/tests/security/test_terraform_supply_chain.py",
    "tools/validate_terraform_supply_chain.py",
    "tests/test_terraform_supply_chain.py",
    "applications/internal-iaas-portal/services/request-api/request_api/saas_paas.py",
    "applications/internal-iaas-portal/tests/api/test_financial_saas_paas.py",
    "docs/platform/private-iaas-golden-path.yaml",
    "docs/adr/0018-financial-hybrid-ready-idp.md",
    "docs/adr/0019-approved-composite-service-catalog.md",
    "docs/adr/0020-persistent-ai-agent-sandbox.md",
    "docs/adr/0021-financial-saas-development-paas.md",
    "docs/evidence-model.md",
    "docs/progress-tracker.md",
    "docs/zero-trust/package-flow.yaml",
    "docs/zero-trust/final-roadmap.yaml",
    "docs/zero-trust/final-execution-plan.yaml",
    "docs/zero-trust/maturity-target.yaml",
    "docs/zero-trust/package-status.yaml",
    "docs/zero-trust/package-acceptance-cases.yaml",
    "schemas/zero-trust-package-flow.schema.json",
    "schemas/zt-roadmap.schema.json",
    "schemas/zt-execution-plan.schema.json",
    "schemas/zt-maturity-target.schema.json",
    "schemas/zt-package-status.schema.json",
    "schemas/zt-package-acceptance-cases.schema.json",
    "schemas/phase-1-acceptance-decision.schema.json",
    "schemas/phase-1-accepted-with-gaps-decision.schema.json",
    "schemas/phase-1-rv-refresh-progress.schema.json",
    "schemas/phase-2-entry-preflight.schema.json",
    "schemas/phase-2-visibility-deployment-contract.schema.json",
    "schemas/phase-2-visibility-native-validation.schema.json",
    "schemas/phase-2-visibility-live-gate-discovery.schema.json",
    "schemas/phase-2-visibility-cinder-prerequisite.schema.json",
    "schemas/phase-2-visibility-terraform-preflight.schema.json",
    "schemas/phase-2-visibility-live-validation.schema.json",
    "schemas/phase-2-visibility-partial-promotion-decision.schema.json",
    "schemas/phase-2-visibility-alert-validation-plan.schema.json",
    "schemas/phase-2-visibility-alert-validation-evidence.schema.json",
    "schemas/zt-vis-002-package.schema.json",
    "tools/validate_scenario_retirement.py",
    "tools/validate_financial_idp_architecture.py",
    "tools/validate_composite_service_catalog.py",
    "tools/validate_ai_agent_sandbox.py",
    "platform/kubernetes/mini-ona/kata-deploy-values.yaml",
    "tools/local-vm/New-MiniOnaK3sVm.ps1",
    "applications/internal-iaas-portal/services/request-api/request_api/agent_jobs.py",
    "applications/internal-iaas-portal/services/request-api/request_api/agent_integrations.py",
    "applications/internal-iaas-portal/services/request-api/request_api/agent_runtime.py",
    "applications/internal-iaas-portal/database/migrations/request-db/versions/0003_agent_job_simulation.py",
    "applications/internal-iaas-portal/database/migrations/request-db/versions/0004_agent_integration_outbox.py",
    "applications/internal-iaas-portal/database/migrations/request-db/versions/0005_agent_budget_telemetry.py",
    "applications/internal-iaas-portal/tests/api/test_agent_job_orchestrator.py",
    "applications/internal-iaas-portal/tests/api/test_agent_runtime_adapters.py",
    "tools/validate_private_iaas_golden_path.py",
    "tools/validate_zero_trust.py",
    "tools/validate_phase1_acceptance.py",
    "tools/validate_phase2_entry.py",
    "tools/validate_p2_vis_001_artifacts.py",
    "tools/check_zero_trust_sync.py",
    "tools/validate_phase1_runbook_baseline.py",
    "docs/runbooks/phase-1/runbook-manifest.yaml",
    "docs/zero-trust/recovery/P1-ACC-001/acceptance-decision.yaml",
    "docs/zero-trust/recovery/P1-ACC-001/acceptance-decision-with-gaps.yaml",
    "docs/zero-trust/recovery/P1-ACC-001/rv-refresh-progress.yaml",
    "docs/evidence/zero-trust/zt-rv-001-refresh-01.sanitized.txt",
    "docs/zero-trust/recovery/P1-ACC-001/authority-audit.yaml",
    "docs/zero-trust/recovery/P1-ACC-001/evidence-index.yaml",
    "docs/zero-trust/recovery/P1-ACC-001/validation-results.yaml",
    "docs/zero-trust/recovery/P1-ACC-001/completion-report.md",
    "docs/zero-trust/recovery/P1-ACC-001/validation-results-with-gaps.yaml",
    "docs/zero-trust/recovery/P1-ACC-001/completion-report-with-gaps.md",
    "docs/zero-trust/exceptions/p1-rv-freshness-001.yaml",
    "docs/zero-trust/phase-2-entry-preflight.yaml",
    "docs/zero-trust/phase-2-visibility-deployment-contract.yaml",
    "docs/zero-trust/phase-2-visibility-native-validation.yaml",
    "docs/zero-trust/phase-2-visibility-alert-validation-plan.yaml",
    "docs/evidence/zero-trust/zt-vis-002-alert-validation.sanitized.json",
    "docs/zero-trust/packages/zt-vis-002-package.yaml",
    "docs/adr/0015-use-vmware-ansible-control-node.md",
    "docs/adr/0016-enable-dedicated-cinder-lvm-prerequisite.md",
    "docs/evidence/zero-trust/zt-vis-002-control-node.sanitized.json",
    "docs/evidence/zero-trust/zt-vis-002-live-gate-discovery.sanitized.json",
    "docs/evidence/zero-trust/zt-vis-002-cinder-prerequisite-activation.sanitized.json",
    "docs/evidence/zero-trust/zt-vis-002-terraform-preflight.sanitized.json",
    "docs/evidence/zero-trust/zt-vis-002-live-validation.sanitized.json",
    "docs/evidence/zero-trust/zt-vis-002-partial-promotion-decision.sanitized.json",
    "tools/local-vm/New-AnsibleControlVm.ps1",
    "tools/local-vm/Add-CinderDiskToOpenStackAio.ps1",
    "terraform/modules/zt-vis-002-openstack/README.md",
    "terraform/envs/zt-vis-002-openstack/README.md",
    "terraform/envs/zt-vis-002-openstack/.terraform.lock.hcl",
    "ansible/roles/zt_vis_002/README.md",
    "ansible/playbooks/zt-vis-002-deploy.yml",
    "ansible/playbooks/zt-vis-002-rollback.yml",
    "ansible/playbooks/zt-vis-002-live-validation.yml",
    "ansible/playbooks/zt-vis-002-alert-validation.yml",
    "tools/live-validation/remote/validate-zt-vis-002-runtime.sh.example",
    "tools/live-validation/remote/validate-zt-vis-002-alert-delivery.py.example",
    "tools/live-validation/validate_zt_vis_002_mtls.py"
)

$packageIds = @("zt-fnd-001", "zt-net-001", "zt-vis-001", "zt-id-001", "zt-cv-001", "zt-rv-001", "zt-sch-001", "zt-arc-001")
foreach ($packageId in $packageIds) {
    $requiredFiles += "docs/zero-trust/packages/$packageId-package.yaml"
}

$retiredPaths = @(
    "scenarios",
    "evidence/L1-foundation",
    "evidence/L2-security-baseline",
    "evidence/L3-service-operations",
    "evidence/L4-failure-recovery",
    "evidence/L5-governance-intelligent-ops",
    "runbooks",
    "tools/validate-all-scenarios.ps1",
    "tools/validate-scenario-quality.ps1",
    "tools/generate-final-evidence-report.ps1"
)

Push-Location $repositoryRoot
try {
    foreach ($path in $requiredFiles) {
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            $failures.Add("required file missing: $path") | Out-Null
        }
    }
    foreach ($path in $retiredPaths) {
        if (Test-Path -LiteralPath $path) {
            $failures.Add("retired authority remains: $path") | Out-Null
        }
    }

    $flow = Get-Content -LiteralPath "docs/zero-trust/package-flow.yaml" -Raw | ConvertFrom-Json
    $expectedFlow = @("ZT-FND-001", "ZT-NET-001", "ZT-VIS-001", "ZT-ID-001", "ZT-CV-001", "ZT-RV-001", "P1-ACC-001")
    if (@(Compare-Object -ReferenceObject $expectedFlow -DifferenceObject @($flow.phase_1_sequence) -SyncWindow 0).Count -ne 0) {
        $failures.Add("canonical package flow differs") | Out-Null
    }
    if ($flow.phase_1_acceptance.completion_status -ne "COMPLETED_WITH_GAPS" -or $flow.phase_1_acceptance.scope_boundary -ne "ZT-RV-001" -or $flow.phase_1_acceptance.decision_status -ne "ACCEPTED_WITH_GAPS" -or $null -ne $flow.phase_1_acceptance.blocking_reason -or $flow.phase_1_acceptance.accepted_exception -ne "P1-RV-FRESHNESS-001" -or $flow.phase_1_acceptance.deferred_final_risk -ne "STALE_RV_EVIDENCE") {
        $failures.Add("Phase 1 acceptance boundary differs") | Out-Null
    }
    if ($flow.deferred_final_work.package_id -ne "ZT-SCH-001" -or $flow.deferred_final_work.schedule_state -ne "DISABLED" -or $flow.deferred_final_work.execution_phase -ne "PHASE_5") {
        $failures.Add("deferred final scheduled-validation boundary differs") | Out-Null
    }

    $trackedRuntime = @(git ls-files .runtime)
    if ($LASTEXITCODE -ne 0) {
        $failures.Add("git ls-files .runtime failed") | Out-Null
    }
    elseif ($trackedRuntime.Count -ne 0) {
        $failures.Add("tracked runtime files found: $($trackedRuntime -join ', ')") | Out-Null
    }
}
finally {
    Pop-Location
}

if ($failures.Count -gt 0) {
    foreach ($failure in $failures) {
        Write-Host "[FAIL] $failure"
    }
    Write-Host "Repository structure summary: failed=$($failures.Count)"
    exit 1
}

Write-Host "[PASS] Required package authorities, schemas, validators, evidence contracts, and runbooks are present."
Write-Host "[PASS] Retired numbered-scenario authorities and tracked runtime are absent."
Write-Host "Repository structure summary: failed=0"
exit 0
