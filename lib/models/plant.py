from sqlalchemy import column, Integer, String, Float
from lib.database import Base

class Plant(Base):
    __tablename__ = 'plants'
    id = column(Integer, primary key=True)
    name = column(String, nullable=False)
    price = column(Float, nullable=False)
    pass