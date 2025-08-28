from lib.database import Base, engine, Session
from lib.models.plant import Plant
from lib.models.customer import Customer
from lib.models.employee import Employee
from lib.models.sale import Sale

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
