"""
Personas v4, esquemas de pydantic
"""
from datetime import date

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class PersonaOut(BaseModel):
    """Esquema para entregar personas"""

    id: int | None = None
    nombres: str | None = None
    apellido_primero: str | None = None
    apellido_segundo: str | None = None
    numero_empleado: int | None = None
    rfc: str | None = None
    curp: str | None = None
    email: str | None = None
    email_secundario: str | None = None
    situacion: str | None = None
    sexo: str | None = None
    estado_civil: str | None = None
    fecha_ingreso_gobierno: date | None = None
    fecha_ingreso_pj: date | None = None
    model_config = ConfigDict(from_attributes=True)


class OnePersonaOut(PersonaOut, OneBaseOut):
    """Esquema para entregar una persona"""
