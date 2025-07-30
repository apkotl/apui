from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.exceptions import apply_exception_handlers
from src.api import apply_routers
from src.middleware import apply_middleware

from src.config.logging import setup_logging, get_logger

logger = setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Pre initialization of the application
    :param app:
    :return:

    - log [v]
    - cash [-]
    - stream [-]
    """
    logger.info("🚀 Starting FastAPI application...")
    try:
        # Здесь можете добавить другую инициализацию
        # stream_repository = await get_streaming_repository_type()
        # await stream_repository.start(settings.kafka)

        logger.info("✅ Application startup completed successfully")

        yield

    except Exception as e:
        logger.error(f"❌ Error during application startup: {e}", exc_info=True)
        raise
    finally:
        logger.info("🛑 Shutting down FastAPI application...")




def create_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        docs_url='/docs',
        openapi_url='/docs.json',
    )

    logger.info("📝 Configuring FastAPI application...")

    # Apply Middle Ware
    app = apply_middleware(app)
    logger.info("✅ Middleware applied")

    # Apply Routers
    app = apply_routers(app)
    logger.info("✅ Routers applied")

    # Apply Exceptions Handlers
    app = apply_exception_handlers(app)
    logger.info("✅ Exception handlers applied")

    logger.info("🎯 FastAPI application configured successfully")

    return app
