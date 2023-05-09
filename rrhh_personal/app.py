"""
PJECZ RRHH Personal API Key
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from config.settings import get_settings

from .v3.acciones.paths import acciones
from .v3.bitacoras.paths import bitacoras
from .v3.modulos.paths import modulos
from .v3.permisos.paths import permisos
from .v3.roles.paths import roles
from .v3.usuarios.paths import usuarios
from .v3.usuarios_acciones.paths import usuarios_acciones
from .v3.usuarios_roles.paths import usuarios_roles


def create_app() -> FastAPI:
    """Crea la aplicación FastAPI"""

    # FastAPI
    app = FastAPI(
        title="PJECZ RRHH Personal API Key",
        description="Bienvenido a PJECZ RRHH Personal API Key. Esta API es para realizar operaciones con la base de datos de RRHH Personal. Se requiere tener una api-key para usarse.",
    )

    # CORSMiddleware
    settings = get_settings()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins.split(","),
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Rutas
    app.include_router(acciones)
    app.include_router(bitacoras)
    app.include_router(modulos)
    app.include_router(permisos)
    app.include_router(roles)
    app.include_router(usuarios)
    app.include_router(usuarios_acciones)
    app.include_router(usuarios_roles)

    # Paginación
    add_pagination(app)

    # Mensaje de Bienvenida
    @app.get("/")
    async def root():
        """Mensaje de Bienvenida"""
        return {"message": "Bienvenido a PJECZ RRHH Personal API Key. Esta API es para realizar operaciones con la base de datos de RRHH Personal. Se requiere tener una api-key para usarse."}

    # Entregar
    return app
