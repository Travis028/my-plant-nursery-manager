from sqlalchemy import Column, Integer, String, event
from sqlalchemy.orm import relationship
from lib.database import Base
from typing import List

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    _name = Column("name", String, nullable=False)
    
    # Relationships
    sales = relationship("Sale", back_populates="employee")

    def __init__(self, name: str):
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or len(value.strip()) < 2:
            raise ValueError("Employee name must be at least 2 characters long")
        self._name = value.strip()

    @classmethod
    def get_all(cls, session):
        """Get all employees."""
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, employee_id):
        """Find an employee by ID."""
        return session.query(cls).filter_by(id=employee_id).first()
        
    @classmethod
    def find_by_name(cls, session, name: str):
        """Find employees by name (case-insensitive partial match)."""
        return session.query(cls).filter(cls._name.ilike(f"%{name}%")).all()

    def update(self, **kwargs):
        """Update employee attributes."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def delete(self, session):
        """Delete this employee and associated sales."""
        # Delete associated sales first
        for sale in self.sales:
            session.delete(sale)
        session.delete(self)
        session.commit()

    def get_sales(self, session):
        """Get all sales for this employee."""
        from .sale import Sale
        return session.query(Sale).filter_by(employee_id=self.id).all()

    def get_total_sales(self, session) -> float:
        """Get total sales amount for this employee."""
        from .sale import Sale
        total = session.query(Sale).filter_by(employee_id=self.id).with_entities(
            func.sum(Sale.total_price)
        ).scalar()
        return float(total) if total else 0.0

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.name}')>"

# Add validation before flush
@event.listens_for(Employee, 'before_insert')
@event.listens_for(Employee, 'before_update')
def validate_employee_data(mapper, connection, target):
    """Validate employee data before database operations."""
    if not target.name or len(target.name.strip()) < 2:
        raise ValueError("Employee name must be at least 2 characters long")