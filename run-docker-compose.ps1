<#
.SYNOPSIS
    PowerShell script to manage Docker Compose for dev and prod environments.

.DESCRIPTION
    This script allows you to:
    - Run Docker Compose for 'dev' or 'prod' environments with specific configuration files.
    - Stop, start, or remove Docker Compose containers and volumes.

.USAGE
    .\docker-compose.ps1 [command]
    Commands:
        up-prod        Run Docker Compose for production environment
        up-dev         Run Docker Compose for development environment
        stop           Stop all running containers
        start          Start stopped containers
        down           Stop and remove containers
        down-volumes   Stop and remove containers and volumes

.EXAMPLE
    .\docker-compose.ps1 up-prod
    .\docker-compose.ps1 up-dev
    .\docker-compose.ps1 stop
    .\docker-compose.ps1 start
    .\docker-compose.ps1 down
    .\docker-compose.ps1 down-volumes
#>

param (
    [Parameter(Position=0)]
    [ValidateSet("up-prod", "up-dev", "stop", "start", "down", "down-volumes")]
    [string]$Command
)

# Check if Docker Compose is installed
if (-not (Get-Command docker-compose -ErrorAction SilentlyContinue)) {
    Write-Error "Docker Compose is not installed or not found in PATH. Please install Docker Compose."
    exit 1
}

switch ($Command) {
    "up-prod" {
        Write-Host "Setting APP_ENVIRONMENT to prod and running Docker Compose..."
        $env:APP_ENVIRONMENT = "prod"
        docker-compose -f docker-compose.yaml -f docker-compose.prod.yaml up -d --build
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Failed to run Docker Compose for prod."
            exit 1
        }
    }
    "up-dev" {
        Write-Host "Setting APP_ENVIRONMENT to dev and running Docker Compose..."
        $env:APP_ENVIRONMENT = "dev"
        docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d --build
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Failed to run Docker Compose for dev."
            exit 1
        }
    }
    "stop" {
        Write-Host "Stopping Docker Compose containers..."
        docker-compose stop
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Failed to stop containers."
            exit 1
        }
    }
    "start" {
        Write-Host "Starting Docker Compose containers..."
        docker-compose start
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Failed to start containers."
            exit 1
        }
    }
    "down" {
        Write-Host "Stopping and removing Docker Compose containers..."
        docker-compose down
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Failed to remove containers."
            exit 1
        }
    }
    "down-volumes" {
        Write-Host "Stopping and removing Docker Compose containers and volumes..."
        docker-compose down --volumes
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Failed to remove containers and volumes."
            exit 1
        }
    }
    default {
        Write-Host "Invalid command. Usage: .\docker-compose.ps1 [prod|dev|stop|start|down|down-volumes]"
        exit 1
    }
}

Write-Host "Command '$Command' executed successfully."