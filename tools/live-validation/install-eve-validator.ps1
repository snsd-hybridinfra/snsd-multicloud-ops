[CmdletBinding()]
param(
    [string]$OperatorAlias = 'eve-validator',
    [string]$PublicKeyPath = (Join-Path $HOME '.ssh\codex_eve_validator_ed25519.pub'),
    [string]$OpenStackHost = '192.168.1.30',
    [int]$OpenStackSshPort = 22,
    [int]$OpenStackApiPort = 5000,
    [string]$ManagementPrefix = '192.168.1.',
    [switch]$Apply
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ($OperatorAlias -notmatch '^[A-Za-z0-9._-]+$') {
    throw 'OperatorAlias contains unsupported characters.'
}
if (-not $Apply) {
    Write-Output 'DRY RUN: no remote changes were made. Re-run with -Apply after review.'
    exit 0
}
if (-not (Test-Path -LiteralPath $PublicKeyPath -PathType Leaf)) {
    throw 'The dedicated EVE validator public key is missing.'
}

$publicKey = (Get-Content -LiteralPath $PublicKeyPath -Raw).Trim()
if ($publicKey -notmatch '^ssh-ed25519 [A-Za-z0-9+/=]+ codex-eve-validator$') {
    throw 'The public key does not match the dedicated EVE validator format.'
}

$remoteRoot = Join-Path $PSScriptRoot 'remote'
$dispatcher = Get-Content -LiteralPath (Join-Path $remoteRoot 'codex-eve-dispatcher.sh.example') -Raw
$validator = Get-Content -LiteralPath (Join-Path $remoteRoot 'validate-eve-readonly.sh.example') -Raw
$sudoers = Get-Content -LiteralPath (Join-Path $remoteRoot 'eve-validator-sudoers.example') -Raw
$authorizedKey = Get-Content -LiteralPath (Join-Path $remoteRoot 'eve-validator-authorized-key.example') -Raw

$validator = $validator.Replace('<OPENSTACK_MANAGEMENT_HOST>', $OpenStackHost)
$validator = $validator.Replace('<OPENSTACK_SSH_PORT>', [string]$OpenStackSshPort)
$validator = $validator.Replace('<OPENSTACK_API_PORT>', [string]$OpenStackApiPort)
$validator = $validator.Replace('<EVE_MANAGEMENT_SUBNET_PREFIX>', $ManagementPrefix)
$authorizedKey = $authorizedKey.Replace('<DEDICATED_EVE_VALIDATOR_PUBLIC_KEY>', $publicKey)

function ConvertTo-Base64([string]$Value) {
    [Convert]::ToBase64String([Text.UTF8Encoding]::new($false).GetBytes(($Value -replace "`r`n", "`n")))
}

$dispatcher64 = ConvertTo-Base64 $dispatcher
$validator64 = ConvertTo-Base64 $validator
$sudoers64 = ConvertTo-Base64 $sudoers
$authorizedKey64 = ConvertTo-Base64 $authorizedKey

$remoteScript = @"
set -euo pipefail
if ! id codex-validator >/dev/null 2>&1; then
  useradd --create-home --shell /bin/bash codex-validator
fi
install -d -o codex-validator -g codex-validator -m 0700 /home/codex-validator/.ssh
if [ -s /home/codex-validator/.ssh/authorized_keys ]; then
  echo 'Refusing to replace an existing non-empty validator authorized_keys file.' >&2
  exit 3
fi
tmpdir=`$(mktemp -d)
trap 'rm -rf "`$tmpdir"' EXIT
printf '%s' '$dispatcher64' | base64 -d > "`$tmpdir/dispatcher"
printf '%s' '$validator64' | base64 -d > "`$tmpdir/validator"
printf '%s' '$sudoers64' | base64 -d > "`$tmpdir/sudoers"
printf '%s' '$authorizedKey64' | base64 -d > "`$tmpdir/authorized_keys"
bash -n "`$tmpdir/dispatcher"
bash -n "`$tmpdir/validator"
/usr/sbin/visudo -cf "`$tmpdir/sudoers"
install -o root -g root -m 0755 "`$tmpdir/dispatcher" /usr/local/sbin/codex-eve-dispatcher
install -o root -g root -m 0755 "`$tmpdir/validator" /usr/local/sbin/validate-eve-readonly
install -o root -g root -m 0440 "`$tmpdir/sudoers" /etc/sudoers.d/codex-eve-validator
install -o codex-validator -g codex-validator -m 0600 "`$tmpdir/authorized_keys" /home/codex-validator/.ssh/authorized_keys
bash -n /usr/local/sbin/codex-eve-dispatcher
bash -n /usr/local/sbin/validate-eve-readonly
/usr/sbin/visudo -cf /etc/sudoers.d/codex-eve-validator
stat -c '%U %G %a %n' /usr/local/sbin/codex-eve-dispatcher /usr/local/sbin/validate-eve-readonly /etc/sudoers.d/codex-eve-validator /home/codex-validator/.ssh/authorized_keys
echo 'EVE restricted validator endpoint installed.'
"@

$ssh = (Get-Command ssh -ErrorAction Stop).Source
$psi = New-Object Diagnostics.ProcessStartInfo
$psi.FileName = $ssh
$psi.Arguments = "-o BatchMode=yes -o ConnectTimeout=10 $OperatorAlias bash -s"
$psi.UseShellExecute = $false
$psi.RedirectStandardInput = $true
$psi.RedirectStandardOutput = $true
$psi.RedirectStandardError = $true
$process = [Diagnostics.Process]::Start($psi)
$process.StandardInput.Write($remoteScript)
$process.StandardInput.Close()
$stdout = $process.StandardOutput.ReadToEnd()
$stderr = $process.StandardError.ReadToEnd()
$process.WaitForExit()
if ($stdout) { Write-Output $stdout.TrimEnd() }
if ($stderr) { Write-Error $stderr.TrimEnd() }
exit $process.ExitCode
