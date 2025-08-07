from typing import Optional, Tuple, List
from sqlalchemy import select, func, or_, asc, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from .i_author import IAuthorRepository
from ..models import AuthorsOrm
from ..schemas import Author, AuthorCreate, AuthorListQueryParams, AuthorOrderBy


class AuthorRepository(IAuthorRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, author_id: int) -> Optional[AuthorsOrm]:
        query = select(AuthorsOrm).where(AuthorsOrm.id == author_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_by_id_with_books(self, author_id: int) -> Optional[AuthorsOrm]:
        query = (select(AuthorsOrm).
                 options(joinedload(AuthorsOrm.books)).
                 where(AuthorsOrm.id == author_id))
        result = await self.session.execute(query)
        return result.scalars().first()


    async def create(self, author_data: AuthorCreate) -> AuthorsOrm:
        new_author = AuthorsOrm(
            first_name =author_data.first_name,
            last_name=author_data.last_name,
            #
            # TODO
            #
        )
        self.session.add(new_author)
        await self.session.flush()
        await self.session.commit()
        await self.session.refresh(new_author)
        return new_author

    async def update(self, author_id: int, author_data: AuthorCreate) -> Optional[AuthorsOrm]:
        author = await self.get_by_id(author_id)
        if author is None:
            return None

        author.first_name = author_data.first_name
        author.last_name = author_data.last_name
        #
        # TODO
        #
        await self.session.commit()
        await self.session.refresh(author)
        return author

    async def delete(self, author_id: int) -> bool:
        author = await self.get_by_id(author_id)
        if author is None:
            return False

        await self.session.delete(author)
        await self.session.commit()
        return True

    async def get_with_pagination(
            self,
            params: AuthorListQueryParams
    ) -> Tuple[List[Author], int]:
        """Получить список авторов книг с пагинацией, сортировкой и поиском"""

        # Базовый запрос
        base_query = select(AuthorsOrm)
        count_query = select(func.count(AuthorsOrm.id))

        # Добавляем поиск если указан
        if params.search:
            search_filter = or_(
                AuthorsOrm.first_name.ilike(f"%{params.search}%"),
                AuthorsOrm.last_name.ilike(f"%{params.search}%")
                #
                # TODO
                #
            )
            base_query = base_query.where(search_filter)
            count_query = count_query.where(search_filter)

        # Получаем общее количество записей
        total_result = await self.session.execute(count_query)
        total_count = total_result.scalar()

        # Добавляем сортировку
        order_column = self._get_order_column(params.order_by)
        base_query = base_query.order_by(order_column)

        # Добавляем пагинацию
        base_query = base_query.offset(params.offset).limit(params.limit)

        # Выполняем запрос
        result = await self.session.execute(base_query)
        authors = result.scalars().all()

        return list(authors), total_count

    def _get_order_column(self, order_by: AuthorOrderBy):
        """Получить колонку и направление сортировки"""
        order_map = {
            AuthorOrderBy.ID_ASC: asc(AuthorsOrm.id),
            AuthorOrderBy.ID_DESC: desc(AuthorsOrm.id),
            AuthorOrderBy.LAST_NAME_ASC: asc(AuthorsOrm.last_name),
            AuthorOrderBy.LAST_NAME_DESC: desc(AuthorsOrm.last_name),
            #
            # TODO
            #
            AuthorOrderBy.CREATED_AT_ASC: asc(AuthorsOrm.created_at) if hasattr(AuthorsOrm, 'created_at') else asc(
                AuthorsOrm.id),
            AuthorOrderBy.CREATED_AT_DESC: desc(AuthorsOrm.created_at) if hasattr(AuthorsOrm, 'created_at') else desc(
                AuthorsOrm.id),
        }
        return order_map.get(order_by, asc(AuthorsOrm.id))
