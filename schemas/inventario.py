from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from models.inventario import EstadoProducto, TipoMovimiento, EstadoRegistro


class InventarioBase(BaseModel):
    producto_id: int
    sede_id: int
    tipo_movimiento: TipoMovimiento
    cantidad: int
    estado_producto: EstadoProducto = EstadoProducto.DISPONIBLE
    usuario_creacion: str
    observaciones: Optional[str] = None


class InventarioCreate(InventarioBase):
    pass


class InventarioResponse(InventarioBase):
    id: int
    estado: EstadoRegistro
    fecha_movimiento: datetime
    fecha_anulacion: Optional[datetime] = None
    usuario_anulacion: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
