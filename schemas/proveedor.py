from pydantic import BaseModel
from typing import Optional
from models.proveedor import EstadoProveedorEnum

class ProveedorBase(BaseModel):
    ruc: str
    razon_social: str
    contacto: str
    telefono_contacto: str
    estado: EstadoProveedorEnum
    usuario_creacion: str

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorUpdate(BaseModel):
    razon_social: Optional[str] = None
    contacto: Optional[str] = None
    telefono_contacto: Optional[str] = None
    estado: Optional[EstadoProveedorEnum] = None

class ProveedorResponse(ProveedorBase):
    ruc: str

    class Config:
        orm_mode = True
