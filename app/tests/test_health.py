"""Testes para verificar os endpoints de diagnostico."""
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint_returns_ok() -> None:
    response = client.get("/health/")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert "timestamp" in payload
    assert "server" in payload


def test_root_endpoint_returns_message() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "message" in response.json()
