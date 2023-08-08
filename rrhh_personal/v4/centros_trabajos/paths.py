"""
Centros de Trabajo v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser
from .crud import get_centro_trabajo_with_clave, get_centros_trabajos
from .schemas import CentroTrabajoOut, OneCentroTrabajoOut

centros_trabajos = APIRouter(prefix="/v3/centros_trabajos", tags=["categoria"])


@centros_trabajos.get("", response_model=CustomList[CentroTrabajoOut])
async def listado_centros_trabajos(
    current_user: CurrentUser,
    database: Annotated[Session, Depends(get_db)],
):
    """Listado de centros de trabajo"""
    if current_user.permissions.get("CENTROS DE TRABAJO", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_centros_trabajos(database=database)
    except MyAnyError as error:
        return CustomList(success=False, message=str(error))
    return paginate(resultados)


@centros_trabajos.get("/{clave}", response_model=OneCentroTrabajoOut)
async def detalle_centro_trabajo(
    current_user: CurrentUser,
    database: Annotated[Session, Depends(get_db)],
    clave: str,
):
    """Detalle de una centro de trabajo a partir de su clave"""
    if current_user.permissions.get("CENTROS DE TRABAJO", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        centro_trabajo = get_centro_trabajo_with_clave(database=database, clave=clave)
    except MyAnyError as error:
        return OneCentroTrabajoOut(success=False, message=str(error))
    return OneCentroTrabajoOut.model_validate(centro_trabajo)
