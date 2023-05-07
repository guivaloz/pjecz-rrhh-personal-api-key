"""
Inicializar la base de datos
"""
import rich
import typer

from sqlalchemy_utils import database_exists, create_database

from config.settings import get_settings
from lib.database import get_db, get_engine, Base

from rrhh_personal.core.acciones.models import Accion
from rrhh_personal.core.bitacoras.models import Bitacora
from rrhh_personal.core.modulos.models import Modulo
from rrhh_personal.core.permisos.models import Permiso
from rrhh_personal.core.roles.models import Rol
from rrhh_personal.core.usuarios.models import Usuario
from rrhh_personal.core.usuarios_acciones.models import UsuarioAccion
from rrhh_personal.core.usuarios_roles.models import UsuarioRol

app = typer.Typer()

settings = get_settings()


@app.command()
def inicializar():
    """Inicializar la base de datos"""
    rich.print("Inicializando la base de datos...")

    # Si no existe, crear la base de datos
    engine = get_engine(settings)
    if not database_exists(engine.url):
        create_database(engine.url)

    # Crear tablas
    Base.metadata.create_all(bind=engine)

    # Mensaje de éxito
    if database_exists(engine.url):
        rich.print("[bold green]Base de datos creada con éxito[/bold green]")
    else:
        rich.print("[bold red]No se pudo crear la base de datos[/bold red]")


@app.command()
def alimentar():
    """Alimentar los datos iniciales"""
    rich.print("Alimentando la base de datos...")
