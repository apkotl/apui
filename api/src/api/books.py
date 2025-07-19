from fastapi import APIRouter
from sqlalchemy import select

from src.models.books import BookModel
from src.shemas.books import NewBookSchema, BookSchema
from src.db.dependencies import AsyncSessionDep


router = APIRouter(tags=["Books"])


@router.get("/db/books")
async def db_get_books(session: AsyncSessionDep):
    query = select(BookModel)
    result = await session.execute(query)
    return {'data': result.scalars().all()}


@router.get("/db/book/{book_id}")
async def db_get_book(book_id: int, session: AsyncSessionDep):
    query = select(BookModel).where(BookModel.id == book_id)
    result = await session.execute(query)
    book = result.scalars().first()
    if book is None:
        return {'data': f"Book with id: {book_id} not found!"}
    return {'data': book}


@router.post("/db/book")
async def db_add_book(data: NewBookSchema, session: AsyncSessionDep):
    new_book = BookModel(
        title = data.title,
        author = data.author,
    )
    session.add(new_book)
    await session.commit()
    return {'data': 'success'}


@router.put("/db/book")
async def db_update_book(data: BookSchema, session: AsyncSessionDep):
    query = select(BookModel).where(BookModel.id == data.id)
    result = await session.execute(query)
    book = result.scalars().first()

    if book is None:
        return {'data': f"Book with id: {data.id} not found!"}

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(book, key, value)

    await session.commit()
    await session.refresh(book)

    return {'data': book}





