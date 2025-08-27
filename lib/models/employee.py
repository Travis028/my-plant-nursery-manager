from sqlalchemy import column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base
from sqlalchemy.orm import base

class Employee(Base):
    __tablename__ = 'employees'
    id = column(Integer, primary_key=True)
    name = column(String, nullable=False)
    role = column(String, nullable=False)

    def __repr__(self):
        return f"<Employee(name={self.name} - {self.role})>"
    
