#___________________DONE BY: [FILL IN NAME]

# Import SQLAlchemy modules

# Define your database URL (replace with actual credentials)

# Create SQLAlchemy engine and sessionmaker

# Define Base using declarative_base()

# Create a function get_db() that opens and closes a database session using yield


# Just adding a new function
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
