"""
Acciones v3, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class AccionOut(BaseModel):
    """Esquema para entregar acciones"""

    id: int | None
    clave: str | None
    descripcion: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneAccionOut(AccionOut, OneBaseOut):
    """Esquema para entregar una accion"""
