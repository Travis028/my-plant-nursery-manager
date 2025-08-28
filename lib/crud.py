# lib/crud.py

from datetime import date
from lib.database import SessionLocal
from lib.models import Customer, Employee, Plant, Sale

# --- Customer CRUD ---
def add_customer(first_name, last_name, phone, email):
    with SessionLocal() as session:
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email)
        session.add(customer)
        session.commit()
        session.refresh(customer)
        return customer

def list_customers():
    with SessionLocal() as session:
        return session.query(Customer).all()

# --- Employee CRUD ---
def add_employee(first_name, last_name, hire_date=None):
    with SessionLocal() as session:
        if not hire_date:
            hire_date = date.today()
        employee = Employee(first_name=first_name, last_name=last_name, hire_date=hire_date)
        session.add(employee)
        session.commit()
        session.refresh(employee)
        return employee

def list_employees():
    with SessionLocal() as session:
        return session.query(Employee).all()

# --- Plant CRUD ---
def add_plant(name, species, price, care_instructions, inventory_count=0):
    with SessionLocal() as session:
        plant = Plant(
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

def list_plants():
    with SessionLocal() as session:
        return session.query(Plant).all()

# --- Sale CRUD ---
def add_sale(customer_id, employee_id, plant_id, quantity=1):
    with SessionLocal() as session:
        sale = Sale(
            sale_date=date.today(),
            customer_id=customer_id,
            employee_id=employee_id,
            plant_id=plant_id,
            quantity=quantity
        )

        # decrease inventory automatically
        plant = session.query(Plant).filter_by(id=plant_id).first()
        if plant:
            if plant.inventory_count >= quantity:
                plant.inventory_count -= quantity
            else:
                raise ValueError("Not enough inventory for this plant.")

        session.add(sale)
        session.commit()
        session.refresh(sale)
        return sale

def list_sales():
    with SessionLocal() as session:
        return session.query(Sale).all()