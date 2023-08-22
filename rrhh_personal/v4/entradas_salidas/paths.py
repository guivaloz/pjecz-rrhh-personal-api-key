"""
Entradas-Salidas v4, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_entrada_salida, get_entradas_salidas
from .schemas import EntradaSalidaOut, OneEntradaSalidaOut

entradas_salidas = APIRouter(prefix="/v3/entradas_salidas", tags=["categoria"])


@entradas_salidas.get("/paginado", response_model=CustomPage[EntradaSalidaOut])
async def listado_entradas_salidas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Listado de entradas-salidas paginados"""
    if current_user.permissions.get("ENTRADAS SALIDAS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_entradas_salidas(database)
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@entradas_salidas.get("/{entrada_salidaget_entrada_salida}", response_model=OneEntradaSalidaOut)
async def detalle_entrada_salidaget_entrada_salida(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    entrada_salidaget_entrada_salida: int,
):
    """Detalle de una entrada-salida a partir de su id"""
    if current_user.permissions.get("ENTRADAS SALIDAS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        entrada_salidaget_entrada_salida = get_entrada_salida(database, entrada_salidaget_entrada_salida)
    except MyAnyError as error:
        return OneEntradaSalidaOut(success=False, message=str(error))
    return OneEntradaSalidaOut.model_validate(entrada_salidaget_entrada_salida)
