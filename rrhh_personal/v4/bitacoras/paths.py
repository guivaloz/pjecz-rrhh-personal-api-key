"""
Bitacoras v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_bitacora, get_bitacoras
from .schemas import BitacoraOut, OneBitacoraOut

bitacoras = APIRouter(prefix="/v3/bitacoras", tags=["usuarios"])


@bitacoras.get("", response_model=CustomPage[BitacoraOut])
async def listado_bitacoras(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    usuario_id: int = None,
    usuario_email: str = None,
):
    """Listado de bitacoras"""
    if current_user.permissions.get("BITACORAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_bitacoras(database=database, usuario_id=usuario_id, usuario_email=usuario_email)
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@bitacoras.get("/{bitacora_id}", response_model=OneBitacoraOut)
async def detalle_bitacora(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    bitacora_id: int,
):
    """Detalle de una bitacoras a partir de su id"""
    if current_user.permissions.get("BITACORAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        bitacora = get_bitacora(database=database, bitacora_id=bitacora_id)
    except MyAnyError as error:
        return OneBitacoraOut(success=False, message=str(error))
    return OneBitacoraOut.model_validate(bitacora)
