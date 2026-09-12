import pytest
from fastapi.testclient import TestClient

from main import app, tickets

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_tickets() -> None:
    tickets.clear()


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_ticket() -> None:
    response = client.post(
        "/tickets",
        json={
            "title": "Cannot log in",
            "description": "Password reset does not work",
            "priority": "high",
        },
    )

    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["status"] == "open"


def test_get_all_tickets() -> None:
    client.post(
        "/tickets",
        json={
            "title": "Cannot log in",
            "description": "Password reset does not work",
        },
    )

    response = client.get("/tickets")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_ticket_by_id() -> None:
    client.post(
        "/tickets",
        json={
            "title": "Cannot log in",
            "description": "Password reset does not work",
        },
    )

    response = client.get("/tickets/1")

    assert response.status_code == 200
    assert response.json()["title"] == "Cannot log in"


def test_unknown_ticket_returns_404() -> None:
    response = client.get("/tickets/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Ticket not found"}


def test_invalid_ticket_returns_422() -> None:
    response = client.post(
        "/tickets",
        json={
            "title": "Hi",
            "description": "No",
            "priority": "urgent",
        },
    )

    assert response.status_code == 422
