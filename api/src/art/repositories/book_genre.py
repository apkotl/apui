from typing import Optional, Tuple, List
from sqlalchemy import select, func, or_, asc, desc
from sqlalchemy.ext.asyncio import AsyncSession
from .i_book_genre import IBookGenreRepository
from ..models import BookGenresOrm
from ..schemas import BookGenre, BookGenreCreate, BookGenreListQueryParams, BookGenreOrderBy


class BookGenreRepository(IBookGenreRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, book_genre_id: int) -> Optional[BookGenresOrm]:
        query = select(BookGenresOrm).where(BookGenresOrm.id == book_genre_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def create(self, book_genre_data: BookGenreCreate) -> BookGenresOrm:
        new_book_genre = BookGenresOrm(
            name=book_genre_data.name,
        )
        self.session.add(new_book_genre)
        await self.session.flush()
        await self.session.commit()
        await self.session.refresh(new_book_genre)
        return new_book_genre

    async def update(self, book_genre_id: int, book_genre_data: BookGenreCreate) -> Optional[BookGenresOrm]:
        book_genre = await self.get_by_id(book_genre_id)
        if book_genre is None:
            return None

        book_genre.name = book_genre_data.name
        await self.session.commit()
        await self.session.refresh(book_genre)
        return book_genre

    async def delete(self, book_genre_id: int) -> bool:
        book_genre = await self.get_by_id(book_genre_id)
        if book_genre is None:
            return False

        await self.session.delete(book_genre)
        await self.session.commit()
        return True

    async def get_book_genres_with_pagination(
            self,
            params: BookGenreListQueryParams
    ) -> Tuple[List[BookGenre], int]:
        """Получить список книг с пагинацией, сортировкой и поиском"""

        # Базовый запрос
        base_query = select(BookGenresOrm)
        count_query = select(func.count(BookGenresOrm.id))

        # Добавляем поиск если указан
        if params.search:
            search_filter = or_(
                #BookModel.title.ilike(f"%{params.search}%"),
                #BookModel.author.ilike(f"%{params.search}%")
                BookGenresOrm.name.ilike(f"%{params.search}%")
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
        book_genres = result.scalars().all()

        return list(book_genres), total_count

    def _get_order_column(self, order_by: BookGenreOrderBy):
        """Получить колонку и направление сортировки"""
        order_map = {
            BookGenreOrderBy.ID_ASC: asc(BookGenresOrm.id),
            BookGenreOrderBy.ID_DESC: desc(BookGenresOrm.id),
            BookGenreOrderBy.NAME_ASC: asc(BookGenresOrm.name),
            BookGenreOrderBy.NAME_DESC: desc(BookGenresOrm.name),
            #BookOrderBy.TITLE_ASC: asc(BookModel.title),
            #BookOrderBy.TITLE_DESC: desc(BookModel.title),
            #BookOrderBy.AUTHOR_ASC: asc(BookModel.author),
            #BookOrderBy.AUTHOR_DESC: desc(BookModel.author),
            BookGenreOrderBy.CREATED_AT_ASC: asc(BookGenresOrm.created_at) if hasattr(BookGenresOrm, 'created_at') else asc(
                BookGenresOrm.id),
            BookGenreOrderBy.CREATED_AT_DESC: desc(BookGenresOrm.created_at) if hasattr(BookGenresOrm, 'created_at') else desc(
                BookGenresOrm.id),
        }
        return order_map.get(order_by, asc(BookGenresOrm.id))