<#
SAMPLE / NON-PRODUCTION

Collects a minimal read-only Bastion SSH evidence bundle from a disposable lab.
Raw output must remain outside the repository. Only the reviewed sanitized copy
may be copied into an evidence directory.

This script never reads private keys, /etc/shadow, passwords, tokens, cloud
credentials, kubeconfig, or secret stores. BatchMode prevents password prompts.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $BastionHost,

    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $SshUser,

    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $OutputRoot
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

Write-Host "SAMPLE / NON-PRODUCTION Bastion evidence collection"

$repositoryRoot = [System.IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot)).TrimEnd('\', '/')
$resolvedOutputRoot = [System.IO.Path]::GetFullPath($OutputRoot).TrimEnd('\', '/')

if ($resolvedOutputRoot.Equals($repositoryRoot, [System.StringComparison]::OrdinalIgnoreCase) -or
    $resolvedOutputRoot.StartsWith($repositoryRoot + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "OutputRoot must be outside the repository because it will contain unsanitized raw output."
}

$sshCommand = Get-Command -Name "ssh" -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
if ($null -eq $sshCommand) {
    throw "The local SSH client is unavailable. Validate retired-numbered-case before collecting Bastion evidence."
}

New-Item -ItemType Directory -Force -Path $resolvedOutputRoot | Out-Null

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$rawPath = Join-Path $resolvedOutputRoot "$timestamp-retired-numbered-case-bastion-reachability.raw.txt"
$sanitizedPath = Join-Path $resolvedOutputRoot "$timestamp-retired-numbered-case-bastion-reachability.sanitized.txt"

$remoteCommand = @'
printf '__HOSTNAME__\n'
hostname
printf '__WHOAMI__\n'
whoami
printf '__UPTIME__\n'
uptime
printf '__IP_ADDR__\n'
ip addr
printf '__SSH_SERVICE__\n'
systemctl is-active ssh
printf '__LISTENING_SOCKETS__\n'
if command -v ss >/dev/null 2>&1; then ss -tulpen; elif command -v netstat >/dev/null 2>&1; then netstat -tulpen; else printf 'socket-tool-unavailable\n'; fi
'@ -replace "`r?`n", "; "

$sshArguments = @(
    "-o", "BatchMode=yes",
    "-o", "StrictHostKeyChecking=yes",
    "-o", "ConnectTimeout=10",
    "$SshUser@$BastionHost",
    $remoteCommand
)

$rawCommandOutput = @(& $sshCommand.Source @sshArguments 2>&1)
$sshExitCode = $LASTEXITCODE

$rawLines = @(
    "SAMPLE / NON-PRODUCTION BASTION EVIDENCE",
    "Collection mode: ReadOnlySSH",
    "SSH exit code: $sshExitCode",
    ""
) + @($rawCommandOutput | ForEach-Object { [string] $_ })

Set-Content -LiteralPath $rawPath -Value $rawLines -Encoding UTF8

$rawText = Get-Content -LiteralPath $rawPath -Raw
$hostnameMatch = [regex]::Match($rawText, '(?m)^__HOSTNAME__\r?\n([^\r\n]+)')
$reportedUserMatch = [regex]::Match($rawText, '(?m)^__WHOAMI__\r?\n([^\r\n]+)')

$sanitizedText = $rawText
$sanitizedText = [regex]::Replace($sanitizedText, '(?<![A-Za-z0-9<])(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?(?![A-Za-z0-9>])', '<lab-ip-masked>')
$sanitizedText = [regex]::Replace($sanitizedText, '(?i)(?<![A-F0-9:])(?:[A-F0-9]{0,4}:){2,7}[A-F0-9]{0,4}(?:/\d{1,3})?(?![A-F0-9:])', '<lab-ip-masked>')
$sanitizedText = [regex]::Replace($sanitizedText, '(?i)(?<![A-F0-9])(?:[A-F0-9]{2}:){5}[A-F0-9]{2}(?![A-F0-9])', '<interface-id-masked>')
$sanitizedText = [regex]::Replace($sanitizedText, [regex]::Escape($SshUser), '<user-masked>', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)

if ($BastionHost -notmatch '^(?:\d{1,3}\.){3}\d{1,3}$') {
    $sanitizedText = [regex]::Replace($sanitizedText, [regex]::Escape($BastionHost), '<hostname-masked>', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
}
if ($hostnameMatch.Success) {
    $sanitizedText = [regex]::Replace($sanitizedText, [regex]::Escape($hostnameMatch.Groups[1].Value.Trim()), '<hostname-masked>', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
}
if ($reportedUserMatch.Success) {
    $sanitizedText = [regex]::Replace($sanitizedText, [regex]::Escape($reportedUserMatch.Groups[1].Value.Trim()), '<user-masked>', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
}

Set-Content -LiteralPath $sanitizedPath -Value $sanitizedText -Encoding UTF8

Write-Host "Raw output (DO NOT COMMIT): $rawPath"
Write-Host "Sanitized output path: $sanitizedPath"
Write-Host "Review the complete sanitized file before copying it to <evidence-path>."

if ($sshExitCode -ne 0) {
    Write-Error "SSH collection failed with exit code $sshExitCode. Review only the sanitized output."
    exit $sshExitCode
}

exit 0
