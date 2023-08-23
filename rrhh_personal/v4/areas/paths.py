"""
Areas v4, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_area, get_areas
from .schemas import AreaOut, OneAreaOut

areas = APIRouter(prefix="/v4/areas", tags=["catalogos"])


@areas.get("", response_model=CustomPage[AreaOut])
async def listado_areas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    centro_trabajo_id: int = None,
    centro_trabajo_clave: str = None,
):
    """Listado de areas"""
    if current_user.permissions.get("AREAS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_areas(
            database=database,
            centro_trabajo_id=centro_trabajo_id,
            centro_trabajo_clave=centro_trabajo_clave,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@areas.get("/{area_id}", response_model=OneAreaOut)
async def detalle_area(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    area_id: int,
):
    """Detalle de una area a partir de su id"""
    if current_user.permissions.get("AREAS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        area = get_area(database, area_id)
    except MyAnyError as error:
        return OneAreaOut(success=False, message=str(error))
    return OneAreaOut.model_validate(area)
