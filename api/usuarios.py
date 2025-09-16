from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from services.exception import ServiceException
from services.usuario import UsuarioService
from schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioResponse, status_code=201)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return UsuarioService.crear_usuario(db, usuario)
    except ServiceException as e:
        raise HTTPException(
            status_code=e.code,
            detail=str(e.message)
        )

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return UsuarioService.obtener_usuario(db, usuario_id)
    except ServiceException as e:
        raise HTTPException(
            status_code=e.code,
            detail=str(e.message)
        )

@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    try:
        return UsuarioService.actualizar_usuario(db, usuario_id, usuario)
    except ServiceException as e:
        raise HTTPException(
            status_code=e.code,
            detail=str(e.message)
        )

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return UsuarioService.eliminar_usuario(db, usuario_id)
    except ServiceException as e:
        raise HTTPException(
            status_code=e.code,
            detail=str(e.message)
        )