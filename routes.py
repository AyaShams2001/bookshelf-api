from fastapi import APIRouter, HTTPException
from typing import Optional
from models import Book
import database

router = APIRouter()

@router.get("/books")
def get_books(skip: int = 0, limit: int = 10):
    return {
        "total": len(database.books),
        "data": database.books[skip:skip + limit]
    }

@router.post("/books")
def add_book(book: Book):
    new_book = {
        "id": database.next_id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "rating": book.rating
    }
    database.books.append(new_book)
    database.next_id += 1
    return new_book


@router.get("/books/search")
def search_books(author: str):
    results = []
    for book in database.books:
        if author.lower() in book["author"].lower():
            results.append(book)
    return results

@router.get("/books/title-search")
def search_books_by_title(title: str):
    results = []
    for book in database.books:
        if title.lower() in book["title"].lower():
            results.append(book)
    return results

@router.get("/books/filter")
def filter_books(title: str = "", author: str = ""):
    results = []

    for book in database.books:
        title_matches = title.lower() in book["title"].lower()
        author_matches = author.lower() in book["author"].lower()

        if title_matches and author_matches:
            results.append(book)

    return results

@router.get("/books/sort")
def sort_books(by: str = "title", order: str = "asc"):
    if by == "title":
        sorted_books = sorted(database.books, key=lambda x: x["title"].lower())
    elif by == "year":
        sorted_books = sorted(database.books, key=lambda x: x["year"])
    else:
        return {"error": "Invalid sort field"}

    if order == "desc":
        sorted_books.reverse()

    return sorted_books

@router.get("/books/top-rated")
def get_top_rated_books(min_rating: float = 4.5):
    results = []

    for book in database.books:
        if book["rating"] >= min_rating:
            results.append(book)

    return results

@router.get("/books/stats")
def get_book_stats():
    total_books = len(database.books)

    if total_books == 0:
        return {
            "total_books": 0,
            "average_rating": 0
        }

    average_rating = sum(book["rating"] for book in database.books) / total_books

    return {
        "total_books": total_books,
        "average_rating": average_rating
    }






@router.get("/books/recent")
def get_recent_books(
    year: Optional[int] = None,
    min_rating: Optional[float] = None,
    order: str = "desc",
    skip: int = 0,
    limit: int = 10
):
    results = []

    for book in database.books:
        year_ok = (year is None) or (book["year"] >= year)
        rating_ok = (min_rating is None) or (book["rating"] >= min_rating)

        if year_ok and rating_ok:
            results.append(book)

    results = sorted(results, key=lambda x: x["year"])

    if order == "desc":
        results.reverse()

    return {
    "total": len(results),
    "data": results[skip:skip + limit]
}



@router.get("/books/{book_id}")
def get_book(book_id: int):
    for book in database.books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for book in database.books:
        if book["id"] == book_id:
            book["title"] = updated_book.title
            book["author"] = updated_book.author
            book["year"] = updated_book.year
            book["rating"] = updated_book.rating
            return book

    raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(database.books):
        if book["id"] == book_id:
            deleted = database.books.pop(index)
            return deleted

    raise HTTPException(status_code=404, detail="Book not found")