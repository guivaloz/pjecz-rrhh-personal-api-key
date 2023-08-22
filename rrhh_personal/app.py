"""
PJECZ RRHH Personal API Key
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from config.settings import get_settings

from .v4.areas.paths import areas
from .v4.bitacoras.paths import bitacoras
from .v4.centros_trabajos.paths import centros_trabajos
from .v4.entradas_salidas.paths import entradas_salidas
from .v4.modulos.paths import modulos
from .v4.roles.paths import roles
from .v4.usuarios.paths import usuarios


def create_app() -> FastAPI:
    """Crea la aplicación FastAPI"""

    # FastAPI
    app = FastAPI(
        title="PJECZ RRHH Personal API Key",
        description="Bienvenido a PJECZ RRHH Personal API Key. Esta API es para realizar operaciones con la base de datos de RRHH Personal. Se requiere tener una api-key para usarse.",
        docs_url="/docs",
        redoc_url=None,
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
    app.include_router(areas)
    app.include_router(bitacoras)
    app.include_router(centros_trabajos)
    app.include_router(entradas_salidas)
    app.include_router(modulos)
    app.include_router(roles)
    app.include_router(usuarios)

    # Paginación
    add_pagination(app)

    # Mensaje de Bienvenida
    @app.get("/")
    async def root():
        """Mensaje de Bienvenida"""
        return {"message": "Bienvenido a PJECZ RRHH Personal API Key. Esta API es para realizar operaciones con la base de datos de RRHH Personal. Se requiere tener una api-key para usarse."}

    # Entregar
    return app
