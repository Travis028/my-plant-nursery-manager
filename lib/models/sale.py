
from datetime import datetime
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, event, func
from sqlalchemy.orm import relationship
from lib.database import Base
from typing import Optional

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships with back_populates
    plant = relationship("Plant", back_populates="sales")
    customer = relationship("Customer", back_populates="sales")
    employee = relationship("Employee", back_populates="sales")

    def __init__(self, plant_id: int = None, customer_id: int = None, employee_id: int = None,
                 plant=None, customer=None, employee=None, quantity: int = 1, 
                 total_price: Optional[float] = None):
        """Initialize a new Sale instance.
        
        Args:
            plant_id: ID of the plant (alternative to plant object)
            customer_id: ID of the customer (alternative to customer object)
            employee_id: ID of the employee (alternative to employee object)
            plant: Plant object (alternative to plant_id)
            customer: Customer object (alternative to customer_id)
            employee: Employee object (alternative to employee_id)
            quantity: Number of items sold (default: 1)
            total_price: Total price (calculated if not provided)
        """
        if plant is not None:
            self.plant = plant
        elif plant_id is not None:
            self.plant_id = plant_id
            
        if customer is not None:
            self.customer = customer
        elif customer_id is not None:
            self.customer_id = customer_id
            
        if employee is not None:
            self.employee = employee
        elif employee_id is not None:
            self.employee_id = employee_id
            
        self.quantity = quantity
        self.total_price = total_price if total_price is not None else 0.0

    @classmethod
    def create_sale(cls, session, plant_id: int, customer_id: int, 
                   employee_id: int, quantity: int = 1) -> 'Sale':
        """Create a new sale with validation."""
        from .plant import Plant
        
        plant = Plant.find_by_id(session, plant_id)
        if not plant:
            raise ValueError("Invalid plant ID")
            
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
            
        total_price = plant.price * quantity
        
        sale = cls(
            plant_id=plant_id,
            customer_id=customer_id,
            employee_id=employee_id,
            quantity=quantity,
            total_price=total_price
        )
        
        session.add(sale)
        session.commit()
        return sale

    @classmethod
    def get_all(cls, session):
        """Get all sales with related data."""
        return session.query(cls).options(
            relationship('Plant'),
            relationship('Customer'),
            relationship('Employee')
        ).all()

    @classmethod
    def find_by_id(cls, session, sale_id):
        """Find a sale by ID with related data."""
        return session.query(cls).options(
            relationship('Plant'),
            relationship('Customer'),
            relationship('Employee')
        ).filter_by(id=sale_id).first()

    @classmethod
    def get_sales_by_date_range(cls, session, start_date: datetime, end_date: datetime):
        """Get all sales within a date range."""
        return session.query(cls).filter(
            cls.created_at.between(start_date, end_date)
        ).all()

    def delete(self, session):
        """Delete this sale."""
        session.delete(self)
        session.commit()

    def __repr__(self):
        return (
            f"<Sale(id={self.id}, "
            f"plant='{self.plant.name if self.plant else 'N/A'}', "
            f"customer='{self.customer.name if self.customer else 'N/A'}', "
            f"employee='{self.employee.name if self.employee else 'N/A'}')"
        )

# Add validation before flush
@event.listens_for(Sale, 'before_insert')
@event.listens_for(Sale, 'before_update')
def validate_sale_data(mapper, connection, target):
    """Validate sale data before database operations."""
    if not all([target.plant_id, target.customer_id, target.employee_id]):
        raise ValueError("Plant, customer, and employee IDs are required")
    if target.quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    if target.total_price < 0:
        raise ValueError("Total price cannot be negative")