"""Definicoes de esquemas para endpoints de saude."""
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Representa o estado geral da aplicacao."""

    status: Literal["ok", "degraded", "fail"] = Field(default="ok", description="Descricao do estado atual")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    server: str = Field(default="unknown", description="Nome do host responsavel")
