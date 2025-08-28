from datetime import date
from sqlalchemy.orm import sessionmaker
from lib.database import engine
from lib.models import Base, Plant, Customer, Employee, Sale


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


session.query(Sale).delete()
session.query(Plant).delete()
session.query(Customer).delete()
session.query(Employee).delete()


