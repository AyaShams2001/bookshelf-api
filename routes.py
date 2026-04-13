from fastapi import APIRouter, HTTPException
from typing import Optional
from models import Book
from database_sql import SessionLocal
from models_sql import BookTable
from sqlalchemy import func

router = APIRouter()

@router.get("/books")
def get_books(skip: int = 0, limit: int = 10):
    db = SessionLocal()

    books = db.query(BookTable).offset(skip).limit(limit).all()
    total = db.query(BookTable).count()

    db.close()

    return {
        "total": total,
        "data": [
            {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "rating": book.rating
            }
            for book in books
        ]
    }

@router.post("/books")
def add_book(book: Book):
    db = SessionLocal()

    new_book = BookTable(
        title=book.title,
        author=book.author,
        year=book.year,
        rating=book.rating
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    db.close()

    return {
        "id": new_book.id,
        "title": new_book.title,
        "author": new_book.author,
        "year": new_book.year,
        "rating": new_book.rating
    }

@router.get("/books/search")
def search_books(author: str):
    db = SessionLocal()

    books = db.query(BookTable).filter(BookTable.author.ilike(f"%{author}%")).all()

    db.close()

    return [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "rating": book.rating
        }
        for book in books
    ]

@router.get("/books/title-search")
def search_books_by_title(title: str):
    db = SessionLocal()

    books = db.query(BookTable).filter(BookTable.title.ilike(f"%{title}%")).all()

    db.close()

    return [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "rating": book.rating
        }
        for book in books
    ]

@router.get("/books/filter")
def filter_books(title: str = "", author: str = ""):
    db = SessionLocal()

    query = db.query(BookTable)

    if title:
        query = query.filter(BookTable.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(BookTable.author.ilike(f"%{author}%"))

    books = query.all()

    db.close()

    return [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "rating": book.rating
        }
        for book in books
    ]

@router.get("/books/sort")
def sort_books(by: str = "title", order: str = "asc"):
    db = SessionLocal()

    if by == "title":
        query = db.query(BookTable).order_by(BookTable.title)
    elif by == "year":
        query = db.query(BookTable).order_by(BookTable.year)
    else:
        db.close()
        return {"error": "Invalid sort field"}

    if order == "desc":
        query = query.order_by(BookTable.title.desc() if by == "title" else BookTable.year.desc())

    books = query.all()

    db.close()

    return [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "rating": book.rating
        }
        for book in books
    ]

@router.get("/books/top-rated")
def get_top_rated_books(min_rating: float = 4.5):
    db = SessionLocal()

    books = db.query(BookTable).filter(BookTable.rating >= min_rating).all()

    db.close()

    return [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "rating": book.rating
        }
        for book in books
    ]

@router.get("/books/stats")
def get_book_stats():
    db = SessionLocal()

    total_books = db.query(BookTable).count()
    average_rating = db.query(func.avg(BookTable.rating)).scalar() or 0
    db.close()

    if total_books == 0:
        return {
            "total_books": 0,
            "average_rating": 0
        }
    
    return {
        "total_books": total_books,
        "average_rating": round(average_rating, 2)
    }




@router.get("/books/recent")
def get_recent_books(
    year: Optional[int] = None,
    min_rating: Optional[float] = None,
    order: str = "desc",
    skip: int = 0,
    limit: int = 10
):
    db = SessionLocal()

    query = db.query(BookTable)

    if year is not None:
        query = query.filter(BookTable.year >= year)

    if min_rating is not None:
        query = query.filter(BookTable.rating >= min_rating)

    total = query.count()

    if order == "desc":
        query = query.order_by(BookTable.year.desc())
    else:
        query = query.order_by(BookTable.year)

    books = query.offset(skip).limit(limit).all()

    db.close()

    return {
        "total": total,
        "data": [
            {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "rating": book.rating
            }
            for book in books
        ]
    }


@router.get("/books/{book_id}")
def get_book(book_id: int):
    db = SessionLocal()

    book = db.query(BookTable).filter(BookTable.id == book_id).first()

    db.close()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "rating": book.rating
    }

@router.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    db = SessionLocal()

    book = db.query(BookTable).filter(BookTable.id == book_id).first()

    if not book:
        db.close()
        raise HTTPException(status_code=404, detail="Book not found")

    book.title = updated_book.title
    book.author = updated_book.author
    book.year = updated_book.year
    book.rating = updated_book.rating

    db.commit()
    db.refresh(book)
    db.close()

    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "rating": book.rating
    }


@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    db = SessionLocal()

    book = db.query(BookTable).filter(BookTable.id == book_id).first()

    if not book:
        db.close()
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    db.close()

    return {"message": "Book deleted successfully"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()