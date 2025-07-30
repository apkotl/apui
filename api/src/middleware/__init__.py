from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.core import const
from src.config import settings

from .cors import CORS_CONFIG_PROD, CORS_CONFIG_DEV
from .logging import LoggingMiddleware


def apply_middleware(app: FastAPI) -> FastAPI:
    """
    Add all middleware configurations

    Add CORS configuration:
    Enabled here for not container or development mode only
    For production mode processed by Nginx
    #app.add_middleware(CORSMiddleware, **CORS_CONFIG_PROD)

    Add Logging configuration:

    :param app: current FastAPI application    :return:
    """

    if (not settings.IS_CONTAINER) or (settings.ENVIRONMENT == const.DEVELOPMENT):
        app.add_middleware(CORSMiddleware, **CORS_CONFIG_DEV)

    app.add_middleware(LoggingMiddleware)

    return app