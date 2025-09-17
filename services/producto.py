from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.producto import Producto
from models.proveedor import Proveedor
from schemas.producto import ProductoCreate, ProductoUpdate
from services.exception import ServiceException

class ProductoService:

    @staticmethod
    def crear(db: Session, data: ProductoCreate):

        # validar Proveedor
        if data.proveedor_ruc:
            proveedor = db.query(Proveedor).filter(Proveedor.ruc == data.proveedor_ruc).first()
            if not proveedor:
                raise ServiceException("El proveedor asignada no existe", code=404)
            
        producto = Producto(**data.model_dump())
        db.add(producto)
        try:
            db.commit()
            db.refresh(producto)
        except IntegrityError:
            db.rollback()
            raise ServiceException("El código de producto ya existe", 409)
        return producto

    @staticmethod
    def obtener(db: Session, producto_id: int):
        producto = db.query(Producto).filter(Producto.id == producto_id).first()
        if not producto:
            raise ServiceException("Producto no encontrado", 404)
        return producto

    @staticmethod
    def listar(db: Session):
        return db.query(Producto).all()

    @staticmethod
    def actualizar(db: Session, producto_id: int, data: ProductoUpdate):
        producto = db.query(Producto).filter(Producto.id == producto_id).first()
        if not producto:
            raise ServiceException("Producto no encontrado", 404)

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(producto, key, value)

        try:
            db.commit()
            db.refresh(producto)
        except IntegrityError:
            db.rollback()
            raise ServiceException("Conflicto al actualizar producto", 409)
        return producto
