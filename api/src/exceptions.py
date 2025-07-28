from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from starlette import status

from src.core.exceptions import APIException
from src.config import settings


PROBLEM_URL_PATH = f"{settings.web_url()}/problems"


async def api_exception_handler(request: Request, exc: APIException) -> JSONResponse:
    """
    Handler for APIException.
    :param request: fastAPI Request
    :param exc: Exception
    :return:
    """
    response_content = {
        "type": exc.type,
        "title": exc.title,
        "status": exc.status_code,
        "detail": exc.detail,
        "instance": exc.instance if exc.instance else str(request.url),
        **exc.extra_data # Adding any extra_data, if you need
    }

    return JSONResponse(
        status_code=exc.status_code,
        content=response_content,
        headers=exc.headers
    )

async def default_http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    """
    Default HTTP Exception Handler
    :param request:
    :param exc:
    :return:
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "type": f"{PROBLEM_URL_PATH}/generic-http-error/{exc.status_code}",
            "title": "An HTTP Error Occurred",
            "detail": exc.detail,
            "status": exc.status_code,
            "instance": str(request.url),
            #"note": "This is a fallback handler. Consider using APIException for structured errors."
        }
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    errors_list = jsonable_encoder(exc.errors())
    response_content = {
        "type": f"{PROBLEM_URL_PATH}/validation-error",
        "title": "Validation Error",
        "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
        "detail": "One or more input fields are invalid.",
        "instance": str(request.url),
        "validation_errors": errors_list
    }
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=response_content,
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