
from fastapi import FastAPI
from .routes import router
from .db_models import BookTable
from .database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Bookshelf API"}



def seed_data():
    db = SessionLocal()

    if db.query(BookTable).count() == 0:
        books = [
            BookTable(title="Atomic Habits", author="James Clear", year=2018, rating=4.5),
            BookTable(title="Sapiens", author="Yuval Noah Harari", year=2011, rating=4.8),
            BookTable(title="The Alchemist", author="Paulo Coelho", year=1988, rating=4.2),
        ]

        db.add_all(books)
        db.commit()

    db.close()


@app.on_event("startup")
def startup_event():
    seed_data()    