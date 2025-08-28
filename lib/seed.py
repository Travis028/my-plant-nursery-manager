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

