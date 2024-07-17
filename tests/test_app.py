# mypy: ignore_errors
import random
import string

import pytest
from fastapi.testclient import TestClient
from src.routers import router as main_router
from src.__main__ import app


@pytest.fixture()
def client() -> TestClient:
    app.include_router(main_router)
    client = TestClient(app)

    return client


def test_hello_world(client: TestClient):
    for name in ["".join(random.choices(string.ascii_letters, k=10)) for _ in range(10)]:
        response = client.post("/api/hi", json={"name": name})
        assert response.status_code == 200
        assert response.json() == {"greeting": f"Hello, {name}!"}
