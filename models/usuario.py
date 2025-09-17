from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from core.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(25), nullable=False)
    email = Column(String(250), unique=True, index=True, nullable=False)
    is_admin = Column(Boolean, default=False)

    sede_id = Column(Integer, ForeignKey("sedes.id"))
    sede = relationship("Sede")
