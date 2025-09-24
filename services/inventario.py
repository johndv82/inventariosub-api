from sqlite3 import IntegrityError
from sqlalchemy.orm import Session
from models.inventario import Inventario, EstadoRegistro
from models.producto import Producto
from models.sede import Sede
from schemas.inventario import InventarioCreate
from datetime import datetime
from services.exception import ServiceException

class InventarioService:

    @staticmethod
    def crear(db: Session, movimiento: InventarioCreate):

        # validar Producto
        if movimiento.producto_id:
            proveedor = db.query(Producto).filter(Producto.id == movimiento.producto_id).first()
            if not proveedor:
                raise ServiceException("El producto registrado no existe", code=404)
            
        # validar sede
        if movimiento.sede_id:
            sede = db.query(Sede).filter(Sede.id == movimiento.sede_id).first()
            if not sede:
                raise ServiceException("La sede registrada no existe", code=404)
            
        nuevo_mov = Inventario(**movimiento.model_dump())
        db.add(nuevo_mov)
        try:
            db.commit()
            db.refresh(nuevo_mov)
        except IntegrityError:
            db.rollback()
            raise ServiceException("Error de integridad con Inventario", 409)
        return nuevo_mov

    @staticmethod
    def anular(db: Session, movimiento_id: int, usuario: str):
        mov = db.query(Inventario).filter(Inventario.id == movimiento_id, Inventario.estado == "EXISTENTE").first()
        if not mov:
            raise ServiceException("El movimiento seleccionado no existe", code=404)
        
        mov.estado = EstadoRegistro.ANULADO
        mov.fecha_anulacion = datetime.now()
        mov.usuario_anulacion = usuario
        try:
            db.commit()
            db.refresh(mov)
        except IntegrityError:
            db.rollback()
            raise ServiceException("Error de integridad con Inventario", 409)
        return mov
    
    @staticmethod
    def obtener(db: Session, inventario_id: int):
        inventario = db.query(Inventario).filter(Inventario.id == inventario_id).first()
        if not inventario:
            raise ServiceException("Registro no encontrado", 404)
        return inventario
