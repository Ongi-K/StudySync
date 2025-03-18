"""
1. Import and initialize FastAPI
2. Include router or endpoints
3. Configure middleware if needed
4. Start the app with uvicorn or similar
"""

from fastapi import FastAPI
# from .routes import user_routes  # Example router

app = FastAPI()

# 1. Attach routers or endpoints
# app.include_router(user_routes, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    """
    Basic root endpoint to confirm server runs.
    Returns a hello message.
    """
    return {"message": "Welcome to StudySync!"}
