from fastapi.testclient import TestClient
import sys
from pyhere import here

sys.path.append(str(here().resolve()))
from main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200


def test_privacy():
    response = client.get("/privacy")
    assert response.status_code == 200


def test_rules():
    response = client.get("/rules")
    assert response.status_code == 200


def test_login():
    response = client.get("/login")
    assert response.status_code == 200


def test_workout_planner():
    response = client.get("/workout")
    assert response.status_code == 200


def test_signup():
    response = client.get("/signup")
    assert response.status_code == 200


def test_reset_password():
    response = client.get("/password_reset")
    assert response.status_code == 200


def test_404():
    response = client.get("/non-existent-page")
    assert response.status_code == 404
