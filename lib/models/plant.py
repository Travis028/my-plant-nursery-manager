from sqlalchemy import Column, Integer, String, Float, ForeignKey, event
from sqlalchemy.orm import relationship, validates
from lib.database import Base
from decimal import Decimal

class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True)
    _name = Column("name", String, nullable=False)
    _price = Column("price", Integer, nullable=False)
    
    # Relationships
    sales = relationship("Sale", back_populates="plant")

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or len(value.strip()) < 2:
            raise ValueError("Plant name must be at least 2 characters long")
        self._name = value.strip()

    @property
    def price(self) -> float:
        return float(self._price) / 100  # Convert cents to dollars

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        self._price = int(round(value * 100))  # Store as cents to avoid floating point issues

    @classmethod
    def get_all(cls, session):
        """Get all plants."""
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, plant_id):
        """Find a plant by ID."""
        return session.query(cls).filter_by(id=plant_id).first()

    def update(self, **kwargs):
        """Update plant attributes."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def delete(self, session):
        """Delete this plant."""
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"<Plant(id={self.id}, name='{self.name}', price={self.price})>"

# Add validation before flush
@event.listens_for(Plant, 'before_insert')
@event.listens_for(Plant, 'before_update')
def validate_plant_data(mapper, connection, target):
    """Validate plant data before database operations."""
    if not target.name or len(target.name.strip()) < 2:
        raise ValueError("Plant name must be at least 2 characters long")
    if target.price <= 0:
        raise ValueError("Price must be greater than 0")