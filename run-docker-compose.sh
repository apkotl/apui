#!/bin/bash

# docker-compose.sh
# This script manages Docker Compose for dev and prod environments.
#
# Usage:
#   ./docker-compose.sh [command]
# Commands:
#   up-prod        Run Docker Compose for production environment
#   up-dev         Run Docker Compose for development environment
#   stop           Stop all running containers
#   start          Start stopped containers
#   down           Stop and remove containers
#   down-volumes   Stop and remove containers and volumes
#
# Example:
#   ./docker-compose.sh up-prod
#   ./docker-compose.sh up-dev
#   ./docker-compose.sh stop
#   ./docker-compose.sh start
#   ./docker-compose.sh down
#   ./docker-compose.sh down-volumes

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Error: Docker Compose is not installed or not found in PATH. Please install Docker Compose."
    exit 1
fi

# Check if a command was provided
if [ $# -eq 0 ]; then
    echo "Error: No command provided. Usage: $0 [up-prod|up-dev|stop|start|down|down-volumes]"
    exit 1
fi

case "$1" in
    up-prod)
        echo "Setting APP_ENVIRONMENT to prod and running Docker Compose..."
        export APP_ENVIRONMENT=prod
        docker-compose -f docker-compose.yaml -f docker-compose.prod.yaml up -d --build
        if [ $? -ne 0 ]; then
            echo "Error: Failed to run Docker Compose for prod."
            exit 1
        fi
        ;;
    up-dev)
        echo "Setting APP_ENVIRONMENT to dev and running Docker Compose..."
        export APP_ENVIRONMENT=dev
        docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d --build
        if [ $? -ne 0 ]; then
            echo "Error: Failed to run Docker Compose for dev."
            exit 1
        fi
        ;;
    stop)
        echo "Stopping Docker Compose containers..."
        docker-compose stop
        if [ $? -ne 0 ]; then
            echo "Error: Failed to stop containers."
            exit 1
        fi
        ;;
    start)
        echo "Starting Docker Compose containers..."
        docker-compose start
        if [ $? -ne 0 ]; then
            echo "Error: Failed to start containers."
            exit 1
        fi
        ;;
    down)
        echo "Stopping and removing Docker Compose containers..."
        docker-compose down
        if [ $? -ne 0 ]; then
            echo "Error: Failed to remove containers."
            exit 1
        fi
        ;;
    down-volumes)
        echo "Stopping and removing Docker Compose containers and volumes..."
        docker-compose down --volumes
        if [ $? -ne 0 ]; then
            echo "Error: Failed to remove containers and volumes."
            exit 1
        fi
        ;;
    *)
        echo "Error: Invalid command. Usage: $0 [up-prod|up-dev|stop|start|down|down-volumes]"
        exit 1
        ;;
esac

echo "Command '$1' executed successfully."