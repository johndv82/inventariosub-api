from pydantic import BaseModel, ConfigDict
from typing import Optional
from models.producto import EstadoProductoEnum, UnidadMedidaEnum

class ProductoBase(BaseModel):
    codigo: str
    descripcion: str
    unidad_medida: UnidadMedidaEnum
    peso_en_kilos: float
    proveedor_ruc: str
    estado: EstadoProductoEnum
    usuario_creacion: str

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    descripcion: Optional[str] = None
    unidad_medida: Optional[UnidadMedidaEnum] = None
    peso_en_kilos: Optional[float] = None
    proveedor_ruc: Optional[str] = None
    estado: Optional[EstadoProductoEnum] = None

class ProductoResponse(ProductoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
