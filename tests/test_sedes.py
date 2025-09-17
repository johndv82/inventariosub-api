from fastapi.testclient import TestClient
from main import app

client= TestClient(app)

def test_crear_sede():
    payload = {"nombre": "Sede Central Nuevo", "direccion": "Av. Principal 222"}
    response = client.post("/sedes/", json=payload)
    assert response.status_code == 201
    assert response.json()["nombre"] == payload["nombre"]


def test_crear_sede_duplicada():
    payload = {"nombre": "Sede Central", "direccion": "Av. Principal 123"}
    response = client.post("/sedes/", json=payload)
    assert response.status_code == 409


def test_listar_sedes():
    response = client.get("/sedes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
