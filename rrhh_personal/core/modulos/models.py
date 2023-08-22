"""
Modulos, modelos
"""
from typing import OrderedDict

from sqlalchemy import Column, Enum, Integer, String

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Modulo(Base, UniversalMixin):
    """Modulo"""

    TIPO = OrderedDict(
        [
            ("ADMINISTRACIÓN", "Administrativo"),
            ("CATÁLOGO", "Catálogo"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "modulos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    nombre = Column(String(32), unique=True, nullable=False)
    descripcion = Column(String(256))
    icono_nombre = Column(String(32), nullable=False)  # Nombre del icono en FontAwesome
    tipo = Column(Enum(*TIPO, name="tipo", native_enum=False), index=False, nullable=False)

    def __repr__(self):
        """Representación"""
        return f"<Modulo {self.nombre}>"
