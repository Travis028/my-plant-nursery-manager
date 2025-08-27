from sqlalchemy import column, Integer, String, Float
from lib.database import Base

class customer(Base):
    __tablename__ = 'customers'
    id = column(Integer, primary_key=True)
    name = column(String, nullable=False)
    email = column(String, nullable=False)

    