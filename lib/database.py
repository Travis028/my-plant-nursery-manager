from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Base class for models
Base = declarative_base()

# Database connection
engine = create_engine("sqlite:///nursery.db", echo=True)

# Session factory
SessionLocal = sessionmaker(bind=engine)