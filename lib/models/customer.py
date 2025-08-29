from sqlalchemy import Column, Integer, String, event
from sqlalchemy.orm import relationship
from lib.database import Base
from typing import List

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    _name = Column("name", String, nullable=False)
    
    # Relationships
    sales = relationship("Sale", back_populates="customer")

    def __init__(self, name: str):
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or len(value.strip()) < 2:
            raise ValueError("Customer name must be at least 2 characters long")
        self._name = value.strip()

    @classmethod
    def get_all(cls, session):
        """Get all customers."""
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, customer_id):
        """Find a customer by ID."""
        return session.query(cls).filter_by(id=customer_id).first()
        
    @classmethod
    def find_by_name(cls, session, name: str):
        """Find customers by name (case-insensitive partial match)."""
        return session.query(cls).filter(cls._name.ilike(f"%{name}%")).all()

    def update(self, **kwargs):
        """Update customer attributes."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def delete(self, session):
        """Delete this customer and associated sales."""
        # Delete associated sales first
        for sale in self.sales:
            session.delete(sale)
        session.delete(self)
        session.commit()

    def get_sales(self, session):
        """Get all sales for this customer."""
        from .sale import Sale
        return session.query(Sale).filter_by(customer_id=self.id).all()

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}')>"

# Add validation before flush
@event.listens_for(Customer, 'before_insert')
@event.listens_for(Customer, 'before_update')
def validate_customer_data(mapper, connection, target):
    """Validate customer data before database operations."""
    if not target.name or len(target.name.strip()) < 2:
        raise ValueError("Customer name must be at least 2 characters long")