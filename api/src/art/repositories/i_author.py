from abc import ABC, abstractmethod
from typing import Optional, List, Tuple
from ..models import AuthorsOrm
from ..schemas import Author, AuthorCreate, AuthorListQueryParams


class IAuthorRepository(ABC):
    @abstractmethod
    async def get_by_id(self, author_id: int) -> Optional[AuthorsOrm]:
        pass

    async def get_by_id_with_books(self, author_id: int) -> Optional[AuthorsOrm]:
        pass

    @abstractmethod
    async def create(self, author_data: AuthorCreate) -> AuthorsOrm:
        pass

    @abstractmethod
    async def update(self, author_id: int, author_data: AuthorCreate) -> Optional[AuthorsOrm]:
        pass

    @abstractmethod
    async def delete(self, author_id: int) -> bool:
        pass

    @abstractmethod
    async def get_with_pagination(
            self,
            params: AuthorListQueryParams
    ) -> Tuple[List[Author], int]:
        """
        Получить список авторов книг с пагинацией и сортировкой
        Возвращает (список_жанров_книг, общее_количество)
        """
        pass