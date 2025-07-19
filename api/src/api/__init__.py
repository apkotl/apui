from fastapi import APIRouter

from src.api.info import router as info_router
from src.api.db_setup import router as db_setup_router
from src.api.books import router as books_router



main_router = APIRouter()
main_router.include_router(info_router)
main_router.include_router(db_setup_router)
main_router.include_router(books_router)