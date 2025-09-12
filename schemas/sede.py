from pydantic import BaseModel

class SedeBase(BaseModel):
    nombre: str
    direccion: str

class SedeCreate(SedeBase):
    pass

class SedeResponse(SedeBase):
    id: int

    class Config:
        from_attributes = True
