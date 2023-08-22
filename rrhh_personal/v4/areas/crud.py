"""
Areas v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.areas.models import Area
from ..centros_trabajos.crud import get_centro_trabajo, get_centro_trabajo_with_clave


def get_areas(
    database: Session,
    centro_trabajo_id: int = None,
    centro_trabajo_clave: str = None,
) -> Any:
    """Consultar los areas activos"""
    consulta = database.query(Area)
    if centro_trabajo_id is not None:
        centro_trabajo = get_centro_trabajo(database, centro_trabajo_id)
        consulta = consulta.filter_by(centro_trabajo_id=centro_trabajo.id)
    elif centro_trabajo_clave is not None:
        centro_trabajo = get_centro_trabajo_with_clave(database, centro_trabajo_clave)
        consulta = consulta.filter_by(centro_trabajo_id=centro_trabajo.id)
    return consulta.filter_by(estatus="A").order_by(Area.id)


def get_area(database: Session, area_id: int) -> Area:
    """Consultar un area por su id"""
    area = database.query(Area).get(area_id)
    if area is None:
        raise MyNotExistsError("No existe ese area")
    if area.estatus != "A":
        raise MyIsDeletedError("No es activo ese area, está eliminado")
    return area
