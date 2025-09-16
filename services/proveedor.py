from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.proveedor import Proveedor
from schemas.proveedor import ProveedorCreate, ProveedorUpdate
from services.exception import ServiceException

class ProveedorService:

    @staticmethod
    def crear(db: Session, data: ProveedorCreate):
        proveedor = Proveedor(**data.model_dump())
        db.add(proveedor)
        try:
            db.commit()
            db.refresh(proveedor)
        except IntegrityError:
            db.rollback()
            raise ServiceException("El RUC ya está registrado", 409)
        return proveedor

    @staticmethod
    def obtener(db: Session, ruc: str):
        proveedor = db.query(Proveedor).filter(Proveedor.ruc == ruc).first()
        if not proveedor:
            raise ServiceException("Proveedor no encontrado", 404)
        return proveedor

    @staticmethod
    def listar(db: Session):
        return db.query(Proveedor).all()

    @staticmethod
    def actualizar(db: Session, ruc: str, data: ProveedorUpdate):
        proveedor = db.query(Proveedor).filter(Proveedor.ruc == ruc).first()
        if not proveedor:
            raise ServiceException("Proveedor no encontrado", 404)

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(proveedor, key, value)

        try:
            db.commit()
            db.refresh(proveedor)
        except IntegrityError:
            db.rollback()
            raise ServiceException("Conflicto al actualizar proveedor", 409)
        return proveedor
