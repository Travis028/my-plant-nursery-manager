from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base

class plant(base)
    __tablename__ = "plant"

    id = Column(Integer, primary_key=True)
    name = column(String, nullable=False)
    category = Column(String, nullable=False)
    price = column(Float, nullable=False)
    care_instructions = column(string)
    stock = Column(Integer, default=0)

    sales = relationship("sale", back_populates="plant")

    def __repr__(self):
        return f"<Plant(name={self.name}), category={self.category, price={self.price}, stock={self.stock}}>"

class customer(Base):
    __tablename__= "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone = Column(string)

sale = relationship("sale", back_populates="customer") 

def __repr__(self):
    return f"<Customer(name={self.name}, email={self.email}, phone={self.phone})>"


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey("plants.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    quantity = Column(Integer, nullable=False)



    plant = relationship("Plant", back_populates="sales")
    customer = relationship("Customer", back_populates="sales")
    employee = relationship("Employee", back_populates="sales")

    def __repr__(self):
        return f"<Sale(plant_id={self.plant_id}, customer_id={self.customer_id}, employee_id={self.employee_id}, quantity={self.quantity})>"
    