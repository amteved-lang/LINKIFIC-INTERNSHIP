from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "running"

def test_health():
    response = client.get(
        "/health"
    )

    assert response.status_code == 200

    assert (
        response.json()["status"]
        == "healthy"
    )

def test_company_info():
    response = client.get(
        "/api/v1/company-info"
    )

    assert response.status_code == 200

    assert (
        response.json()["company"]
        == "HearMe"
    )

def test_company_search():
    response = client.post(
        "/api/v1/search",
        json={
            "query": "How is ASR performance measured?"
        }
    )

    assert response.status_code == 200

    assert "result" in response.json()

def test_invalid_search():
    response = client.post(
        "/api/v1/search",
        json={
            "query": ""
        }
    )

    assert response.status_code == 422

def test_unknown_search():
    response = client.post(
        "/api/v1/search",
        json={
            "query": "spaceship launch schedule"
        }
    )

    assert response.status_code == 404