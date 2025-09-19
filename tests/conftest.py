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

Base.metadata.create_all(bind=engine)

# Crear tablas en la BD Test
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture
def sede_creada():
    data = {
        "nombre": "Sede Prueba",
        "direccion": "Av. Central 123"
    }
    response = client.post("/sedes/", json=data)
    assert response.status_code in (200, 201, 409) 
    return response.json().get("id") 


@pytest.fixture
def proveedor_creado():
    data = {
        "ruc": "12345678901",
        "razon_social": "Proveedor Test",
        "contacto": "Juan Perez",
        "telefono_contacto": "999999999",
        "estado": "ACTIVO",
        "usuario_creacion": "tester"
    }
    response = client.post("/proveedores/", json=data)
    assert response.status_code in (200, 201, 409)
    return data["ruc"]
