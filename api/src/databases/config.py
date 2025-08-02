from src.config import settings


db_host = "db" if settings.IS_CONTAINER else "localhost"
redis_host = "redis" if settings.IS_CONTAINER else "localhost"


# PostgresSQL
DATABASE_URL = f"postgresql+asyncpg://" \
    f"{settings.DB_USER}:{settings.DB_PASSWORD}" \
    f"@" \
    f"{db_host}:{settings.DB_PORT}/" \
    f"{settings.DB_NAME}"

DATABASE_CONFIG = {
    'url': DATABASE_URL,
    'pool_size': 5,
    'max_overflow': 10,
}


# Redis
REDIS_URL = f"redis://{redis_host}:{settings.REDIS_PORT}/0"

REDIS_CONFIG = {
    'url': REDIS_URL,
    'encoding': 'utf-8',
    'decode_responses': True,
    'max_connections': 20,
    'retry_on_timeout': True,
    'socket_timeout': 5,
    'socket_connect_timeout': 5,
}