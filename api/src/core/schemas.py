import time

from pydantic import BaseModel, Field
from typing import Generic, TypeVar, Optional, List, Dict, Any

# Определяем TypeVar для гибкости в data
T = TypeVar("T")

class BaseResponse(BaseModel, Generic[T]):
    """
    Базовая Pydantic модель для всех успешных ответов API.
    """
    status: str = Field(..., description="Статус ответа (например, 'success', 'error').")
    message: str | None = Field(None, description="Человекочитаемое сообщение об ответе.")
    data_type: str = Field(..., description="Тип данных, содержащихся в объекте data")
    data: T | None = Field(None, description="Полезные данные ответа.")
    # Дополнительные поля, если нужны
    #timestamp: float = Field(..., description="Время генерации ответа в Unix timestamp.")
    timestamp: float = Field(default_factory=time.time, description="Время генерации ответа в Unix timestamp.")

    class Config:
        # Добавляем настройку для Pydantic, чтобы позволить Generic type
        arbitrary_types_allowed = True

    def __init__(self, **data: Any):
        super().__init__(**data)

        #self.timestamp = time.time() # Автоматически заполняем timestamp