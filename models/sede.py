from sqlalchemy import Column, Integer, String
from core.database import Base

class Sede(Base):
    __tablename__ = "sedes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(250), unique=True, nullable=False)
    direccion = Column(String(250), nullable=False)