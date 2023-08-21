"""
Roles v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_rol_with_nombre, get_roles
from .schemas import OneRolOut, RolOut

roles = APIRouter(prefix="/v3/roles", tags=["usuarios"])


@roles.get("", response_model=CustomList[RolOut])
async def listado_roles(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Listado de roles"""
    if current_user.permissions.get("ROLES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_roles(database=database)
    except MyAnyError as error:
        return CustomList(success=False, message=str(error))
    return paginate(resultados)


@roles.get("/{nombre}", response_model=OneRolOut)
async def detalle_rol(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    nombre: str,
):
    """Detalle de una roles a partir de su id"""
    if current_user.permissions.get("ROLES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        rol = get_rol_with_nombre(database=database, nombre=nombre)
    except MyAnyError as error:
        return OneRolOut(success=False, message=str(error))
    return OneRolOut.model_validate(rol)
