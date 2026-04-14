from pydantic import BaseModel, Field
from typing import List


class Book(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int
    rating: float = Field(ge=0, le=5)

class BookResponse(Book):
    id: int

class BooksListResponse(BaseModel):
    total: int
    data: List[BookResponse]    

class BookStatsResponse(BaseModel):
    total_books: int
    average_rating: float    

class MessageResponse(BaseModel):
    message: str    