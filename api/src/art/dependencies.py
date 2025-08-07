from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.databases.dependencies import get_async_session

from .repositories.author import AuthorRepository
from .repositories.book import BookRepository
from .repositories.book_genre import BookGenreRepository
from .services.author import AuthorService
from .services.book import BookService
from .services.book_genre import BookGenreService

from .repositories.i_author import IAuthorRepository
from .repositories.i_book import IBookRepository
from .repositories.i_book_genre import IBookGenreRepository
from .services.i_author import IAuthorService
from .services.i_book import IBookService
from .services.i_book_genre import IBookGenreService



def get_author_repository(session: AsyncSession = Depends(get_async_session)) -> IAuthorRepository:
    return AuthorRepository(session)

def get_author_service(
    author_repository: IAuthorRepository = Depends(get_author_repository)
) -> IAuthorService:
    return AuthorService(author_repository)


def get_book_genre_repository(session: AsyncSession = Depends(get_async_session)) -> IBookGenreRepository:
    return BookGenreRepository(session)

def get_book_genre_service(
    book_genre_repository: IBookGenreRepository = Depends(get_book_genre_repository)
) -> IBookGenreService:
    return BookGenreService(book_genre_repository)


def get_book_repository(session: AsyncSession = Depends(get_async_session)) -> IBookRepository:
    return BookRepository(session)

def get_book_service(
    book_repository: IBookRepository = Depends(get_book_repository)
) -> IBookService:
    return BookService(book_repository)

