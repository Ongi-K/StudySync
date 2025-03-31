#___________________DONE BY: [FILL IN NAME]

# Import SQLAlchemy Column types and Base

# Define the User model:
# - id (Integer, primary key)
# - name (String, required)
# - email (String, unique, required)
# - city (String)
# - availability (String)
# - year_of_study (Integer)
# - tech_stack (String)
from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    location = Column(String)
    status = Column(String)
    tech_stack = Column(String)
    year = Column(String)
    social_link = Column(String)
