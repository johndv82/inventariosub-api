from fastapi import FastAPI
from api import sedes, usuarios, proveedores, productos
from api import inventario as inventarioApi
from core.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from models import *

Base.metadata.create_all(bind=engine)
app = FastAPI(title="InventarioSub API", version="1.0")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sedes.router)
app.include_router(usuarios.router)
app.include_router(proveedores.router)
app.include_router(productos.router)
app.include_router(inventarioApi.router)