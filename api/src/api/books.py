from fastapi import APIRouter, Path, Query, status
from sqlalchemy import select

from src.db.dependencies import AsyncSessionDep

from src.models.books import BookModel

from src.shemas.books import (
    NewBookSchema, BookSchema,
    SingleBookResponse,
    ListBooksResponse
)

from src.core.exceptions import (
        APIException_BadRequest,
        APIException_Forbidden,
        APIException_NotFound
)



router = APIRouter(prefix="/db/books", tags=["Books"])



# TODO ...
def serialize_book(book: BookModel) -> BookSchema:
    return BookSchema.model_validate(book)

def create_not_found_detail(book_id: int) -> str:
    return f"Book with id='{book_id}' not found."



@router.get("")
async def db_get_books(session: AsyncSessionDep):
    query = select(BookModel).order_by('id')
    result = await session.execute(query)
    books = result.scalars().all()
    #return {'books': books}
    #return api_success(data={'books': [serialize_book(b) for b in books]})
    return ListBooksResponse(
        data=[serialize_book(b) for b in books],
        total_count=1000
    )


@router.get("/{id}")
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
        #raise DbRecordNotFoundError(name="book", param=str(book_id))
        #raise BookPermissionDeniedError()
        raise APIException_NotFound(
            detail=create_not_found_detail(book_id)
        )

    #return {'data': book}
    #return api_success(data={'book': serialize_book(book)})
    return SingleBookResponse(data=serialize_book(book))


@router.post("", status_code=status.HTTP_201_CREATED)
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
    #return api_success(data={'book': serialize_book(new_book)})
    return SingleBookResponse(
        data=serialize_book(new_book),
        message="Book is successfully create"
    )



@router.put("")
async def db_update_books(
        session: AsyncSessionDep,
        data: BookSchema
):
    query = select(BookModel).where(BookModel.id == data.id)
    result = await session.execute(query)
    book = result.scalars().first()

    if book is None:
        raise APIException_NotFound(
            detail=create_not_found_detail(data.id)
        )

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(book, key, value)

    await session.commit()
    await session.refresh(book)

    #return {'data': book}
    #return api_success(data={'book': serialize_book(book)})
    return SingleBookResponse(data=serialize_book(book))


@router.patch("/{id}")
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
        raise APIException_NotFound(
            detail=create_not_found_detail(book_id)
        )

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
    #return api_success(data={'book': serialize_book(book)})
    return SingleBookResponse(data=serialize_book(book))


@router.delete("/{id}", status_code=status.HTTP_200_OK)
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
        raise APIException_NotFound(
            detail=create_not_found_detail(book_id)
        )

    await session.delete(book)
    await session.commit()

    #return None  # 204 No Content
    #return {'data': 'success'}
    #return api_success(data=None, message=f"Book with id: {book_id} was deleted")

    return SingleBookResponse(
        data=book,
        message=f"Book with id: {book_id} was deleted",
    )




