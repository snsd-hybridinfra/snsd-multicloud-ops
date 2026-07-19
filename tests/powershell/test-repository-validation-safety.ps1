$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Import-Module (Join-Path $repositoryRoot "tools\modules\RepositoryValidationSafety.psm1") -Force

$passed = 0
$failed = 0
$temporaryRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("p1-hyg-guard-tests-" + [guid]::NewGuid().ToString('N'))

function Assert-Case {
    param([string] $Name, [bool] $Condition)
    if ($Condition) {
        $script:passed++
        Write-Host "[PASS] $Name"
    }
    else {
        $script:failed++
        Write-Host "[FAIL] $Name"
    }
}

function New-TestRepository {
    param([string] $Name)
    $path = Join-Path $temporaryRoot $Name
    New-Item -ItemType Directory -Force -Path $path | Out-Null
    & git -C $path init --quiet
    if ($LASTEXITCODE -ne 0) { throw "Unable to initialize test repository: $Name" }
    return $path
}

New-Item -ItemType Directory -Force -Path $temporaryRoot | Out-Null
try {
    $cleanRepository = New-TestRepository "clean"
    $cleanBefore = Get-RepositoryStateSnapshot $cleanRepository
    $cleanAfter = Get-RepositoryStateSnapshot $cleanRepository
    Assert-Case "clean temporary repository remains unchanged" (
        (Compare-RepositoryStateSnapshot $cleanBefore $cleanAfter).Unchanged
    )

    $trackedRepository = New-TestRepository "tracked-modification"
    Set-Content -LiteralPath (Join-Path $trackedRepository "tracked.txt") -Value "baseline" -Encoding UTF8
    & git -C $trackedRepository add tracked.txt
    Add-Content -LiteralPath (Join-Path $trackedRepository "tracked.txt") -Value "pre-existing modification" -Encoding UTF8
    $trackedBefore = Get-RepositoryStateSnapshot $trackedRepository
    $trackedAfter = Get-RepositoryStateSnapshot $trackedRepository
    Assert-Case "pre-existing tracked modification is accepted and preserved" (
        $trackedBefore.TrackedModifiedCount -eq 1 -and
        (Compare-RepositoryStateSnapshot $trackedBefore $trackedAfter).Unchanged
    )

    $untrackedRepository = New-TestRepository "untracked"
    Set-Content -LiteralPath (Join-Path $untrackedRepository "existing-untracked.txt") -Value "approved" -Encoding UTF8
    $untrackedBefore = Get-RepositoryStateSnapshot $untrackedRepository
    $untrackedAfter = Get-RepositoryStateSnapshot $untrackedRepository
    Assert-Case "pre-existing untracked file is accepted and preserved" (
        $untrackedBefore.UntrackedCount -eq 1 -and
        (Compare-RepositoryStateSnapshot $untrackedBefore $untrackedAfter).Unchanged
    )

    $failureRepository = New-TestRepository "failure"
    Set-Content -LiteralPath (Join-Path $failureRepository "nested-failure.ps1") -Value "exit 7" -Encoding UTF8
    $failureBefore = Get-RepositoryStateSnapshot $failureRepository
    & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $failureRepository "nested-failure.ps1")
    $nestedExitCode = $LASTEXITCODE
    $failureAfter = Get-RepositoryStateSnapshot $failureRepository
    Assert-Case "nested validator failure preserves state and exit code" (
        $nestedExitCode -eq 7 -and
        (Compare-RepositoryStateSnapshot $failureBefore $failureAfter).Unchanged
    )

    $newFileRepository = New-TestRepository "new-file"
    $newFileBefore = Get-RepositoryStateSnapshot $newFileRepository
    Set-Content -LiteralPath (Join-Path $newFileRepository "generated-report.md") -Value "unexpected" -Encoding UTF8
    $newFileAfter = Get-RepositoryStateSnapshot $newFileRepository
    Assert-Case "new validator-created file is detected" (
        -not (Compare-RepositoryStateSnapshot $newFileBefore $newFileAfter).Unchanged
    )

    $hashRepository = New-TestRepository "hash-change"
    Set-Content -LiteralPath (Join-Path $hashRepository "existing.txt") -Value "before" -Encoding UTF8
    $hashBefore = Get-RepositoryStateSnapshot $hashRepository
    Set-Content -LiteralPath (Join-Path $hashRepository "existing.txt") -Value "after" -Encoding UTF8
    $hashAfter = Get-RepositoryStateSnapshot $hashRepository
    Assert-Case "existing file hash change is detected" (
        -not (Compare-RepositoryStateSnapshot $hashBefore $hashAfter).Unchanged
    )

    $stagedRepository = New-TestRepository "staged"
    Set-Content -LiteralPath (Join-Path $stagedRepository "candidate.txt") -Value "candidate" -Encoding UTF8
    $stagedBefore = Get-RepositoryStateSnapshot $stagedRepository
    & git -C $stagedRepository add candidate.txt
    $stagedAfter = Get-RepositoryStateSnapshot $stagedRepository
    Assert-Case "new staged state is detected" (
        $stagedBefore.StagedCount -eq 0 -and $stagedAfter.StagedCount -eq 1 -and
        -not (Compare-RepositoryStateSnapshot $stagedBefore $stagedAfter).Unchanged
    )

    $noStageRepository = New-TestRepository "no-stage"
    Set-Content -LiteralPath (Join-Path $noStageRepository "approved.txt") -Value "approved" -Encoding UTF8
    $noStageBefore = Get-RepositoryStateSnapshot $noStageRepository
    & powershell.exe -NoProfile -Command "exit 0"
    $noStageAfter = Get-RepositoryStateSnapshot $noStageRepository
    Assert-Case "read-only command creates no staged state" (
        $noStageAfter.StagedCount -eq 0 -and
        (Compare-RepositoryStateSnapshot $noStageBefore $noStageAfter).Unchanged
    )
}
finally {
    $resolvedTemporaryRoot = [System.IO.Path]::GetFullPath($temporaryRoot)
    $resolvedSystemTemp = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath())
    if (
        $resolvedTemporaryRoot.StartsWith($resolvedSystemTemp, [System.StringComparison]::OrdinalIgnoreCase) -and
        (Split-Path -Leaf $resolvedTemporaryRoot) -like 'p1-hyg-guard-tests-*'
    ) {
        Remove-Item -LiteralPath $resolvedTemporaryRoot -Recurse -Force
    }
}

Write-Host "Repository safety regression summary: passed=$passed failed=$failed"
if ($failed -gt 0) { exit 1 }
exit 0
