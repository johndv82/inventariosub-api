from fastapi import FastAPI
from api import sede as sedeApi
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

app.include_router(sedeApi.router)