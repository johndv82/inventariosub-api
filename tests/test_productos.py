from fastapi.testclient import TestClient
from main import app

client= TestClient(app)

def test_crear_producto(proveedor_creado):
    data = {
        "codigo": "PRD2001 345",
        "descripcion": "Producto de prueba",
        "unidad_medida": "GR",
        "peso_en_kilos": 10.5,
        "estado": "ACTIVO",
        "usuario_creacion": "tester",
        "proveedor_ruc": proveedor_creado
    }
    response = client.post("/productos/", json=data)
    assert response.status_code == 201
    
def test_crear_producto_proveedor_inexistente():
    data = {
        "codigo": "PRD-4044534",
        "descripcion": "Producto inválido",
        "unidad_medida": "GR",
        "peso_en_kilos": 5,
        "estado": "ACTIVO",
        "usuario_creacion": "tester",
        "proveedor_ruc": "00000000000"
    }
    response = client.post("/productos/", json=data)
    assert response.status_code == 404


def test_obtener_producto(proveedor_creado):
    # 1. Crear producto
    data = {
        "codigo": "PRD-GET",
        "descripcion": "Producto para obtener",
        "unidad_medida": "GR",
        "peso_en_kilos": 2.5,
        "estado": "ACTIVO",
        "usuario_creacion": "tester",
        "proveedor_ruc": proveedor_creado
    }
    response = client.post("/productos/", json=data)
    assert response.status_code == 201

    producto_id = response.json().get("id")

    # 2. Obtener producto
    response = client.get(f"/productos/{producto_id}")
    assert response.status_code == 200
    body = response.json()
    assert body["codigo"] == "PRD-GET"
    assert body["descripcion"] == "Producto para obtener"


def test_actualizar_producto(proveedor_creado):
    # 1. Crear producto
    data = {
        "codigo": "PRD-UPD",
        "descripcion": "Harina sin refinar",
        "unidad_medida": "KL",
        "peso_en_kilos": 1,
        "estado": "ACTIVO",
        "usuario_creacion": "tester",
        "proveedor_ruc": proveedor_creado
    }
    response = client.post("/productos/", json=data)
    assert response.status_code == 201
    producto_id = response.json().get("id") 

    # 2. Actualizar producto
    payload = {"descripcion": "Harina refinada 1kg", "unidad_medida": "KL"}
    response = client.put(f"/productos/{producto_id}", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["descripcion"] == payload["descripcion"]
    assert body["unidad_medida"] == payload["unidad_medida"]


def test_listar_productos():
    response = client.get("/productos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
