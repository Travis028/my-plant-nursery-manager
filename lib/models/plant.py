from sqlalchemy import column, Integer, String, Float
from lib.database import Base

class Plant(Base):
    __tablename__ = 'plants'
    id = Column(Integer, primary_key=True)
    name = column(String, nullable=False)
    price = column(Float, nullable=False)

    def __repr__(self):
        return f"<plant(name={self.name} - ${self.price})>"
    
    