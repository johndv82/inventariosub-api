from pydantic import BaseModel, ConfigDict

class SedeBase(BaseModel):
    nombre: str
    direccion: str

class SedeCreate(SedeBase):
    pass

class SedeResponse(SedeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
