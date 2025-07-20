#!/bin/bash

#
# SYNOPSIS
# This Bash script runs a Uvicorn server locally.
#
# DESCRIPTION
# This Bash script sets an environment variable,
# installs Python packages using Poetry,
# and then starts the Uvicorn server.
#
# USAGE
# ./run_uvicorn.sh [-e <dev|prod|qa>]
#
# PARAMETERS
# -e, --env, --environment <dev|prod|qa>
#   The operation mode: dev, prod, or qa. Default is 'dev'.
#

# Set ENV_SHORT to empty
ENV_SHORT=""

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -e|--env|--environment)
            if [ -n "$2" ] && [[ "$2" =~ ^(dev|prod|qa)$ ]]; then
                ENV_SHORT="$2"
                shift # past argument
            else
                echo "Error: Invalid or missing value for $1. Please use 'dev', 'prod', or 'qa'." >&2
                exit 1
            fi
            ;;
        *)
            echo "Error: Unknown parameter passed: $1" >&2
            exit 1
            ;;
    esac
    shift # past argument or value
done

# If ENV_SHORT is still empty, prompt the user
if [ -z "$ENV_SHORT" ]; then
#if [ -z "$ENV_SHORT" ] || [[ "$ENV_SHORT" == "dev" ]]; then
#if [[ ! "$ENV_SHORT" =~ ^(dev|prod|qa)$ ]]; then
    read -p 'Set environment: dev/prod/qa (default: dev): ' USER_INPUT_ENV
    if [ -n "$USER_INPUT_ENV" ] && [[ "$USER_INPUT_ENV" =~ ^(dev|prod|qa)$ ]]; then
        ENV_SHORT="$USER_INPUT_ENV"
    else
        echo "No valid environment provided, defaulting to 'dev'."
        ENV_SHORT="dev"
    fi
fi

ENVIRONMENT=""
case "$ENV_SHORT" in
    prod)
        ENVIRONMENT="production"
        ;;
    qa)
        ENVIRONMENT="qa"
        ;;
    dev)
        ENVIRONMENT="development"
        ;;
    *)
        # This case should ideally not be reached due to validation above,
        # but as a fallback, default to development.
        ENVIRONMENT="development"
        ;;
esac

echo "Preparing to run script with:"
echo " - ENV_SHORT = $ENV_SHORT"
echo " - ENVIRONMENT = $ENVIRONMENT"
echo ""

echo ""
echo "Setting the environment variable ENVIRONMENT to '$ENVIRONMENT'..."
export ENVIRONMENT=$ENVIRONMENT

echo ""
echo "Running 'poetry install'..."
if ! poetry install --no-root; then
    echo "Error while executing 'poetry install'. Exiting." >&2
    exit 1
fi

echo ""
echo "Starting Uvicorn server..."
UVICORN_ARGS="src.main:app --host 0.0.0.0 --port 8000"

if [ "$ENVIRONMENT" = "development" ]; then
    UVICORN_ARGS+=" --reload" # Enable auto-reloading in development mode
    echo "Running Uvicorn in development mode (with --reload)..."
else
    echo "Running Uvicorn in '$ENVIRONMENT' mode..."
fi

if ! poetry run uvicorn $UVICORN_ARGS; then
    echo "Error starting Uvicorn server. Exiting." >&2
    exit 1
fi