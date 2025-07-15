FROM nginx:alpine


# Устанавливаем gettext (для envsubst)
RUN apk add --no-cache gettext


# Копируем шаблон конфигурации Nginx
COPY nginx.conf.template /etc/nginx/nginx.conf.template


# Устанавливаем скрипт запуска, который будет выполнять подстановку
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh


# Open ports
EXPOSE 80
EXPOSE 443


# Используем наш entrypoint скрипт
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
# Указываем команду для запуска Nginx
CMD ["nginx", "-g", "daemon off;"]
