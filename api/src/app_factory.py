from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.exceptions import apply_exception_handlers
from src.api import apply_routers
from src.config import CORS_CONFIG


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Pre initialization of the application
    :param app:
    :return:

    - log
    - cash
    - stream
    """
    #set_logging()

    # stream_repository = await get_streaming_repository_type()
    # await stream_repository.start(settings.kafka)

    yield


def create_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        docs_url='/docs',
        openapi_url='/docs.json',
    )

    # Add CORS configuration (Disabled here, processed by Nginx)
    # app.add_middleware(CORSMiddleware, **CORS_CONFIG)
    # app = apply_middleware(app)

    # Apply Routers
    app = apply_routers(app)

    # Apply Exceptions Handlers
    app = apply_exception_handlers(app)

    return app
