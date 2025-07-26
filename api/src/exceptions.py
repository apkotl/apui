from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.exception_handlers import http_exception_handler


from  src.core.exceptions import (
        DbRecordNotFoundError,
        PermissionDeniedError
)



async def db_record_not_found_error_handler(request: Request, error: DbRecordNotFoundError) -> Response:
    return await http_exception_handler(
        request, HTTPException(
            #status_code=status.HTTP_404_NOT_FOUND,
            status_code=status.HTTP_200_OK,
            detail=error.message
        )
    )

async def permission_denied_error_handler(request: Request, error: PermissionDeniedError) -> Response:
    return await http_exception_handler(
        request, HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=error.message
        )
    )



def apply_exception_handlers(app: FastAPI) -> FastAPI:
    """
    Apply global exception handlers
    :param app:
    :return:
    """
    app.exception_handler(DbRecordNotFoundError)(db_record_not_found_error_handler)
    app.exception_handler(PermissionDeniedError)(permission_denied_error_handler)
    #app.add_exception_handler(DbRecordNotFoundError, db_record_not_found_error_handler)
    #app.add_exception_handler(PermissionDeniedError, permission_denied_error_handler)
    return app