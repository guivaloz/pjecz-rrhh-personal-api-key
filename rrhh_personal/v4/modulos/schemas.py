"""
Modulos v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class ModuloOut(BaseModel):
    """Esquema para entregar modulos"""

    id: int | None = None
    descripcion: str | None = None
    icono_nombre: str | None = None
    tipo: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneModuloOut(ModuloOut, OneBaseOut):
    """Esquema para entregar un modulo"""
