"""Ponto de entrada do aplicativo FastAPI."""
from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import configure_logging
from app.api.routes.health import router as health_router

configure_logging()

app = FastAPI(title=settings.app_name, version=settings.app_version)

app.include_router(health_router, prefix="/health", tags=["health"])


@app.get("/", tags=["root"])
async def read_root() -> dict[str, str]:
    """Endpoint raiz simples para verificar se a aplicacao esta ativa."""
    return {"message": f"{settings.app_name} is running"}
