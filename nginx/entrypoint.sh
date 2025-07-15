#!/bin/sh
set -e

# Выполняем подстановку переменных в файл конфигурации Nginx
envsubst '$NGINX_PORT $NGINX_SERVER_NAME $API_HOST $API_PORT' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf

# Выполняем команду, переданную в CMD
exec "$@"