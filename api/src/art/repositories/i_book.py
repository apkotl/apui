from abc import ABC, abstractmethod
from typing import Optional, List, Tuple
from ..models import BooksOrm, BooksOrm
from ..schemas import Book, BookCreate, BookListQueryParams


class IBookRepository(ABC):
    @abstractmethod
    async def get_by_id(self, book_id: int) -> Optional[BooksOrm]:
        pass

    @abstractmethod
    async def create(self, book_data: BookCreate) -> BooksOrm:
        pass

    @abstractmethod
    async def update(self, book_id: int, book_data: BookCreate) -> Optional[BooksOrm]:
        pass

    @abstractmethod
    async def delete(self, book_id: int) -> bool:
        pass

    @abstractmethod
    async def get_with_pagination(
            self,
            params: BookListQueryParams
    ) -> Tuple[List[Book], int]:
        """
        Получить список книг с пагинацией и сортировкой
        Возвращает (список_жанров_книг, общее_количество)
        """
        pass