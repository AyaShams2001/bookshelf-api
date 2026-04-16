# Bookshelf API

A FastAPI backend application for managing books, built with PostgreSQL and deployed on Render.

2. Live links 
## Live API

Base URL:  
https://bookshelf-api-jd9k.onrender.com/

API Docs (Swagger):  
https://bookshelf-api-jd9k.onrender.com/docs
3. Features
## Features

- Add books
- View all books
- Search books
- Filter books
- Persistent storage with PostgreSQL
- RESTful API built with FastAPI
- Deployed on Render
4. Tech stack
## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Render (deployment)
5. Example request (this is powerful)
## Example Request

POST /books

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "year": 2018,
  "rating": 4.5
}

---

## 6. Run locally

```md
## Run Locally

```bash
git clone https://github.com/AyaShams2001/bookshelf-api.git
cd bookshelf-api

pip install -r requirements.txt
uvicorn app.main:app --reload

---


## What I Learned

- Building REST APIs with FastAPI
- Structuring backend projects
- Using SQLAlchemy with PostgreSQL
- Deploying applications on Render
- Handling environment variables and database connections