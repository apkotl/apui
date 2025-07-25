from typing import Any

from pydantic import BaseModel


class BaseResponse(BaseModel):
    success: bool
    message: str | None = None

class SuccessResponse(BaseResponse):
    data: Any

class ErrorDetail(BaseModel):
    code: int
    desc: str

class ErrorResponse(BaseResponse):
    error: ErrorDetail


def api_success(*, data: Any, message: str | None = None) -> SuccessResponse:
    return SuccessResponse(
        success=True,
        data=data,
        message=message
    )

def api_error(*, code: int = 400, desc: str, message: str | None = None) -> ErrorResponse:
    return ErrorResponse(
        success=False,
        error=ErrorDetail(code=code, desc=desc),
        message=message
    )