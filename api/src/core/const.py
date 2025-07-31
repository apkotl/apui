from enum import Enum


#HTTP: str = "http"
#HTTPS: str = "https"

PRODUCTION: str = "production"
DEVELOPMENT: str = "development"

class Protocol(str, Enum):
    HTTP = "http"
    HTTPS = "https"

    def __str__(self) -> str:
        return self.value

