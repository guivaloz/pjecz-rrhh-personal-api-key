"""
Personas v4, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_rfc, safe_string

from ...core.personas.models import Persona


def get_personas(
    database: Session,
    estado_civil: str | None = None,
    rfc: str | None = None,
    sexo: str | None = None,
    situacion: str | None = None,
) -> Any:
    """Consultar los personas activos"""
    consulta = database.query(Persona)
    if estado_civil is not None:
        estado_civil = safe_string(estado_civil)
        consulta = consulta.filter_by(estado_civil=estado_civil)
    if rfc is not None:
        rfc = safe_rfc(rfc, search_fragment=True)
        consulta = consulta.filter(Persona.rfc.contains(rfc))
    if sexo is not None:
        sexo = safe_string(sexo)
        consulta = consulta.filter_by(sexo=sexo)
    if situacion is not None:
        situacion = safe_string(situacion)
        consulta = consulta.filter_by(situacion=situacion)
    return consulta.filter_by(estatus="A").order_by(Persona.curp)


def get_persona(database: Session, persona_id: int) -> Persona:
    """Consultar un persona por su id"""
    persona = database.query(Persona).get(persona_id)
    if persona is None:
        raise MyNotExistsError("No existe ese persona")
    if persona.estatus != "A":
        raise MyIsDeletedError("No es activa ese persona, está eliminada")
    return persona


def get_persona_with_curp(database: Session, persona_curp: str) -> Persona:
    """Consultar un persona por su CURP"""
    try:
        curp = safe_string(persona_curp)
    except ValueError as error:
        raise MyNotValidParamError(str(error)) from error
    persona = database.query(Persona).filter_by(curp=curp).first()
    if persona is None:
        raise MyNotExistsError("No existe ese persona")
    if persona.estatus != "A":
        raise MyIsDeletedError("No es activa ese persona, está eliminada")
    return persona
