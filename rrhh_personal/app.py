"""
PJECZ RRHH Personal API Key
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from config.settings import get_settings


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

    # Paginación
    add_pagination(app)

    # Mensaje de Bienvenida
    @app.get("/")
    async def root():
        """Mensaje de Bienvenida"""
        return {"message": "Bienvenido a PJECZ RRHH Personal API Key. Esta API es para realizar operaciones con la base de datos de RRHH Personal. Se requiere tener una api-key para usarse."}

    # Entregar
    return app
