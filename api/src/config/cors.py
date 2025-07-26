from src.config.settings import settings


# CORS settings
CORS_ORIGINS = [
    f"{settings.WEB_PROTOCOL}://{settings.WEB_HOST}",
    f"{settings.WEB_PROTOCOL}://{settings.WEB_HOST}:{settings.WEB_PORT}",
]

CORS_CONFIG = {
    'allow_origins': CORS_ORIGINS,
    'allow_credentials': True,
    'allow_methods': ["*"], # Allow all methods (GET, POST, PUT, DELETE, etc.)
    'allow_headers': ["*"], # Allow all headers
}