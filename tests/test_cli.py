import builtins
from lib.database import Base, engine, Session
from lib import Plant
from lib.cli import add_plant, list_plants

def setup_function():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def test_add_and_list_plants(monkeypatch, capsys):
    session = Session()

    monkeypatch.setattr(builtins, "input", lambda _: "Lily" if _ == "Enter plant name: " else "20")
    add_plant(session)

    plants = session.query(Plant).all()
    assert len(plants) == 1
    assert plants[0].name == "Lily"
    assert plants[0].price == 20

    list_plants(session)
    captured = capsys.readouterr()
    assert "Lily" in captured.out