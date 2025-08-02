import time
from enum import Enum

from pydantic import BaseModel, Field, ConfigDict
from typing import Generic, TypeVar, Optional, List, Dict, Any, Literal

from src.config import settings


# Defining TypeVar for flexibility in data
T = TypeVar("T")


class ResponseStatus(str, Enum):
    OK = "ok"
    ERROR = "error"
    VALIDATION_ERROR = "validation_error"
    EXCEPTION = "exception"

    def __str__(self) -> str:
        return self.value


class ErrorDetail(BaseModel):
    """Модель для детальной информации об ошибке"""
    type: str = Field(description="Type of error")
    loc: list[str | int] = Field(default_factory=list, description="Location path where error occurred")
    msg: str = Field(description="Error message")
    input: Any = Field(default=None, description="Input value that caused the error")


class ResponseSchema(BaseModel, Generic[T]):
    model_config = ConfigDict(extra="allow")

    version: Literal[settings.APP_API_VERSION] = Field(default=settings.APP_API_VERSION)
    code: int = Field(default=200, description="status code")
    status: ResponseStatus = Field(default=ResponseStatus.OK)

    detail: str = Field(default="")
    data: T | None = Field(default=None, description="response data")

    errors: list[ErrorDetail] = Field(default_factory=list)

    instance: str | None = Field(default=None)
    timestamp: int = Field(default_factory=lambda: int(time.time()))

    #extra_data: Any | None = Field(default=None)


