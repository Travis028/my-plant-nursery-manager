from .database import Base, Session, engine
from .models import Plant, Customer, Employee, Sale
from .helpers import *

# Re-export common items
__all__ = [
    # Database
    'Base', 'Session', 'engine',
    
    # Models
    'Plant', 'Customer', 'Employee', 'Sale',
    
    # Helpers
    'format_currency', 'get_all', 'find_by_id', 'delete',
    'validate_plant_data', 'validate_sale_data', 'get_related_sales'
]

# Initialize database
def init_db():
    """Initialize the database with tables."""
    Base.metadata.create_all(bind=engine)

# Import after models are defined to avoid circular imports
from . import helpers  # noqa
