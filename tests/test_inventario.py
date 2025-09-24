from fastapi.testclient import TestClient
from main import app

client= TestClient(app)

def test_crear_movimiento(producto_creado, sede_creada):
    data = {
        "producto_id": producto_creado,
        "sede_id": sede_creada,
        "tipo_movimiento": "INGRESO",
        "cantidad": 14,
        "estado_producto": "DISPONIBLE",
        "usuario_creacion": "admin",
        "observaciones": "Guia de R. N 12312-5"
    }
    response = client.post("/inventario/", json=data)
    assert response.status_code == 201

def test_anular_movimiento(producto_creado, sede_creada):
    #Crear movimiento
    data = {
        "producto_id": producto_creado,
        "sede_id": sede_creada,
        "tipo_movimiento": "INGRESO",
        "cantidad": 20,
        "estado_producto": "DISPONIBLE",
        "usuario_creacion": "tester",
        "observaciones": "Guia de R. N 9686848-5"
    }
    response = client.post("/inventario/", json=data)
    id_movimiento = response.json().get("id")
    print(response.json())
    data= {"movimiento_id": id_movimiento, "usuario": "tester"}
    response = client.delete(f"/inventario/{id_movimiento}", params=data)
    assert response.status_code == 200

def test_anular_movimiento_inexistente():
    movimiento_id = 0
    data = {"usuario": "tester"}

    response = client.delete(f"/inventario/{movimiento_id}", params=data)

    assert response.status_code == 404
    body = response.json()
    assert "detail" in body
    assert body["detail"] == f"El movimiento seleccionado no existe"