from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from core.database import Base


class TipoMovimiento(str, enum.Enum):
    INGRESO = "INGRESO"
    SALIDA = "SALIDA"


class EstadoProducto(str, enum.Enum):
    DISPONIBLE = "DISPONIBLE"
    COMPROMETIDO = "COMPROMETIDO"
    DANADO = "DANADO" #Dañado
    OTRO = "OTRO" 


class EstadoRegistro(str, enum.Enum):
    EXISTENTE = "EXISTENTE"
    ANULADO = "ANULADO"


class Inventario(Base):
    __tablename__ = "inventario"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    sede_id = Column(Integer, ForeignKey("sedes.id"), nullable=False)
    tipo_movimiento = Column(Enum(TipoMovimiento), nullable=False)
    cantidad = Column(Integer, nullable=False)
    estado_producto = Column(Enum(EstadoProducto), nullable=False, default=EstadoProducto.DISPONIBLE)
    estado = Column(Enum(EstadoRegistro), nullable=False, default=EstadoRegistro.EXISTENTE)

    fecha_movimiento = Column(DateTime, default=datetime.now, nullable=False)
    usuario_creacion = Column(String(50), nullable=False)
    observaciones = Column(Text, nullable=True)

    fecha_anulacion = Column(DateTime, nullable=True)
    usuario_anulacion = Column(String(50), nullable=True)

    producto = relationship("Producto", back_populates="movimientos")
    sede = relationship("Sede", back_populates="movimientos")
