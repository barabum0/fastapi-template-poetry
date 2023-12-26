# mypy: ignore_errors
import pytest
from fastapi.testclient import TestClient
from fastapi_app.routers import router as main_router
from fastapi_app.__main__ import app


@pytest.fixture()
def client() -> TestClient:
    app.include_router(main_router)
    client = TestClient(app)

    return client


def test_hello_world_1(client: TestClient):
    response = client.post("/api/hi", json={"name": "Roman"})
    assert response.status_code == 200
    assert response.json() == {"greeting": "Hello, Roman!"}


def test_hello_world_2(client: TestClient):
    response = client.post("/api/hi", json={"name": "Alex"})
    assert response.status_code == 200
    assert response.json() == {"greeting": "Hello, Alex!"}
