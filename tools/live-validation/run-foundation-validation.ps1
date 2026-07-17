[CmdletBinding()]
param(
    [string]$OutputDirectory = ".runtime/zero-trust/foundation",
    [switch]$SecurityBoundaryValidated
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Continue'

$root = (Resolve-Path (Join-Path $PSScriptRoot "../..")).Path
$outputRoot = [IO.Path]::GetFullPath((Join-Path $root $OutputDirectory))
[IO.Directory]::CreateDirectory($outputRoot) | Out-Null
$stamp = [DateTime]::UtcNow.ToString("yyyyMMddTHHmmssZ")
$summaryPath = Join-Path $outputRoot "$stamp-foundation-summary.json"

function Invoke-RestrictedValidation {
    param([string]$Name, [string]$Script)
    $childOutput = Join-Path $OutputDirectory $Name
    $windowsPowerShell = (Get-Command powershell -ErrorAction Stop).Source
    & $windowsPowerShell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot $Script) -OutputDirectory $childOutput | ForEach-Object { Write-Host $_ }
    $exitCode = if ($null -eq $LASTEXITCODE) { 2 } else { $LASTEXITCODE }
    [ordered]@{ name = $Name; exit_code = $exitCode; available = ($exitCode -ne 255) }
}

$openstack = Invoke-RestrictedValidation -Name 'openstack-validator' -Script 'validate-openstack-live.ps1'
$eve = Invoke-RestrictedValidation -Name 'eve-validator' -Script 'validate-eve-live.ps1'
$sshConfiguration = & (Get-Command ssh -ErrorAction Stop).Source -G snsd-r1-validator 2>$null
$routerAliasConfigured = ($LASTEXITCODE -eq 0) -and (($sshConfiguration -join "`n") -match '(?m)^user codex-router-validator$')
$router = if ($routerAliasConfigured) {
    Invoke-RestrictedValidation -Name 'router-validator' -Script 'validate-router-live.ps1'
} else {
    [ordered]@{ name = 'router-validator'; exit_code = $null; available = $false; skipped = 'SSH alias is not configured.' }
}

$result = [ordered]@{
    package_id = 'ZT-FND-001'
    generated_at = [DateTime]::UtcNow.ToString('o')
    execution_authority = 'LOCAL_WRAPPER_EXECUTION'
    openstack = $openstack
    eve = $eve
    router = $router
    security_boundary = [ordered]@{
        status = if ($SecurityBoundaryValidated -and $openstack.exit_code -eq 0 -and $eve.exit_code -eq 0) { 'VERIFIED_SEPARATELY' } elseif ($openstack.exit_code -eq 0 -and $eve.exit_code -eq 0) { 'PENDING_SEPARATE_TEST' } else { 'NOT_TESTED_WHEN_ENDPOINT_UNAVAILABLE' }
        note = 'The integration wrapper runs allowed commands only. Harmless boundary tests are executed and evidenced separately.'
    }
}
$result | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $summaryPath -Encoding utf8
Write-Output "Foundation runtime summary: $summaryPath"

if ($openstack.exit_code -eq 0 -and $eve.exit_code -eq 0 -and (-not $router.available -or $router.exit_code -eq 0)) { exit 0 }
exit 1
