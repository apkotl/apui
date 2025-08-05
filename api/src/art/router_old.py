from fastapi import APIRouter, Request, Path, Query, HTTPException, status
from sqlalchemy import select

from src.databases.dependencies import AsyncSessionDep

from src.art.models import BookModel


from .schemas import (
    NewBookSchema, BookSchema,
    SingleBookResponse,
    ListBooksResponse
)

from src.logging import get_logger

from src.core.exceptions import (
        APIException_NotFound
)



router = APIRouter(prefix="/databases/books", tags=["Books"])
logger = get_logger('app.api.books')


# TODO ...
def serialize_book(book: BookModel) -> BookSchema:
    return BookSchema.model_validate(book)

def create_not_found_detail(book_id: int) -> str:
    return f"Book with id='{book_id}' not found."


@router.get("")
async def db_get_books(session: AsyncSessionDep, request: Request):
    request_id = getattr(request.state, 'request_id', 'unknown')
    logger.info(f"[{request_id}] Getting all books")

    try:
        query = select(BookModel).order_by('id')
        result = await session.execute(query)
        books = result.scalars().all()
        logger.info(f"[{request_id}] Successfully retrieved all books")
        return ListBooksResponse(
            data=[serialize_book(b) for b in books],
            total_count=1000
        )
    except HTTPException as e:
        raise
    except Exception as e:
        logger.error(f"[{request_id}] Error getting all books: {str(e)}", exc_info=True)
        raise


@router.get("/{id}")
async def db_get_books_by_id(
        session: AsyncSessionDep,
        request: Request,
        book_id: int = Path(..., alias='id')
):
    request_id = getattr(request.state, 'request_id', 'unknown')
    logger.info(f"[{request_id}] Getting book with ID: {book_id}")

    try:
        query = select(BookModel).where(BookModel.id == book_id)
        result = await session.execute(query)
        book = result.scalars().first()
        if book is None:
            logger.warning(f"[{request_id}] {create_not_found_detail(book_id)}")
            raise APIException_NotFound(
                detail=create_not_found_detail(book_id),
                resource_type="databases:books:id",
                resource_id=book_id
            )

        logger.info(f"[{request_id}] Successfully retrieved book: {book_id}")
        return SingleBookResponse(data=serialize_book(book))
    except HTTPException as e:
        raise
    except Exception as e:
        logger.error(f"[{request_id}] Error getting book {book_id}: {str(e)}", exc_info=True)
        raise


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




