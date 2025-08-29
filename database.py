# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DB_URL = "sqlite:///budget.db"


engine = create_engine(DB_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, future=True)

def init_db():
    """Create the SQLite DB file and tables (if they don't exist)."""
    Base.metadata.create_all(engine)

