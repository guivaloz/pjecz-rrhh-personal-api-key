"""
Areas v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class AreaOut(BaseModel):
    """Esquema para entregar areas"""

    id: int | None = None
    centro_trabajo_id: int | None = None
    centro_trabajo_clave: str | None = None
    centro_trabajo_nombre: str | None = None
    nombre: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneAreaOut(AreaOut, OneBaseOut):
    """Esquema para entregar un area"""
