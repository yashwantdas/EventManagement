from fastapi import FastAPI
from app.database import init_db
from app.routes import event_routes

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()  # Initialize the database

app.include_router(event_routes.router, prefix="/api")
