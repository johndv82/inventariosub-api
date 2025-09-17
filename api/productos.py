from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from services.producto import ProductoService
from schemas.producto import ProductoCreate, ProductoUpdate, ProductoResponse
from services.exception import ServiceException
from fastapi import HTTPException

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", response_model=ProductoResponse, status_code=201)
def crear(data: ProductoCreate, db: Session = Depends(get_db)):
    try:
        return ProductoService.crear(db, data)
    except ServiceException as e:
        raise HTTPException(status_code=e.code, detail=e.message)

@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener(producto_id: int, db: Session = Depends(get_db)):
    try:
        return ProductoService.obtener(db, producto_id)
    except ServiceException as e:
        raise HTTPException(status_code=e.code, detail=e.message)

@router.get("/", response_model=list[ProductoResponse])
def listar(db: Session = Depends(get_db)):
    return ProductoService.listar(db)

@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar(producto_id: int, data: ProductoUpdate, db: Session = Depends(get_db)):
    try:
        return ProductoService.actualizar(db, producto_id, data)
    except ServiceException as e:
        raise HTTPException(status_code=e.code, detail=e.message)
