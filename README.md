Your content is good, but it’s missing **Markdown formatting**, so GitHub shows it as plain text instead of structured sections.

Copy this **exact version** — it will render cleanly on GitHub:

````md
# Bookshelf API

A FastAPI backend application for managing books, powered by PostgreSQL and deployed on Render.

This project demonstrates backend fundamentals including REST API design, database integration with SQLAlchemy, and cloud deployment.

---

## Live API

**Base URL**  
https://bookshelf-api-jd9k.onrender.com/

**API Docs (Swagger UI)**  
https://bookshelf-api-jd9k.onrender.com/docs

---

## Features

- Create, read, update, and delete books
- Search and filter functionality
- Persistent storage using PostgreSQL
- RESTful API built with FastAPI
- Deployed and hosted on Render

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn
- Render

---

## API Endpoints

| Method | Endpoint     | Description         |
|--------|-------------|---------------------|
| GET    | /books      | Get all books       |
| POST   | /books      | Create a new book   |
| GET    | /books/{id} | Get a book by ID    |
| PUT    | /books/{id} | Update a book       |
| DELETE | /books/{id} | Delete a book       |

---

## Example Request

**POST /books**

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "year": 2018,
  "rating": 4.5
}
````

---

## How to Use the API

1. Open the Swagger documentation:
   [https://bookshelf-api-jd9k.onrender.com/docs](https://bookshelf-api-jd9k.onrender.com/docs)

2. Use `POST /books` to add a new book

3. Use `GET /books` to retrieve all books

4. Use other endpoints to update or delete books

---

## Run Locally

```bash
git clone https://github.com/AyaShams2001/bookshelf-api.git
cd bookshelf-api

pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## Project Structure

```
app/
├── main.py        # Application entry point
├── routes.py      # API route definitions
├── models.py      # Database models
├── database.py    # Database connection setup
```

---

## What I Learned

* Building REST APIs with FastAPI
* Structuring backend applications
* Integrating PostgreSQL using SQLAlchemy
* Managing environment variables
* Deploying applications on Render

````


