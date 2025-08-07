from abc import ABC, abstractmethod
from typing import Optional

from src.core.schemas import ListResponse
from ..schemas import Author, AuthorCreate, AuthorListQueryParams, AuthorWithBooks


class IAuthorService(ABC):
    @abstractmethod
    async def get_author_by_id(self, author_id: int) -> Optional[Author]:
        pass

    @abstractmethod
    async def get_author_by_id_with_books(self, author_id: int) -> Optional[AuthorWithBooks]:
        pass

    @abstractmethod
    async def create_author(self, author_data: AuthorCreate) -> Author:
        pass

    @abstractmethod
    async def update_author(self, author_id: int, author_data: AuthorCreate) -> Optional[Author]:
        pass

    @abstractmethod
    async def delete_author(self, author_id: int) -> bool:
        pass

    @abstractmethod
    async def get_authors_list(self, params: AuthorListQueryParams) -> ListResponse[Author]:
        """Получить список авторов книг с пагинацией и сортировкой"""
        pass