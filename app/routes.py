from fastapi import APIRouter, HTTPException
from typing import Optional, List
from .database import SessionLocal
from .db_models import BookTable
from .schemas import Book, BookResponse , BooksListResponse , BookStatsResponse, MessageResponse
from . import crud

router = APIRouter()

@router.get("/books/sort", response_model=List[BookResponse])
def sort_books(by: str = "title", order: str = "asc"):
    db = SessionLocal()
    try:
        books = crud.sort_books(db, by, order)

        if books is None:
            raise HTTPException(status_code=400, detail="Invalid sort field")

        return books
    finally:
        db.close()

@router.get("/books", response_model=BooksListResponse)
def get_books(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    try:
        books, total = crud.get_books(db, skip, limit)
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
    finally:
        db.close()


@router.post("/books", response_model=BookResponse)
def add_book(book: Book):
    db = SessionLocal()
    try:
        new_book = crud.create_book(db, book)

        return {
           book
        }
    finally:
        db.close()


@router.get("/books/search", response_model=List[BookResponse])
def search_books(author: str):
    db = SessionLocal()
    try:
        books = crud.get_books_by_author(db, author)
        return books
    finally:
        db.close()


@router.get("/books/title-search", response_model=List[BookResponse])
def search_books_by_title(title: str):
    db = SessionLocal()
    try:
        books = crud.get_books_by_title(db, title)
        return books
    finally:
        db.close()


@router.get("/books/filter", response_model=List[BookResponse])
def filter_books(title: str = "", author: str = ""):
    db = SessionLocal()
    try:
        books = crud.filter_books(db, title, author)
        return books
    finally:
        db.close()


@router.get("/books/filter", response_model=List[BookResponse])
def filter_books(title: str = "", author: str = ""):
    db = SessionLocal()
    try:
        books = crud.filter_books(db, title, author)
        return books
    finally:
        db.close()


@router.get("/books/top-rated", response_model=List[BookResponse])
def get_top_rated_books(min_rating: float = 4.5):
    db = SessionLocal()
    try:
        books = crud.get_top_rated_books(db, min_rating)
        return books
    finally:
        db.close()


@router.get("/books/stats", response_model=BookStatsResponse)
def get_book_stats():
    db = SessionLocal()
    try:
        return crud.get_book_stats(db)
    finally:
        db.close()



@router.get("/books/recent", response_model=BooksListResponse)
def get_recent_books(
    year: Optional[int] = None,
    min_rating: Optional[float] = None,
    order: str = "desc",
    skip: int = 0,
    limit: int = 10
):
    db = SessionLocal()
    try:
        books, total = crud.get_recent_books(
            db, year, min_rating, order, skip, limit
        )
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
    finally:
        db.close()


@router.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    db = SessionLocal()
    try:
        book = crud.get_book_by_id(db, book_id)

        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        return book
        
    finally:
        db.close()


@router.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, updated_book: Book):
    db = SessionLocal()
    try:
        book = crud.update_book_by_id(db, book_id, updated_book)

        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        return book

    finally:
        db.close()


@router.delete("/books/{book_id}", response_model=MessageResponse)
def delete_book(book_id: int):
    db = SessionLocal()
    try:
        book = crud.delete_book_by_id(db, book_id)

        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        return {"message": "Book deleted successfully"}
    finally:
        db.close()

