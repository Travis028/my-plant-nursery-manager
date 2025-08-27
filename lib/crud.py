
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



