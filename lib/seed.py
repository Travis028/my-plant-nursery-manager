from datetime import date
from sqlalchemy.orm import sessionmaker
from lib.database import engine
from lib.models import Base, Plant, Customer, Employee, Sale


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


session.query(Sale).delete()
session.query(Plant).delete()
session.query(Customer).delete()
session.query(Employee).delete()

plants = [
    Plant(name="Rose", category="Flower", price=5.0, care_instructions="Water daily", stock=30),
    Plant(name="Tulip", category="Flower", price=3.0, care_instructions="Water every 2 days", stock=20),
    Plant(name="Aloe Vera", category="Succulent", price=7.5, care_instructions="Water weekly", stock=15),
]
session.add_all(plants)

customers = [
    Customer(name="Alice Johnson", email="alice@example.com", phone="123456789"),
    Customer(name="Bob Smith", email="bob@example.com", phone="987654321"),
]
session.add_all(customers)


employees = [
    Employee(name="Jane Doe", hire_date=date(2022, 5, 10)),
    Employee(name="Mark Lee", hire_date=date(2023, 1, 15)),
]
session.add_all(employees)

session.commit()
