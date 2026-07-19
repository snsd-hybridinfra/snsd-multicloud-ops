$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Import-Module (Join-Path $repositoryRoot "tools\modules\NodeReadinessParser.psm1") -Force
Import-Module (Join-Path $repositoryRoot "tools\modules\RepositoryValidationSafety.psm1") -Force

$passed = 0
$failed = 0

function Assert-Case {
    param(
        [string] $Name,
        [bool] $Condition
    )

    if ($Condition) {
        $script:passed++
        Write-Host "[PASS] $Name"
    }
    else {
        $script:failed++
        Write-Host "[FAIL] $Name"
    }
}

$stateBefore = Get-RepositoryStateSnapshot -RepositoryRoot $repositoryRoot

$nullResult = ConvertFrom-NodeStatusEvidence -Lines $null
Assert-Case "null input is a valid zero-result condition" (
    $nullResult.IsValid -and $nullResult.InputWasNull -and $nullResult.NodeCount -eq 0 -and
    $nullResult.Nodes.GetType().Name -eq 'Object[]'
)

$emptyResult = ConvertFrom-NodeStatusEvidence -Lines ([object[]]@())
Assert-Case "empty collection remains an empty collection" (
    $emptyResult.IsValid -and -not $emptyResult.InputWasNull -and $emptyResult.NodeCount -eq 0
)

$oneResult = ConvertFrom-NodeStatusEvidence -Lines ([object[]]@('node-1 Ready'))
Assert-Case "one scalar-like row is normalized" (
    $oneResult.IsValid -and $oneResult.NodeCount -eq 1 -and $oneResult.Nodes[0].Status -eq 'Ready'
)

$manyResult = ConvertFrom-NodeStatusEvidence -Lines ([object[]]@(
    'node-1 Ready',
    'node-2 NotReady',
    'node-3 Ready,SchedulingDisabled'
))
Assert-Case "multiple rows remain a collection" (
    $manyResult.IsValid -and $manyResult.NodeCount -eq 3 -and $manyResult.Nodes.GetType().Name -eq 'Object[]'
)

$malformedColumnResult = ConvertFrom-NodeStatusEvidence -Lines ([object[]]@('missing-status'))
Assert-Case "missing status column is rejected" (
    -not $malformedColumnResult.IsValid -and $malformedColumnResult.MalformedCount -eq 1 -and
    $malformedColumnResult.MalformedRecords[0].Reason -eq 'MISSING_STATUS_COLUMN'
)

$malformedStatusResult = ConvertFrom-NodeStatusEvidence -Lines ([object[]]@('node-1 Broken'))
Assert-Case "invalid status value is rejected" (
    -not $malformedStatusResult.IsValid -and $malformedStatusResult.MalformedCount -eq 1 -and
    $malformedStatusResult.MalformedRecords[0].Reason -eq 'INVALID_STATUS_VALUE'
)

$embeddedNullResult = ConvertFrom-NodeStatusEvidence -Lines ([object[]]@('node-1 Ready', $null))
Assert-Case "embedded null record is malformed" (
    -not $embeddedNullResult.IsValid -and $embeddedNullResult.NodeCount -eq 1 -and
    $embeddedNullResult.MalformedRecords[0].Reason -eq 'NULL_RECORD'
)

$expectedResult = ConvertFrom-NodeStatusEvidence -Lines ([object[]]@(
    'SAMPLE / NON-PRODUCTION',
    'NAME STATUS ROLES AGE VERSION',
    'control-plane-placeholder Ready control-plane 1d v0.0.0',
    'worker-node-placeholder-01 Ready worker 1d v0.0.0',
    'worker-node-placeholder-02 Ready worker 1d v0.0.0'
))
Assert-Case "expected fixture parses deterministically under strict mode" (
    $expectedResult.IsValid -and $expectedResult.NodeCount -eq 3
)

$stateAfter = Get-RepositoryStateSnapshot -RepositoryRoot $repositoryRoot
$comparison = Compare-RepositoryStateSnapshot -Before $stateBefore -After $stateAfter
Assert-Case "parser tests do not mutate the repository" $comparison.Unchanged

Write-Host "S021 parser regression summary: passed=$passed failed=$failed"
if ($failed -gt 0) { exit 1 }
exit 0
