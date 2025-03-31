#___________________DONE BY: [FILL IN NAME]

# Import necessary FastAPI modules

# Import database engine and Base class

# Import routers from routes directory

# Create FastAPI app instance

# Create all tables (Base.metadata.create_all)

# Include user routes with app.include_router(...)
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/matches/")
def get_matches(location: str, db: Session = Depends(database.get_db)):
    return crud.get_matches_by_location(db=db, location=location)

@app.get("/")
def read_root():
    return {"message": "StudySync API is live 🎉"}

