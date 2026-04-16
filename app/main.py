from fastapi import FastAPI
from .database import engine, Base, SessionLocal
from .routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)