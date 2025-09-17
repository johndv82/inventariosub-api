from fastapi.testclient import TestClient
from main import app

client= TestClient(app)

def test_crear_usuario(sede_creada):
    data = {
        "nombre": "Usuario Test 222 456",
        "email": "usuario@test.com",
        "is_admin": False,
        "sede_id": sede_creada
    }
    response = client.post("/usuarios/", json=data)
    assert response.status_code in (200, 201, 409)


def test_obtener_usuario(sede_creada):
    # 1. Crear usuario
    data = {
        "nombre": "Usuario Test Obtener 222 35 1222",
        "email": "usuario.obtener@test.com",
        "is_admin": False,
        "sede_id": sede_creada
    }
    response = client.post("/usuarios/", json=data)
    assert response.status_code in (200, 201)
    usuario_id = response.json()["id"]

    # 2. Obtener usuario
    response = client.get(f"/usuarios/{usuario_id}")
    assert response.status_code == 200

    body = response.json()
    assert body["id"] == usuario_id
    assert body["email"] == data["email"]

def test_obtener_usuario_inexistente():
    response = client.get("/usuarios/9999")
    assert response.status_code == 404


def test_actualizar_usuario(sede_creada):
    # 1. Crear usuario inicial
    data = {
        "nombre": "Juan Lopez 11212",
        "email": "juan@test.com",
        "is_admin": False,
        "sede_id": sede_creada
    }
    response = client.post("/usuarios/", json=data)
    assert response.status_code in (200, 201)
    usuario_id = response.json()["id"]

    payload = {
        "nombre": "Juan Lopez Actualizado",
        "email": "juan@example.com"
    }

    # 2. Actualizar usuario
    response = client.put(f"/usuarios/{usuario_id}", json=payload)
    assert response.status_code == 200
    body = response.json()

    assert body["nombre"] == payload["nombre"]
    assert body["email"] == payload["email"]


def test_eliminar_usuario(sede_creada):
    # 1. Crear usuario
    data = {
        "nombre": "Usuario Eliminar 1122333",
        "email": "usuario.eliminar@test.com",
        "is_admin": False,
        "sede_id": sede_creada
    }
    response = client.post("/usuarios/", json=data)
    assert response.status_code in (200, 201)
    usuario_id = response.json()["id"]

    # 2. Eliminar usuario
    response = client.delete(f"/usuarios/{usuario_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Usuario eliminado correctamente"

    # 3. Verificar
    response = client.get(f"/usuarios/{usuario_id}")
    assert response.status_code == 404
