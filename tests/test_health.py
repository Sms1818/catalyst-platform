from fastapi.testclient import TestClient

from app.app import create_app

app = create_app()
client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
