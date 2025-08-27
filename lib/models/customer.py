from sqlalchemy import Column, Integer, String
from lib.database import Base
from sqlalchemy import column, Integer, String, Float


class customer(Base):
    __tablename__ = 'customers'
    id = column(Integer, primary_key=True)
    name = column(String, nullable=False)
    email = column(String, nullable=False)

    def __repr__(self):
        return f"<customer(name={self.name} - {self.email})>"
    