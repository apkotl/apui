from typing import Optional

from src.core.schemas import ListResponse
from .i_book import IBookService
from ..repositories.i_book import IBookRepository
from ..schemas import Book, BookCreate, BookListQueryParams, BookWithObjects


class BookService(IBookService):
    def __init__(self, book_repository: IBookRepository):
        self.book_repository = book_repository

    async def get_book_by_id(self, book_id: int) -> Optional[BookWithObjects]:
        book = await self.book_repository.get_by_id(book_id)
        if book is None:
            return None
        return BookWithObjects.model_validate(book, from_attributes=True)

    async def create_book(self, book_data: BookCreate) -> Book:
        book = await self.book_repository.create(book_data)
        return Book.model_validate(book)

    async def update_book(self, book_id: int, book_data: BookCreate) -> Optional[Book]:
        book = await self.book_repository.update(book_id, book_data)
        if book is None:
            return None
        return Book.model_validate(book)

    async def delete_book(self, book_id: int) -> bool:
        return await self.book_repository.delete(book_id)

    async def get_books_list(self, params: BookListQueryParams) -> ListResponse[Book]:
        """Получить список книг с пагинацией, сортировкой и поиском"""

        books_orm, total_count = await self.book_repository.get_with_pagination(params)

        # Сериализуем книги
        books = [Book.model_validate(book_orm) for book_orm in books_orm]

        # Создаем информацию о пагинации
        pagination_info = {
            "total": total_count,
            "offset": params.offset,
            "limit": params.limit,
            "has_more": (params.offset + params.limit) < total_count,
            "current_page": (params.offset // params.limit) + 1,
            "total_pages": (total_count + params.limit - 1) // params.limit
        }

        # Формируем сообщение
        message = f"Found {total_count} books"
        if params.search:
            message += f" matching '{params.search}'"

        return ListResponse[Book](
            items=books,
            pagination=pagination_info,
            message=message
        )