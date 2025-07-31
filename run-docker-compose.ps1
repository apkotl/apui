<#
.SYNOPSIS
This PowerShell script simplifies Docker Compose operations for different environments.

.DESCRIPTION
This script allows you to run various Docker Compose commands (up, start, stop, down)
while dynamically selecting the appropriate Docker Compose file based on the
specified environment (dev, prod, qa). It supports passing additional arguments
directly to the Docker Compose command.

.PARAMETER Environment
The operational mode for Docker Compose: 'dev', 'prod', or 'qa'. Default is 'dev'.

.PARAMETER ComposeCommand
The Docker Compose command to execute (e.g., 'up', 'start', 'stop', 'down').
This is a positional parameter and should be the first argument after '--env'.

.PARAMETER PassthruArgs
Any additional arguments to pass directly to the Docker Compose command.
#>

[CmdletBinding(PositionalBinding = $False, DefaultParameterSetName = 'Default')]
Param(
    [Alias("environment", "env", "e")]
    [ValidateSet("dev", "prod", "qa")]
    [string]$EnvironmentShort = "dev", # Default to 'dev'

    [Parameter(Mandatory = $True, Position = 0)]
    [ValidateSet("up", "start", "stop", "down")]
    [string]$ComposeCommand,

    [Parameter(ValueFromRemainingArguments = $True)]
    [string[]]$PassthruArgs
)


# 1. Map short environment to full environment name & set environment
$EnvironmentFull = switch ($EnvironmentShort) {
    "dev"  { "development" }
    "prod" { "production" }
    "qa"   { "qa" }
    default { "development" } # Fallback, though ValidateSet should prevent this
}

$env:ENV_SHORT=$EnvironmentShort
$env:ENVIRONMENT=$EnvironmentFull

$ENV_FILE = ".env.$EnvironmentFull"
$DOCKER = "docker"

Write-Host "Preparing to run Docker Compose with:" -ForegroundColor Cyan
Write-Host " - Environment (short): $EnvironmentShort" -ForegroundColor Cyan
Write-Host " - Environment (full):  $EnvironmentFull" -ForegroundColor Cyan
Write-Host " - Env File:  $ENV_FILE" -ForegroundColor Cyan
Write-Host " - Docker Compose Command: $ComposeCommand" -ForegroundColor Cyan
if ($PassthruArgs.Count -gt 0) {
    Write-Host " - Additional Arguments: $($PassthruArgs -join ' ')" -ForegroundColor Cyan
}
Write-Host ""


# 2. Build the base Docker Compose arguments
# -f docker-compose.base.yaml -f docker-compose.{env_short}.yaml
$baseArgs = @(
    "compose"
    "--env-file", "$ENV_FILE"
    "-f", "docker-compose.base.yaml",
    "-f", "docker-compose.$EnvironmentShort.yaml"
)

# 3.0. - Create args for run command, if need
$DockerComposeArgs_0 = @()
if (($EnvironmentFull -eq "production") -or ($EnvironmentFull -eq "development")) {
    $DockerComposeArgs_0 = switch ($ComposeCommand) {
        "up" { $baseArgs + @("run", "--rm", "--build", "web_vue3") }
        "stop" { @() }
        "start" { $baseArgs + @("run", "--rm", "--build", "web_vue3") }
        "down" { @() }
        default { @() }
    }
}

# 3.1. - Add command, addition args and list of services
$baseArgs = $baseArgs + $ComposeCommand
if ($PassthruArgs.Count -gt 0) {
    $baseArgs += $PassthruArgs
}
$DockerComposeArgs_1 = switch ($ComposeCommand) {
    "up" { $baseArgs + @("-d", "--build", "api", "db", "redis", "nginx") }
    "stop" { $baseArgs + @("api", "db", "redis", "nginx") }
    "start" { $baseArgs + @("api", "db", "redis", "nginx") }
    "down" { $baseArgs + @("api", "db", "redis", "nginx") }
    default { @() }
}

# 4. Execute docker compose
Write-Host "Executing command: docker compose" -ForegroundColor Green
Write-Host ""


if ($DockerComposeArgs_0.Count -gt 0) {
    Write-Host "Executing command: docker $($DockerComposeArgs_0 -join ' ')" -ForegroundColor Green
    Write-Host ""

    try {
        Start-Process -FilePath $DOCKER -ArgumentList $DockerComposeArgs_0 -Wait -NoNewWindow
    }
    catch {
        Write-Error "Error executing Docker Compose command: $($_.Exception.Message)"
        exit 1
    }
}

if ($DockerComposeArgs_1.Count -gt 0) {
    Write-Host "Executing command: docker $($DockerComposeArgs_1 -join ' ')" -ForegroundColor Green
    Write-Host ""

    try {
        Start-Process -FilePath $DOCKER -ArgumentList $DockerComposeArgs_1 -Wait -NoNewWindow
    }
    catch {
        Write-Error "Error executing Docker Compose command: $($_.Exception.Message)"
        exit 1
    }
}

Write-Host ""
Write-Host "Docker Compose command completed." -ForegroundColor Green