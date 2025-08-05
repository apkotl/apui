from typing import Optional

from src.core.schemas import ListResponse
from .i_book_genre import IBookGenreService
from ..repositories.i_book_genre import IBookGenreRepository
from ..schemas import BookGenre, BookGenreCreate, BookGenreListQueryParams


class BookGenreService(IBookGenreService):
    def __init__(self, book_genre_repository: IBookGenreRepository):
        self.book_genre_repository = book_genre_repository

    async def get_book_genre_by_id(self, book_genre_id: int) -> Optional[BookGenre]:
        book_genre = await self.book_genre_repository.get_by_id(book_genre_id)
        if book_genre is None:
            return None
        return BookGenre.model_validate(book_genre)

    async def create_book_genre(self, book_genre_data: BookGenreCreate) -> BookGenre:
        book_genre = await self.book_genre_repository.create(book_genre_data)
        return BookGenre.model_validate(book_genre)

    async def update_book_genre(self, book_genre_id: int, book_genre_data: BookGenreCreate) -> Optional[BookGenre]:
        book_genre = await self.book_genre_repository.update(book_genre_id, book_genre_data)
        if book_genre is None:
            return None
        return BookGenre.model_validate(book_genre)

    async def delete_book_genre(self, book_id: int) -> bool:
        return await self.book_genre_repository.delete(book_id)

    async def get_book_genres_list(self, params: BookGenreListQueryParams) -> ListResponse[BookGenre]:
        """Получить список книг с пагинацией, сортировкой и поиском"""

        book_genres_orm, total_count = await self.book_genre_repository.get_book_genres_with_pagination(params)

        # Сериализуем жанры книг
        #serialized_books = [serialize_book(book) for book in books]
        book_genres = [BookGenre.model_validate(book_genre_orm) for book_genre_orm in book_genres_orm]

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

        return ListResponse[BookGenre](
            items=book_genres,
            pagination=pagination_info,
            message=message
        )