#!/bin/sh
set -e


# Perform variable substitution in the Nginx configuration template
envsubst '$NGINX_API_PORT $NGINX_API_SERVER_NAME $NGINX_API_HOST $API_PORT $NGINX_WEB_PORT $NGINX_WEB_SERVER_NAME' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf


# Execute the command passed in CMD
exec "$@"
