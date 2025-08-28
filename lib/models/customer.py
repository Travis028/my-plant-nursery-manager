from sqlalchemy import Column, Integer, String
from ..database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}')>"