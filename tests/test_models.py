import pytest
from lib.database import Base, engine, Session
from lib.models import Plant, Customer, Employee, Sale

@pytest.fixture(scope="function")
def session():
    # Fresh test DB
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.close()
