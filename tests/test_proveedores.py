from fastapi.testclient import TestClient
from main import app

client= TestClient(app)

def test_crear_proveedor():
    payload = {
        "ruc": "98760987654",
        "razon_social": "Proveedor A",
        "contacto": "Carlos Lopez",
        "telefono_contacto": "987654321",
        "estado": "ACTIVO",
        "usuario_creacion": "admin"
    }
    response = client.post("/proveedores/", json=payload)
    assert response.status_code == 201
    assert response.json()["razon_social"] == payload["razon_social"]

def test_crear_proveedor_duplicada():
    payload = {
        "ruc": "55555555555",
        "razon_social": "Proveedor B",
        "contacto": "Carlos Arias",
        "telefono_contacto": "34563434",
        "estado": "ACTIVO",
        "usuario_creacion": "admin"
    }
    response = client.post("/proveedores/", json=payload)
    assert response.status_code == 201
    response = client.post("/proveedores/", json=payload)
    assert response.status_code == 409

def test_obtener_proveedor(proveedor_creado):
    response = client.get(f"/proveedores/{proveedor_creado}")
    assert response.status_code == 200

    body = response.json()
    assert body["ruc"] == proveedor_creado
    assert "razon_social" in body
    assert "estado" in body


def test_actualizar_proveedor(proveedor_creado):
    dataUpd = {
        "razon_social": "Proveedor A Modificado",
        "contacto": "Carlos L.",
        "telefono_contacto": "01010101",
        "estado": "ACTIVO"
    }

    response = client.put(f"/proveedores/{proveedor_creado}", json=dataUpd)
    assert response.status_code == 200
    body = response.json()
    assert body["razon_social"] == dataUpd["razon_social"]
    assert body["contacto"] == dataUpd["contacto"]


def test_listar_proveedores():
    response = client.get("/proveedores/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
