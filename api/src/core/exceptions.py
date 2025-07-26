import uuid
from typing import Any, Generic, TypeVar

from fastapi import FastAPI, HTTPException, status
from fastapi.exception_handlers import http_exception_handler
from pyexpat.errors import messages

# from src.core.db import Base
# ModelType = TypeVar('ModelType', bound=Base)

"""
class ModelNotFoundException(HTTPException, Generic[ModelType]):
    def __init__(
            self,
            model: type[ModelType],
            model_id: uuid.UUID | None = None,
            headers: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=(
                f"Unable to find the {model.__name__} with id {model_id}."
                if model_id is not None
                else f"{model.__name__} is not found"
            ),
            headers=headers,
        )
"""

class DbRecordNotFoundError(Exception):
    def __init__(self, name: str, param: str):
        message = f"{name} with id='{param}' not found!"
        super().__init__(message)
        self.message = message


class PermissionDeniedError(Exception):
    message = 'Permission Denied'


class BookPermissionDeniedError(PermissionDeniedError):
    message = 'Book Permission Denied'