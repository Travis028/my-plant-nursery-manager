from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///nursery.db')
Session = sessionmaker(bind=engine)
Session = Session()
Base = declarative_base()