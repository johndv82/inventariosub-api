import uuid
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from core.database import Base, get_db
from sqlalchemy.pool import StaticPool

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Crear tablas en la BD Test
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def sede_creada(client):
    data = {
        "nombre": f"Sede Prueba {uuid.uuid4().hex[:6]}",
        "direccion": "Av. Central 123"
    }
    response = client.post("/sedes/", json=data)
    assert response.status_code == 201
    return response.json().get("id") 


@pytest.fixture
def proveedor_creado(client):
    ruc = str(uuid.uuid4().int)[:11] 
    data = {
        "ruc": ruc,
        "razon_social": "Proveedor Test",
        "contacto": "Juan Perez",
        "telefono_contacto": "999999999",
        "estado": "ACTIVO",
        "usuario_creacion": "tester"
    }
    response = client.post("/proveedores/", json=data)
    assert response.status_code == 201
    return data["ruc"]

@pytest.fixture
def producto_creado(client, proveedor_creado):
    codigo = str(uuid.uuid4().int)[:18] 
    data = {
        "codigo": codigo,
        "descripcion": "Chocolate Fleishman 1.5kl",
        "unidad_medida": "KL",
        "peso_en_kilos": 1.5,
        "proveedor_ruc": proveedor_creado,
        "estado": "ACTIVO",
        "usuario_creacion": "tester"
    }
    response = client.post("/productos/", json=data)
    assert response.status_code == 201
    return response.json().get("id") 
