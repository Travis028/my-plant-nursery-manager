from lib.seed import seed
from lib.database import Session
from lib.models import Plant, Customer, Employee, Sale

def test_seed_creates_data():
    seed()
    session = Session()
    plants = session.query(Plant).all()
    customers = session.query(Customer).all()
    employees = session.query(Employee).all()
    sales = session.query(Sale).all()


    assert len(plants) > 0
    assert len(customers) > 0
    assert len(employees) > 0
    assert len(sales) > 0