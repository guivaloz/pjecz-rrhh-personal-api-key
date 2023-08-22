"""
Permisos, modelos
"""


class Permiso:
    """Permiso tiene como constantes enteros de potencia dos"""

    VER_CATALOGOS = 1
    MODIFICAR_CATALOGOS = 2
    CREAR_CATALOGOS = 4

    VER_PERSONAL = 8
    MODIFICAR_PERSONAL = 16
    CREAR_PERSONAL = 32

    VER_CUENTAS = 64
    MODIFICAR_CUENTAS = 128
    CREAR_CUENTAS = 256

    VER_CAMPOS_ESPECIALES = 512

    def __repr__(self):
        """Representación"""
        return "<Permiso>"
