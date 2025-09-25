"""Configuracoes carregadas a partir de variaveis de ambiente."""
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Nocode API BR"
    app_version: str = "0.1.0"
    app_env: str = "development"
    app_debug: bool = True
    log_level: str = "INFO"
    database_url: str = "sqlite:///./app.db"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    """Retorna instancia unica de configuracao."""
    return Settings()


def reset_settings_cache() -> None:
    """Limpa cache de configuracoes, util em testes."""
    get_settings.cache_clear()


settings = get_settings()
