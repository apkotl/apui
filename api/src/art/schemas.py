from typing import Generic, TypeVar, Optional, List, Dict, Any
from pydantic import BaseModel, ConfigDict, Field

from src.core.schemas import BaseResponse


class NewBookSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    author: str


class BookSchema(NewBookSchema):
    id: int


# Специфичные модели ответов на основе BaseResponse
class SingleBookResponse(BaseResponse[BookSchema]):
    """
    Ответ для получения одной книги.
    """
    # Здесь не нужно добавлять поля, так как они уже определены в BaseResponse<Book>
    # Но можно переопределить defaults, если нужно
    message: str = "Book retrieved successfully."
    status: str = "success"
    data_type: str = "book"

    def __init__(self, data: BookSchema = None, message: str = message, **kwargs: Any):
        super().__init__(data=data, message=message, **kwargs)

class ListBooksResponse(BaseResponse[List[BookSchema]]):
    """
    Ответ для получения списка книг.
    """
    message: str = "Books list retrieved successfully."
    status: str = "success"
    data_type: str = "books"

    # Можно добавить метаданные для списков, например, пагинацию
    total_count: int = Field(0, description="Общее количество элементов.")
    page: int = Field(1, description="Текущая страница.")
    page_size: int = Field(10, description="Размер страницы.")

    # Переопределяем __init__ для удобства, чтобы передавать total_count и т.д.
    def __init__(self, data: List[BookSchema], total_count: int, page: int = 1, page_size: int = 10, **kwargs: Any):
        super().__init__(data=data, total_count=total_count, page=page, page_size=page_size, **kwargs)

