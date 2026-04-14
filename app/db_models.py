from sqlalchemy import Column, Integer, String, Float
from .database_sql import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BookTable(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)

Base.metadata.create_all(bind=engine)