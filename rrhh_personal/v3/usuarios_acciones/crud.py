"""
Usuarios-Acciones v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_clave

from ...core.usuarios_acciones.models import UsuarioAccion
from ..acciones.crud import get_accion, get_accion_with_clave
from ..usuarios.crud import get_usuario, get_usuario_with_email


def get_usuarios_acciones(
    db: Session,
    accion_id: int = None,
    accion_clave: str = None,
    usuario_id: int = None,
    usuario_email: str = None,
) -> Any:
    """Consultar los usuarios-acciones activos"""
    consulta = db.query(UsuarioAccion)
    if accion_id is not None:
        accion = get_accion(db, accion_id)
        consulta = consulta.filter(accion == accion)
    elif accion_clave is not None:
        accion = get_accion_with_clave(db, accion_clave)
        consulta = consulta.filter(accion == accion)
    if usuario_id is not None:
        usuario = get_usuario(db, usuario_id)
        consulta = consulta.filter(usuario == usuario)
    elif usuario_email is not None:
        usuario = get_usuario_with_email(db, usuario_email)
        consulta = consulta.filter(usuario == usuario)
    return consulta.filter_by(estatus="A").order_by(UsuarioAccion.id)


def get_usuario_accion(db: Session, usuario_accion_id: int) -> UsuarioAccion:
    """Consultar un usuario-accion por su id"""
    usuario_accion = db.query(UsuarioAccion).get(usuario_accion_id)
    if usuario_accion is None:
        raise MyNotExistsError("No existe ese usuario-accion")
    if usuario_accion.estatus != "A":
        raise MyIsDeletedError("No es activo ese usuario-accion, está eliminado")
    return usuario_accion
