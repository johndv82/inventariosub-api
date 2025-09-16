from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    is_admin: bool = False
    sede_id: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    is_admin: Optional[bool] = None
    sede_id: Optional[int] = None

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
