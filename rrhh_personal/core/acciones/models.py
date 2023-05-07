"""
Acciones, modelos
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Accion(Base, UniversalMixin):
    """Accion"""

    # Nombre de la tabla
    __tablename__ = "acciones"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    clave = Column(String(16), nullable=False, unique=True)
    descripcion = Column(String(256), nullable=False)

    # Hijos
    usuarios_acciones = relationship("UsuarioAccion", back_populates="accion")

    def __repr__(self):
        """Representación"""
        return f"<Accion {self.id}>"
