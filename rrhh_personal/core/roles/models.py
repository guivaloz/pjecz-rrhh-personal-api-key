"""
Roles, modelos
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin

from ...core.permisos.models import Permiso


class Rol(Base, UniversalMixin):
    """Rol"""

    # Nombre de la tabla
    __tablename__ = "roles"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    nombre = Column(String(256), unique=True, nullable=False)
    permiso = Column(Integer, nullable=False)

    # Hijos
    usuarios = relationship("Usuario", back_populates="rol")

    def has_permission(self, perm):
        """¿Tiene el permiso dado?"""
        return self.permiso & perm == perm

    def can_view(self, module):
        """¿Tiene permiso para ver?"""
        if module in ("BITACORAS", "ENTRADAS_SALIDAS", "MODULOS", "ROLES", "TAREAS"):
            return self.has_permission(Permiso.VER_CUENTAS)
        if module in ("AREAS", "CENTROS_TRABAJOS"):
            return self.has_permission(Permiso.VER_CATALOGOS)
        return True

    @property
    def permissions(self):
        """Permisos"""
        return {
            "AREAS": self.has_permission(Permiso.VER_CATALOGOS),
            "BITACORAS": self.has_permission(Permiso.VER_CUENTAS),
            "CENTROS_TRABAJOS": self.has_permission(Permiso.VER_CATALOGOS),
            "ENTRADAS_SALIDAS": self.has_permission(Permiso.VER_CUENTAS),
            "MODULOS": self.has_permission(Permiso.VER_CUENTAS),
            "PERSONAS": self.has_permission(Permiso.VER_PERSONAL),
            "ROLES": self.has_permission(Permiso.VER_CUENTAS),
            "USUARIOS": self.has_permission(Permiso.VER_CUENTAS),
        }

    def __repr__(self):
        """Representación"""
        return f"<Rol {self.nombre}>"
