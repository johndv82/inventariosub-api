from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import Usuario, Sede
from schemas.usuario import UsuarioCreate, UsuarioUpdate
from services.exception import ServiceException

class UsuarioService:

    @staticmethod
    def crear_usuario(db: Session, usuario: UsuarioCreate):
        # validar sede
        if usuario.sede_id:
            sede = db.query(Sede).filter(Sede.id == usuario.sede_id).first()
            if not sede:
                raise ServiceException("La sede asignada no existe", code=404)
            
        nuevo_usuario = Usuario(**usuario.model_dump())
        db.add(nuevo_usuario)
        try:
            db.commit()
            db.refresh(nuevo_usuario)
        except IntegrityError:
            db.rollback()
            raise ServiceException("El email ya está registrado", code=409)
        return nuevo_usuario

    @staticmethod
    def obtener_usuario(db: Session, usuario_id: int):
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not usuario:
            raise ServiceException("Usuario no encontrado", code=404)
        return usuario

    @staticmethod
    def actualizar_usuario(db: Session, usuario_id: int, usuario_update: UsuarioUpdate):
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not usuario:
            raise ServiceException("Usuario no encontrado", code=404)
        for key, value in usuario_update.model_dump(exclude_unset=True).items():
            setattr(usuario, key, value)
        try:
            db.commit()
            db.refresh(usuario)
        except IntegrityError:
            db.rollback()
            raise ServiceException("El email ya está registrado", code=409)
        return usuario

    @staticmethod
    def eliminar_usuario(db: Session, usuario_id: int):
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not usuario:
            raise ServiceException("Usuario no encontrado", code=404)
        db.delete(usuario)
        db.commit()
        return {"detail": "Usuario eliminado correctamente"}
