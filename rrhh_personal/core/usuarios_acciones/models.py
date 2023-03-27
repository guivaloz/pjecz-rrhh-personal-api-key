"""
Usuarios-Acciones, modelos
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class UsuarioAccion(Base, UniversalMixin):
    """UsuarioAccion"""

    # Nombre de la tabla
    __tablename__ = "usuarios_acciones"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    accion_id = Column(Integer, ForeignKey("acciones.id"), index=True, nullable=False)
    accion = relationship("Accion", back_populates="acciones_usuarios")
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), index=True, nullable=False)
    usuario = relationship("Usuario", back_populates="usuarios_roles")

    # Columnas
    descripcion = Column(String(256), nullable=False)

    def __repr__(self):
        """Representación"""
        return f"<UsuarioAccion {self.id}>"
