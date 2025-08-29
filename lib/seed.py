from .database import Base, engine, Session
from . import Plant, Customer, Employee, Sale

def seed():
    # reset database
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = Session()

    plant1 = Plant(name="Rose", price=10.0)
    plant2 = Plant(name="Tulip", price=8.5)
    customer1 = Customer(name="Alice")
    employee1 = Employee(name="John Doe")

    session.add_all([plant1, plant2, customer1, employee1])
    session.commit()
    session.close()

    print("✅ Database seeded successfully!")
