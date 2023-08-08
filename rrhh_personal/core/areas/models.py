"""
Areas, modelos
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Area(Base, UniversalMixin):
    """Area"""

    # Nombre de la tabla
    __tablename__ = "areas"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    centro_trabajo_id = Column(Integer, ForeignKey("centros_trabajos.id"), index=True, nullable=False)
    centro_trabajo = relationship("CentroTrabajo", back_populates="areas")

    # Columnas
    nombre = Column(String(128), nullable=False)

    @property
    def centro_trabajo_clave(self):
        """Clave del centro de trabajo"""
        return self.centro_trabajo.clave

    @property
    def centro_trabajo_nombre(self):
        """Nombre del centro de trabajo"""
        return self.centro_trabajo.nombre

    def __repr__(self):
        """Representación"""
        return f"<Area {self.id}>"
