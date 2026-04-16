from fastapi import FastAPI
from .database import engine, Base
from .routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Bookshelf API",
        "docs": "/docs"
    }

app.include_router(router)