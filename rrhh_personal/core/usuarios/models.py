"""
Usuarios, modelos
"""
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Usuario(Base, UniversalMixin):
    """Usuario"""

    # Nombre de la tabla
    __tablename__ = "usuarios"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    rol_id = Column(Integer, ForeignKey("roles.id"), index=True, nullable=False)
    rol = relationship("Rol", back_populates="usuarios")

    # Columnas
    nombres = Column(String(256), nullable=False)
    apellido_paterno = Column(String(256), nullable=False)
    apellido_materno = Column(String(256))
    telefono_celular = Column(String(256))
    email = Column(String(256))

    # Columnas que no deben ser expuestas
    api_key = Column(String(128), nullable=False)
    api_key_expiracion = Column(DateTime(), nullable=False)
    contrasena = Column(String(256), nullable=False)

    # Hijos
    bitacoras = relationship("Bitacora", back_populates="usuario")
    entradas_salidas = relationship("EntradaSalida", back_populates="usuario")

    @property
    def nombre(self):
        """Junta nombres, apellido_paterno y apellido materno"""
        return self.nombres + " " + self.apellido_paterno + " " + self.apellido_materno

    @property
    def rol_nombre(self):
        """Nombre del rol"""
        return self.rol.nombre

    @classmethod
    def find_by_identity(cls, identity):
        """Encontrar a un usuario por su correo electrónico"""
        return Usuario.query.filter(Usuario.email == identity).first()

    @property
    def is_active(self):
        """¿Es activo?"""
        return self.estatus == "A"

    @property
    def permissions(self):
        """Permisos"""
        return self.rol.permissions

    def can(self, perm):
        """¿Tiene permiso?"""
        return self.rol.has_permission(perm)

    def can_view(self, module):
        """¿Tiene permiso para ver?"""
        return self.rol.can_view(module)

    def __repr__(self):
        """Representación"""
        return f"<Usuario {self.email}>"
