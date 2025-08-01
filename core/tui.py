from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from core.database.db import SessionLocal
from core.database.models import Person, Username
from core.workflows.username_inspect import inspect_username
import typer

session = PromptSession()

def list_people():
    db = SessionLocal()
    people = db.query(Person).all()
    for p in people:
        typer.echo(f"{p.id}: {p.full_name} ({p.alias}) – {p.nationality}")
    db.close()

def add_person():
    name = session.prompt("Full name: ")
    alias = session.prompt("Alias (optional): ")
    nationality = session.prompt("Nationality (default Unknown): ") or "Unknown"
    db = SessionLocal()
    p = Person(full_name=name, alias=alias, nationality=nationality)
    db.add(p); db.commit(); db.close()
    typer.echo(f"👤 Added {name}.")

def search_person():
    db = SessionLocal()
    names = [p.full_name for p in db.query(Person).all()]
    db.close()
    completer = WordCompleter(names, ignore_case=True)
    name = session.prompt("Search name: ", completer=completer)
    db = SessionLocal()
    person = db.query(Person).filter(Person.full_name.ilike(f"%{name}%")).first()
    if not person:
        typer.echo("❌ No match.")
    else:
        typer.echo(f"👤 {person.full_name} (Alias: {person.alias}, Nationality: {person.nationality})")
        for phone in person.phones:
            typer.echo(f"   📞 {phone.number}")
        for email in person.emails:
            typer.echo(f"   📧 {email.email}")
        for uname in person.usernames:
            typer.echo(f"   🔑 {uname.username} on {uname.platform}")
    db.close()

def username_inspect():
    username = session.prompt("Username to inspect: ")
    inspect_username(username)

def run():
    while True:
        typer.echo("\n[TUI] Choose an action:")
        typer.echo(" 1. List people")
        typer.echo(" 2. Add person")
        typer.echo(" 3. Search person")
        typer.echo(" 4. Inspect username")
        typer.echo(" 5. Quit")
        choice = session.prompt("> ")
        if choice == '1':
            list_people()
        elif choice == '2':
            add_person()
        elif choice == '3':
            search_person()
        elif choice == '4':
            username_inspect()
        elif choice == '5':
            break
        else:
            typer.echo("❗ Invalid choice.")

def main():
    import typer as _typer
    _typer.run(run)
