from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, event, func
from sqlalchemy.orm import relationship, validates
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional, Dict, Any
import re

from lib.database import Base

class Employee(Base):
    """Employee model representing a nursery employee.
    
    Attributes:
        id: Primary key
        name: Employee's full name (required, min 2 chars)
        email: Employee's email (optional, must be valid format)
        phone: Employee's contact number (optional)
        created_at: Timestamp when record was created
        updated_at: Timestamp when record was last updated
    """
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    _name = Column("name", String(100), nullable=False, index=True)
    email = Column(String(120), unique=True, nullable=True, index=True)
    phone = Column(String(20), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, 
                       onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    sales = relationship("Sale", back_populates="employee", 
                        cascade="all, delete-orphan")

    def __init__(self, name: str, email: str = None, phone: str = None):
        """Initialize a new Employee instance.
        
        Args:
            name: Full name of the employee
            email: Email address (optional)
            phone: Contact number (optional)
        """
        self.name = name
        self.email = email
        self.phone = phone

    @property
    def name(self) -> str:
        """Get the employee's name."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Set the employee's name with validation.
        
        Args:
            value: The name to set
            
        Raises:
            ValueError: If name is empty or too short
        """
        if not value or len(value.strip()) < 2:
            raise ValueError("Employee name must be at least 2 characters long")
        self._name = value.strip()
        self.updated_at = datetime.utcnow()
        
    @validates('email')
    def validate_email(self, key: str, email: Optional[str]) -> Optional[str]:
        """Validate email format if provided.
        
        Args:
            key: The attribute name (automatically passed by SQLAlchemy)
            email: The email to validate
            
        Returns:
            The validated email (stripped and lowercased) or None
            
        Raises:
            ValueError: If email format is invalid
        """
        if email is None:
            return None
            
        email = email.strip().lower()
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise ValueError("Invalid email format")
            
        return email
    
    @validates('phone')
    def validate_phone(self, key: str, phone: Optional[str]) -> Optional[str]:
        """Validate phone number format if provided.
        
        Args:
            key: The attribute name (automatically passed by SQLAlchemy)
            phone: The phone number to validate
            
        Returns:
            The validated phone number (digits only) or None
        """
        if phone is None:
            return None
            
        # Remove all non-digit characters
        digits = re.sub(r'\D', '', phone)
        return digits if digits else None

    @classmethod
    def get_all(cls, session) -> List['Employee']:
        """Get all employees ordered by name.
        
        Args:
            session: SQLAlchemy session
            
        Returns:
            List[Employee]: List of all employees
        """
        try:
            return session.query(cls).order_by(cls._name).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Error fetching employees: {str(e)}")

    @classmethod
    def find_by_id(cls, session, employee_id: int) -> Optional['Employee']:
        """Find an employee by ID.
        
        Args:
            session: SQLAlchemy session
            employee_id: ID of the employee to find
            
        Returns:
            Optional[Employee]: Employee if found, None otherwise
            
        Raises:
            RuntimeError: If there's a database error
        """
        try:
            return session.query(cls).get(employee_id)
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Error finding employee: {str(e)}")
        
    @classmethod
    def find_by_name(cls, session, name: str) -> List['Employee']:
        """Find employees by name (case-insensitive partial match).
        
        Args:
            session: SQLAlchemy session
            name: Full or partial name to search for
            
        Returns:
            List[Employee]: List of matching employees
            
        Raises:
            RuntimeError: If there's a database error
        """
        if not name or not name.strip():
            return []
            
        try:
            search = f"%{name.strip()}%"
            return session.query(cls).filter(
                func.lower(cls._name).ilike(func.lower(search))
            ).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Error searching for employees: {str(e)}")

    def update(self, **kwargs) -> None:
        """Update employee attributes.
        
        Args:
            **kwargs: Attributes to update (name, email, phone)
            
        Raises:
            ValueError: If any validation fails
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()

    def delete(self, session) -> bool:
        """Delete this employee and cascade delete related sales.
        
        Args:
            session: SQLAlchemy session
            
        Returns:
            bool: True if deletion was successful
            
        Raises:
            RuntimeError: If there's a database error
        """
        try:
            session.delete(self)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Error deleting employee: {str(e)}")

    def get_sales(self, session) -> 'List':
        """Get all sales made by this employee.
        
        Args:
            session: SQLAlchemy session
            
        Returns:
            List[Sale]: List of sales made by this employee
            
        Raises:
            RuntimeError: If there's a database error
        """
        from .sale import Sale  # Avoid circular import
        try:
            return session.query(Sale).filter_by(employee_id=self.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Error fetching sales: {str(e)}")

    def get_total_sales(self, session) -> float:
        """Calculate total sales amount for this employee.
        
        Args:
            session: SQLAlchemy session
            
        Returns:
            float: Total sales amount
            
        Raises:
            RuntimeError: If there's a database error
        """
        from .sale import Sale  # Avoid circular import
        try:
            total = session.query(func.sum(Sale.total_price)).filter(
                Sale.employee_id == self.id
            ).scalar()
            return float(total or 0.0)
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Error calculating total sales: {str(e)}")

    def to_dict(self) -> Dict[str, Any]:
        """Convert employee details to a dictionary.
        
        Returns:
            dict: Dictionary containing employee details
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self) -> str:
        """String representation of the Employee.
        
        Returns:
            str: String representation
        """
        return f"<Employee(id={self.id}, name='{self.name}', email='{self.email}')>"

# Event listeners for validation
@event.listens_for(Employee, 'before_insert')
@event.listens_for(Employee, 'before_update')
def validate_employee_data(mapper, connection, target):
    """Validate employee data before database operations.
    
    Args:
        mapper: The mapper object
        connection: The database connection
        target: The Employee instance being validated
        
    Raises:
        ValueError: If validation fails
    """
    # Name validation
    if not target.name or len(target.name.strip()) < 2:
        raise ValueError("Employee name must be at least 2 characters long")
    
    # Email validation if provided
    if target.email and '@' not in target.email:
        raise ValueError("Invalid email format")
    
    # Phone validation if provided
    if target.phone and not target.phone.replace(' ', '').replace('-', '').replace('+', '').isdigit():
        raise ValueError("Phone number can only contain digits, spaces, hyphens, and plus sign")