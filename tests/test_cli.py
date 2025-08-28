import builtins
from lib.database import Base, engine, Session
from lib.models import Plant
from lib.cli import add_plant, list_plants

def setup_function():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def test_add_and_list_plants(monkeypatch, capsys):
    session = Session()

    monkeypatch.setattr(builtins, "input", lambda _: "Lily" if _ == "Enter plant name: " else "20")
    add_plant(session)