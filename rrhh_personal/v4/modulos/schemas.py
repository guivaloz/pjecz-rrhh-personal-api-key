"""
Modulos v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class ModuloListOut(BaseModel):
    """Esquema para entregar modulos como listado"""

    id: int | None = None
    descripcion: str | None = None
    model_config = ConfigDict(from_attributes=True)


class ModuloOut(BaseModel):
    """Esquema para entregar modulos"""

    icono_nombre: str | None = None
    tipo: str | None = None


class OneModuloOut(ModuloOut, OneBaseOut):
    """Esquema para entregar un modulo"""
