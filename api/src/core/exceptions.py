from typing import Any

#from starlette.exceptions import HTTPException as StarletteHTTPException
#from starlette import status

from fastapi import HTTPException, status

from src.config import settings


PROBLEM_URL_PATH = f"{settings.web_url()}/problems"

#class APIException(StarletteHTTPException):
class APIException(HTTPException):
    """
    Common API Exception class.
    """
    def __init__(
        self,
        status_code: int,
        type: str,
        title: str,
        detail: str,
        instance: str | None = None,
        headers: dict[str, str] | None = None,
        extra_data: dict[str, Any] | None = None, # Additional data, if needed
    ):
        super().__init__(status_code=status_code, detail=detail, headers=headers)
        self.type = type
        self.title = title
        self.instance = instance
        self.extra_data = extra_data or {} # Init empty dict, if extra_data is None


class APIException_NotFound(APIException):
    def __init__(
            self,
            detail: str = "Resource not found.",
            instance: str | None = None,
            headers: dict[str, str] | None = None,
            resource_type: str | None = None,
            resource_id: Any | None = None,
    ):
        # Preset values for 404
        base_detail = detail
        if resource_type and resource_id:
            base_detail = f"{resource_type} with ID '{resource_id}' not found."
            if detail != "Resource not found.":
                base_detail = detail

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            type=f"{PROBLEM_URL_PATH}/resource-not-found",
            title="Resource Not Found",
            detail=base_detail,
            instance=instance,
            headers=headers,
            extra_data={
                "resource_type": resource_type,
                "resource_id": str(resource_id)
            } if resource_type or resource_id else None
        )


class APIException_Forbidden(APIException):
    def __init__(
            self,
            detail: str = "You do not have permission to access this resource.",
            instance: str | None = None,
            headers: dict[str, str] | None = None,
            required_role: str | None = None,
    ):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            type=f"{PROBLEM_URL_PATH}/access-denied",
            title="Access Denied",
            detail=detail,
            instance=instance,
            headers=headers,
            extra_data={
                "required_role": required_role
            } if required_role else None
        )


class APIException_BadRequest(APIException):
    def __init__(
            self,
            detail: str = "Bad request.",
            instance: str | None = None,
            headers: dict[str, str] | None = None,
            invalid_fields: dict[str, str] | None = None,
    ):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            type=f"{PROBLEM_URL_PATH}/bad-request",
            title="Bad Request",
            detail=detail,
            instance=instance,
            headers=headers,
            extra_data={
                "invalid_fields": invalid_fields
            } if invalid_fields else None
        )