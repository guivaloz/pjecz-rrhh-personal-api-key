"""
Centros de Trabajo v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_clave

from ...core.centros_trabajos.models import CentroTrabajo


def get_centros_trabajos(database: Session) -> Any:
    """Consultar los centros de trabajo activos"""
    return database.query(CentroTrabajo).filter_by(estatus="A").order_by(CentroTrabajo.id)


def get_centro_trabajo(database: Session, centro_trabajo_id: int) -> CentroTrabajo:
    """Consultar un centro de trabajo por su id"""
    centro_trabajo = database.query(CentroTrabajo).get(centro_trabajo_id)
    if centro_trabajo is None:
        raise MyNotExistsError("No existe ese centro de trabajo")
    if centro_trabajo.estatus != "A":
        raise MyIsDeletedError("No es activo ese centro de trabajo, está eliminado")
    return centro_trabajo


def get_centro_trabajo_with_clave(database: Session, clave: str) -> CentroTrabajo:
    """Consultar un centro de trabajo por su clave"""
    try:
        clave = safe_clave(clave)
    except ValueError as error:
        raise MyNotValidParamError(str(error)) from error
    centro_trabajo = database.query(CentroTrabajo).filter_by(clave=clave).first()
    if centro_trabajo is None:
        raise MyNotExistsError("No existe ese centro de trabajo")
    if centro_trabajo.estatus != "A":
        raise MyIsDeletedError("No es activo ese centro de trabajo, está eliminado")
    return centro_trabajo
