from typing import Optional, Tuple, List
from sqlalchemy import select, func, or_, asc, desc
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from .i_book import IBookRepository
from ..models import BooksOrm
from ..schemas import Book, BookCreate, BookListQueryParams, BookOrderBy


class BookRepository(IBookRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, book_id: int) -> Optional[BooksOrm]:
        #query = select(BooksOrm).where(BooksOrm.id == book_id)
        query = (
            select(BooksOrm).
            options(joinedload(BooksOrm.author)).
            options(joinedload(BooksOrm.genre)).
            where(BooksOrm.id == book_id)
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def create(self, book_data: BookCreate) -> BooksOrm:
        new_book = BooksOrm(
            title=book_data.title,
            #
            # TODO
            #
        )
        self.session.add(new_book)
        await self.session.flush()
        await self.session.commit()
        await self.session.refresh(new_book)
        return new_book

    async def update(self, book_id: int, book_data: BookCreate) -> Optional[BooksOrm]:
        book = await self.get_by_id(book_id)
        if book is None:
            return None

        book.title = book_data.title
        #
        # TODO
        #
        await self.session.commit()
        await self.session.refresh(book)
        return book

    async def delete(self, book_id: int) -> bool:
        book = await self.get_by_id(book_id)
        if book is None:
            return False

        await self.session.delete(book)
        await self.session.commit()
        return True

    async def get_with_pagination(
            self,
            params: BookListQueryParams
    ) -> Tuple[List[Book], int]:
        """Получить список книг с пагинацией, сортировкой и поиском"""

        # Базовый запрос
        base_query = select(BooksOrm)
        count_query = select(func.count(BooksOrm.id))

        # Добавляем поиск если указан
        if params.search:
            search_filter = or_(
                BooksOrm.title.ilike(f"%{params.search}%"),
                BooksOrm.author.ilike(f"%{params.search}%")
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
        books = result.scalars().all()

        return list(books), total_count

    def _get_order_column(self, order_by: BookOrderBy):
        """Получить колонку и направление сортировки"""
        order_map = {
            BookOrderBy.ID_ASC: asc(BooksOrm.id),
            BookOrderBy.ID_DESC: desc(BooksOrm.id),
            BookOrderBy.TITLE_ASC: asc(BooksOrm.title),
            BookOrderBy.TITLE_DESC: desc(BooksOrm.title),
            #
            # TODO
            #
            #BookOrderBy.AUTHOR_ASC: asc(BookModel.author),
            #BookOrderBy.AUTHOR_DESC: desc(BookModel.author),
            BookOrderBy.CREATED_AT_ASC: asc(BooksOrm.created_at) if hasattr(BooksOrm, 'created_at') else asc(
                BooksOrm.id),
            BookOrderBy.CREATED_AT_DESC: desc(BooksOrm.created_at) if hasattr(BooksOrm, 'created_at') else desc(
                BooksOrm.id),
        }
        return order_map.get(order_by, asc(BooksOrm.id))
