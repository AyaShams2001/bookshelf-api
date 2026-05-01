# Bookshelf API

A FastAPI backend application for managing books, powered by PostgreSQL and deployed on Render.

This project demonstrates backend fundamentals including REST API design, database integration with SQLAlchemy, containerization with Docker, and multi-service architecture using Docker Compose.

---

## 🌐 Live API

**Base URL**
https://bookshelf-api-jd9k.onrender.com/

**API Docs (Swagger UI)**
https://bookshelf-api-jd9k.onrender.com/docs

---

## 🚀 Run with Docker (Recommended)

This project uses Docker Compose to run both the API and PostgreSQL database.

### 1. Clone the repository

```bash
git clone https://github.com/AyaShams2001/bookshelf-api.git
cd bookshelf-api
```

### 2. Start the application

```bash
docker compose up --build
```

### 3. Access the API

```text
http://localhost:8000/docs
```

---

## 🧱 Architecture

* **API Service** → FastAPI application
* **Database Service** → PostgreSQL container
* **Docker Network** → communication between services
* **Volume** → persistent database storage

---

## ⚙️ Environment Configuration

The API uses the following environment variable inside Docker:

```text
DATABASE_URL=postgresql://postgres:postgres@db:5432/bookshelf_db
```

* `db` is the PostgreSQL container (service name)
* No manual database setup is required

---

## 🐳 Services

Defined in `docker-compose.yml`:

* `api` → FastAPI backend
* `db` → PostgreSQL database

---

## 🛑 Stop the application

```bash
docker compose down
```

---

## Features

* Create, read, update, and delete books
* Search and filter functionality
* PostgreSQL database integration
* RESTful API with FastAPI
* Dockerized multi-container setup
* Deployed on Render

---

## 🛠 Tech Stack

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Uvicorn
* Docker & Docker Compose
* Render

---

## 📌 API Endpoints

| Method | Endpoint    | Description       |
| ------ | ----------- | ----------------- |
| GET    | /books      | Get all books     |
| POST   | /books      | Create a new book |
| GET    | /books/{id} | Get a book by ID  |
| PUT    | /books/{id} | Update a book     |
| DELETE | /books/{id} | Delete a book     |

---

## 📦 Example Request

**POST /books**

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "year": 2018,
  "rating": 4.5
}
```

---

## 🧪 Run Locally (Without Docker)

```bash
git clone https://github.com/AyaShams2001/bookshelf-api.git
cd bookshelf-api

pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📁 Project Structure

```
app/
├── main.py        # Application entry point
├── routes.py      # API routes
├── db_models.py   # Database models
├── database.py    # DB connection setup
├── schemas.py     # Pydantic schemas
├── crud.py        # Database operations
```

---

## 📚 What I Learned

* Building REST APIs with FastAPI
* Structuring backend applications
* Integrating PostgreSQL using SQLAlchemy
* Managing environment-based configuration
* Containerizing applications with Docker
* Running multi-service systems with Docker Compose
* Handling service dependencies and startup order
* Deploying backend services on Render
