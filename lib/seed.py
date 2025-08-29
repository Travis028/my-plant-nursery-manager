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
    
    # Create a sample sale
    sale = Sale(plant_id=plant1.id, customer_id=customer1.id, employee_id=employee1.id, quantity=2, total_price=plant1.price * 2)
    session.add(sale)
    session.commit()
    
    session.close()

    print("✅ Database seeded successfully!")
