"""
Centros de Trabajos, modelos
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class CentroTrabajo(Base, UniversalMixin):
    """CentroTrabajo"""

    # Nombre de la tabla
    __tablename__ = "centros_trabajos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    clave = Column(String(16), unique=True, nullable=False)
    nombre = Column(String(128), nullable=False)
    telefono = Column(String(128), nullable=True)
    num_ext = Column(String(64), nullable=True)

    # Hijos
    areas = relationship("Area", back_populates="centro_trabajo")

    def __repr__(self):
        """Representación"""
        return f"<CentroTrabajo {self.id}>"
