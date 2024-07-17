import random
import string

import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture(scope="session")
def client() -> TestClient:
    client = TestClient(app)

    return client


# uncomment to use async client
# @pytest.fixture(scope="session")
# async def client() -> AsyncGenerator[AsyncClient, None]:
#     """Получить тестовый клиент"""
#     async with AsyncClient(app=app, base_url="http://testserver") as client:
#         yield client



@pytest.mark.parametrize("name", ["".join(random.choices(string.ascii_letters, k=10)) for _ in range(10)])
def test_hello_world(client: TestClient, name: str) -> None:
    response = client.post("/api/hi", json={"name": name})
    assert response.status_code == 200
    assert response.json() == {"greeting": f"Hello, {name}!"}