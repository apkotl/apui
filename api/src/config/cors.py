from src.config.settings import  settings


# CORS settings
CORS_ORIGINS = [
    f"{settings.NGINX_WEB_HTTP_PROTOCOL}://{settings.NGINX_WEB_SERVER_NAME}",

    #"http://localhost",
    #"http://localhost:5173",
    #"http://your_domain.com",
]

CORS_CONFIG = {
    'allow_origins': CORS_ORIGINS,
    'allow_credentials': True,
    'allow_methods': ["*"], # Allow all methods (GET, POST, PUT, DELETE, etc.)
    'allow_headers': ["*"], # Allow all headers
}