"""
Modulos v4, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList

from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_modulo_with_nombre, get_modulos
from .schemas import ModuloOut, OneModuloOut

modulos = APIRouter(prefix="/v4/modulos", tags=["usuarios"])


@modulos.get("", response_model=CustomList[ModuloOut])
async def listado_modulos(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Listado de modulos"""
    if current_user.permissions.get("MODULOS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_modulos(database)
    except MyAnyError as error:
        return CustomList(success=False, message=str(error))
    return paginate(resultados)


@modulos.get("/{nombre}", response_model=OneModuloOut)
async def detalle_modulo(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    nombre: str,
):
    """Detalle de una modulos a partir de su id"""
    if current_user.permissions.get("MODULOS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        modulo = get_modulo_with_nombre(database, nombre)
    except MyAnyError as error:
        return OneModuloOut(success=False, message=str(error))
    return OneModuloOut.model_validate(modulo)
