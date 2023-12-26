# mypy: ignore_errors
from fastapi.testclient import TestClient
from fastapi_app.routers import router as main_router
from fastapi_app.__main__ import app


def test_hello_world_1():
    app.include_router(main_router)
    client = TestClient(app)

    response = client.post("/api/hi", json={"name": "Roman"})
    assert response.status_code == 200
    assert response.json() == {"greeting": "Hello, Roman!"}


def test_hello_world_2():
    app.include_router(main_router)
    client = TestClient(app)

    response = client.post("/api/hi", json={"name": "Alex"})
    assert response.status_code == 200
    assert response.json() == {"greeting": "Hello, Alex!"}
