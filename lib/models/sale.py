from sqlalchemy import column, Integer, String, Float
from sqlalchemy.orm import relationship
from lib.database import Base

class Sale(Base):
    __tablename__ = 'sales'
    id = column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey("plants.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    quality = column(Integer, default=1)

    plant relationship("plant")
    customer relationship("customer")

    def __repr__(self):
        return f"<self {self.quality} x {self.plant.name} to {self.customer.name}>"



 