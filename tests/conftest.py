import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def sede_creada():
    data = {
        "nombre": "Sede prueba test 123",
        "direccion": "Av. Central 123"
    }
    response = client.post("/sedes/", json=data)
    assert response.status_code in (200, 201, 409) 
    return response.json().get("id", 1) 


@pytest.fixture
def proveedor_creado():
    data = {
        "ruc": "98765432109",
        "razon_social": "Proveedor Test",
        "contacto": "Juan Perez",
        "telefono_contacto": "999999999",
        "estado": "ACTIVO",
        "usuario_creacion": "tester"
    }
    response = client.post("/proveedores/", json=data)
    assert response.status_code in (200, 201, 409)
    return data["ruc"]
