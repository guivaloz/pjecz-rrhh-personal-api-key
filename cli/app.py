"""
Command Line Interface
"""
import typer

from cli.db.app import app as db_app

app = typer.Typer()
app.add_typer(db_app, name="db")  # Inicializar y alimentar la base de datos


if __name__ == "__main__":
    app()
