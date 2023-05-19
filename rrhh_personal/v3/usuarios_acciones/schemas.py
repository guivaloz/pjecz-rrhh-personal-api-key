"""
Usuarios-Acciones v3, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class UsuarioAccionOut(BaseModel):
    """Esquema para entregar usuarios-acciones"""

    id: int | None
    accion_id: int | None
    accion_clave: str | None
    usuario_id: int | None
    usuario_nombre: str | None
    descripcion: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneUsuarioAccionOut(UsuarioAccionOut, OneBaseOut):
    """Esquema para entregar un usuario-accion"""
