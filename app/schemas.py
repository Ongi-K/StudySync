#___________________DONE BY: [FILL IN NAME]

# Import Pydantic BaseModel and EmailStr

# Define UserCreate Pydantic model with:
# - name
# - email
# - city
# - availability
# - year_of_study
# - tech_stack

# Define UserOut Pydantic model with:
# - id
# - all other fields above

# Add Config class with orm_mode = True

from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    location: str
    status: str
    tech_stack: str
    year: str
    social_link: str

class UserOut(UserCreate):
    id: int

    class Config:
        orm_mode = True
