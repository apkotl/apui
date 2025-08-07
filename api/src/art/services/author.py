from typing import Optional

from src.core.schemas import ListResponse
from .i_author import IAuthorService
from ..repositories.i_author import IAuthorRepository
from ..schemas import Author, AuthorCreate, AuthorListQueryParams, AuthorWithBooks


class AuthorService(IAuthorService):
    def __init__(self, author_repository: IAuthorRepository):
        self.author_repository = author_repository

    async def get_author_by_id(self, author_id: int) -> Optional[Author]:
        author = await self.author_repository.get_by_id(author_id)
        if author is None:
            return None
        return Author.model_validate(author)

    async def get_author_by_id_with_books(self, author_id: int) -> Optional[AuthorWithBooks]:
        author = await self.author_repository.get_by_id_with_books(author_id)
        if author is None:
            return None
        return AuthorWithBooks.model_validate(author, from_attributes=True)

    async def create_author(self, author_data: AuthorCreate) -> Author:
        author = await self.author_repository.create(author_data)
        return Author.model_validate(author)

    async def update_author(self, author_id: int, author_data: AuthorCreate) -> Optional[Author]:
        author = await self.author_repository.update(author_id, author_data)
        if author is None:
            return None
        return Author.model_validate(author)

    async def delete_author(self, author_id: int) -> bool:
        return await self.author_repository.delete(author_id)

    async def get_authors_list(self, params: AuthorListQueryParams) -> ListResponse[Author]:
        """Получить список авторов книг с пагинацией, сортировкой и поиском"""

        authors_orm, total_count = await self.author_repository.get_with_pagination(params)

        # Сериализуем авторов книг
        authors = [Author.model_validate(author_orm) for author_orm in authors_orm]

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
        message = f"Found {total_count} authors"
        if params.search:
            message += f" matching '{params.search}'"

        return ListResponse[Author](
            items=authors,
            pagination=pagination_info,
            message=message
        )