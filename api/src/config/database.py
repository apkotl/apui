from src.config import settings


db_host = "db" if settings.IS_CONTAINER else "localhost"

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
