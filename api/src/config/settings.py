import os

from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr
from pathlib import Path

import src.core.const as const

ENV = os.getenv("ENVIRONMENT", default="development")
BASE_DIR = str(Path(__file__).resolve().parents[3])
ENV_FILE_FULL_NAME = f"{BASE_DIR}{"" if BASE_DIR == "/" else os.sep}.env.{ENV}"

# singleton decorator
#def singleton(cls):
#    instances = {}
#
#    def get_instance(*args, **kwargs):
#        if cls not in instances:
#            instances[cls] = cls(*args, **kwargs)
#        return instances[cls]
#
#    return get_instance


#@singleton
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE_FULL_NAME,
        env_file_encoding='utf-8',
        extra="ignore"
    )

    # base_dir: str = Field(BASE_DIR)
    ENVIRONMENT: str = Field(ENV)

    IS_CONTAINER: bool = Field(False)
    ENV_FILE: str = Field(ENV_FILE_FULL_NAME)

    #app_name: str = Field(..., env="APP_NAME")

    APP_NAME: str = Field(...)
    APP_API_VERSION: str = Field(...)
    APP_WEB_VERSION: str = Field(...)

    WEB_HOST: str = Field(...)
    WEB_PROTOCOL: const.Protocol = Field(...)
    WEB_PORT: int = Field(...)
    FRONTEND_PORT: int = Field(...)

    API_HOST: str = Field(...)
    API_PROTOCOL: const.Protocol = Field(...)
    API_PORT: int = Field(...)
    #API_UVICORN_PORT: str = Field(...)

    DB_NAME: str = Field(...)
    DB_USER: str = Field(...)
    DB_PASSWORD: str = Field(...)
    DB_PORT: str = Field(...)
    REDIS_PORT: str = Field(...)
    #DB_ADMINER_PORT: str = Field(...)

    OAUTH_GOOGLE_CLIENT_ID: str = Field(...)
    OAUTH_GOOGLE_CLIENT_SECRET: str = Field(...)


    def web_url(self, path: str = ''):
        _port = ""
        if self.WEB_PROTOCOL == const.Protocol.HTTP and self.WEB_PORT == 80:
            pass
        elif self.WEB_PROTOCOL == const.Protocol.HTTPS and self.WEB_PORT == 443:
            pass
        else:
            _port = f":{self.WEB_PORT}"

        return f"{self.WEB_PROTOCOL}://{self.WEB_HOST}{_port}{path}"

    def frontend_url(self, path: str = ''):
        _port = ""
        if self.WEB_PROTOCOL == const.Protocol.HTTP and self.FRONTEND_PORT == 80:
            pass
        elif self.WEB_PROTOCOL == const.Protocol.HTTPS and self.FRONTEND_PORT == 443:
            pass
        else:
            _port = f":{self.FRONTEND_PORT}"

        return f"{self.WEB_PROTOCOL}://{self.WEB_HOST}{_port}{path}"


# Create a settings instance that will be used throughout the application
settings = Settings()


if __name__ == "__main__":
    print(f"__file__: {__file__}")
    print(f"--------")
    print(f"ENVIRONMENT: {settings.ENVIRONMENT}")
    print(f"IS_CONTAINER: {settings.IS_CONTAINER}")
    print(f"ENV_FILE: {settings.ENV_FILE}")
    print(f"--------")
    print(f"APP_NAME: {settings.APP_NAME}")
    print(f"APP_API_VERSION: {settings.APP_API_VERSION}")
    print(f"APP_WEB_VERSION: {settings.APP_WEB_VERSION}")
    print(f"--------")
    print(f"WEB_HOST: {settings.WEB_HOST}")
    print(f"WEB_PROTOCOL: {settings.WEB_PROTOCOL}")
    print(f"WEB_PORT: {settings.WEB_PORT}")
    print(f"FRONTEND_PORT: {settings.FRONTEND_PORT}")
    print(f"--------")
    print(f"API_HOST: {settings.API_HOST}")
    print(f"API_PROTOCOL: {settings.API_PROTOCOL}")
    print(f"API_PORT: {settings.API_PORT}")
    print(f"--------")
    print(f"DB_NAME: {settings.DB_NAME}")
    print(f"DB_USER: {settings.DB_USER}")
    print(f"DB_PASSWORD: {settings.DB_PASSWORD}")
    print(f"DB_PORT: {settings.DB_PORT}")
    print(f"REDIS_PORT: {settings.REDIS_PORT}")
    print(f"--------")
    print(f"OAUTH_GOOGLE_CLIENT_ID: {settings.OAUTH_GOOGLE_CLIENT_ID}")



