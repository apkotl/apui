from src.config import settings


# CORS settings (Production mode)
CORS_ORIGINS_PROD = [
    f"{settings.WEB_PROTOCOL}://{settings.WEB_HOST}",
    f"{settings.WEB_PROTOCOL}://{settings.WEB_HOST}:{settings.WEB_PORT}",
]

CORS_CONFIG_PROD = {
    'allow_origins': CORS_ORIGINS_PROD,
    'allow_credentials': True,
    'allow_methods': ["*"], # Allow all methods (GET, POST, PUT, DELETE, etc.)
    'allow_headers': ["*"], # Allow all headers
}

# CORS settings (Development mode)
CORS_ORIGINS_DEV = [
    #"http://localhost:5173",
    #f"{settings.WEB_PROTOCOL}://{settings.WEB_HOST}",
    #f"{settings.WEB_PROTOCOL}://{settings.WEB_HOST}:{settings.WEB_PORT}",
    "*"
]

CORS_CONFIG_DEV = {
    'allow_origins': CORS_ORIGINS_DEV,
    'allow_credentials': True,
    'allow_methods': ["*"], # Allow all methods (GET, POST, PUT, DELETE, etc.)
    'allow_headers': ["*"], # Allow all headers
}