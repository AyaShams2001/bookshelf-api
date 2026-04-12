# Bookshelf API

A FastAPI project to manage books.

## Features

- Create, read, update, delete books
- Search by author and title
- Filter, sort, and paginate results
- Book ratings and statistics

## How to run

1. Install dependencies:

pip install fastapi uvicorn sqlalchemy


2. Run the server:

python -m uvicorn main:app --reload


3. Open in browser:

http://127.0.0.1:8000/docs


## Project structure

- main.py → app entry point  
- routes.py → API endpoints  
- models.py → data models  
- database.py → in-memory data (temporary)

## Tech

- Python
- FastAPI