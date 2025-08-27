
from datatime import data
from lib.database import SessionLocal
from lib.models import customer, Employee, Plant, sale

#-----customer CRUD operations-----

def add_customer(first_name, last_name, email):
    with SessionLocal() as session:
        customer = customer(first_name=first_name, last_name=last_name, email=email)
        session.add(customer)
        session.commit()
        session.refresh(customer)
        return customer
    
def list_customers():
    with SessionLocal() session:
        return session.query(customer).all()
    
#-----plant CRUD operations-----

def add_plant(name, species, price, care_instructions, inventory_count=0):
    with SessionLocal() as session:
        plant = plant(
            name=name,
            species=species,
            price=price,
            care_instructions=care_instructions,
            inventory_count=inventory_count
        )

        session.add(plant)
        session.commit()
        session.refresh(plant)
        return plant

