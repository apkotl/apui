from abc import ABC, abstractmethod
from typing import Optional

from src.core.schemas import ListResponse
from ..schemas import Book, BookCreate, BookListQueryParams, BookWithObjects


class IBookService(ABC):
    @abstractmethod
    async def get_book_by_id(self, book_id: int) -> Optional[BookWithObjects]:
        pass

    @abstractmethod
    async def create_book(self, book_data: BookCreate) -> Book:
        pass

    @abstractmethod
    async def update_book(self, book_id: int, book_data: BookCreate) -> Optional[Book]:
        pass

    @abstractmethod
    async def delete_book(self, book_id: int) -> bool:
        pass

    @abstractmethod
    async def get_books_list(self, params: BookListQueryParams) -> ListResponse[Book]:
        """Получить список книг с пагинацией и сортировкой"""
        pass