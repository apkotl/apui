import time
import uuid
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from src.config.logging import get_logger

logger = get_logger('app.requests')


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware для логирования HTTP запросов и ответов
    """

    async def dispatch(self, request: Request, call_next):
        # Генерируем уникальный ID для запроса
        request_id = str(uuid.uuid4())[:8]

        # Время начала обработки
        start_time = time.time()

        # Логируем входящий запрос
        logger.info(
            f"[{request_id}] Incoming request: {request.method} {request.url} "
            f"from {request.client.host if request.client else 'unknown'}"
        )

        # Логируем заголовки (только важные)
        important_headers = {
            'user-agent': request.headers.get('user-agent'),
            'content-type': request.headers.get('content-type'),
            'authorization': 'Bearer ***' if request.headers.get('authorization') else None,
            'x-forwarded-for': request.headers.get('x-forwarded-for'),
        }
        filtered_headers = {k: v for k, v in important_headers.items() if v is not None}

        if filtered_headers:
            logger.debug(f"[{request_id}] Headers: {filtered_headers}")

        # Добавляем request_id в состояние запроса для использования в других частях приложения
        request.state.request_id = request_id

        try:
            # Обрабатываем запрос
            response: Response = await call_next(request)

            # Время обработки
            process_time = time.time() - start_time

            # Логируем ответ
            if response.status_code >= 400:
                logger.warning(
                    f"[{request_id}] Response: {response.status_code} "
                    f"({process_time:.3f}s)"
                )
            else:
                logger.info(
                    f"[{request_id}] Response: {response.status_code} "
                    f"({process_time:.3f}s)"
                )

            # Добавляем заголовок с request_id в ответ
            response.headers["X-Request-ID"] = request_id

            return response

        except Exception as e:
            # Время обработки при ошибке
            process_time = time.time() - start_time

            # Логируем ошибку
            logger.error(
                f"[{request_id}] Request failed: {str(e)} "
                f"({process_time:.3f}s)",
                exc_info=True
            )

            # Пробрасываем исключение дальше
            raise