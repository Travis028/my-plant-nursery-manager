from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///nursery.db", echo=False, future=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)