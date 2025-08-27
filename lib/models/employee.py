from sqlalchemy import column, Integer, String, Float
from sqlalchemy.orm import base

class Employee(Base):
    __tablename__ = 'employees'
    id = column(Integer, primary_key=True)
    name = column(String, nullable=False)
    role = column(String, nullable=False)