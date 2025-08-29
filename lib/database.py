import os
from contextlib import contextmanager
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from sqlalchemy.exc import SQLAlchemyError

# Get database URL from environment variable or use default
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///nursery.db')

# Configure engine with connection pooling and other settings
engine = create_engine(
    DATABASE_URL,
    echo=bool(os.environ.get('SQL_ECHO', False)),
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=3600
)

# Create a thread-safe session factory
session_factory = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Session = scoped_session(session_factory)

# Base class for all models
Base = declarative_base()
Base.query = Session.query_property()

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    finally:
        session.close()

# Enable foreign key support for SQLite
if 'sqlite' in DATABASE_URL:
    @event.listens_for(engine, 'connect')
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute('PRAGMA foreign_keys=ON')
        cursor.close()

def init_db():
    """Initialize the database by creating all tables.
    
    Call this function when the application starts.
    """
    Base.metadata.create_all(bind=engine)

def drop_db():
    """Drop all tables in the database.
    
    WARNING: This will delete all data!
    """
    Base.metadata.drop_all(bind=engine)