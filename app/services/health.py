"""Servicos para diagnosticos do sistema."""
from platform import node

from app.schemas.health import HealthResponse


def get_health_status() -> HealthResponse:
    """Retorna informacoes simples sobre o estado atual do servico."""
    return HealthResponse(server=node())
