import logging
import logging.config
import os
from datetime import datetime


def setup_logging():
    """
    Настройка логирования для всего приложения
    """
    # Создаем директорию для логов если её нет
    os.makedirs("logs", exist_ok=True)

    # Конфигурация логирования
    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '{asctime} - {name} - {levelname} - {message}',
                'style': '{',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'detailed': {
                'format': '{asctime} - {name} - {levelname} - {pathname}:{lineno} - {message}',
                'style': '{',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'INFO',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'detailed',
                'level': 'DEBUG',
                'filename': f'logs/app_{datetime.now().strftime("%Y-%m-%d")}.log',
                'maxBytes': 10485760,  # 10MB
                'backupCount': 5,
                'encoding': 'utf8'
            },
            'error_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'detailed',
                'level': 'ERROR',
                'filename': f'logs/errors_{datetime.now().strftime("%Y-%m-%d")}.log',
                'maxBytes': 10485760,  # 10MB
                'backupCount': 5,
                'encoding': 'utf8'
            }
        },
        'loggers': {
            # Логгер для вашего приложения
            'app': {
                'level': 'DEBUG',
                'handlers': ['console', 'file', 'error_file'],
                'propagate': False
            },
            # Логгер для FastAPI
            'fastapi': {
                'level': 'INFO',
                'handlers': ['console', 'file'],
                'propagate': False
            },
            # Логгер для uvicorn
            'uvicorn': {
                'level': 'INFO',
                'handlers': ['console', 'file'],
                'propagate': False
            },
            'uvicorn.access': {
                'level': 'INFO',
                'handlers': ['console', 'file'],
                'propagate': False
            }
        },
        'root': {
            'level': 'INFO',
            'handlers': ['console', 'file']
        }
    }

    # Применяем конфигурацию
    logging.config.dictConfig(LOGGING_CONFIG)

    # Возвращаем основной логгер для приложения
    return logging.getLogger('app')


def get_logger(name: str = 'app') -> logging.Logger:
    """
    Получить логгер по имени
    """
    return logging.getLogger(name)