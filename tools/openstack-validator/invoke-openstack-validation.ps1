[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# This wrapper intentionally exposes no remote-command parameter. The SSH key
# and alias configuration live outside the repository. The remote forced
# command accepts only "validate-all" and produces sanitized read-only output.
$ssh = Get-Command ssh -ErrorAction Stop

& $ssh.Source `
    -o BatchMode=yes `
    -o ConnectTimeout=10 `
    openstack-validator `
    validate-all

exit $LASTEXITCODE
