#!/bin/bash

#
# SYNOPSIS
# This Bash script simplifies Docker Compose operations for different environments.
#
# DESCRIPTION
# This script allows you to run various Docker Compose commands (up, start, stop, down)
# while dynamically selecting the appropriate Docker Compose file based on the
# specified environment (dev, prod, qa). It supports passing additional arguments
# directly to the Docker Compose command.
#
# USAGE
# ./run-docker-compose.sh [-e <dev|prod|qa>] <compose_command> [additional_args...]
#
# PARAMETERS
# -e, --env, --environment <dev|prod|qa>
#   The operational mode for Docker Compose: 'dev', 'prod', or 'qa'. Default is 'dev'.
#
# compose_command
#   The Docker Compose command to execute (e.g., 'up', 'start', 'stop', 'down').
#   This is a positional parameter and should be the first argument after '--env'.
#
# additional_args
#   Any additional arguments to pass directly to the Docker Compose command.
#

# Default environment
EnvironmentShort="dev"
ComposeCommand=""
PassthruArgs=() # Initialize as an empty array

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case "$1" in
        -e|--env|--environment)
            if [ -n "$2" ] && [[ "$2" =~ ^(dev|prod|qa)$ ]]; then
                EnvironmentShort="$2"
                shift 2 # Consume argument and its value
            else
                echo "Error: Invalid or missing value for $1. Please use 'dev', 'prod', or 'qa'." >&2
                exit 1
            fi
            ;;
        up|start|stop|down)
            if [ -z "$ComposeCommand" ]; then # Only set if not already set (first positional arg)
                ComposeCommand="$1"
            else
                PassthruArgs+=("$1") # Add to passthrough if already command set
            fi
            shift # Consume argument
            ;;
        *) # Catch all other arguments as passthrough
            PassthruArgs+=("$1")
            shift # Consume argument
            ;;
    esac
done

# Validate ComposeCommand
if [ -z "$ComposeCommand" ]; then
    echo "Error: Docker Compose command (up, start, stop, down) is mandatory." >&2
    exit 1
fi

# 1. Map short environment to full environment name & set environment variables
case "$EnvironmentShort" in
    prod)
        EnvironmentFull="production"
        ;;
    qa)
        EnvironmentFull="qa"
        ;;
    dev)
        EnvironmentFull="development"
        ;;
    *) # Should not be reached due to validation, but as a fallback
        EnvironmentFull="development"
        ;;
esac

export ENV_SHORT="$EnvironmentShort"
export ENVIRONMENT="$EnvironmentFull"

ENV_FILE=".env.$EnvironmentFull"
DOCKER="docker"

# Define colors for output
COLOR_CYAN='\033[0;36m'
COLOR_GREEN='\033[0;32m'
COLOR_RESET='\033[0m' # Reset to default color

echo -e "${COLOR_CYAN}Preparing to run Docker Compose with:${COLOR_RESET}"
echo -e "${COLOR_CYAN} - Environment (short): ${EnvironmentShort}${COLOR_RESET}"
echo -e "${COLOR_CYAN} - Environment (full):  ${EnvironmentFull}${COLOR_RESET}"
echo -e "${COLOR_CYAN} - Env File:  ${ENV_FILE}${COLOR_RESET}"
echo -e "${COLOR_CYAN} - Docker Compose Command: ${ComposeCommand}${COLOR_RESET}"
if [ ${#PassthruArgs[@]} -gt 0 ]; then
    echo -e "${COLOR_CYAN} - Additional Arguments: ${PassthruArgs[*]}${COLOR_RESET}"
fi
echo ""

# 2. Build the base Docker Compose arguments
# -f docker-compose.base.yaml -f docker-compose.{env_short}.yaml
baseArgs=(
    "compose"
    "--env-file" "$ENV_FILE"
    "-f" "docker-compose.base.yaml"
    "-f" "docker-compose.$EnvironmentShort.yaml"
)

# 3.0. - Create args for run command, if need (Production specific run)
DockerComposeArgs_0=()
if [[ "$EnvironmentFull" =~ ^(production|development)$ ]]; then
    case "$ComposeCommand" in
        "up"|"start")
            DockerComposeArgs_0=("${baseArgs[@]}" "run" "--rm" "--build" "web_vue3")
            ;;
        # For 'stop' and 'down' in production, DockerComposeArgs_0 remains empty, as per PS script
        *)
            ;;
    esac
fi

# 3.1. - Add command, addition args and list of services
# The baseArgs variable is modified here, so we need to be careful with its state.
# It's better to create a new array for DockerComposeArgs_1 from scratch or from baseArgs.
currentComposeArgs=("${baseArgs[@]}" "$ComposeCommand") # Start with base + main command

if [ ${#PassthruArgs[@]} -gt 0 ]; then
    currentComposeArgs+=("${PassthruArgs[@]}")
fi

DockerComposeArgs_1=()
case "$ComposeCommand" in
    "up")
        DockerComposeArgs_1=("${currentComposeArgs[@]}" "-d" "--build" "api" "db" "redis" "nginx")
        ;;
    "stop"|"start"|"down")
        DockerComposeArgs_1=("${currentComposeArgs[@]}" "api" "db" "redis" "nginx")
        ;;
    *)
        # Default case for other commands if any, remains empty
        ;;
esac

# 4. Execute docker compose
echo -e "${COLOR_GREEN}Executing Docker Compose commands:${COLOR_RESET}"
echo ""

# Execute DockerComposeArgs_0 if present
if [ ${#DockerComposeArgs_0[@]} -gt 0 ]; then
    echo -e "${COLOR_GREEN}Executing: ${DOCKER} ${DockerComposeArgs_0[*]}${COLOR_RESET}"
    echo ""
    if ! "$DOCKER" "${DockerComposeArgs_0[@]}"; then
        echo "Error executing Docker Compose command (DockerComposeArgs_0). Exiting." >&2
        exit 1
    fi
fi

# Execute DockerComposeArgs_1 if present
if [ ${#DockerComposeArgs_1[@]} -gt 0 ]; then
    echo -e "${COLOR_GREEN}Executing: ${DOCKER} ${DockerComposeArgs_1[*]}${COLOR_RESET}"
    echo ""
    if ! "$DOCKER" "${DockerComposeArgs_1[@]}"; then
        echo "Error executing Docker Compose command (DockerComposeArgs_1). Exiting." >&2
        exit 1
    fi
fi

echo ""
echo -e "${COLOR_GREEN}Docker Compose command(s) completed.${COLOR_RESET}"