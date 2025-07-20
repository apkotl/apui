<#
.SYNOPSIS
This PowerShell script runs a Uvicorn server locally.

.DESCRIPTION
This PowerShell script sets an environment variable,
installs Python packages using Poetry,
and then starts the Uvicorn server.

.PARAMETER Environment
The operation mode: dev, prod, or qa. Default is 'dev'.
#>


[CmdletBinding()]
Param(
    [Alias("environment", "env", "e")]
    [ValidateSet("dev", "prod", "qa")]
    [string]$ENV_SHORT = ""
)


# Set the default environment if the parameter was not provided
if ([string]::IsNullOrWhiteSpace($ENV_SHORT)) {
    $ENV_SHORT = Read-Host -Prompt 'Set environment: dev/prod/qa (by default: dev)'
    if ([string]::IsNullOrWhiteSpace($ENV_SHORT) -or ($ENV_SHORT -notin "dev", "prod", "qa")) {
        $ENV_SHORT = "dev"
    }
}

$POETRY = "poetry"
$ENVIRONMENT = "development"
if ($ENV_SHORT -eq "prod") {
    $ENVIRONMENT = "production"
}
elseif ($ENV_SHORT -eq "qa") {
    $ENVIRONMENT = "qa"
}

Write-Host "Preparing to run script with:" -ForegroundColor Cyan
Write-Host " - ENV_SHORT = $ENV_SHORT" -ForegroundColor Cyan
Write-Host " - ENVIRONMENT = $ENVIRONMENT" -ForegroundColor Cyan
Write-Host ""


Write-Host ""
Write-Host "Setting the environment variable ENVIRONMENT to '$ENVIRONMENT'..." -ForegroundColor Green
$env:ENVIRONMENT=$ENVIRONMENT

Write-Host ""
Write-Host "Running 'poetry install' ..." -ForegroundColor Green
$poetryArguments = @(
    "install",
    "--no-root"
)
try {
    # --sync removes unused packages. --no-root is typically for "editable" installs,
    # but '--sync' is generally preferred for dependency management.
    # poetry install --no-root

    Start-Process -FilePath $POETRY -ArgumentList $poetryArguments -Wait -NoNewWindow
}
catch {
    Write-Error "Error while executing 'poetry install': $($_.Exception.Message)"
    exit 1
}

Write-Host ""
Write-Host "Starting Uvicorn server ..." -ForegroundColor Green

# Define Uvicorn arguments as an array of strings
$poetryArguments = @(
    "run",
    "uvicorn",
    "src.main:app",
    "--host", "0.0.0.0",
    "--port", "8000"
)

if ($ENVIRONMENT -eq "development") {
    $poetryArguments += " --reload"
    Write-Host "Running Uvicorn in development mode (with --reload) ..." -ForegroundColor Yellow
}
else {
    Write-Host "Running Uvicorn in mode $ENVIRONMENT ..." -ForegroundColor Cyan
}

try {
    Start-Process -FilePath $POETRY -ArgumentList $poetryArguments -Wait -NoNewWindow
}
catch {
    Write-Error "Error starting Uvicorn server: $($_.Exception.Message)"
    exit 1
}
