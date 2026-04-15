# Bookshelf API

A backend API built with FastAPI for managing a collection of books.

## Features

- Add, update, delete books
- Search books by author or title
- Filter books by title and/or author
- Sort books by title or year
- Get top-rated books
- Get recent books with filtering, sorting, and pagination
- View overall book statistics (total + average rating)

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite

## Project Structure


app/
main.py # app entry point
routes.py # API endpoints
crud.py # database logic
db_models.py # SQLAlchemy models
schemas.py # Pydantic schemas


##  Run Locally

```bash
uvicorn app.main:app --reload

Then open:

http://127.0.0.1:8000/docs


## 🚀 Endpoint Examples

Get all books
GET /books
Search by author
GET /books/search?author=james
Filter books
GET /books/filter?title=atomic&author=james
Sort books
GET /books/sort?by=year&order=desc
Recent books
GET /books/recent?year=2010&min_rating=4
Book stats
GET /books/stats



