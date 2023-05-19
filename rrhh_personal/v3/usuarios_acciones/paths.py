"""
Usuarios-Acciones v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_usuarios_acciones, get_usuario_accion
from .schemas import UsuarioAccionOut, OneUsuarioAccionOut

usuarios_acciones = APIRouter(prefix="/v3/usuarios_acciones", tags=["usuarios"])


@usuarios_acciones.get("", response_model=CustomPage[UsuarioAccionOut])
async def listado_usuarios_acciones(
    current_user: CurrentUser,
    db: DatabaseSession,
):
    """Listado de usuarios-acciones"""
    if current_user.permissions.get("USUARIOS ACCIONES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_usuarios_acciones(db=db)
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@usuarios_acciones.get("/{usuario_accion_id}", response_model=OneUsuarioAccionOut)
async def detalle_usuario_accion(
    current_user: CurrentUser,
    db: DatabaseSession,
    usuario_accion_id: int,
):
    """Detalle de un usuario-accion a partir de su id"""
    if current_user.permissions.get("USUARIOS ACCIONES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        usuario_accion = get_usuario_accion(db=db, usuario_accion_id=usuario_accion_id)
    except MyAnyError as error:
        return OneUsuarioAccionOut(success=False, message=str(error))
    return OneUsuarioAccionOut.from_orm(usuario_accion)
