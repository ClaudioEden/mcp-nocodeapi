"""Configuracao padrao de logging para o projeto."""
import logging
from logging.config import dictConfig

from app.core.config import settings


def configure_logging() -> None:
    """Configura logging global apenas uma vez."""
    if logging.getLogger().handlers:
        return

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
                }
            },
            "handlers": {
                "default": {
                    "level": settings.log_level,
                    "formatter": "standard",
                    "class": "logging.StreamHandler",
                }
            },
            "root": {
                "level": settings.log_level,
                "handlers": ["default"],
            },
        }
    )


__all__ = ["configure_logging"]
