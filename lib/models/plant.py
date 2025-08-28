from sqlalchemy import Column, Integer, String
from ..database import Base

class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Plant(id={self.id}, name='{self.name}', price={self.price})>"