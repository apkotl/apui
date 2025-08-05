from abc import ABC, abstractmethod
from typing import Optional, List, Tuple
from ..models import BookGenresOrm, BooksOrm
from ..schemas import BookGenre, BookGenreCreate, BookGenreListQueryParams


class IBookGenreRepository(ABC):
    @abstractmethod
    async def get_by_id(self, book_id: int) -> Optional[BookGenresOrm]:
        pass

    @abstractmethod
    async def create(self, book_data: BookGenreCreate) -> BookGenresOrm:
        pass

    @abstractmethod
    async def update(self, book_id: int, book_data: BookGenreCreate) -> Optional[BookGenresOrm]:
        pass

    @abstractmethod
    async def delete(self, book_id: int) -> bool:
        pass

    @abstractmethod
    async def get_book_genres_with_pagination(
            self,
            params: BookGenreListQueryParams
    ) -> Tuple[List[BookGenre], int]:
        """
        Получить список жанров книг с пагинацией и сортировкой
        Возвращает (список_жанров_книг, общее_количество)
        """
        pass