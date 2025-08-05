from typing import Any

from src.core.schemas import ResponseSchema


class GoogleUriTestResponse(ResponseSchema[str]):

    message: str = "Google Uri Test Response."
    status: str = "success"
    data_type: str = "URL"

    def __init__(self, data: str = None, message: str = message, **kwargs: Any):
        super().__init__(data=data, message=message, **kwargs)




"""
class UserResponse(BaseResponse[User]):

    ###Ответ для получения данных пользователя.

    message: str = "User retrieved successfully."
    status: str = "success"

class MessageResponse(BaseResponse[Dict[str, Any]]):

    ###Общий ответ для операций, которые возвращают только сообщение (например, удаление).

    message: str
    status: str = "success"
    data: Optional[Dict[str, Any]] = None # Здесь data может быть пустым или содержать доп. инфо
"""
