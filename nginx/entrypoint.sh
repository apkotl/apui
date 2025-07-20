#!/bin/sh
set -e


# Perform variable substitution in the Nginx configuration template
envsubst '$API_HOST $API_PROTOCOL $API_PORT $API_UVICORN_PORT $WEB_HOST $WEB_PROTOCOL $WEB_PORT' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf


# Execute the command passed in CMD
exec "$@"
