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


def test_create_plant(session):
    plant = Plant(name="Orchid", price=15)
    session.add(plant)
    session.commit()
    assert plant.id is not None
    assert plant.name == "Orchid"

def test_create_customer_and_employee(session):
    customer = Customer(name="TestUser")
    employee = Employee(name="Seller")
    session.add_all([customer, employee])
    session.commit()
    assert customer.id is not None
    assert employee.id is not None

def test_record_sale(session):
    plant = Plant(name="Cactus", price=7)
    customer = Customer(name="Buyer")
    employee = Employee(name="Cashier")
    session.add_all([plant, customer, employee])
    session.commit()
