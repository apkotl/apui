from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.databases.dependencies import get_async_session

from .repositories.book_genre import BookGenreRepository
from .services.book_genre import BookGenreService

from .repositories.i_book_genre import IBookGenreRepository
from .services.i_book_genre import IBookGenreService



def get_book_genre_repository(session: AsyncSession = Depends(get_async_session)) -> IBookGenreRepository:
    return BookGenreRepository(session)

def get_book_genre_service(
    book_genre_repository: IBookGenreRepository = Depends(get_book_genre_repository)
) -> IBookGenreService:
    return BookGenreService(book_genre_repository)