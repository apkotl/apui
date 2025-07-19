from src.config import settings


db_host = "db" if settings.DOCKER_CONTAINER_MODE else settings.NGINX_WEB_SERVER_NAME

DATABASE_URL = f"postgresql+asyncpg://" \
    f"{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}" \
    f"@" \
    f"{db_host}:{settings.POSTGRES_PORT}/" \
    f"{settings.POSTGRES_DB}"

DATABASE_CONFIG = {
    'url': DATABASE_URL,
    'pool_size': 5,
    'max_overflow': 10,
}
