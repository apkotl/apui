from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from starlette import status

from src.dto.api_response import ResponseSchema, ResponseStatus, ErrorDetail
from src.core.exceptions import APIException
from src.config import settings


#PROBLEM_URL_PATH = f"{settings.web_url()}/problems"


async def api_exception_handler(request: Request, exc: APIException) -> JSONResponse:
    """
    Handler for APIException.
    """
    response_data = ResponseSchema(
        code=exc.status_code,
        status=ResponseStatus.ERROR,
        data=None,
        detail=exc.detail,
        errors=[ErrorDetail(type=exc.type, msg=exc.detail)],
        instance=exc.instance if exc.instance else str(request.url)
    #).model_dump(exclude_none=True)
    ).model_dump()

    if exc.extra_data:
        response_data.update(exc.extra_data)

    return JSONResponse(
        status_code=exc.status_code,
        content=response_data,
        headers=exc.headers
    )

async def default_http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    """
    Default HTTP Exception Handler
    """
    return JSONResponse(
        status_code=exc.status_code,
        content=ResponseSchema(
            code=exc.status_code,
            status=ResponseStatus.EXCEPTION,
            data=None,
            detail=exc.detail,
            errors=[ ErrorDetail(type="exception", msg=exc.detail) ],
            instance=str(request.url)
        ).model_dump(),
        headers=exc.headers
    )

async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
) -> JSONResponse:
    """
    Validation default exception
    """
    errors_list = jsonable_encoder(exc.errors())
    detail = "" if len(errors_list) == 0 else errors_list[0].get("msg")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=ResponseSchema(
            code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            status=ResponseStatus.VALIDATION_ERROR,
            data=None,
            detail=detail,
            errors=errors_list,
            instance=str(request.url)
        ).model_dump()
    )




def apply_exception_handlers(app: FastAPI) -> FastAPI:
    """
    Apply global exception handlers & custom exception handlers
    :param app: current FastAPI application
    :return: current FastAPI application
    """
    # Global API, HTTP & Validation Exceptions
    app.add_exception_handler(APIException, api_exception_handler)
    app.add_exception_handler(StarletteHTTPException, default_http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)

    # Custom Exceptions
    #app.exception_handler(DbRecordNotFoundError)(db_record_not_found_error_handler)
    #app.exception_handler(PermissionDeniedError)(permission_denied_error_handler)
    return app