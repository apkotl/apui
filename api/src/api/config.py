from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parents[3])


# singleton decorator
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        #env_file="../../../.env",
        env_file=f"{BASE_DIR}/.env",
        env_file_encoding='utf-8',
        extra="ignore"
    )

    #app_name: str = Field(..., env="APP_NAME")
    APP_ENVIRONMENT: str = Field(...)
    DOCKER_CONTAINER_MODE: bool = Field(False)

    APP_NAME: str = Field(...)
    APP_VERSION: str = Field(...)
    APP_API_VERSION: str = Field(...)
    APP_WEB_VERSION: str = Field(...)

    NGINX_WEB_SERVER_NAME: str = Field()
    NGINX_API_SERVER_NAME: str = Field()
    NGINX_WEB_HTTP_PROTOCOL: str = Field()
    NGINX_API_HTTP_PROTOCOL: str = Field()
    NGINX_WEB_PORT: str = Field()
    NGINX_API_PORT: str = Field()

    POSTGRES_DB: str = Field()
    POSTGRES_USER: str = Field()
    POSTGRES_PASSWORD: str = Field()
    POSTGRES_PORT: str = Field()

    base_dir: str = Field(BASE_DIR)


# Создаем экземпляр настроек, который будет использоваться во всем приложении
settings = Settings()

if __name__ == "__main__":
    print(f"base_dir: {settings.base_dir}")
    print(f"APP_ENVIRONMENT: {settings.APP_ENVIRONMENT}")
    print(f"DOCKER_CONTAINER_MODE: {settings.DOCKER_CONTAINER_MODE}")
    print(f"APP_NAME: {settings.APP_NAME}")
    print(f"APP_VERSION: {settings.APP_VERSION}")
    print(f"APP_API_VERSION: {settings.APP_API_VERSION}")
    print(f"APP_WEB_VERSION: {settings.APP_WEB_VERSION}")
    #print(f"NGINX_WEB_SERVER_NAME: {settings.NGINX_WEB_SERVER_NAME}")
