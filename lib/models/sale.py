
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey("plants.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))

    plant = relationship("Plant")
    customer = relationship("Customer")
    employee = relationship("Employee")

    def __repr__(self):
        return f"<Sale(id={self.id}, plant={self.plant.name}, customer={self.customer.name}, employee={self.employee.name})>"