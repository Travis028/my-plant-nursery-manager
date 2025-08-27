import click_
 
from lib.database import Base, engine, Session
from lib.models.plant import Plant
from lib.models.customer import customer
from lib.models.sale import Sale
from lib.models.employee import Employee

Base.metadata.create_all(engine)