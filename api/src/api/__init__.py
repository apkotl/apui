from fastapi import FastAPI


from src.api.auth import router as auth_router
from src.api.info import router as info_router
from src.api.db_setup import router as db_setup_router
from src.api.books import router as books_router


def apply_routers(app: FastAPI) -> FastAPI:
    app.include_router(auth_router)
    app.include_router(info_router)
    app.include_router(db_setup_router)
    app.include_router(books_router)
    return app
