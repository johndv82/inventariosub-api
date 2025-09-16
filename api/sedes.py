from fastapi import APIRouter, Depends, HTTPException, status
from core.database import get_db
from schemas.sede import SedeCreate, SedeResponse
from services import sede as SedeService
from sqlalchemy.orm import Session
from services.exception import ServiceException

router = APIRouter(prefix="/sedes", tags=["Sedes"])

@router.post("/", response_model=SedeResponse, status_code=201)
def crear(sede: SedeCreate, db: Session = Depends(get_db)):
    try:
        return SedeService.crear_sede(db, sede)
    except ServiceException as e:
        raise HTTPException(
            status_code=e.code,
            detail=str(e.message)
        )

@router.get("/", response_model=list[SedeResponse])
def listar(db: Session = Depends(get_db)):
    return SedeService.listar_sede(db)
