"""
Acciones v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_clave

from ...core.acciones.models import Accion


def get_acciones(db: Session) -> Any:
    """Consultar las acciones activas"""
    return db.query(Accion).filter_by(estatus="A").order_by(Accion.clave)


def get_accion(db: Session, accion_id: int) -> Accion:
    """Consultar una accion por su id"""
    accion = db.query(Accion).get(accion_id)
    if accion is None:
        raise MyNotExistsError("No existe ese accion")
    if accion.estatus != "A":
        raise MyIsDeletedError("No es activo ese accion, está eliminado")
    return accion


def get_accion_with_clave(db: Session, clave: str) -> Accion:
    """Consultar una accion por su clave"""
    try:
        clave = safe_clave(clave)
    except ValueError as error:
        raise MyNotValidParamError(str(error)) from error
    accion = db.query(Accion).filter_by(clave=clave).first()
    if accion is None:
        raise MyNotExistsError("No existe ese accion")
    if accion.estatus != "A":
        raise MyIsDeletedError("No es activo ese accion, está eliminado")
    return accion
