from .db_models import BookTable
from sqlalchemy.orm import Session
from sqlalchemy import func

def get_book_stats(db: Session):
    total_books = db.query(BookTable).count()
    average_rating = db.query(func.avg(BookTable.rating)).scalar() or 0

    return {
        "total_books": total_books,
        "average_rating": round(average_rating, 2) if total_books > 0 else 0
    }

def get_books(db: Session, skip: int = 0, limit: int = 10):
    books = db.query(BookTable).offset(skip).limit(limit).all()
    total = db.query(BookTable).count()
    return books, total


def get_book_by_id(db: Session, book_id: int):
    return db.query(BookTable).filter(BookTable.id == book_id).first()


def create_book(db: Session, book):
    new_book = BookTable(
        title=book.title,
        author=book.author,
        year=book.year,
        rating=book.rating
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def delete_book_by_id(db: Session, book_id: int):
    book = db.query(BookTable).filter(BookTable.id == book_id).first()

    if not book:
        return None

    db.delete(book)
    db.commit()
    return book


def update_book_by_id(db: Session, book_id: int, updated_book):
    book = db.query(BookTable).filter(BookTable.id == book_id).first()

    if not book:
        return None

    book.title = updated_book.title
    book.author = updated_book.author
    book.year = updated_book.year
    book.rating = updated_book.rating

    db.commit()
    db.refresh(book)
    return book    


def get_books_by_author(db: Session, author: str):
    return db.query(BookTable).filter(BookTable.author.ilike(f"%{author}%")).all()


def get_books_by_title(db: Session, title: str):
    return db.query(BookTable).filter(BookTable.title.ilike(f"%{title}%")).all()

def filter_books(db: Session, title: str = "", author: str = ""):
    query = db.query(BookTable)

    if title:
        query = query.filter(BookTable.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(BookTable.author.ilike(f"%{author}%"))

    return query.all()

def get_top_rated_books(db: Session, min_rating: float = 4.5):
    return db.query(BookTable).filter(BookTable.rating >= min_rating).all()


def sort_books(db: Session, by: str = "title", order: str = "asc"):
    if by == "title":
        sort_column = BookTable.title
    elif by == "year":
        sort_column = BookTable.year
    else:
        return None

    if order == "desc":
        return db.query(BookTable).order_by(sort_column.desc()).all()
    return db.query(BookTable).order_by(sort_column).all()



def get_recent_books(
    db: Session,
    year: int | None = None,
    min_rating: float | None = None,
    order: str = "desc",
    skip: int = 0,
    limit: int = 10
):
    query = db.query(BookTable)

    if year is not None:
        query = query.filter(BookTable.year >= year)

    if min_rating is not None:
        query = query.filter(BookTable.rating >= min_rating)

    total = query.count()

    if order == "desc":
        query = query.order_by(BookTable.year.desc())
    else:
        query = query.order_by(BookTable.year)

    books = query.offset(skip).limit(limit).all()
    return books, total