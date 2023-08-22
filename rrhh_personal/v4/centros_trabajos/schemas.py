"""
Centros de Trabajo v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class CentroTrabajoOut(BaseModel):
    """Esquema para entregar centros de trabajos"""

    id: int | None = None
    clave: str | None = None
    nombre: str | None = None
    telefono: str | None = None
    num_ext: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneCentroTrabajoOut(CentroTrabajoOut, OneBaseOut):
    """Esquema para entregar un centro de trabajo"""
