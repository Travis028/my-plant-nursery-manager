from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .models import Plant, Customer, Employee, Sale
from typing import List, Optional, Type, TypeVar, Any
from decimal import Decimal

T = TypeVar('T')

def format_currency(value: float) -> str:
    """Format numeric value as currency."""
    return f"${value:,.2f}"

def get_all(session: Session, model: Type[T]) -> List[T]:
    """Get all records of a model."""
    return session.query(model).all()

def find_by_id(session: Session, model: Type[T], id: int) -> Optional[T]:
    """Find a record by ID."""
    return session.query(model).filter_by(id=id).first()

def delete(session: Session, model: Type[T], id: int) -> bool:
    """Delete a record by ID."""
    obj = find_by_id(session, model, id)
    if obj:
        session.delete(obj)
        session.commit()
        return True
    return False

def validate_plant_data(name: str, price: float) -> 'Tuple[bool, str]':
    """Validate plant data."""
    if not name or len(name.strip()) < 2:
        return False, "Name must be at least 2 characters long"
    if price <= 0:
        return False, "Price must be greater than 0"
    return True, ""

def validate_sale_data(plant_id: int, customer_id: int, employee_id: int, quantity: int) -> 'Tuple[bool, str]':
    """Validate sale data."""
    if quantity <= 0:
        return False, "Quantity must be greater than 0"
    if plant_id <= 0 or customer_id <= 0 or employee_id <= 0:
        return False, "Invalid ID provided"
    return True, ""

def get_related_sales(session: Session, model: Type[T], id: int) -> List[Sale]:
    """Get all sales related to a model instance."""
    if model == Customer:
        return session.query(Sale).filter_by(customer_id=id).all()
    elif model == Employee:
        return session.query(Sale).filter_by(employee_id=id).all()
    elif model == Plant:
        return session.query(Sale).filter_by(plant_id=id).all()
    return []
