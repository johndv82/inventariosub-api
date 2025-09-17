from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.orm import relationship
from core.database import Base
from datetime import datetime
import enum

class EstadoProveedorEnum(str, enum.Enum):
    ACTIVO = "ACTIVO"
    INACTIVO = "INACTIVO"

class Proveedor(Base):
    __tablename__ = "proveedores"

    ruc = Column(String(11), primary_key=True, index=True)
    razon_social = Column(String(250), nullable=False)
    contacto = Column(String(250), nullable=False)
    telefono_contacto = Column(String(50), nullable=True)
    estado = Column(Enum(EstadoProveedorEnum), default=EstadoProveedorEnum.ACTIVO, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.now, nullable=False)
    usuario_creacion = Column(String(25), nullable=False)

    productos = relationship("Producto", back_populates="proveedor")