from abc import ABC, abstractmethod
from typing import Optional

from src.core.schemas import ListResponse
from ..schemas import BookGenre, BookGenreCreate, BookGenreListQueryParams


class IBookGenreService(ABC):
    @abstractmethod
    async def get_book_genre_by_id(self, book_genre_id: int) -> Optional[BookGenre]:
        pass

    @abstractmethod
    async def create_book_genre(self, book_genre_data: BookGenreCreate) -> BookGenre:
        pass

    @abstractmethod
    async def update_book_genre(self, book_genre_id: int, book_genre_data: BookGenreCreate) -> Optional[BookGenre]:
        pass

    @abstractmethod
    async def delete_book_genre(self, book_genre_id: int) -> bool:
        pass

    @abstractmethod
    async def get_book_genres_list(self, params: BookGenreListQueryParams) -> ListResponse[BookGenre]:
        """Получить список книг с пагинацией и сортировкой"""
        pass