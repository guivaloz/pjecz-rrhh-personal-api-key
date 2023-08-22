"""
Personas v4, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_persona_with_curp, get_personas
from .schemas import OnePersonaOut, PersonaOut

personas = APIRouter(prefix="/v4/personas", tags=["categoria"])


@personas.get("", response_model=CustomPage[PersonaOut])
async def paginado_personas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    estado_civil: str | None = None,
    sexo: str | None = None,
    situacion: str | None = None,
):
    """Paginado de personas"""
    if current_user.permissions.get("PERSONAS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_personas(
            database=database,
            estado_civil=estado_civil,
            sexo=sexo,
            situacion=situacion,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@personas.get("/{curp}", response_model=OnePersonaOut)
async def detalle_persona(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    curp: str,
):
    """Detalle de una persona a partir de su clave"""
    if current_user.permissions.get("PERSONAS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        persona = get_persona_with_curp(database, curp)
    except MyAnyError as error:
        return OnePersonaOut(success=False, message=str(error))
    return OnePersonaOut.model_validate(persona)
