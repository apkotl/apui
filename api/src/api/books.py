from fastapi import APIRouter, Path, Query, HTTPException
from sqlalchemy import select

from src.core.exceptions import DbRecordNotFoundError, BookPermissionDeniedError
from src.models.books import BookModel
from src.shemas.books import NewBookSchema, BookSchema
from src.db.dependencies import AsyncSessionDep
from src.shemas.api_response import api_success, api_error

router = APIRouter(tags=["Books"])

# TODO ...
def serialize_book(book: BookModel) -> BookSchema:
    return BookSchema.model_validate(book)




@router.get("/db/books")
async def db_get_books(session: AsyncSessionDep):
    query = select(BookModel).order_by('id')
    result = await session.execute(query)
    books = result.scalars().all()
    #return {'books': books}
    return api_success(data={'books': [serialize_book(b) for b in books]})


@router.get("/db/books/{id}")
async def db_get_books_by_id(
        session: AsyncSessionDep,
        book_id: int = Path(..., alias='id')
):
    query = select(BookModel).where(BookModel.id == book_id)
    result = await session.execute(query)
    book = result.scalars().first()
    if book is None:
        #return {'data': f"Book with id: {book_id} not found!"}
        #raise HTTPException(
        #    status_code=200,
        #    detail=f"Book with id={book_id} not found"
        #)
        # return api_error(code=404, desc=f"Book with id: {book_id} not found.")
        raise DbRecordNotFoundError(name="book", param=str(book_id))
        #raise BookPermissionDeniedError()

    #return {'data': book}
    return api_success(data={'book': serialize_book(book)})


@router.post("/db/books")
async def db_add_books(
        session: AsyncSessionDep,
        data: NewBookSchema
):
    new_book = BookModel(
        title = data.title,
        author = data.author,
    )
    session.add(new_book)
    await session.flush()
    await session.commit()
    await session.refresh(new_book)
    #return {'data': 'success', 'book': new_book}
    return api_success(data={'book': serialize_book(new_book)})



@router.put("/db/books")
async def db_update_books(
        session: AsyncSessionDep,
        data: BookSchema
):
    query = select(BookModel).where(BookModel.id == data.id)
    result = await session.execute(query)
    book = result.scalars().first()

    if book is None:
        #return {'data': f"Book with id: {data.id} not found!"}
        return api_error(code=404, desc=f"Book with id: {data.id} not found.")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(book, key, value)

    await session.commit()
    await session.refresh(book)

    #return {'data': book}
    return api_success(data={'book': serialize_book(book)})


@router.patch("/db/books/{id}")
async def db_update_book(
    session: AsyncSessionDep,
    book_id: int = Path(..., alias="id"),
    title: str | None = Query(None),
    author: str | None = Query(None),
):
    result = await session.execute(
        select(BookModel).where(BookModel.id == book_id)
    )
    book = result.scalar_one_or_none()

    if book is None:
        #raise HTTPException(
        #    status_code=404,
        #    detail=f"Book with id={book_id} not found"
        #)
        #return {'data': f"Book with id: {book_id} not found!"}
        return api_error(code=404, desc=f"Book with id: {book_id} not found.")

    updated = False
    if title is not None:
        book.title = title
        updated = True
    if author is not None:
        book.author = author
        updated = True

    if updated:
        #session.add(book)
        await session.commit()
        await session.refresh(book)

    #return {"data": "ok", "book": book}
    return api_success(data={'book': serialize_book(book)})


#@router.delete("/db/book/{id}", status_code=HTTP_204_NO_CONTENT)
@router.delete("/db/books/{id}")
async def db_delete_books(
        session: AsyncSessionDep,
        book_id: int = Path(..., alias='id')
):
    result = await session.execute(
        select(BookModel).where(BookModel.id == book_id)
    )
    book = result.scalar_one_or_none()

    #if book is None:
    #    raise HTTPException(
    #        status_code=status.HTTP_404_NOT_FOUND,
    #        detail=f"Book with id={book_id} not found"
    #    )
    if book is None:
        #return {'data': f"Book with id: {book_id} not found!"}
        return api_error(code=404, desc=f"Book with id: {book_id} not found.")

    await session.delete(book)
    await session.commit()

    #return None  # 204 No Content
    #return {'data': 'success'}
    return api_success(data=None, message=f"Book with id: {book_id} was deleted")




