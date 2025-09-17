from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from core.database import Base
from datetime import datetime
import enum

class UnidadMedidaEnum(str, enum.Enum):
    LT = "LT"
    GR = "GR"
    KL = "KL"
    UND = "UND"

class EstadoProductoEnum(str, enum.Enum):
    ACTIVO = "ACTIVO"
    INACTIVO = "INACTIVO"

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(50), unique=True, nullable=False, index=True)
    descripcion = Column(Text, nullable=False)
    unidad_medida = Column(Enum(UnidadMedidaEnum), nullable=False)
    peso_en_kilos = Column(Numeric(10, 3), nullable=True)
    proveedor_ruc = Column(String(11), ForeignKey("proveedores.ruc"), nullable=True)
    estado = Column(Enum(EstadoProductoEnum), default=EstadoProductoEnum.ACTIVO, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.now, nullable=False)
    usuario_creacion = Column(String(25), nullable=False)

    proveedor = relationship("Proveedor", back_populates="productos")
