from typing import Optional

from fastapi import APIRouter, Request, Path, Query, HTTPException, status
from fastapi.params import Depends


from src.core.schemas import ResponseSchema, ListResponse
from src.logging import get_logger
from src.core.exceptions import (
        APIException,
        APIException_NotFound
)

from .schemas import (
    AuthorCreate, Author, AuthorWithBooks, AuthorOrderBy, AuthorListQueryParams,
    BookGenreCreate, BookGenre, BookGenreOrderBy, BookGenreListQueryParams,
    BookCreate, Book, BookOrderBy, BookListQueryParams, BookWithObjects,
)
from .services.i_author import IAuthorService
from .services.i_book_genre import IBookGenreService
from .services.i_book import IBookService
from .dependencies import (
        get_author_service,
        get_book_genre_service,
        get_book_service
)

router = APIRouter(prefix="/art", tags=["art"])
logger = get_logger('api.art')


def create_not_found_detail(item_name: str, item_id: int) -> str:
    return f"{item_name.title()} with id='{item_id}' not found."


###################################################
# Authors (begin)
###################################################
@router.get("/authors/{id}")
async def get_author(
        request: Request,
        author_id: int = Path(..., alias='id'),
        author_service: IAuthorService = Depends(get_author_service)
) -> ResponseSchema[Author]:
    request_id = getattr(request.state, 'request_id', 'unknown')
    logger.info(f"[{request_id}] Getting author with ID: {author_id}")

    try:
        author = await author_service.get_author_by_id(author_id)
        if author is None:
            not_found_detail = create_not_found_detail("author", author_id)
            logger.warning(f"[{request_id}] {not_found_detail}")
            raise APIException_NotFound(
                detail=not_found_detail,
                type="database:author:id",
                input=str(author_id)
            )

        logger.info(f"[{request_id}] Successfully retrieved author: {author_id}")
        return ResponseSchema[Author](
            detail=f"Get author with id: {author_id}",
            data=author
        )

    except HTTPException as e:
        raise
    except Exception as e:
        logger.error(f"[{request_id}] Error getting author {author_id}: {str(e)}", exc_info=True)
        raise APIException(
            detail=str(e)
        )


@router.get("/authors_with_books/{id}")
async def get_author_with_books(
        request: Request,
        author_id: int = Path(..., alias='id'),
        author_service: IAuthorService = Depends(get_author_service)
) -> ResponseSchema[AuthorWithBooks]:
    request_id = getattr(request.state, 'request_id', 'unknown')
    logger.info(f"[{request_id}] Getting author (with books) with ID: {author_id}")

    try:
        author = await author_service.get_author_by_id_with_books(author_id)
        if author is None:
            not_found_detail = create_not_found_detail("author", author_id)
            logger.warning(f"[{request_id}] {not_found_detail}")
            raise APIException_NotFound(
                detail=not_found_detail,
                type="database:author:id",
                input=str(author_id)
            )

        logger.info(f"[{request_id}] Successfully retrieved author: {author_id}")
        return ResponseSchema[AuthorWithBooks](
            detail=f"Get author with id: {author_id}",
            data=author
        )

    except HTTPException as e:
        raise
    except Exception as e:
        logger.error(f"[{request_id}] Error getting author {author_id}: {str(e)}", exc_info=True)
        raise APIException(
            detail=str(e)
        )
###################################################
# Authors (end)
###################################################



###################################################
# Book  (begin)
###################################################
@router.get("/books/{id}")
async def get_book(
        request: Request,
        book_id: int = Path(..., alias='id'),
        book_service: IBookService = Depends(get_book_service)
) -> ResponseSchema[BookWithObjects]:
    request_id = getattr(request.state, 'request_id', 'unknown')
    logger.info(f"[{request_id}] Getting book with ID: {book_id}")

    try:
        book = await book_service.get_book_by_id(book_id)
        if book is None:
            not_found_detail = create_not_found_detail("book", book_id)
            logger.warning(f"[{request_id}] {not_found_detail}")
            raise APIException_NotFound(
                detail=not_found_detail,
                type="database:book:id",
                input=str(book_id)
            )

        logger.info(f"[{request_id}] Successfully retrieved book: {book_id}")
        return ResponseSchema[BookWithObjects](
            detail=f"Get book with id: {book_id}",
            data=book
        )

    except HTTPException as e:
        raise
    except Exception as e:
        logger.error(f"[{request_id}] Error getting book {book_id}: {str(e)}", exc_info=True)
        raise APIException(
            detail=str(e)
        )
###################################################
# Book  (end)
###################################################


