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
                "base_dir": f"{settings.base_dir}",
                "APP_ENVIRONMENT": settings.APP_ENVIRONMENT,
                "DOCKER_CONTAINER_MODE": settings.DOCKER_CONTAINER_MODE,

                "APP_NAME": settings.APP_NAME,
                "APP_VERSION": settings.APP_VERSION,
                "APP_API_VERSION": settings.APP_API_VERSION,
                "APP_WEB_VERSION": settings.APP_WEB_VERSION,

                "NGINX_API_SERVER_NAME": settings.NGINX_API_SERVER_NAME,
                "NGINX_API_HTTP_PROTOCOL": settings.NGINX_API_HTTP_PROTOCOL,
                "NGINX_API_PORT": settings.NGINX_API_PORT,

                "NGINX_WEB_SERVER_NAME": settings.NGINX_WEB_SERVER_NAME,
                "NGINX_WEB_HTTP_PROTOCOL": settings.NGINX_WEB_HTTP_PROTOCOL,
                "NGINX_WEB_PORT": settings.NGINX_WEB_PORT,

                "all_settings": settings if settings.APP_ENVIRONMENT == "dev" else "only available for 'dev' of the environment"
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
