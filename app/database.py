"""
1. Import necessary libraries (SQLAlchemy, etc.)
2. Read DB connection info (URL, credentials)
3. Create an engine for Postgres
4. Initialize a session factory
5. Provide a helper to get DB session
"""

# Example placeholder imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. DB connection string, e.g. from environment variables
DATABASE_URL = "postgresql://user:password@localhost/studysync_db"

# 2. Create engine
engine = create_engine(DATABASE_URL)

# 3. Configure session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Yields a database session.
    Make sure to close it after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
