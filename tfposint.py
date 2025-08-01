# tfposint.py

import typer
from core.database.db import init_db, SessionLocal, engine
from core.database.models import Base
from seed_data import seed_db
from core import tui

app = typer.Typer()

@app.command("init-db")
def init_db_cmd():
    init_db()
    typer.echo("✅ Database schema initialized.")

@app.command("wipe-db")
def wipe_db_cmd():
    Base.metadata.drop_all(bind=engine)
    typer.echo("🗑️ Database schema dropped.")

@app.command("wipe-data")
def wipe_data_cmd():
    session = SessionLocal()
    for table in reversed(Base.metadata.sorted_tables):
        session.execute(table.delete())
    session.commit()
    session.close()
    typer.echo("🧹 All data wiped from database.")

@app.command("seed-db")
def seed_db_cmd():
    """Populate database with seed data."""
    seed_db()
    typer.echo("🌱 Seed data loaded.")

@app.command("tui")
def tui_cmd():
    """Launch the interactive TUI."""
    tui.run()

if __name__ == "__main__":
    app()
