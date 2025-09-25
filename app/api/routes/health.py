"""Rotas relacionadas a diagnosticos da aplicacao."""
from fastapi import APIRouter

from app.schemas.health import HealthResponse
from app.services.health import get_health_status

router = APIRouter()


@router.get("/", response_model=HealthResponse)
async def check_health() -> HealthResponse:
    """Retorna status basico indicando se a API esta funcional."""
    return get_health_status()
