from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.database import get_db
from models.sede import Sede
from schemas.sede import SedeCreate, SedeResponse

router = APIRouter(prefix="/sedes", tags=["Sedes"])

@router.post("/", response_model=SedeResponse)
def crear_sede(sede: SedeCreate, db: Session = Depends(get_db)):
    nueva_sede = Sede(**sede.model_dump())
    db.add(nueva_sede)
    try:
        db.commit()
        db.refresh(nueva_sede)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe una sede con ese nombre"
        )
    return nueva_sede

@router.get("/", response_model=list[SedeResponse])
def listar_sedes(db: Session = Depends(get_db)):
    return db.query(Sede).all()
