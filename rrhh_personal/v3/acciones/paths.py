"""
Acciones v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList, custom_list_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_acciones, get_accion_with_clave
from .schemas import AccionOut, OneAccionOut

acciones = APIRouter(prefix="/v3/acciones", tags=["categoria"])


@acciones.get("", response_model=CustomList[AccionOut])
async def listado_acciones(
    current_user: CurrentUser,
    db: DatabaseSession,
):
    """Listado de acciones"""
    if current_user.permissions.get("ACCIONES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_acciones(db=db)
    except MyAnyError as error:
        return custom_list_success_false(error)
    return paginate(resultados)


@acciones.get("/{clave}", response_model=OneAccionOut)
async def detalle_accion(
    current_user: CurrentUser,
    db: DatabaseSession,
    clave: str,
):
    """Detalle de una accion a partir de su clave"""
    if current_user.permissions.get("ACCIONES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        accion = get_accion_with_clave(db=db, clave=clave)
    except MyAnyError as error:
        return OneAccionOut(success=False, message=str(error))
    return OneAccionOut.from_orm(accion)
