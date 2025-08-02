from fastapi import APIRouter, status, Response, Request
from pydantic import BaseModel, Field


from src.core.exceptions import APIException, APIException_NotFound
from src.dto.api_response import ResponseSchema, ResponseStatus
from src.config.settings import settings

router = APIRouter(tags=["Info"])


@router.get("/")
def read_root(request: Request):# -> ResponseSchema[str]:
    return ResponseSchema[str](
        data="Hello API!",
        instance=str(request.url)
    )


@router.get("/env")
def read_item():# -> ResponseSchema[dict[str, str | int]]:
    return ResponseSchema[dict[str, str | int]](
        detail = "Environment variables.",
        data = {
            "ENVIRONMENT": settings.ENVIRONMENT,
            "IS_CONTAINER": settings.IS_CONTAINER,
            "ENV_FILE": settings.ENV_FILE,

            "APP_NAME": settings.APP_NAME,
            "APP_API_VERSION": settings.APP_API_VERSION,
            "APP_WEB_VERSION": settings.APP_WEB_VERSION,

            "WEB_HOST": settings.WEB_HOST,
            "WEB_PROTOCOL": settings.WEB_PROTOCOL,
            "WEB_PORT": settings.WEB_PORT,
            "FRONTEND_PORT": settings.FRONTEND_PORT,

            "API_HOST": settings.API_HOST,
            "API_PROTOCOL": settings.API_PROTOCOL,
            "API_PORT": settings.API_PORT,

            "DB_NAME": settings.DB_NAME,
            "DB_USER": settings.DB_USER,
            "DB_PASSWORD": settings.DB_PASSWORD,
            "DB_PORT": settings.DB_PORT,

            "OAUTH_GOOGLE_CLIENT_ID": settings.OAUTH_GOOGLE_CLIENT_ID,

            "web_url": settings.web_url(),
            "frontend_url": settings.frontend_url(),

            #"all_settings": str(settings) if settings.ENVIRONMENT == "development" else "only available in 'development' mode"
        }
    )



class ItemsSchema(BaseModel):
    item_count: int = Field(...)
    prefix: str = Field(...)
    items: list[dict[str, str | int]] = Field(default_factory=list)


@router.get("/items/ten")
def read_item_10(prefix: str | None = "i_#") -> ResponseSchema[ItemsSchema]:
    return read_item(item_count=10, prefix=prefix)


@router.get("/items/{item_count}")
def read_item(item_count: int, prefix: str | None = "item_#") -> ResponseSchema[ItemsSchema]:
    items = ResponseSchema[ItemsSchema](
        detail="test items",
        data = ItemsSchema(
            item_count=item_count,
            prefix=prefix,
            items=[item for item in simple_item_generator(item_count, prefix)]
        )
    )
    return  items


def simple_item_generator(limit:int, prefix:str) -> dict[int: str]:
    current_number = 1
    while current_number <= limit:
        yield {
            'id': current_number,
            'name': f"{prefix}{current_number}"
        }
        current_number += 1
