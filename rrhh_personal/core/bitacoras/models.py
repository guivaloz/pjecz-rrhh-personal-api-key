"""
Bitacoras, modelos
"""
from typing import OrderedDict

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Bitacora(Base, UniversalMixin):
    """Bitacora"""

    MODULOS = OrderedDict(
        [
            ("AREAS", "Áreas"),
            ("CURSOS", "Cursos"),
            ("DISTRITOS", "Distritos"),
            ("DOMICILIOS", "Domicilios"),
            ("FOTOGRAFIAS", "Fotografías"),
            ("NIVELES_ACADEMICOS", "Niveles Académicos"),
            ("CARRERAS", "Carreras"),
            ("PUESTOS", "Puestos"),
            ("USUARIOS", "Usuarios"),
            ("SISTEMAS", "Sistemas"),
            ("SISTEMAS_PERSONAS", "Acceso a Sistema"),
            ("MODULOS", "Módulos"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "bitacoras"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), index=True, nullable=False)
    usuario = relationship("Usuario", back_populates="bitacoras")

    # Columnas
    modulo = Column(Enum(*MODULOS, name="tipos_modulos", native_enum=False), index=True, nullable=False)
    descripcion = Column(String(256), nullable=False)
    url = Column(String(512), nullable=False, default="", server_default="")

    @property
    def modulo_nombre(self):
        """Nombre del modulo"""
        return self.modulo.nombre

    @property
    def usuario_nombre(self):
        """Nombre del usuario"""
        return self.usuario.nombre

    def __repr__(self):
        """Representación"""
        return f"<Bitacora {self.id}>"