###################################################
# Book Genres (begin)
###################################################
@router.get("/book_genres")
async def get_book_genres(
        request: Request,
        offset: int = Query(default=0, ge=0, description="Смещение для пагинации"),
        limit: int = Query(default=10, ge=1, le=100, description="Количество записей (максимум 100)"),
        order_by: BookGenreOrderBy = Query(default=BookGenreOrderBy.ID_ASC, description="Поле и направление сортировки"),
        search: Optional[str] = Query(default=None, min_length=1, max_length=255, description="Поиск по названию или автору"),
        book_genre_service: IBookGenreService = Depends(get_book_genre_service)
):
    """
        Получить список жанров книг с пагинацией, сортировкой и поиском

        - **offset**: Смещение для пагинации (по умолчанию 0)
        - **limit**: Количество записей на странице (по умолчанию 10, максимум 100)
        - **order_by**: Поле и направление сортировки
        - **search**: Поиск по названию (опционально)
    """
    request_id = getattr(request.state, 'request_id', 'unknown')
    logger.info(f"[{request_id}] Getting books list with offset={offset}, limit={limit}, order_by={order_by}, search={search}")

    try:
        # Создаем параметры запроса
        params = BookGenreListQueryParams(
            offset=offset,
            limit=limit,
            order_by=order_by,
            search=search
        )

        # Получаем список жанров книг
        result = await book_genre_service.get_book_genres_list(params)

        logger.info(
            f"[{request_id}] Successfully retrieved {len(result.items)} book genres (total: {result.pagination['total']})")

        return ResponseSchema[ListResponse[BookGenre]](
            detail=f"Successfully retrieved {len(result.items)} book genres (total: {result.pagination['total']})",
            data=result
        )

    except HTTPException as e:
        raise
    except Exception as e:
        logger.error(f"[{request_id}] Error getting book genres: {str(e)}", exc_info=True)
        raise APIException(
            detail=str(e)
        )


@router.get("/book_genres/{id}")
async def get_book_genre(
        request: Request,
        book_genre_id: int = Path(..., alias='id'),
        book_genre_service: IBookGenreService = Depends(get_book_genre_service)
):
    request_id = getattr(request.state, 'request_id', 'unknown')
    logger.info(f"[{request_id}] Getting book genre with ID: {book_genre_id}")

    try:
        book_genre = await book_genre_service.get_book_genre_by_id(book_genre_id)
        if book_genre is None:
            not_found_detail = create_not_found_detail("book genre", book_genre_id)
            logger.warning(f"[{request_id}] {not_found_detail}")
            raise APIException_NotFound(
                detail=not_found_detail,
                type="database:book_genres:id",
                input=str(book_genre_id)
            )

        logger.info(f"[{request_id}] Successfully retrieved book genre: {book_genre_id}")
        return ResponseSchema[BookGenre](
            detail=f"Get book genre with id: {book_genre_id}",
            data=book_genre
        )

    except HTTPException as e:
        raise
    except Exception as e:
        logger.error(f"[{request_id}] Error getting book genre {book_genre_id}: {str(e)}", exc_info=True)
        raise APIException(
            detail=str(e)
        )


@router.post("/book_genres", status_code=status.HTTP_201_CREATED)
async def create_book_genre(
    request: Request,
    data: BookGenreCreate,
    book_genre_service: IBookGenreService = Depends(get_book_genre_service)
):
    request_id = getattr(request.state, 'request_id', 'unknown')
    logger.info(f"[{request_id}] Create new book genre")

    try:
        book_genre = await book_genre_service.create_book_genre(data)
        return ResponseSchema[BookGenre](
            code=status.HTTP_201_CREATED,
            message="Book genre is successfully created",
            data=book_genre
        )
    except HTTPException as e:
        raise
    except Exception as e:
        logger.error(f"Error creating book genre: {str(e)}", exc_info=True)
        raise APIException(
            detail=str(e)
        )


@router.put("/book_genres/{id}")
async def update_book_genre(
        request: Request,
        book_genre_id: int = Path(..., alias='id'),
        book_genre_service: IBookGenreService = Depends(get_book_genre_service),
        data: BookGenreCreate = None,
):
    request_id = getattr(request.state, 'request_id', 'unknown')
    logger.info(f"[{request_id}] Updating book genre with ID: {book_genre_id}")

    try:
        book_genre = await book_genre_service.update_book_genre(book_genre_id, data)
        if book_genre is None:
            not_found_detail = create_not_found_detail("book genre", book_genre_id)
            logger.warning(f"[{request_id}] {not_found_detail}")
            raise APIException_NotFound(
                detail=not_found_detail,
                type="database:book_genres:id",
                input=str(book_genre_id)
            )

        return ResponseSchema[BookGenre](
            detail=f"Book genre with id: {book_genre_id} was updated",
            data=book_genre
        )
    except HTTPException as e:
        raise
    except Exception as e:
        logger.error(f"Error updating book genre {book_genre_id}: {str(e)}", exc_info=True)
        raise APIException(
            detail=str(e)
        )


@router.delete("/book_genres/{id}")
async def delete_book_genre(
    request: Request,
    book_genre_id: int = Path(..., alias='id'),
    book_genre_service: IBookGenreService = Depends(get_book_genre_service)
):
    request_id = getattr(request.state, 'request_id', 'unknown')
    logger.info(f"[{request_id}] Deleting book genre with ID: {book_genre_id}")

    try:
        success = await book_genre_service.delete_book_genre(book_genre_id)
        if not success:
            not_found_detail = create_not_found_detail("book genre", book_genre_id)
            logger.warning(f"[{request_id}] {not_found_detail}")
            raise APIException_NotFound(
                detail=not_found_detail,
                type="database:book_genres:id",
                input=str(book_genre_id)
            )

        return ResponseSchema[str](
            detail=f"Book genre with id: {book_genre_id} was deleted",
            data=f"Book genre with id: {book_genre_id} was deleted",
        )
    except HTTPException as e:
        raise
    except Exception as e:
        logger.error(f"Error deleting book genre {book_genre_id}: {str(e)}", exc_info=True)
        raise APIException(
            detail=str(e)
        )
###################################################
# Book Genres (end)
###################################################


