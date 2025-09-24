from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.inventario import InventarioCreate, InventarioResponse
from services.exception import ServiceException
from services.inventario import InventarioService

router = APIRouter(prefix="/inventario", tags=["Inventario"])


@router.post("/", response_model=InventarioResponse)
def crear_movimiento(movimiento: InventarioCreate, db: Session = Depends(get_db)):
    try:
        return InventarioService.crear(db, movimiento)
    except ServiceException as e:
        raise HTTPException(status_code=e.code, detail=e.message)


@router.delete("/{movimiento_id}", response_model=InventarioResponse)
def anular_movimiento(movimiento_id: int, usuario: str, db: Session = Depends(get_db)):
    try:
        return InventarioService.anular(db, movimiento_id, usuario)
    except ServiceException as e:
        raise HTTPException(status_code=e.code, detail=e.message)

@router.get("/{inventario_id}", response_model=InventarioResponse)
def obtener_movimiento(inventario_id: int, db: Session = Depends(get_db)):
    try:
        return InventarioService.obtener(db, inventario_id)
    except ServiceException as e:
        raise HTTPException(status_code=e.code, detail=e.message)