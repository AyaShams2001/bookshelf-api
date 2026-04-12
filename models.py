from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int
    rating: float = Field(ge=0, le=5)