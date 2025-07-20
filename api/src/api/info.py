from fastapi import APIRouter

from src.config.settings import settings

router = APIRouter(tags=["Info"])


@router.get("/")
def read_root():
    return {"data": "Hello API"}


@router.get("/version")
def read_item(q: str | None = None):
    return {"data": {"version": settings.APP_API_VERSION, "q": q}}


@router.get("/env")
def read_item():
    return {
        "data":
            {
                "ENVIRONMENT": settings.ENVIRONMENT,
                "IS_CONTAINER": settings.IS_CONTAINER,
                "ENV_FILE": settings.ENV_FILE,

                "APP_NAME": settings.APP_NAME,
                "APP_API_VERSION": settings.APP_API_VERSION,
                "APP_WEB_VERSION": settings.APP_WEB_VERSION,

                "WEB_HOST": settings.WEB_HOST,
                "WEB_PROTOCOL": settings.WEB_PROTOCOL,
                "WEB_PORT": settings.WEB_PORT,

                "API_HOST": settings.API_HOST,
                "API_PROTOCOL": settings.API_PROTOCOL,
                "API_PORT": settings.API_PORT,

                "DB_NAME": settings.DB_NAME,
                "DB_USER": settings.DB_USER,
                "DB_PASSWORD": settings.DB_PASSWORD,
                "DB_PORT": settings.DB_PORT,

                "all_settings": settings if settings.ENVIRONMENT == "development" else "only available in 'development' mode"
            }
    }


@router.get("/items/{item_count}")
def read_item(item_count: int, prefix: str | None = "item_#"):
    return {
        "data": {"version": settings.APP_API_VERSION, "item_count": item_count, "prefix": prefix},
        "items": [item for item in simple_item_generator(item_count, prefix)]
    }


def simple_item_generator(limit:int, prefix:str) -> dict[int: str]:
    current_number = 1
    while current_number <= limit:
        yield {
            'id': current_number,
            'name': f"{prefix}{current_number}"
        }
        current_number += 1
