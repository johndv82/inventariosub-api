from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models.sede import Sede
from schemas.sede import SedeCreate
from services.exception import ServiceException

@staticmethod
def crear_sede(db:Session, data: SedeCreate):
    nueva_sede = Sede(**data.model_dump())
    db.add(nueva_sede)
    try:
        db.commit()
        db.refresh(nueva_sede)
    except IntegrityError:
        db.rollback()
        raise ServiceException("El nombre ya está en uso", code=409) # HTTP_409_CONFLICT
    return nueva_sede

@staticmethod
def listar_sede(db:Session):
    sedes = db.query(Sede).all()
    return sedes