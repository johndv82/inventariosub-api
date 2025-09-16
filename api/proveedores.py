from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from services.proveedor import ProveedorService
from schemas.proveedor import ProveedorCreate, ProveedorUpdate, ProveedorResponse
from services.exception import ServiceException
from fastapi import HTTPException

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])

@router.post("/", response_model=ProveedorResponse, status_code=201)
def crear(data: ProveedorCreate, db: Session = Depends(get_db)):
    try:
        return ProveedorService.crear(db, data)
    except ServiceException as e:
        raise HTTPException(status_code=e.code, detail=e.message)

@router.get("/{ruc}", response_model=ProveedorResponse)
def obtener(ruc: str, db: Session = Depends(get_db)):
    try:
        return ProveedorService.obtener(db, ruc)
    except ServiceException as e:
        raise HTTPException(status_code=e.code, detail=e.message)

@router.get("/", response_model=list[ProveedorResponse])
def listar(db: Session = Depends(get_db)):
    return ProveedorService.listar(db)

@router.put("/{ruc}", response_model=ProveedorResponse)
def actualizar(ruc: str, data: ProveedorUpdate, db: Session = Depends(get_db)):
    try:
        return ProveedorService.actualizar(db, ruc, data)
    except ServiceException as e:
        raise HTTPException(status_code=e.code, detail=e.message)
